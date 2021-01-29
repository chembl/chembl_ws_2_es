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
            # 'CHEMBL1374728' , 'CHEMBL1374729' , 'CHEMBL1374738' , 'CHEMBL1374739' , 'CHEMBL1374741' , 'CHEMBL1374745' 
            # , 'CHEMBL1374753' , 'CHEMBL1374755' , 'CHEMBL1374757' , 'CHEMBL137476'
            'chembl_id_number': 'NUMERIC',
            # EXAMPLES:
            # '1374728' , '1374729' , '1374738' , '1374739' , '1374741' , '1374745' , '1374753' , '1374755' , '1374757' 
            # , '137476'
            'entity_type': 'TEXT',
            # EXAMPLES:
            # 'COMPOUND' , 'COMPOUND' , 'COMPOUND' , 'COMPOUND' , 'COMPOUND' , 'COMPOUND' , 'COMPOUND' , 'COMPOUND' , 'C
            # OMPOUND' , 'COMPOUND'
            'resource_url': 'TEXT',
            # EXAMPLES:
            # '/chembl/api/data/molecule/CHEMBL1374728' , '/chembl/api/data/molecule/CHEMBL1374729' , '/chembl/api/data/
            # molecule/CHEMBL1374738' , '/chembl/api/data/molecule/CHEMBL1374739' , '/chembl/api/data/molecule/CHEMBL137
            # 4741' , '/chembl/api/data/molecule/CHEMBL1374745' , '/chembl/api/data/molecule/CHEMBL1374753' , '/chembl/a
            # pi/data/molecule/CHEMBL1374755' , '/chembl/api/data/molecule/CHEMBL1374757' , '/chembl/api/data/molecule/C
            # HEMBL137476'
            'status': 'TEXT',
            # EXAMPLES:
            # 'ACTIVE' , 'ACTIVE' , 'ACTIVE' , 'ACTIVE' , 'ACTIVE' , 'ACTIVE' , 'ACTIVE' , 'ACTIVE' , 'ACTIVE' , 'ACTIVE
            # '
        }
    }
