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
            # '34544046' , '34544047' , '34544048' , '34544049' , '34544050' , '34544051' , '34544052' , '34544053' , '3
            # 4544054' , '34544055'
            'molecule_chembl_id': 'TEXT',
            # EXAMPLES:
            # 'CHEMBL2205881' , 'CHEMBL2205882' , 'CHEMBL2206028' , 'CHEMBL2206762' , 'CHEMBL2216877' , 'CHEMBL2219513' 
            # , 'CHEMBL2219607' , 'CHEMBL2219650' , 'CHEMBL2219694' , 'CHEMBL2219698'
        }
    }
