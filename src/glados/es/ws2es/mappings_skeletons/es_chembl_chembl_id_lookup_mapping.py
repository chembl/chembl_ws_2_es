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
            'chembl_id': 'TEXT',
            # EXAMPLES:
            # 'CHEMBL1024208' , 'CHEMBL1005814' , 'CHEMBL1037331' , 'CHEMBL100582' , 'CHEMBL1033293' , 'CHEMBL100584' , 
            # 'CHEMBL1041939' , 'CHEMBL102421' , 'CHEMBL1024191' , 'CHEMBL1005840'
            'chembl_id_number': 'NUMERIC',
            # EXAMPLES:
            # '1024208' , '1005814' , '1037331' , '100582' , '1033293' , '100584' , '1041939' , '102421' , '1024191' , '
            # 1005840'
            'entity_type': 'TEXT',
            # EXAMPLES:
            # 'ASSAY' , 'ASSAY' , 'ASSAY' , 'COMPOUND' , 'ASSAY' , 'COMPOUND' , 'ASSAY' , 'COMPOUND' , 'ASSAY' , 'ASSAY'
            'resource_url': 'TEXT',
            # EXAMPLES:
            # '/chembl/api/data/assay/CHEMBL1024208' , '/chembl/api/data/assay/CHEMBL1005814' , '/chembl/api/data/assay/
            # CHEMBL1037331' , '/chembl/api/data/molecule/CHEMBL100582' , '/chembl/api/data/assay/CHEMBL1033293' , '/che
            # mbl/api/data/molecule/CHEMBL100584' , '/chembl/api/data/assay/CHEMBL1041939' , '/chembl/api/data/molecule/
            # CHEMBL102421' , '/chembl/api/data/assay/CHEMBL1024191' , '/chembl/api/data/assay/CHEMBL1005840'
            'status': 'TEXT',
            # EXAMPLES:
            # 'ACTIVE' , 'ACTIVE' , 'ACTIVE' , 'ACTIVE' , 'ACTIVE' , 'ACTIVE' , 'ACTIVE' , 'ACTIVE' , 'ACTIVE' , 'ACTIVE
            # '
        }
    }
