import argparse
import sys
import time
from datetime import datetime, timedelta
from glados.es.ws2es.es_util import ESUtil, num_shards_by_num_rows, DefaultMappings, CURRENT_ES_VERSION
import glados.es.ws2es.signal_handler as signal_handler
import glados.es.ws2es.resources_description as resources_description
import glados.es.ws2es.progress_bar_handler as pbh
from threading import Thread
from glados.es.ws2es.util import query_yes_no
import traceback
import yaml
import glados.es.ws2es.util as util
import os
import os.path
import datetime

__author__ = 'jfmosquera@ebi.ac.uk'


# ----------------------------------------------------------------------------------------------------------------------
# Replication
# ----------------------------------------------------------------------------------------------------------------------


class IndexReplicator(Thread):

    def __init__(self, idx_name: str, es_util_origin: ESUtil, es_util_dest: ESUtil, delete_dest_idx: bool = False,
                 skip_update_mappings: bool = False, es_query=None):
        super().__init__()
        self.idx_name = idx_name
        self.es_util_origin = es_util_origin
        self.es_util_dest = es_util_dest
        self.delete_dest_idx = delete_dest_idx
        self.update_mappings = not skip_update_mappings
        self.es_query = es_query

    def replicate_idx(self):
        origin_count = self.es_util_origin.get_idx_count(self.idx_name)
        if origin_count <= 0:
            print('ERROR: Skipping empty index {0} in origin cluster. COUNT: {1}'.format(self.idx_name, origin_count))
            return
        idx_exists = self.es_util_dest.get_idx_count(self.idx_name) >= 0
        # noinspection PyBroadException
        try:
            if idx_exists and self.delete_dest_idx:
                # self.es_util_dest.delete_idx(self.idx_name)
                print('INFO: INDEX DELETED : {0}.'.format(self.idx_name), file=sys.stderr)

            if not idx_exists or (idx_exists and self.delete_dest_idx):
                self.es_util_dest.create_idx(
                    self.idx_name, num_shards_by_num_rows(origin_count), 0,
                    analysis=DefaultMappings.COMMON_ANALYSIS,
                    mappings=self.es_util_origin.get_index_mapping(self.idx_name)
                )
                print('INFO: INDEX CREATED : {0}.'.format(self.idx_name), file=sys.stderr)
            elif self.update_mappings:
                self.es_util_dest.update_mappings_idx(
                    self.idx_name, self.es_util_origin.get_index_mapping(self.idx_name)
                )
                print('INFO: INDEX MAPPINGS UPDATED : {0}.'.format(self.idx_name), file=sys.stderr)
        except Exception as e:
            traceback.print_exc(file=sys.stderr)
            print('ERROR: INDEX CREATION/UPDATE FAILED : {0}.'.format(self.idx_name), file=sys.stderr)
            return

        sys.stderr.flush()

        def index_doc_on_doc(scan_doc, scan_doc_id, total_docs, current_count, firts_doc, last_doc):
            if 'request_date' in scan_doc:
                try:
                    scan_doc['request_date'] = int(scan_doc['request_date'])
                except:
                    pass
            if idx_exists:
                self.es_util_dest.update_doc_bulk(self.idx_name, scan_doc_id, doc=scan_doc, upsert=True)
            else:
                self.es_util_dest.index_doc_bulk(self.idx_name, scan_doc_id, scan_doc)

        self.es_util_origin.scan_index(self.idx_name, index_doc_on_doc, query=self.es_query)

    def run(self):
        try:
            self.replicate_idx()
        except:
            traceback.print_exc()


