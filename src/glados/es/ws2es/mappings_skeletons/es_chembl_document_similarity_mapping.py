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
            # 'CHEMBL1128878' , 'CHEMBL1126335' , 'CHEMBL1126335' , 'CHEMBL1128878' , 'CHEMBL1127285' , 'CHEMBL1126335' 
            # , 'CHEMBL1128878' , 'CHEMBL1128878' , 'CHEMBL1128878' , 'CHEMBL1126335'
            'document_2_chembl_id': 'TEXT',
            # EXAMPLES:
            # 'CHEMBL1121581' , 'CHEMBL1126981' , 'CHEMBL1127205' , 'CHEMBL1121714' , 'CHEMBL1142485' , 'CHEMBL1126962' 
            # , 'CHEMBL1121718' , 'CHEMBL1121911' , 'CHEMBL1121779' , 'CHEMBL1126514'
            'mol_tani': 'NUMERIC',
            # EXAMPLES:
            # '0.0' , '0.0' , '0.0' , '0.0' , '0.0' , '0.0' , '0.0' , '0.0' , '0.0' , '0.03'
            'tid_tani': 'NUMERIC',
            # EXAMPLES:
            # '1.0' , '1.0' , '1.0' , '1.0' , '1.0' , '1.0' , '1.0' , '1.0' , '1.0' , '1.0'
        }
    }
