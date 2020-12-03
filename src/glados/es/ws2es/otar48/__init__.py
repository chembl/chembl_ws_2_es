import time
import argparse
from glados.es.ws2es.es_util import es_util
from glados.es.ws2es.resources_description import ASSAY
import json
import copy


def get_assay_activities(assay_chembl_id):
    assay_activities = []

    def on_activity_doc(act_doc, activity_id, total_docs, count, first, last):
        assay_activities.append(act_doc)

    es_util.scan_index(
        ASSAY.res_name, on_doc=on_activity_doc,
        query={
            'query_string': {
                'query': 'assay_chembl_id:{0}'.format(assay_chembl_id)
            }
        },
        progressbar=False
    )
    return assay_activities


def generate_variants_json_file():
    with open('./OTAR48-variant-assay-data.json', 'w') as variant_data_file:
        def generate_assay_json(assay_doc, assay_id, total_docs, count, first, last):
            variant_data = copy.deepcopy(assay_doc)
            variant_data['activities'] = get_assay_activities(assay_id)

            variant_data_file.write(json.dumps(variant_data)+'\n')
        es_util.scan_index(
            ASSAY.res_name, on_doc=generate_assay_json,
            query={
                'query_string': {
                    'query': '_exists_:variant_sequence'
                }
            }
        )


def main():
    t_ini = time.time()
    parser = argparse.ArgumentParser(description="Migrate ChEMBL data from the WebServices to Elastic Search")
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
    args = parser.parse_args()
    es_util.setup_connection(args.es_host, args.es_port, args.es_user, args.es_password)
    generate_variants_json_file()


if __name__ == "__main__":
    main()
