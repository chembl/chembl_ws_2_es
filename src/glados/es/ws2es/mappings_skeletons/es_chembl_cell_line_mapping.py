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
                    # '{'input': 'DC3F', 'weight': 100}' , '{'input': 'CHEMBL3307242', 'weight': 10}' , '{'input': 'CVCL
                    # _N513', 'weight': 10}' , '{'input': 'Carcinoma', 'weight': 30}' , '{'input': 'CVCL_1783', 'weight'
                    # : 10}' , '{'input': 'Lung', 'weight': 30}' , '{'input': 'Leukaemia', 'weight': 30}' , '{'input': '
                    # Rattus norvegicus', 'weight': 30}' , '{'input': 'CVCL_3620', 'weight': 10}' , '{'input': 'Colon Ad
                    # enocarcinoma', 'weight': 30}'
                }
            },
            'cell_chembl_id': 'TEXT',
            # EXAMPLES:
            # 'CHEMBL3307241' , 'CHEMBL3307242' , 'CHEMBL3307243' , 'CHEMBL3307244' , 'CHEMBL3307245' , 'CHEMBL3307246' 
            # , 'CHEMBL3307247' , 'CHEMBL3307248' , 'CHEMBL3307249' , 'CHEMBL3307250'
            'cell_description': 'TEXT',
            # EXAMPLES:
            # 'DC3F' , 'P3HR-1' , 'UCLA P-3' , 'UMSCC22B' , 'UMUC3' , 'V79-4' , 'VCR100' , 'W256' , 'WEHI265.1' , 'WiDr-
            # NTR'
            'cell_id': 'NUMERIC',
            # EXAMPLES:
            # '1' , '2' , '3' , '4' , '5' , '6' , '7' , '8' , '9' , '10'
            'cell_name': 'TEXT',
            # EXAMPLES:
            # 'DC3F' , 'P3HR-1' , 'UCLA P-3' , 'UMSCC22B' , 'UMUC3' , 'V79-4' , 'VCR100' , 'W256' , 'WEHI265.1' , 'WiDr-
            # NTR'
            'cell_source_organism': 'TEXT',
            # EXAMPLES:
            # 'Cricetulus griseus' , 'Homo sapiens' , 'Homo sapiens' , 'Homo sapiens' , 'Homo sapiens' , 'Cricetulus gri
            # seus' , 'Mus musculus' , 'Rattus norvegicus' , 'Mus musculus' , 'Homo sapiens'
            'cell_source_tax_id': 'NUMERIC',
            # EXAMPLES:
            # '10029' , '9606' , '9606' , '9606' , '9606' , '10029' , '10090' , '10116' , '10090' , '9606'
            'cell_source_tissue': 'TEXT',
            # EXAMPLES:
            # 'Lung' , 'Lyphoma' , 'Lung Adenocarcinoma' , 'Carcinoma' , 'Bladder Carcinoma' , 'Lung' , 'Leukaemia' , 'M
            # onocytic Carcinosarcoma' , 'Macrophage' , 'Colon Adenocarcinoma'
            'cellosaurus_id': 'TEXT',
            # EXAMPLES:
            # 'CVCL_4704' , 'CVCL_2676' , 'CVCL_N513' , 'CVCL_7732' , 'CVCL_1783' , 'CVCL_2796' , 'CVCL_3537' , 'CVCL_36
            # 20' , 'CVCL_1891' , 'CVCL_1794'
            'cl_lincs_id': 'TEXT',
            # EXAMPLES:
            # 'LCL-2024' , 'LCL-1721' , 'LCL-1792' , 'LCL-1511' , 'LCL-1031' , 'LCL-2001' , 'LCL-1514' , 'LCL-1889' , 'L
            # CL-1166' , 'LCL-1734'
            'clo_id': 'TEXT',
            # EXAMPLES:
            # 'CLO_0008331' , 'CLO_0009487' , 'CLO_0009504' , 'CLO_0007335' , 'CLO_0009576' , 'CLO_0009645' , 'CLO_00097
            # 11' , 'CLO_0003434' , 'CLO_0007018' , 'CLO_0050994'
            'efo_id': 'TEXT',
            # EXAMPLES:
            # 'EFO_0002312' , 'EFO_0002387' , 'EFO_0006778' , 'EFO_0002179' , 'EFO_0006703' , 'EFO_0002344' , 'EFO_00023
            # 77' , 'EFO_0002084' , 'EFO_0006562' , 'EFO_0002866'
        }
    }
