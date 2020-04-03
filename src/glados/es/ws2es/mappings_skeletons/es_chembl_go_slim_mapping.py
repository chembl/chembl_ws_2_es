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
            'aspect': 'TEXT',
            # EXAMPLES:
            # 'P' , 'F' , 'F' , 'F' , 'C' , 'C' , 'P' , 'F' , 'F' , 'F'
            'class_level': 'NUMERIC',
            # EXAMPLES:
            # '1' , '2' , '1' , '4' , '3' , '3' , '1' , '1' , '1' , '3'
            'go_id': 'TEXT',
            # EXAMPLES:
            # 'GO:0000003' , 'GO:0000149' , 'GO:0000166' , 'GO:0000215' , 'GO:0000228' , 'GO:0000229' , 'GO:0000902' , '
            # GO:0000988' , 'GO:0001071' , 'GO:0001515'
            'parent_go_id': 'TEXT',
            # EXAMPLES:
            # 'GO:0008150' , 'GO:0005515' , 'GO:0003674' , 'GO:0016772' , 'GO:0005694' , 'GO:0005694' , 'GO:0008150' , '
            # GO:0003674' , 'GO:0003674' , 'GO:0005102'
            'path': 'TEXT',
            # EXAMPLES:
            # 'biological_process  reproduction' , 'molecular_function  protein binding  SNARE binding' , 'molecular_fun
            # ction  nucleotide binding' , 'molecular_function  catalytic activity  transferase activity  transferase ac
            # tivity, transferring phosphorus-containing groups  tRNA 2'-phosphotransferase activity' , 'cellular_compon
            # ent  organelle  chromosome  nuclear chromosome' , 'cellular_component  organelle  chromosome  cytoplasmic 
            # chromosome' , 'biological_process  cell morphogenesis' , 'molecular_function  protein binding transcriptio
            # n factor activity' , 'molecular_function  nucleic acid binding transcription factor activity' , 'molecular
            # _function  protein binding  receptor binding  opioid peptide activity'
            'pref_name': 'TEXT',
            # EXAMPLES:
            # 'reproduction' , 'SNARE binding' , 'nucleotide binding' , 'tRNA 2'-phosphotransferase activity' , 'nuclear
            #  chromosome' , 'cytoplasmic chromosome' , 'cell morphogenesis' , 'protein binding transcription factor act
            # ivity' , 'nucleic acid binding transcription factor activity' , 'opioid peptide activity'
        }
    }
