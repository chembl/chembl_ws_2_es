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
            'drugind_id': 'NUMERIC',
            # EXAMPLES:
            # '22606' , '22607' , '22608' , '22609' , '22610' , '22612' , '22613' , '22614' , '22615' , '22617'
            'efo_id': 'TEXT',
            # EXAMPLES:
            # 'EFO:0000404' , 'EFO:0000685' , 'EFO:0002690' , 'EFO:0000612' , 'EFO:0001663' , 'EFO:0000400' , 'EFO:00001
            # 95' , 'EFO:0003095' , 'EFO:0001360' , 'HP:0001945'
            'efo_term': 'TEXT',
            # EXAMPLES:
            # 'diffuse scleroderma' , 'rheumatoid arthritis' , 'systemic lupus erythematosus' , 'myocardial infarction' 
            # , 'prostate carcinoma' , 'diabetes mellitus' , 'metabolic syndrome' , 'non-alcoholic fatty liver disease' 
            # , 'type II diabetes mellitus' , 'Fever'
            'indication_refs': 
            {
                'properties': 
                {
                    'ref_id': 'TEXT',
                    # EXAMPLES:
                    # 'NCT00442611,NCT02161406' , 'NCT00048568,NCT00048581,NCT00048932,NCT00095147,NCT00122382,NCT001244
                    # 49,NCT00124982,NCT00162201,NCT00162266,NCT00162279,NCT00254293,NCT00279734,NCT00279760,NCT00345748
                    # ,NCT00409838,NCT00420199,NCT00484289,NCT00533897,NCT00547521,NCT00559585,NCT00663702,NCT00767325,N
                    # CT00929864,NCT00989235,NCT01001832,NCT01142726,NCT01221636,NCT01299961,NCT01333878,NCT01350804,NCT
                    # 01351480,NCT01439204,NCT01844895,NCT01890473,NCT02504268,NCT02722694,NCT02805010,NCT03086343,NCT03
                    # 784261,NCT04120831' , 'NCT00119678,NCT00430677,NCT00774852,NCT02270957' , 'NCT00046228,NCT00299377
                    # ,NCT00426751,NCT00638638,NCT02181985' , 'NCT00473746,NCT00474383,NCT00544440,NCT00600535,NCT009107
                    # 54,NCT01017939,NCT01217697,NCT01400555,NCT01576172,NCT01664728,NCT01695135,NCT01715285,NCT01834209
                    # ,NCT02160353,NCT03902951' , 'A10BF01' , 'NCT00629213' , 'NCT00677521' , 'NCT00000620,NCT00551954,N
                    # CT01177384,NCT01245166,NCT01316861,NCT01388153,NCT01514838,NCT01554631,NCT01728740,NCT01839344,NCT
                    # 02315495,NCT03349684,NCT04065581' , 'N02BE01'
                    'ref_type': 'TEXT',
                    # EXAMPLES:
                    # 'ClinicalTrials' , 'ClinicalTrials' , 'ClinicalTrials' , 'ClinicalTrials' , 'ClinicalTrials' , 'AT
                    # C' , 'ClinicalTrials' , 'ClinicalTrials' , 'ClinicalTrials' , 'ATC'
                    'ref_url': 'TEXT',
                    # EXAMPLES:
                    # 'https://clinicaltrials.gov/search?id=%22NCT00442611%22OR%22NCT02161406%22' , 'https://clinicaltri
                    # als.gov/search?id=%22NCT00048568%22OR%22NCT00048581%22OR%22NCT00048932%22OR%22NCT00095147%22OR%22N
                    # CT00122382%22OR%22NCT00124449%22OR%22NCT00124982%22OR%22NCT00162201%22OR%22NCT00162266%22OR%22NCT0
                    # 0162279%22OR%22NCT00254293%22OR%22NCT00279734%22OR%22NCT00279760%22OR%22NCT00345748%22OR%22NCT0040
                    # 9838%22OR%22NCT00420199%22OR%22NCT00484289%22OR%22NCT00533897%22OR%22NCT00547521%22OR%22NCT0055958
                    # 5%22OR%22NCT00663702%22OR%22NCT00767325%22OR%22NCT00929864%22OR%22NCT00989235%22OR%22NCT01001832%2
                    # 2OR%22NCT01142726%22OR%22NCT01221636%22OR%22NCT01299961%22OR%22NCT01333878%22OR%22NCT01350804%22OR
                    # %22NCT01351480%22OR%22NCT01439204%22OR%22NCT01844895%22OR%22NCT01890473%22OR%22NCT02504268%22OR%22
                    # NCT02722694%22OR%22NCT02805010%22OR%22NCT03086343%22OR%22NCT03784261%22OR%22NCT04120831%22' , 'htt
                    # ps://clinicaltrials.gov/search?id=%22NCT00119678%22OR%22NCT00430677%22OR%22NCT00774852%22OR%22NCT0
                    # 2270957%22' , 'https://clinicaltrials.gov/search?id=%22NCT00046228%22OR%22NCT00299377%22OR%22NCT00
                    # 426751%22OR%22NCT00638638%22OR%22NCT02181985%22' , 'https://clinicaltrials.gov/search?id=%22NCT004
                    # 73746%22OR%22NCT00474383%22OR%22NCT00544440%22OR%22NCT00600535%22OR%22NCT00910754%22OR%22NCT010179
                    # 39%22OR%22NCT01217697%22OR%22NCT01400555%22OR%22NCT01576172%22OR%22NCT01664728%22OR%22NCT01695135%
                    # 22OR%22NCT01715285%22OR%22NCT01834209%22OR%22NCT02160353%22OR%22NCT03902951%22' , 'http://www.whoc
                    # c.no/atc_ddd_index/?code=A10BF01' , 'https://clinicaltrials.gov/search?id=%22NCT00629213%22' , 'ht
                    # tps://clinicaltrials.gov/search?id=%22NCT00677521%22' , 'https://clinicaltrials.gov/search?id=%22N
                    # CT00000620%22OR%22NCT00551954%22OR%22NCT01177384%22OR%22NCT01245166%22OR%22NCT01316861%22OR%22NCT0
                    # 1388153%22OR%22NCT01514838%22OR%22NCT01554631%22OR%22NCT01728740%22OR%22NCT01839344%22OR%22NCT0231
                    # 5495%22OR%22NCT03349684%22OR%22NCT04065581%22' , 'http://www.whocc.no/atc_ddd_index/?code=N02BE01'
                }
            },
            'max_phase_for_ind': 'NUMERIC',
            # EXAMPLES:
            # '2' , '4' , '2' , '3' , '4' , '4' , '3' , '2' , '4' , '4'
            'mesh_heading': 'TEXT',
            # EXAMPLES:
            # 'Scleroderma, Diffuse' , 'Arthritis, Rheumatoid' , 'Lupus Erythematosus, Systemic' , 'Myocardial Infarctio
            # n' , 'Prostatic Neoplasms' , 'Diabetes Mellitus' , 'Metabolic Syndrome' , 'Non-alcoholic Fatty Liver Disea
            # se' , 'Diabetes Mellitus, Type 2' , 'Fever'
            'mesh_id': 'TEXT',
            # EXAMPLES:
            # 'D045743' , 'D001172' , 'D008180' , 'D009203' , 'D011471' , 'D003920' , 'D024821' , 'D065626' , 'D003924' 
            # , 'D005334'
            'molecule_chembl_id': 'TEXT',
            # EXAMPLES:
            # 'CHEMBL1201823' , 'CHEMBL1201823' , 'CHEMBL1201823' , 'CHEMBL1201584' , 'CHEMBL271227' , 'CHEMBL1566' , 'C
            # HEMBL1566' , 'CHEMBL1566' , 'CHEMBL1566' , 'CHEMBL112'
            'parent_molecule_chembl_id': 'TEXT',
            # EXAMPLES:
            # 'CHEMBL1201823' , 'CHEMBL1201823' , 'CHEMBL1201823' , 'CHEMBL1201584' , 'CHEMBL271227' , 'CHEMBL1566' , 'C
            # HEMBL1566' , 'CHEMBL1566' , 'CHEMBL1566' , 'CHEMBL112'
        }
    }
