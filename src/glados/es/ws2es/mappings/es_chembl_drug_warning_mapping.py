# Elastic search mapping definition for the Molecule entity
from glados.es.ws2es.es_util import DefaultMappings
import glados.es.ws2es.mappings.es_chembl_molecule_n_drug_shared_mapping as molecule_n_drug_mapping

# Shards size - can be overridden from the default calculated value here
# shards = 3,
replicas = 0

analysis = DefaultMappings.COMMON_ANALYSIS

mappings = \
    {
    }
