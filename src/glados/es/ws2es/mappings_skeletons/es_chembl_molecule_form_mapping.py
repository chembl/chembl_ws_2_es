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
            'is_parent': 'BOOLEAN',
            # EXAMPLES:
            # 'True' , 'True' , 'True' , 'True' , 'True' , 'True' , 'True' , 'True' , 'True' , 'True'
            'molecule_chembl_id': 'TEXT',
            # EXAMPLES:
            # 'CHEMBL33484' , 'CHEMBL276352' , 'CHEMBL29041' , 'CHEMBL7696' , 'CHEMBL274663' , 'CHEMBL23312' , 'CHEMBL77
            # 27' , 'CHEMBL279454' , 'CHEMBL33491' , 'CHEMBL10950'
            'parent_chembl_id': 'TEXT',
            # EXAMPLES:
            # 'CHEMBL33484' , 'CHEMBL276352' , 'CHEMBL29041' , 'CHEMBL7696' , 'CHEMBL274663' , 'CHEMBL23312' , 'CHEMBL77
            # 27' , 'CHEMBL279454' , 'CHEMBL33491' , 'CHEMBL10950'
        }
    }
