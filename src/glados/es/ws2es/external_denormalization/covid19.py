
import glados.es.ws2es.resources_description as resources_description
from glados.es.ws2es.es_util import es_util, DefaultMappings
import csv
import os


molecules_file = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'covid19-molecules.csv')

molecule_chembl_ids = set()

with open(molecules_file, 'r') as csv_file:
    molecule_reader = csv.reader(csv_file)
    for row in molecule_reader:
        molecule_chembl_ids.add(row[0].strip())

print("READ {} DISTINCT MOLECULES".format(len(molecule_chembl_ids)))

NEW_MAPPINGS = {
    'properties': {
        '_metadata': {
            'properties': {
                'is_covid19_ds': DefaultMappings.BOOLEAN
            }
        }
    }
}

es_util.update_mappings_idx(resources_description.MOLECULE.idx_name, NEW_MAPPINGS)

es_util.bulk_submitter.start()
for chembl_id_i in molecule_chembl_ids:
    update_doc = {
            '_metadata': {
                'is_covid19_ds': True
            }
        }
    es_util.update_doc_bulk(resources_description.MOLECULE.idx_name, chembl_id_i, doc=update_doc)

es_util.bulk_submitter.join()
