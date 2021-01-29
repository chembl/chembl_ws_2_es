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
            'level1': 'TEXT',
            # EXAMPLES:
            # 'P' , 'P' , 'P' , 'P' , 'P' , 'P' , 'P' , 'P' , 'P' , 'P'
            'level1_description': 'TEXT',
            # EXAMPLES:
            # 'ANTIPARASITIC PRODUCTS, INSECTICIDES AND REPELLENTS' , 'ANTIPARASITIC PRODUCTS, INSECTICIDES AND REPELLEN
            # TS' , 'ANTIPARASITIC PRODUCTS, INSECTICIDES AND REPELLENTS' , 'ANTIPARASITIC PRODUCTS, INSECTICIDES AND RE
            # PELLENTS' , 'ANTIPARASITIC PRODUCTS, INSECTICIDES AND REPELLENTS' , 'ANTIPARASITIC PRODUCTS, INSECTICIDES 
            # AND REPELLENTS' , 'ANTIPARASITIC PRODUCTS, INSECTICIDES AND REPELLENTS' , 'ANTIPARASITIC PRODUCTS, INSECTI
            # CIDES AND REPELLENTS' , 'ANTIPARASITIC PRODUCTS, INSECTICIDES AND REPELLENTS' , 'ANTIPARASITIC PRODUCTS, I
            # NSECTICIDES AND REPELLENTS'
            'level2': 'TEXT',
            # EXAMPLES:
            # 'P01' , 'P01' , 'P01' , 'P01' , 'P01' , 'P01' , 'P01' , 'P01' , 'P01' , 'P01'
            'level2_description': 'TEXT',
            # EXAMPLES:
            # 'ANTIPROTOZOALS' , 'ANTIPROTOZOALS' , 'ANTIPROTOZOALS' , 'ANTIPROTOZOALS' , 'ANTIPROTOZOALS' , 'ANTIPROTOZ
            # OALS' , 'ANTIPROTOZOALS' , 'ANTIPROTOZOALS' , 'ANTIPROTOZOALS' , 'ANTIPROTOZOALS'
            'level3': 'TEXT',
            # EXAMPLES:
            # 'P01A' , 'P01A' , 'P01A' , 'P01A' , 'P01A' , 'P01A' , 'P01A' , 'P01A' , 'P01A' , 'P01A'
            'level3_description': 'TEXT',
            # EXAMPLES:
            # 'AGENTS AGAINST AMOEBIASIS AND OTHER PROTOZOAL DISEASES' , 'AGENTS AGAINST AMOEBIASIS AND OTHER PROTOZOAL 
            # DISEASES' , 'AGENTS AGAINST AMOEBIASIS AND OTHER PROTOZOAL DISEASES' , 'AGENTS AGAINST AMOEBIASIS AND OTHE
            # R PROTOZOAL DISEASES' , 'AGENTS AGAINST AMOEBIASIS AND OTHER PROTOZOAL DISEASES' , 'AGENTS AGAINST AMOEBIA
            # SIS AND OTHER PROTOZOAL DISEASES' , 'AGENTS AGAINST AMOEBIASIS AND OTHER PROTOZOAL DISEASES' , 'AGENTS AGA
            # INST AMOEBIASIS AND OTHER PROTOZOAL DISEASES' , 'AGENTS AGAINST AMOEBIASIS AND OTHER PROTOZOAL DISEASES' ,
            #  'AGENTS AGAINST AMOEBIASIS AND OTHER PROTOZOAL DISEASES'
            'level4': 'TEXT',
            # EXAMPLES:
            # 'P01AA' , 'P01AA' , 'P01AA' , 'P01AA' , 'P01AB' , 'P01AB' , 'P01AB' , 'P01AB' , 'P01AB' , 'P01AB'
            'level4_description': 'TEXT',
            # EXAMPLES:
            # 'Hydroxyquinoline derivatives' , 'Hydroxyquinoline derivatives' , 'Hydroxyquinoline derivatives' , 'Hydrox
            # yquinoline derivatives' , 'Nitroimidazole derivatives' , 'Nitroimidazole derivatives' , 'Nitroimidazole de
            # rivatives' , 'Nitroimidazole derivatives' , 'Nitroimidazole derivatives' , 'Nitroimidazole derivatives'
            'level5': 'TEXT',
            # EXAMPLES:
            # 'P01AA02' , 'P01AA04' , 'P01AA05' , 'P01AA52' , 'P01AB01' , 'P01AB02' , 'P01AB03' , 'P01AB04' , 'P01AB05' 
            # , 'P01AB06'
            'who_name': 'TEXT',
            # EXAMPLES:
            # 'clioquinol' , 'chlorquinaldol' , 'tilbroquinol' , 'clioquinol, combinations' , 'metronidazole' , 'tinidaz
            # ole' , 'ornidazole' , 'azanidazole' , 'propenidazole' , 'nimorazole'
        }
    }
