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
            # '55747' , '25275' , '55748' , '25276' , '55749' , '25279' , '55750' , '25283' , '55751' , '25284'
            'efo_id': 'TEXT',
            # EXAMPLES:
            # 'EFO:0007445' , 'EFO:0005532' , 'Orphanet:77' , 'Orphanet:91378' , 'Orphanet:98878' , 'Orphanet:355' , 'Or
            # phanet:98879' , 'EFO:0001360' , 'Orphanet:98895' , 'EFO:0003907'
            'efo_term': 'TEXT',
            # EXAMPLES:
            # 'Plasmodium vivax malaria' , 'angioedema' , 'Aniridia' , 'Hereditary angioedema' , 'Hemophilia A' , 'Gauch
            # er disease' , 'Hemophilia B' , 'type II diabetes mellitus' , 'Becker muscular dystrophy' , 'deep vein thro
            # mbosis'
            'indication_refs': 
            {
                'properties': 
                {
                    'ref_id': 'TEXT',
                    # EXAMPLES:
                    # 'NCT01625871,NCT02184637,NCT02348788' , 'NCT01036659,NCT01343823' , 'NCT02647359,NCT04117880' , 'B
                    # 06AC03' , 'NCT00947193' , 'NCT00358150,NCT00891202,NCT00943111,NCT01074944' , 'NCT00947193' , 'NCT
                    # 00558571,NCT00749190,NCT00789035,NCT00881530,NCT00885118,NCT01011868,NCT01131676,NCT01159600,NCT01
                    # 167881,NCT01177813,NCT01193218,NCT01210001,NCT01248364,NCT01257334,NCT01276288,NCT01289990,NCT0136
                    # 8081,NCT01422876,NCT01649297,NCT01734785,NCT01778049,NCT01867307,NCT01907113,NCT01924767,NCT019478
                    # 55,NCT01984606,NCT02121483,NCT02453555,NCT02471963,NCT02489968,NCT02752113,NCT02854748,NCT02863328
                    # ,NCT02890745,NCT03060980,NCT03118336,NCT03132181,NCT03351478,NCT03429543,NCT03565458,NCT04195243,N
                    # CT04233801' , 'NCT00592553,NCT00847379,NCT01009294,NCT01557400' , 'NCT00839163,NCT01662908,NCT0188
                    # 0216,NCT02368314,NCT03003390,NCT03299296'
                    'ref_type': 'TEXT',
                    # EXAMPLES:
                    # 'ClinicalTrials' , 'ClinicalTrials' , 'ClinicalTrials' , 'ATC' , 'ClinicalTrials' , 'ClinicalTrial
                    # s' , 'ClinicalTrials' , 'ClinicalTrials' , 'ClinicalTrials' , 'ClinicalTrials'
                    'ref_url': 'TEXT',
                    # EXAMPLES:
                    # 'https://clinicaltrials.gov/search?id=%22NCT01625871%22OR%22NCT02184637%22OR%22NCT02348788%22' , '
                    # https://clinicaltrials.gov/search?id=%22NCT01036659%22OR%22NCT01343823%22' , 'https://clinicaltria
                    # ls.gov/search?id=%22NCT02647359%22OR%22NCT04117880%22' , 'http://www.whocc.no/atc_ddd_index/?code=
                    # B06AC03' , 'https://clinicaltrials.gov/search?id=%22NCT00947193%22' , 'https://clinicaltrials.gov/
                    # search?id=%22NCT00358150%22OR%22NCT00891202%22OR%22NCT00943111%22OR%22NCT01074944%22' , 'https://c
                    # linicaltrials.gov/search?id=%22NCT00947193%22' , 'https://clinicaltrials.gov/search?id=%22NCT00558
                    # 571%22OR%22NCT00749190%22OR%22NCT00789035%22OR%22NCT00881530%22OR%22NCT00885118%22OR%22NCT01011868
                    # %22OR%22NCT01131676%22OR%22NCT01159600%22OR%22NCT01167881%22OR%22NCT01177813%22OR%22NCT01193218%22
                    # OR%22NCT01210001%22OR%22NCT01248364%22OR%22NCT01257334%22OR%22NCT01276288%22OR%22NCT01289990%22OR%
                    # 22NCT01368081%22OR%22NCT01422876%22OR%22NCT01649297%22OR%22NCT01734785%22OR%22NCT01778049%22OR%22N
                    # CT01867307%22OR%22NCT01907113%22OR%22NCT01924767%22OR%22NCT01947855%22OR%22NCT01984606%22OR%22NCT0
                    # 2121483%22OR%22NCT02453555%22OR%22NCT02471963%22OR%22NCT02489968%22OR%22NCT02752113%22OR%22NCT0285
                    # 4748%22OR%22NCT02863328%22OR%22NCT02890745%22OR%22NCT03060980%22OR%22NCT03118336%22OR%22NCT0313218
                    # 1%22OR%22NCT03351478%22OR%22NCT03429543%22OR%22NCT03565458%22OR%22NCT04195243%22OR%22NCT04233801%2
                    # 2' , 'https://clinicaltrials.gov/search?id=%22NCT00592553%22OR%22NCT00847379%22OR%22NCT01009294%22
                    # OR%22NCT01557400%22' , 'https://clinicaltrials.gov/search?id=%22NCT00839163%22OR%22NCT01662908%22O
                    # R%22NCT01880216%22OR%22NCT02368314%22OR%22NCT03003390%22OR%22NCT03299296%22'
                }
            },
            'max_phase_for_ind': 'NUMERIC',
            # EXAMPLES:
            # '3' , '2' , '2' , '4' , '2' , '4' , '2' , '4' , '3' , '4'
            'mesh_heading': 'TEXT',
            # EXAMPLES:
            # 'Malaria, Vivax' , 'Angioedema' , 'Aniridia' , 'Angioedemas, Hereditary' , 'Hemophilia A' , 'Gaucher Disea
            # se' , 'Hemophilia B' , 'Diabetes Mellitus, Type 2' , 'Muscular Dystrophy, Duchenne' , 'Venous Thrombosis'
            'mesh_id': 'TEXT',
            # EXAMPLES:
            # 'D016780' , 'D000799' , 'D015783' , 'D054179' , 'D006467' , 'D005776' , 'D002836' , 'D003924' , 'D020388' 
            # , 'D020246'
            'molecule_chembl_id': 'TEXT',
            # EXAMPLES:
            # 'CHEMBL566534' , 'CHEMBL1201837' , 'CHEMBL256997' , 'CHEMBL1201837' , 'CHEMBL256997' , 'CHEMBL4297066' , '
            # CHEMBL256997' , 'CHEMBL2107830' , 'CHEMBL256997' , 'CHEMBL1201476'
            'parent_molecule_chembl_id': 'TEXT',
            # EXAMPLES:
            # 'CHEMBL566534' , 'CHEMBL1201837' , 'CHEMBL256997' , 'CHEMBL1201837' , 'CHEMBL256997' , 'CHEMBL2110588' , '
            # CHEMBL256997' , 'CHEMBL2107830' , 'CHEMBL256997' , 'CHEMBL1201476'
        }
    }
