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
            # 'CHEMBL16832' , 'CHEMBL13266' , 'CHEMBL13267' , 'CHEMBL13368' , 'CHEMBL273428' , 'CHEMBL16590' , 'CHEMBL12
            # 867' , 'CHEMBL276589' , 'CHEMBL13316' , 'CHEMBL273372'
            'parent_chembl_id': 'TEXT',
            # EXAMPLES:
            # 'CHEMBL16832' , 'CHEMBL13266' , 'CHEMBL13267' , 'CHEMBL13368' , 'CHEMBL273428' , 'CHEMBL16590' , 'CHEMBL12
            # 867' , 'CHEMBL276589' , 'CHEMBL13316' , 'CHEMBL273372'
        }
    }
