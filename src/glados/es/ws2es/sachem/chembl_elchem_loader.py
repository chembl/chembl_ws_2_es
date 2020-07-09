import argparse
import sys
import time
from datetime import datetime, timedelta
from glados.es.ws2es.es_util import ESUtil, num_shards_by_num_rows, DefaultMappings, CURRENT_ES_VERSION
import glados.es.ws2es.signal_handler as signal_handler
import glados.es.ws2es.progress_bar_handler as pbh
from glados.es.ws2es.resources_description import MOLECULE

__author__ = 'jfmosquera@ebi.ac.uk'

# ----------------------------------------------------------------------------------------------------------------------
# Scan chembl and load
# ----------------------------------------------------------------------------------------------------------------------

INDEX_NAME = 'chembl_molecule_elchem'

INDEX_MAPPINGS = {
    'properties': {
        'chembl_id': DefaultMappings.CHEMBL_ID,
        'molecule_smiles': DefaultMappings.CHEM_STRUCT_FIELD,
        'molecule_molfile': DefaultMappings.CHEM_STRUCT_FIELD,
    }
}


def load_chembl_data(es_util_origin: ESUtil, es_util_destination: ESUtil):
    global INDEX_NAME, INDEX_MAPPINGS
    # create index
    es_util_destination.create_idx(INDEX_NAME, 5, 1, analysis=DefaultMappings.COMMON_ANALYSIS, mappings=INDEX_MAPPINGS)

    # Index molecules
    def on_molecule_doc(molecule_doc: dict, doc_id: str, total_docs: int, index: int, first: bool, last: bool):
        molecule_structures = molecule_doc.get('molecule_structures', None)
        doc_to_index = {
          'chembl_id': doc_id,
          'molecule_smiles': molecule_structures
              .get('canonical_smiles', None) if molecule_structures is not None else None,
          'molecule_molfile': molecule_structures
              .get('molfile', None) if molecule_structures is not None else None,
        }
        es_util_destination.update_doc_bulk(
          INDEX_NAME, doc_id, doc=doc_to_index, upsert=True
        )

    molecules_query = {
        '_source': ['molecule_chembl_id', 'molecule_structures']
    }

    es_util_origin.scan_index(MOLECULE.idx_name, on_doc=on_molecule_doc, query=molecules_query)


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

    print('ORIGIN:')
    print(args.es_host_origin, args.es_port_origin, args.es_user_origin)
    print('DESTINATION:')
    print(args.es_host_destination, args.es_port_destination, args.es_user_destination)

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

    load_chembl_data(es_util_origin, es_util_destination)

    es_util_destination.bulk_submitter.finish_current_queues()
    es_util_destination.bulk_submitter.join()
    pbh.write_after_progress_bars()

    end_msg = 'LOADING FINISHED'

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

