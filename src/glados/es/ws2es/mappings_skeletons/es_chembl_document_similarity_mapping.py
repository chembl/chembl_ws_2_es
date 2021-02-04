# Elastic search mapping definition for the Molecule entity
from glados.es.ws2es.es_util import DefaultMappings

# Shards size - can be overridden from the default calculated value here
# shards = 3,
replicas = 1

analysis = DefaultMappings.COMMON_ANALYSIS

mappings = \
    {
        'properties': 
        {
            'document_1_chembl_id': 'TEXT',
            # EXAMPLES:
            # 'CHEMBL1123391' , 'CHEMBL1124609' , 'CHEMBL1123916' , 'CHEMBL1124352' , 'CHEMBL1122748' , 'CHEMBL1123391' 
            # , 'CHEMBL1122714' , 'CHEMBL1123161' , 'CHEMBL1123019' , 'CHEMBL1122631'
            'document_2_chembl_id': 'TEXT',
            # EXAMPLES:
            # 'CHEMBL1134667' , 'CHEMBL1125120' , 'CHEMBL1124618' , 'CHEMBL1125525' , 'CHEMBL1123382' , 'CHEMBL1134374' 
            # , 'CHEMBL1157040' , 'CHEMBL1129695' , 'CHEMBL1123571' , 'CHEMBL1123753'
            'mol_tani': 'NUMERIC',
            # EXAMPLES:
            # '0.0' , '0.0' , '0.0' , '0.0' , '0.0' , '0.0' , '0.0' , '0.0' , '0.0' , '0.0'
            'tid_tani': 'NUMERIC',
            # EXAMPLES:
            # '1.0' , '1.0' , '1.0' , '1.0' , '1.0' , '1.0' , '1.0' , '1.0' , '1.0' , '1.0'
        }
    }
