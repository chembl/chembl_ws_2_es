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
            # 'CHEMBL13223' , 'CHEMBL6819' , 'CHEMBL10584' , 'CHEMBL10698' , 'CHEMBL13372' , 'CHEMBL7060' , 'CHEMBL9932'
            #  , 'CHEMBL13399' , 'CHEMBL20341' , 'CHEMBL416156'
            'parent_chembl_id': 'TEXT',
            # EXAMPLES:
            # 'CHEMBL13223' , 'CHEMBL6819' , 'CHEMBL10584' , 'CHEMBL10698' , 'CHEMBL13372' , 'CHEMBL7060' , 'CHEMBL9932'
            #  , 'CHEMBL13399' , 'CHEMBL20341' , 'CHEMBL416156'
        }
    }
