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
            # '26' , 'BA16' , 'BA18' , 'BA19' , 'BA47' , 'BA48' , 'BA62' , 'BA63' , 'BA90' , 'BA94'
            'compound_name': 'TEXT',
            # EXAMPLES:
            # '3-(3-(3-carbamimidoylphenyl)isoxazol-5-yl)-4-methoxybenzimidamide dihydrochloride' , '1-butyl-5-(4-methox
            # ybenzoyl)pyrimidine-2,4,6(1H,3H,5H)-trione' , '2,4,6-trioxohexahydropyrimidine-5-carbaldehyde' , '1-methyl
            # -2,4,6-trioxohexahydropyrimidine-5-carbaldehyde' , '5-(2-hydroxybenzylidene)pyrimidine-2,4,6-trione' , '5-
            # (2,4-dihydroxybenzylidene)-1,3-dimethylpyrimidine-2,4,6(1H,3H,5H)-trione' , '5-cyclohexylpyrimidine-2,4,6(
            # 1H,3H,5H)-trione' , '5-(3-cyclohexylpropyl)pyrimidine-2,4,6(1H,3H,5H)-trione' , '1,3-dimethyl-5-[(E)-(phen
            # ylimino)methyl]pyrimidine-2,4,6-trione' , '5-{(E)-[(2-hydroxyphenyl)imino]methyl}-1,3-dimethylpyrimidine-2
            # ,4,6-trione'
            'document_chembl_id': 'TEXT',
            # EXAMPLES:
            # 'CHEMBL3102749' , 'CHEMBL3102843' , 'CHEMBL3102843' , 'CHEMBL3102843' , 'CHEMBL3102843' , 'CHEMBL3102843' 
            # , 'CHEMBL3102843' , 'CHEMBL3102843' , 'CHEMBL3102843' , 'CHEMBL3102843'
            'molecule_chembl_id': 'TEXT',
            # EXAMPLES:
            # 'CHEMBL3216374' , 'CHEMBL3103692' , 'CHEMBL3103694' , 'CHEMBL3103695' , 'CHEMBL577056' , 'CHEMBL3103700' ,
            #  'CHEMBL3103706' , 'CHEMBL3103707' , 'CHEMBL3102867' , 'CHEMBL3103729'
            'record_id': 'NUMERIC',
            # EXAMPLES:
            # '1958437' , '1958444' , '1958446' , '1958447' , '1958458' , '1958459' , '1958469' , '1958470' , '1958491' 
            # , '1958495'
            'src_id': 'NUMERIC',
            # EXAMPLES:
            # '1' , '1' , '1' , '1' , '1' , '1' , '1' , '1' , '1' , '1'
        }
    }
