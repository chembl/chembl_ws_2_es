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
            # 'X' , 'V' , 'IX' , 'XIX' , 'Tylosin' , 'Rosaramicin' , 'XII' , 'XIV' , 'XVII' , '7'
            'compound_name': 'TEXT',
            # EXAMPLES:
            # 'Bis(3-[14-Benzyl-11-(1H-indol-3-ylmethyl)-2-isobutyl-13-methyl-5-(2-methylsulfanyl-ethyl)-3,6,9,12,15,20-
            # hexaoxo-1,4,7,10,13,16-hexaaza-bicyclo[15.2.1]icos-18-en-8-yl]-propionamide)' , '3-[11,14-Dibenzyl-2-isobu
            # tyl-5-(2-methylsulfanyl-ethyl)-3,6,9,12,15,20-hexaoxo-1,4,7,10,13,16-hexaaza-bicyclo[15.2.1]icos-18-en-8-y
            # l]-propionamide' , '3-[14-Benzyl-11-(1H-indol-3-ylmethyl)-2-isobutyl-13-methyl-5-(2-methylsulfanyl-ethyl)-
            # 3,6,9,12,15,20-hexaoxo-1,4,7,10,13,16-hexaaza-bicyclo[15.2.1]icos-18-en-8-yl]-propionamide' , '3-[5-Benzyl
            # -8-(1H-indol-3-ylmethyl)-17-isobutyl-14-(2-methylsulfanyl-ethyl)-4,7,10,13,16,19-hexaoxo-octadecahydro-3a,
            # 6,9,12,15,18-hexaaza-cyclopentacyclooctadecen-11-yl]-propionamide' , 'Tylosin' , '[(E)-(1S,2R,3R,7R,8S,9S,
            # 10R,12R,16S)-9-((2S,3R,4S,6R)-4-Dimethylamino-3-hydroxy-6-methyl-tetrahydro-pyran-2-yloxy)-3-ethyl-7-hydro
            # xy-2,8,12,16-tetramethyl-5,13-dioxo-4,17-dioxa-bicyclo[14.1.0]heptadec-14-en-10-yl]-acetaldehyde' , '3-[17
            # ,20-Dibenzyl-2-isobutyl-5-(2-methylsulfanyl-ethyl)-3,6,12,15,18,21,26-heptaoxo-1,4,7,13,16,19,22-heptaaza-
            # tricyclo[21.2.1.0*7,11*]hexacos-24-en-14-yl]-propionamide' , '3-[17-Benzyl-14-(4-hydroxy-benzyl)-2-isobuty
            # l-5-(2-methylsulfanyl-ethyl)-3,6,9,12,15,18,23-heptaoxo-1,4,7,10,13,16,19-heptaaza-bicyclo[18.2.1]tricos-2
            # 1-en-11-yl]-propionamide' , '3-[8-Benzyl-5-(1H-indol-3-ylmethyl)-14-isobutyl-17-(2-methylsulfanyl-ethyl)-3
            # ,6,9,12,15,18-hexaoxo-1,4,7,10,13,16hexaaza-cyclooctadec-2-yl]-propionamide' , '(11E,13E)-(5S,6S,7R,9R,15S
            # ,16R)-7-(2-Azepan-1-yl-ethyl)-6-((2S,3R,4S,6R)-4-dimethylamino-3-hydroxy-6-methyl-tetrahydro-pyran-2-yloxy
            # )-16-ethyl-4-hydroxy-5,9,13,15-tetramethyl-oxacyclohexadeca-11,13-diene-2,10-dione'
            'document_chembl_id': 'TEXT',
            # EXAMPLES:
            # 'CHEMBL1126670' , 'CHEMBL1126670' , 'CHEMBL1126670' , 'CHEMBL1126670' , 'CHEMBL1130408' , 'CHEMBL1130408' 
            # , 'CHEMBL1126670' , 'CHEMBL1126670' , 'CHEMBL1126670' , 'CHEMBL1130408'
            'molecule_chembl_id': 'TEXT',
            # EXAMPLES:
            # 'CHEMBL3349687' , 'CHEMBL3349799' , 'CHEMBL3349688' , 'CHEMBL3349619' , 'CHEMBL42743' , 'CHEMBL8965' , 'CH
            # EMBL3349462' , 'CHEMBL3349511' , 'CHEMBL3349620' , 'CHEMBL266595'
            'record_id': 'NUMERIC',
            # EXAMPLES:
            # '1' , '2' , '3' , '6' , '5005' , '5007' , '9' , '10' , '11' , '5014'
            'src_id': 'NUMERIC',
            # EXAMPLES:
            # '1' , '1' , '1' , '1' , '1' , '1' , '1' , '1' , '1' , '1'
        }
    }
