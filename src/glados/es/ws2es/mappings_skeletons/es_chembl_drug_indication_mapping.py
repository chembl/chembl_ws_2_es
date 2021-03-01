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
                    'all_molecule_chembl_ids': 'TEXT',
                    # EXAMPLES:
                    # 'CHEMBL4297840' , 'CHEMBL655' , 'CHEMBL1200796' , 'CHEMBL161' , 'CHEMBL236297' , 'CHEMBL4297318' ,
                    #  'CHEMBL538943' , 'CHEMBL1200523' , 'CHEMBL161' , 'CHEMBL1201631'
                }
            },
            'drugind_id': 'NUMERIC',
            # EXAMPLES:
            # '115692' , '69600' , '63241' , '69045' , '58251' , '125520' , '58126' , '41794' , '69046' , '49396'
            'efo_id': 'TEXT',
            # EXAMPLES:
            # 'EFO:0000182' , 'EFO:0003047' , 'EFO:0002617' , 'EFO:1001312' , 'EFO:0003876' , 'EFO:0004616' , 'EFO:00038
            # 69' , 'EFO:0003830' , 'EFO:1001388' , 'EFO:0001073'
            'efo_term': 'TEXT',
            # EXAMPLES:
            # 'hepatocellular carcinoma' , 'hepatitis C virus infection' , 'metastatic melanoma' , 'Endometritis' , 'int
            # ermittent vascular claudication' , 'osteoarthritis, knee' , 'breast neoplasm' , 'prostatitis' , 'Pelvic In
            # flammatory Disease' , 'obesity'
            'indication_refs': 
            {
                'properties': 
                {
                    'ref_id': 'TEXT',
                    # EXAMPLES:
                    # 'NCT03412773,NCT03419897,NCT04183088' , 'NCT00996879' , 'NCT00314106,NCT00610311,NCT00612222,NCT01
                    # 236573,NCT01319565,NCT01369875,NCT01369888,NCT01468818,NCT01495572,NCT01542255,NCT01740557,NCT0183
                    # 3767,NCT01955460,NCT01993719,NCT01995344,NCT02062359,NCT02278887,NCT02379195,NCT02489266,NCT025005
                    # 76,NCT02650986,NCT03475134,NCT03773744' , 'NCT02742948' , 'NCT00251849' , 'NCT00041756' , 'NCT0248
                    # 9409' , '06091653-e568-4e82-acc7-aefbce16de17' , 'NCT01160640' , 'NCT02237053,NCT02642523'
                    'ref_type': 'TEXT',
                    # EXAMPLES:
                    # 'ClinicalTrials' , 'ClinicalTrials' , 'ClinicalTrials' , 'ClinicalTrials' , 'ClinicalTrials' , 'Cl
                    # inicalTrials' , 'ClinicalTrials' , 'DailyMed' , 'ClinicalTrials' , 'ClinicalTrials'
                    'ref_url': 'TEXT',
                    # EXAMPLES:
                    # 'https://clinicaltrials.gov/search?id=%22NCT03412773%22OR%22NCT03419897%22OR%22NCT04183088%22' , '
                    # https://clinicaltrials.gov/search?id=%22NCT00996879%22' , 'https://clinicaltrials.gov/search?id=%2
                    # 2NCT00314106%22OR%22NCT00610311%22OR%22NCT00612222%22OR%22NCT01236573%22OR%22NCT01319565%22OR%22NC
                    # T01369875%22OR%22NCT01369888%22OR%22NCT01468818%22OR%22NCT01495572%22OR%22NCT01542255%22OR%22NCT01
                    # 740557%22OR%22NCT01833767%22OR%22NCT01955460%22OR%22NCT01993719%22OR%22NCT01995344%22OR%22NCT02062
                    # 359%22OR%22NCT02278887%22OR%22NCT02379195%22OR%22NCT02489266%22OR%22NCT02500576%22OR%22NCT02650986
                    # %22OR%22NCT03475134%22OR%22NCT03773744%22' , 'https://clinicaltrials.gov/search?id=%22NCT02742948%
                    # 22' , 'https://clinicaltrials.gov/search?id=%22NCT00251849%22' , 'https://clinicaltrials.gov/searc
                    # h?id=%22NCT00041756%22' , 'https://clinicaltrials.gov/search?id=%22NCT02489409%22' , 'http://daily
                    # med.nlm.nih.gov/dailymed/drugInfo.cfm?setid=06091653-e568-4e82-acc7-aefbce16de17' , 'https://clini
                    # caltrials.gov/search?id=%22NCT01160640%22' , 'https://clinicaltrials.gov/search?id=%22NCT02237053%
                    # 22OR%22NCT02642523%22'
                }
            },
            'max_phase_for_ind': 'NUMERIC',
            # EXAMPLES:
            # '3' , '1' , '3' , '2' , '3' , '2' , '3' , '4' , '2' , '1'
            'mesh_heading': 'TEXT',
            # EXAMPLES:
            # 'Carcinoma, Hepatocellular' , 'Hepatitis C' , 'Melanoma' , 'Endometritis' , 'Intermittent Claudication' , 
            # 'Osteoarthritis, Knee' , 'Breast Neoplasms' , 'Prostatitis' , 'Pelvic Inflammatory Disease' , 'Obesity'
            'mesh_id': 'TEXT',
            # EXAMPLES:
            # 'D006528' , 'D006526' , 'D008545' , 'D004716' , 'D007383' , 'D020370' , 'D001943' , 'D011472' , 'D000292' 
            # , 'D009765'
            'molecule_chembl_id': 'TEXT',
            # EXAMPLES:
            # 'CHEMBL4297840' , 'CHEMBL655' , 'CHEMBL1200796' , 'CHEMBL161' , 'CHEMBL236297' , 'CHEMBL4297318' , 'CHEMBL
            # 538943' , 'CHEMBL1200523' , 'CHEMBL161' , 'CHEMBL1201631'
            'parent_molecule_chembl_id': 'TEXT',
            # EXAMPLES:
            # 'CHEMBL4297840' , 'CHEMBL655' , 'CHEMBL88' , 'CHEMBL161' , 'CHEMBL236297' , 'CHEMBL4297318' , 'CHEMBL55302
            # 5' , 'CHEMBL1435' , 'CHEMBL161' , 'CHEMBL1201631'
        }
    }