def replicate_clusters(
    es_util_origin: ESUtil, es_util_dest: ESUtil,
    resources_to_run=resources_description.ALL_RELEASE_RESOURCES,
    delete_dest_idx: bool = False, skip_update_mappings: bool = False, unichem: bool = False,
    unichem_cron_update: bool = False
):
    replicators = []
    if unichem:
        scan_query = None
        if unichem_cron_update:
            max_dates_result = es_util_origin.run_yaml_query(
                os.path.join(os.path.abspath(os.path.dirname(__file__)), './unichem_max_dates_query.yaml'),
                'unichem', return_all=True
            )
            max_created_date = util.get_js_path_from_dict(
                max_dates_result, 'aggregations.MAX_CREATED_DATE.value'
            )
            max_updated_date = util.get_js_path_from_dict(
                max_dates_result, 'aggregations.MAX_UPDATED_DATE.value'
            )

            max_created_date = datetime.datetime.fromtimestamp(max_created_date/1000.0)
            max_updated_date = datetime.datetime.fromtimestamp(max_updated_date/1000.0)
            max_date = max(max_created_date, max_updated_date)
            update_date = max_date - timedelta(days=14)
            print(
                'MAX DATE: {0} --- {1}\nUPDATE FROM: {2} --- {3}'
                .format(max_date, max_date.timestamp()*1000, update_date, update_date.timestamp()*1000)
            )
            scan_query = {
                'query': {
                    'query_string': {
                        'query': 'sources.last_updated:>={0} OR sources.created_at:>={0}'
                        .format(int(update_date.timestamp()*1000))
                    }
                }
            }
        unichem_replicator = IndexReplicator(
            'unichem', es_util_origin, es_util_dest, delete_dest_idx=delete_dest_idx,
            skip_update_mappings=skip_update_mappings, es_query=scan_query
        )
        unichem_replicator.start()
        replicators.append(unichem_replicator)
    else:
        for resource_i in resources_to_run:
            res_it_i = IndexReplicator(resource_i.idx_name, es_util_origin, es_util_dest, delete_dest_idx=delete_dest_idx,
                                       skip_update_mappings=skip_update_mappings)
            res_it_i.start()
            replicators.append(res_it_i)
    for res_it_i in replicators:
        res_it_i.join()


def check_origin_vs_destination_counts(
    es_util_origin: ESUtil, es_util_dest: ESUtil,
    resources_to_run=resources_description.ALL_RELEASE_RESOURCES
):
    for resource_i in resources_to_run:
        origin_count = es_util_origin.get_idx_count(resource_i.idx_name)
        destination_count = es_util_dest.get_idx_count(resource_i.idx_name)
        mismatch = origin_count == -1 or destination_count == -1 or origin_count != destination_count
        mismatch_txt = 'MISMATCH' if mismatch else ''
        formatted_ws_count = '{0:,}'.format(origin_count)
        formatted_ws_count = ' ' * (12 - len(formatted_ws_count)) + formatted_ws_count
        formatted_es_count = '{0:,}'.format(destination_count)
        formatted_es_count = ' ' * (12 - len(formatted_es_count)) + formatted_es_count
        print_txt = '{0}: origin_count: {1} - destination_count: {2}  {3}' \
            .format(resource_i.get_res_name_for_print(), formatted_ws_count, formatted_es_count, mismatch_txt)
        print(print_txt, file=sys.stderr)

# ----------------------------------------------------------------------------------------------------------------------
# MAIN
# ----------------------------------------------------------------------------------------------------------------------


def parse_config():
    parser = argparse.ArgumentParser(
        description="Replicate ChEMBL and UniChem data existing in Elastic Search from origin to destination."
    )
    parser.add_argument("--config",
                        dest="config_file",
                        help="Configuration file for the replication process.")
    args = parser.parse_args()

    if not args.config_file:
        print(
            'ERROR: a configuration file needs to be specified using --config',
            file=sys.stderr
        )
        sys.exit(1)
    try:
        config_data = None
        with open(args.config_file, 'r') as conf_file:
            config_data = yaml.safe_load(conf_file)
        return config_data
    except:
        traceback.print_exc()
        print(
            'ERROR: could not parse the config file at {0}'.format(args.config_file),
            file=sys.stderr
        )
        sys.exit(1)


