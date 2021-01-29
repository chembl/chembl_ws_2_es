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
            'alert': 
            {
                'properties': 
                {
                    'alert_id': 'NUMERIC',
                    # EXAMPLES:
                    # '1' , '1' , '1' , '1' , '1' , '1' , '1' , '1' , '1' , '1'
                    'alert_name': 'TEXT',
                    # EXAMPLES:
                    # 'R1 Reactive alkyl halides' , 'R1 Reactive alkyl halides' , 'R1 Reactive alkyl halides' , 'R1 Reac
                    # tive alkyl halides' , 'R1 Reactive alkyl halides' , 'R1 Reactive alkyl halides' , 'R1 Reactive alk
                    # yl halides' , 'R1 Reactive alkyl halides' , 'R1 Reactive alkyl halides' , 'R1 Reactive alkyl halid
                    # es'
                    'alert_set': 
                    {
                        'properties': 
                        {
                            'priority': 'NUMERIC',
                            # EXAMPLES:
                            # '8' , '8' , '8' , '8' , '8' , '8' , '8' , '8' , '8' , '8'
                            'set_name': 'TEXT',
                            # EXAMPLES:
                            # 'Glaxo' , 'Glaxo' , 'Glaxo' , 'Glaxo' , 'Glaxo' , 'Glaxo' , 'Glaxo' , 'Glaxo' , 'Glaxo' , 
                            # 'Glaxo'
                        }
                    },
                    'smarts': 'TEXT',
                    # EXAMPLES:
                    # '[Br,Cl,I][CX4;CH,CH2]' , '[Br,Cl,I][CX4;CH,CH2]' , '[Br,Cl,I][CX4;CH,CH2]' , '[Br,Cl,I][CX4;CH,CH
                    # 2]' , '[Br,Cl,I][CX4;CH,CH2]' , '[Br,Cl,I][CX4;CH,CH2]' , '[Br,Cl,I][CX4;CH,CH2]' , '[Br,Cl,I][CX4
                    # ;CH,CH2]' , '[Br,Cl,I][CX4;CH,CH2]' , '[Br,Cl,I][CX4;CH,CH2]'
                }
            },
            'cpd_str_alert_id': 'NUMERIC',
            # EXAMPLES:
            # '45615903' , '45615905' , '45615909' , '45615916' , '45615922' , '45615928' , '45615929' , '45615933' , '4
            # 5615937' , '45615938'
            'molecule_chembl_id': 'TEXT',
            # EXAMPLES:
            # 'CHEMBL391973' , 'CHEMBL246568' , 'CHEMBL246773' , 'CHEMBL395676' , 'CHEMBL245651' , 'CHEMBL399509' , 'CHE
            # MBL398896' , 'CHEMBL246997' , 'CHEMBL397134' , 'CHEMBL247589'
        }
    }
