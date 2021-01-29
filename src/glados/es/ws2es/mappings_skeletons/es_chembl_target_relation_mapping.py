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
            'related_target_chembl_id': 'TEXT',
            # EXAMPLES:
            # 'CHEMBL4296064' , 'CHEMBL4106151' , 'CHEMBL2111413' , 'CHEMBL3430899' , 'CHEMBL4106157' , 'CHEMBL2111366' 
            # , 'CHEMBL4956' , 'CHEMBL2111370' , 'CHEMBL1847' , 'CHEMBL2093872'
            'relationship': 'TEXT',
            # EXAMPLES:
            # 'SUPERSET OF' , 'OVERLAPS WITH' , 'OVERLAPS WITH' , 'OVERLAPS WITH' , 'OVERLAPS WITH' , 'OVERLAPS WITH' , 
            # 'SUPERSET OF' , 'OVERLAPS WITH' , 'SUPERSET OF' , 'SUBSET OF'
            'target_chembl_id': 'TEXT',
            # EXAMPLES:
            # 'CHEMBL2094130' , 'CHEMBL2094130' , 'CHEMBL2094130' , 'CHEMBL2094130' , 'CHEMBL2094130' , 'CHEMBL2094130' 
            # , 'CHEMBL2094130' , 'CHEMBL2094130' , 'CHEMBL2094130' , 'CHEMBL2094130'
        }
    }
