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
            'compound_key': 'TEXT',
            # EXAMPLES:
            # '56' , '13, (PD-135478)' , '1, BMS-201038' , 'Prazosin' , '12' , '68' , '14' , '2b' , '7b' , '31e'
            'compound_name': 'TEXT',
            # EXAMPLES:
            # '(R)-4-(1,3-Dioxo-5-phenyl-1,3-dihydro-isoindol-2-yl)-2-[(S)-3-methyl-1-((S)-1-methylcarbamoyl-2-phenyl-et
            # hylcarbamoyl)-butylamino]-butyric acid' , '1-(4-Phenyl-cyclohex-3-enyl)-4-pyridin-2-yl-piperazine' , '9-(4
            # -{4-[(4'-Trifluoromethyl-biphenyl-2-carbonyl)-amino]-piperidin-1-yl}-butyl)-9H-fluorene-9-carboxylic acid 
            # (2,2,2-trifluoro-ethyl)-amide' , '[4-(4-Amino-6,7-dimethoxy-quinazolin-2-yl)-piperazin-1-yl]-furan-2-yl-me
            # thanone' , '5-(3-Chloro-phenylcarbamoyl)-pyridine-2-carboxylic acid' , '3-(4-tert-Butyl-benzoylamino)-thio
            # phene-2-carboxylic acid (3-carbamimidoyl-phenyl)-amide' , 'N-{4-[4-(2,3-Dichloro-phenyl)-piperazin-1-yl]-b
            # ut-2-enyl}-3-iodo-benzamide' , '2-Amino-2-(4-nonyl-benzyl)-propane-1,3-diol' , '3-(2-Ethylamino-propyl)-8-
            # methyl-1,2,3,4-tetrahydro-chromeno[3,4-c]pyridin-5-one' , '7-(3-Amino-azetidin-1-yl)-1-cyclopropyl-6-fluor
            # o-4-oxo-1,4-dihydro-quinoline-3-carboxylic acid'
            'document_chembl_id': 'TEXT',
            # EXAMPLES:
            # 'CHEMBL1127698' , 'CHEMBL1151026' , 'CHEMBL1134640' , 'CHEMBL1122903' , 'CHEMBL1125385' , 'CHEMBL1132963' 
            # , 'CHEMBL1145183' , 'CHEMBL1128879' , 'CHEMBL1124631' , 'CHEMBL1126625'
            'molecule_chembl_id': 'TEXT',
            # EXAMPLES:
            # 'CHEMBL352068' , 'CHEMBL157422' , 'CHEMBL354541' , 'CHEMBL2' , 'CHEMBL167097' , 'CHEMBL172336' , 'CHEMBL17
            # 9053' , 'CHEMBL171166' , 'CHEMBL347449' , 'CHEMBL336758'
            'record_id': 'NUMERIC',
            # EXAMPLES:
            # '314501' , '309913' , '333536' , '343104' , '328433' , '338167' , '361662' , '333600' , '314566' , '328889
            # '
            'src_id': 'NUMERIC',
            # EXAMPLES:
            # '1' , '1' , '1' , '1' , '1' , '1' , '1' , '1' , '1' , '1'
        }
    }
