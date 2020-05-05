import argparse
import sys
import time
from datetime import datetime, timedelta
from glados.es.ws2es.es_util import ESUtil
import glados.es.ws2es.signal_handler as signal_handler
import glados.es.ws2es.resources_description as resources_description
import glados.es.ws2es.progress_bar_handler as pbh
from threading import Thread
import traceback

__author__ = 'jfmosquera@ebi.ac.uk'

# ----------------------------------------------------------------------------------------------------------------------
# Replication
# ----------------------------------------------------------------------------------------------------------------------


class IndexReplicator(Thread):

    def __init__(self, idx_name: str, es_util_origin: ESUtil, es_util_dest: ESUtil):
        super().__init__()
        self.idx_name = idx_name
        self.es_util_origin = es_util_origin
        self.es_util_dest = es_util_dest

    def replicate_idx(self):
        self.es_util_dest.delete_idx(self.idx_name)
        self.es_util_dest.create_idx(self.idx_name, mappings=self.es_util_origin.get_index_mapping(self.idx_name))
        print('INFO: Index created for {0}.'.format(self.idx_name), file=sys.stderr)
        sys.stderr.flush()

        def index_doc_on_doc(scan_doc, scan_doc_id, total_docs, current_count, firts_doc, last_doc):
            self.es_util_dest.index_doc_bulk(self.idx_name, scan_doc_id, scan_doc)

        self.es_util_origin.scan_index(self.idx_name, index_doc_on_doc)

    def run(self):
        try:
            self.replicate_idx()
        except:
            traceback.print_exc()


def replicate_clusters(es_util_origin: ESUtil, es_util_dest: ESUtil):
    replicators = []
    for resource_i in resources_description.ALL_RESOURCES:
        res_it_i = IndexReplicator(resource_i.idx_name, es_util_origin, es_util_dest)
        res_it_i.start()
        replicators.append(res_it_i)
    for res_it_i in replicators:
        res_it_i.join()

# ----------------------------------------------------------------------------------------------------------------------
# MAIN
# ----------------------------------------------------------------------------------------------------------------------


def main():
    t_ini = time.time()
    parser = argparse.ArgumentParser(
        description="Replicate ChEMBL data existing in Elastic Search from origin to destination."
    )
    parser.add_argument("--host-origin",
                        dest="es_host_origin",
                        help="Elastic Search Hostname or IP address for origin cluster.",
                        default="localhost")
    parser.add_argument("--user-origin",
                        dest="es_user_origin",
                        help="Elastic Search username for origin cluster.",
                        default=None)
    parser.add_argument("--password-origin",
                        dest="es_password_origin",
                        help="Elastic Search username password for origin cluster.",
                        default=None)
    parser.add_argument("--port-origin",
                        dest="es_port_origin",
                        help="Elastic Search port for origin cluster.",
                        default=9200)
    parser.add_argument("--host-destination",
                        dest="es_host_destination",
                        help="Elastic Search Hostname or IP address for destination cluster.",
                        default="localhost")
    parser.add_argument("--user-destination",
                        dest="es_user_destination",
                        help="Elastic Search username for destination cluster.",
                        default=None)
    parser.add_argument("--password-destination",
                        dest="es_password_destination",
                        help="Elastic Search username password for destination cluster.",
                        default=None)
    parser.add_argument("--port-destination",
                        dest="es_port_destination",
                        help="Elastic Search port for destination cluster.",
                        default=9200)
    args = parser.parse_args()

    es_util_origin = ESUtil()
    es_util_origin.setup_connection(
      args.es_host_origin, args.es_port_origin, args.es_user_origin, args.es_password_origin
    )
    es_util_destination = ESUtil()
    es_util_destination.setup_connection(
      args.es_host_destination, args.es_port_destination, args.es_user_destination, args.es_password_destination
    )

    ping_failed = False

    if not es_util_origin.ping():
        print('ERROR: Ping failed to origin cluster.', file=sys.stderr)
        ping_failed = True

    if not es_util_destination.ping():
        print('ERROR: Ping failed to destination cluster.', file=sys.stderr)
        ping_failed = True

    if ping_failed:
        return

    es_util_destination.bulk_submitter.start()

    signal_handler.add_termination_handler(es_util_origin.stop_scan)
    signal_handler.add_termination_handler(es_util_destination.stop_scan)
    signal_handler.add_termination_handler(es_util_destination.bulk_submitter.stop_submitter)

    replicate_clusters(es_util_origin, es_util_destination)

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


if __name__ == "__main__":
    main()
