import argparse
import sys
import time
from datetime import datetime, timedelta
import glados.es.ws2es.es_util as es_util
import glados.es.ws2es.signal_handler as signal_handler

__author__ = 'jfmosquera@ebi.ac.uk'


# ----------------------------------------------------------------------------------------------------------------------
# Replication
# ----------------------------------------------------------------------------------------------------------------------

def replicate_clusters(cluster_connection_origin, cluster_connection_2):
    pass

# ----------------------------------------------------------------------------------------------------------------------
# MAIN
# ----------------------------------------------------------------------------------------------------------------------


def main():
    t_ini = time.time()
    parser = argparse.ArgumentParser(description="Denormalize ChEMBL data existing in Elastic Search")
    parser.add_argument("--host",
                        dest="es_host",
                        help="Elastic Search Hostname or IP address.",
                        default="localhost")
    parser.add_argument("--user",
                        dest="es_user",
                        help="Elastic Search username.",
                        default=None)
    parser.add_argument("--password",
                        dest="es_password",
                        help="Elastic Search username password.",
                        default=None)
    parser.add_argument("--port",
                        dest="es_port",
                        help="Elastic Search port.",
                        default=9200)
    parser.add_argument("--unichem",
                        dest="denormalize_unichem",
                        help="If included will denormalize the unichem related data.",
                        action="store_true",)
    parser.add_argument("--activity",
                        dest="denormalize_activity",
                        help="If included will denormalize the configured activity related data.",
                        action="store_true",)
    parser.add_argument("--compound_hierarchy",
                        dest="denormalize_compound_hierarchy",
                        help="If included will denormalize the Compound Hierarchy data.",
                        action="store_true",)
    parser.add_argument("--mechanism_and_drug_indication",
                        dest="denormalize_mechanism_and_drug_indication",
                        help="If included will denormalize the Mechanism and Drug Indication data.",
                        action="store_true",)
    args = parser.parse_args()

    es_util.setup_connection(args.es_host, args.es_port, args.es_user, args.es_password)
    es_util.bulk_submitter.start()

    signal_handler.add_termination_handler(es_util.stop_scan)

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
