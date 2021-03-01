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
            # 'CHEMBL3885645' , 'CHEMBL304' , 'CHEMBL4523741' , 'CHEMBL4523705' , 'CHEMBL1907608' , 'CHEMBL2096672' , 'C
            # HEMBL4523744' , 'CHEMBL6089' , 'CHEMBL2096668' , 'CHEMBL2111448'
            'relationship': 'TEXT',
            # EXAMPLES:
            # 'OVERLAPS WITH' , 'SUPERSET OF' , 'OVERLAPS WITH' , 'OVERLAPS WITH' , 'SUBSET OF' , 'OVERLAPS WITH' , 'OVE
            # RLAPS WITH' , 'SUPERSET OF' , 'SUBSET OF' , 'OVERLAPS WITH'
            'target_chembl_id': 'TEXT',
            # EXAMPLES:
            # 'CHEMBL4296119' , 'CHEMBL2095175' , 'CHEMBL4296117' , 'CHEMBL3883286' , 'CHEMBL303' , 'CHEMBL2095175' , 'C
            # HEMBL4296117' , 'CHEMBL3883289' , 'CHEMBL2363044' , 'CHEMBL2095942'
        }
    }
