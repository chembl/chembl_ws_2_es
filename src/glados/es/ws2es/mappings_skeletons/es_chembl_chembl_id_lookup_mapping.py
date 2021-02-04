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
            # 'CHEMBL1024100' , 'CHEMBL1010384' , 'CHEMBL1029193' , 'CHEMBL103739' , 'CHEMBL1042014' , 'CHEMBL1005898' ,
            #  'CHEMBL1037390' , 'CHEMBL1024102' , 'CHEMBL103336' , 'CHEMBL1033204'
            'chembl_id_number': 'NUMERIC',
            # EXAMPLES:
            # '1024100' , '1010384' , '1029193' , '103739' , '1042014' , '1005898' , '1037390' , '1024102' , '103336' , 
            # '1033204'
            'entity_type': 'TEXT',
            # EXAMPLES:
            # 'ASSAY' , 'ASSAY' , 'ASSAY' , 'COMPOUND' , 'ASSAY' , 'ASSAY' , 'ASSAY' , 'ASSAY' , 'COMPOUND' , 'ASSAY'
            'resource_url': 'TEXT',
            # EXAMPLES:
            # '/chembl/api/data/assay/CHEMBL1024100' , '/chembl/api/data/assay/CHEMBL1010384' , '/chembl/api/data/assay/
            # CHEMBL1029193' , '/chembl/api/data/molecule/CHEMBL103739' , '/chembl/api/data/assay/CHEMBL1042014' , '/che
            # mbl/api/data/assay/CHEMBL1005898' , '/chembl/api/data/assay/CHEMBL1037390' , '/chembl/api/data/assay/CHEMB
            # L1024102' , '/chembl/api/data/molecule/CHEMBL103336' , '/chembl/api/data/assay/CHEMBL1033204'
            'status': 'TEXT',
            # EXAMPLES:
            # 'ACTIVE' , 'ACTIVE' , 'ACTIVE' , 'ACTIVE' , 'ACTIVE' , 'ACTIVE' , 'ACTIVE' , 'ACTIVE' , 'ACTIVE' , 'ACTIVE
            # '
        }
    }
