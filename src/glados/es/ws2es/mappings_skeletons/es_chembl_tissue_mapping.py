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
            '_metadata': 
            {
                'properties': 
                {
                    'es_completion': 'TEXT',
                    # EXAMPLES:
                    # '{'input': 'BTO:0001421', 'weight': 10}' , '{'input': 'TS-2037', 'weight': 10}' , '{'input': 'CHEM
                    # BL4296343', 'weight': 10}' , '{'input': 'BTO:0001073', 'weight': 10}' , '{'input': 'Submucosa', 'w
                    # eight': 100}' , '{'input': 'UBERON:0000014', 'weight': 10}' , '{'input': 'CHEMBL3988049', 'weight'
                    # : 10}' , '{'input': 'Tube', 'weight': 100}' , '{'input': 'UBERON:0000029', 'weight': 10}' , '{'inp
                    # ut': 'Lamina propria', 'weight': 100}'
                }
            },
            'bto_id': 'TEXT',
            # EXAMPLES:
            # 'BTO:0001421' , 'BTO:0000840' , 'BTO:0000991' , 'BTO:0001073' , 'BTO:0002107' , 'BTO:0001463' , 'BTO:00007
            # 84' , 'BTO:0002330' , 'BTO:0000282' , 'BTO:0001356'
            'caloha_id': 'TEXT',
            # EXAMPLES:
            # 'TS-0134' , 'TS-2037' , 'TS-0741' , 'TS-0798' , 'TS-0579' , 'TS-0436' , 'TS-1021' , 'TS-0954' , 'TS-0397' 
            # , 'TS-1084'
            'efo_id': 'TEXT',
            # EXAMPLES:
            # 'EFO:0000979' , 'EFO:0000856' , 'EFO:0000857' , 'EFO:0000885' , 'EFO:0000872' , 'EFO:0000964' , 'EFO:00009
            # 00' , 'EFO:0000899' , 'EFO:0000930' , 'EFO:0000931'
            'pref_name': 'TEXT',
            # EXAMPLES:
            # 'Uterine cervix' , 'Nose' , 'Islets of langerhans' , 'Pituitary gland' , 'Submucosa' , 'Zone of skin' , 'W
            # ing' , 'Tube' , 'Lymph node' , 'Lamina propria'
            'tissue_chembl_id': 'TEXT',
            # EXAMPLES:
            # 'CHEMBL3988026' , 'CHEMBL3987869' , 'CHEMBL4296343' , 'CHEMBL3638173' , 'CHEMBL3987982' , 'CHEMBL3638174' 
            # , 'CHEMBL3988049' , 'CHEMBL3988015' , 'CHEMBL3638175' , 'CHEMBL3987795'
            'uberon_id': 'TEXT',
            # EXAMPLES:
            # 'UBERON:0000002' , 'UBERON:0000004' , 'UBERON:0000006' , 'UBERON:0000007' , 'UBERON:0000009' , 'UBERON:000
            # 0014' , 'UBERON:0000023' , 'UBERON:0000025' , 'UBERON:0000029' , 'UBERON:0000030'
        }
    }
