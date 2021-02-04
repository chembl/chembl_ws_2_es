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
                    # '17' , '17' , '6' , '1' , '17' , '17' , '17' , '17' , '17' , '17'
                    'alert_name': 'TEXT',
                    # EXAMPLES:
                    # 'R17 acylhydrazide' , 'R17 acylhydrazide' , 'R6 Acid anhydrides' , 'R1 Reactive alkyl halides' , '
                    # R17 acylhydrazide' , 'R17 acylhydrazide' , 'R17 acylhydrazide' , 'R17 acylhydrazide' , 'R17 acylhy
                    # drazide' , 'R17 acylhydrazide'
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
                    # '[N;R0][N;R0]C(=O)' , '[N;R0][N;R0]C(=O)' , 'C(=O)OC(=O)' , '[Br,Cl,I][CX4;CH,CH2]' , '[N;R0][N;R0
                    # ]C(=O)' , '[N;R0][N;R0]C(=O)' , '[N;R0][N;R0]C(=O)' , '[N;R0][N;R0]C(=O)' , '[N;R0][N;R0]C(=O)' , 
                    # '[N;R0][N;R0]C(=O)'
                }
            },
            'cpd_str_alert_id': 'NUMERIC',
            # EXAMPLES:
            # '45642224' , '45652083' , '45628085' , '45623089' , '45652209' , '45642227' , '45642569' , '45638026' , '4
            # 5652429' , '45657296'
            'molecule_chembl_id': 'TEXT',
            # EXAMPLES:
            # 'CHEMBL575545' , 'CHEMBL1966168' , 'CHEMBL1305819' , 'CHEMBL3219166' , 'CHEMBL1968352' , 'CHEMBL568037' , 
            # 'CHEMBL595427' , 'CHEMBL51996' , 'CHEMBL1972257' , 'CHEMBL2414862'
        }
    }