def main():
    t_ini = time.time()

    config = parse_config()

    progress_bar_out = config.get('progress_bar_out', None)
    pbh.set_progressbar_out_path(progress_bar_out)

    delete_indexes = config.get('delete_indexes', False)
    skip_update_mappings = config.get('skip_update_mappings', False)
    unichem = config.get('unichem', False)
    unichem_cron_update = config.get('unichem-cron-update', False)
    monitoring = config.get('monitoring', False)

    es_host_origin = util.get_js_path_from_dict(config, 'es_clusters.origin.host')
    es_port_origin = util.get_js_path_from_dict(config, 'es_clusters.origin.port')
    es_user_origin = util.get_js_path_from_dict(config, 'es_clusters.origin.user')
    es_password_origin = util.get_js_path_from_dict(config, 'es_clusters.origin.password')

    es_host_destination = util.get_js_path_from_dict(config, 'es_clusters.destination.host')
    es_port_destination = util.get_js_path_from_dict(config, 'es_clusters.destination.port')
    es_user_destination = util.get_js_path_from_dict(config, 'es_clusters.destination.user')
    es_password_destination = util.get_js_path_from_dict(config, 'es_clusters.destination.password')

    if es_host_origin == es_host_destination and es_port_origin == es_port_destination:
        print('ERROR: Origin and destination clusters are the same.')
        sys.exit(1)

    es_major_version_origin = util.get_js_path_from_dict(config, 'es_clusters.origin.es_client_major_version')
    if es_major_version_origin is not None:
        try:
            es_major_version_origin = int(es_major_version_origin)
            assert es_major_version_origin <= CURRENT_ES_VERSION
        except:
            traceback.print_exc()
            print(
                'ERROR: Major version for elastic "{0}" is not valid, it must be an integer lower than {1}.'
                .format(es_major_version_origin, CURRENT_ES_VERSION),
                file=sys.stderr
            )
            sys.exit(1)

    selected_resources = None
    resources = config.get('resource', None)
    if resources is not None:
        if resources is not isinstance(resources, list):
            selected_resources = resources.split(',')
        else:
            selected_resources = resources
    resources_to_run = resources_description.ALL_MONITORING_RESOURCES if monitoring else \
        resources_description.ALL_RELEASE_RESOURCES

    if not unichem:
        if selected_resources:
            resources_to_run = []
            for resource_i_str in selected_resources:
                resource_i = resources_description.RESOURCES_BY_RES_NAME.get(resource_i_str, None)
                if resource_i is None:
                    print('Unknown resource {0}'.format(resource_i_str), file=sys.stderr)
                    sys.exit(1)
                resources_to_run.append(resource_i)

    # if args.delete_indexes:
    #     if not query_yes_no("This procedure will delete and create all indexes again in the destination server.\n"
    #                         "Do you want to proceed?", default="no"):
    #         return

    es_util_origin = ESUtil(es_major_version=es_major_version_origin)
    es_util_origin.setup_connection(
        es_host_origin, es_port_origin, es_user_origin, es_password_origin
    )
    es_util_destination = ESUtil()
    es_util_destination.setup_connection(
        es_host_destination, es_port_destination, es_user_destination, es_password_destination
    )

    ping_failed = False

    if not es_util_origin.ping():
        print('ERROR: Ping failed to origin cluster.', file=sys.stderr)
        ping_failed = True

    if not es_util_destination.ping():
        print('ERROR: Ping failed to destination cluster.', file=sys.stderr)
        ping_failed = True

    if ping_failed:
        sys.exit(1)

    es_util_destination.bulk_submitter.start()

    signal_handler.add_termination_handler(es_util_origin.stop_scan)
    signal_handler.add_termination_handler(es_util_destination.stop_scan)
    signal_handler.add_termination_handler(es_util_destination.bulk_submitter.stop_submitter)

    replicate_clusters(
        es_util_origin, es_util_destination, resources_to_run=resources_to_run, delete_dest_idx=delete_indexes,
        skip_update_mappings=skip_update_mappings, unichem=unichem, unichem_cron_update=unichem_cron_update
    )

    es_util_destination.bulk_submitter.finish_current_queues()
    es_util_destination.bulk_submitter.join()
    pbh.write_after_progress_bars()

    end_msg = 'REPLICATION FINISHED'

    total_time = time.time() - t_ini
    sec = timedelta(seconds=total_time)
    d = datetime(1, 1, 1) + sec

    print(end_msg, file=sys.stderr)
    print(
        "Finished in: {0} Day(s), {1} Hour(s), {2} Minute(s) and {3} Second(s)"
        .format(d.day-1, d.hour, d.minute, d.second),
        file=sys.stderr
    )
    check_origin_vs_destination_counts(es_util_origin, es_util_destination, resources_to_run=resources_to_run)


if __name__ == "__main__":
    main()
