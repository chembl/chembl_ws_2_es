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
                    # 'CHEMBL3545252' , 'CHEMBL4303288' , 'CHEMBL1252' , 'CHEMBL2103827' , 'CHEMBL112' , 'CHEMBL1131' , 
                    # 'CHEMBL3039502' , 'CHEMBL1201580' , 'CHEMBL1201828' , 'CHEMBL922'
                }
            },
            'molecule_chembl_id': 'TEXT',
            # EXAMPLES:
            # 'CHEMBL3545252' , 'CHEMBL4303288' , 'CHEMBL1252' , 'CHEMBL2103827' , 'CHEMBL112' , 'CHEMBL1131' , 'CHEMBL3
            # 039502' , 'CHEMBL1201580' , 'CHEMBL1201828' , 'CHEMBL922'
            'parent_molecule_chembl_id': 'TEXT',
            # EXAMPLES:
            # 'CHEMBL92' , 'CHEMBL1380' , 'CHEMBL1252' , 'CHEMBL2103827' , 'CHEMBL112' , 'CHEMBL1131' , 'CHEMBL3039502' 
            # , 'CHEMBL1201580' , 'CHEMBL1201828' , 'CHEMBL922'
            'warning_class': 'TEXT',
            # EXAMPLES:
            # 'Gastrotoxicity' , 'Immune system toxicity' , 'Vascular toxicity' , 'Misuse' , 'Teratogenicity' , 'Respira
            # tory toxicity' , 'Infections' , 'Hepatotoxicity' , 'Nephrotoxicity' , 'Vascular toxicity'
            'warning_country': 'TEXT',
            # EXAMPLES:
            # 'European Union' , 'United States' , 'United States' , 'Germany; Spain; United Kingdom' , 'United Kingdom;
            #  United States' , 'Worldwide' , 'United States' , 'United States' , 'United States' , 'United States'
            'warning_description': 'TEXT',
            # EXAMPLES:
            # 'Liver toxicity' , 'Ventricular Tachycardia and Arrhythmia' , 'Increased mortality at higher doses; increa
            # sed hospitalizations' , 'Risk for heart attack, stroke, and unstable angina' , 'Risk for heart attack, str
            # oke, and unstable angina' , 'Serious toxicity to the heart' , 'Serious, irreversible, and even fatal nephr
            # otoxicity and hepatotoxicity' , 'Serious, irreversible, and even fatal nephrotoxicity and hepatotoxicity' 
            # , 'Fatal bronchospasm' , 'Unspecific Experimental Toxicity'
            'warning_id': 'NUMERIC',
            # EXAMPLES:
            # '2431' , '3' , '5' , '2437' , '16' , '26' , '2440' , '33' , '2442' , '36'
            'warning_refs': 
            {
                'properties': 
                {
                    'ref_id': 'TEXT',
                    # EXAMPLES:
                    # 'a6417655-9448-4886-ba03-f57f36bcbd14' , 'de109a2b-e36c-40d0-85fc-a67a9e7f1ae8' , '2179f02c-48d7-4
                    # 8eb-8007-5ae43d8d16bc' , 'c5177abd-9465-40d8-861d-3904496d82b7' , '6af396c2-af3e-436d-ba9a-5836374
                    # 95910' , '47547f93-489c-4298-aeea-d6a37ca6cb1d' , 'ebcd67fa-b4d1-4a22-b33d-ee8bf6b9c722' , 'e047f3
                    # b2-feae-4c5e-9d07-1fefb4c0ec25' , 'e77d3400-56ad-11e3-949a-0800200c9a66' , 'e047f3b2-feae-4c5e-9d0
                    # 7-1fefb4c0ec25'
                    'ref_type': 'TEXT',
                    # EXAMPLES:
                    # 'FDA' , 'FDA' , 'FDA' , 'FDA' , 'FDA' , 'FDA' , 'FDA' , 'FDA' , 'FDA' , 'FDA'
                    'ref_url': 'TEXT',
                    # EXAMPLES:
                    # 'https://api.fda.gov/drug/label.json?search=set_id:a6417655-9448-4886-ba03-f57f36bcbd14' , 'https:
                    # //api.fda.gov/drug/label.json?search=set_id:de109a2b-e36c-40d0-85fc-a67a9e7f1ae8' , 'https://api.f
                    # da.gov/drug/label.json?search=set_id:2179f02c-48d7-48eb-8007-5ae43d8d16bc' , 'https://api.fda.gov/
                    # drug/label.json?search=set_id:c5177abd-9465-40d8-861d-3904496d82b7' , 'https://api.fda.gov/drug/la
                    # bel.json?search=set_id:6af396c2-af3e-436d-ba9a-583637495910' , 'https://api.fda.gov/drug/label.jso
                    # n?search=set_id:47547f93-489c-4298-aeea-d6a37ca6cb1d' , 'https://api.fda.gov/drug/label.json?searc
                    # h=set_id:ebcd67fa-b4d1-4a22-b33d-ee8bf6b9c722' , 'https://api.fda.gov/drug/label.json?search=set_i
                    # d:e047f3b2-feae-4c5e-9d07-1fefb4c0ec25' , 'https://api.fda.gov/drug/label.json?search=set_id:e77d3
                    # 400-56ad-11e3-949a-0800200c9a66' , 'https://api.fda.gov/drug/label.json?search=set_id:e047f3b2-fea
                    # e-4c5e-9d07-1fefb4c0ec25'
                }
            },
            'warning_type': 'TEXT',
            # EXAMPLES:
            # 'Black Box Warning' , 'Black Box Warning' , 'Black Box Warning' , 'Black Box Warning' , 'Black Box Warning
            # ' , 'Black Box Warning' , 'Black Box Warning' , 'Black Box Warning' , 'Black Box Warning' , 'Black Box War
            # ning'
            'warning_year': 'NUMERIC',
            # EXAMPLES:
            # '2010' , '1991' , '1993' , '2006' , '2007' , '2007' , '2014' , '2001' , '2001' , '2001'
        }
    }
