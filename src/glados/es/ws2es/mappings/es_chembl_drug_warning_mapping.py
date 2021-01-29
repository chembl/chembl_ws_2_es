# Elastic search mapping definition for the Molecule entity
from glados.es.ws2es.es_util import DefaultMappings
import glados.es.ws2es.mappings.es_chembl_molecule_n_drug_shared_mapping as molecule_n_drug_mapping

# Shards size - can be overridden from the default calculated value here
# shards = 3,
replicas = 0

analysis = DefaultMappings.COMMON_ANALYSIS

mappings = \
    {
        'properties': 
        {
            'molecule_chembl_id': DefaultMappings.CHEMBL_ID_REF,
            # EXAMPLES:
            # 'CHEMBL4303288' , 'CHEMBL4303288' , 'CHEMBL4303288' , 'CHEMBL3301581' , 'CHEMBL1252' , 'CHEMBL2108570' , '
            # CHEMBL112' , 'CHEMBL112' , 'CHEMBL1131' , 'CHEMBL1131'
            'parent_molecule_chembl_id': DefaultMappings.CHEMBL_ID_REF,
            # EXAMPLES:
            # 'CHEMBL1380' , 'CHEMBL1380' , 'CHEMBL1380' , 'CHEMBL3301581' , 'CHEMBL1252' , 'CHEMBL2108570' , 'CHEMBL112
            # ' , 'CHEMBL112' , 'CHEMBL1131' , 'CHEMBL1131'
            'warning_class': DefaultMappings.LOWER_CASE_KEYWORD,
            # EXAMPLES:
            # 'Hepatotoxicity' , 'Metabolism toxicity' , 'Immune system toxicity' , 'Carcinogenicity' , 'Misuse' , 'Hepa
            # totoxicity' , 'Teratogenicity' , 'Hepatotoxicity' , 'Metabolism toxicity' , 'Hepatotoxicity'
            'warning_country': DefaultMappings.LOWER_CASE_KEYWORD,
            # EXAMPLES:
            # 'European Union' , 'United States' , 'United States' , 'Germany; Spain; United Kingdom' , 'United Kingdom;
            #  United States' , 'Worldwide' , 'United States' , 'United States' , 'United States' , 'United States'
            'warning_description': DefaultMappings.LOWER_CASE_KEYWORD,
            # EXAMPLES:
            # 'Liver toxicity' , 'Ventricular Tachycardia and Arrhythmia' , 'Increased mortality at higher doses; increa
            # sed hospitalizations' , 'Risk for heart attack, stroke, and unstable angina' , 'Risk for heart attack, str
            # oke, and unstable angina' , 'Serious toxicity to the heart' , 'Serious, irreversible, and even fatal nephr
            # otoxicity and hepatotoxicity' , 'Serious, irreversible, and even fatal nephrotoxicity and hepatotoxicity' 
            # , 'Fatal bronchospasm' , 'Unspecific Experimental Toxicity'
            'warning_id': DefaultMappings.ID_REF,
            # EXAMPLES:
            # '1' , '2' , '3' , '4' , '5' , '11' , '16' , '17' , '26' , '27'
            'warning_refs': 
            {
                'properties': 
                {
                    'ref_id': DefaultMappings.ID_REF,
                    # EXAMPLES:
                    # 'de109a2b-e36c-40d0-85fc-a67a9e7f1ae8' , 'de109a2b-e36c-40d0-85fc-a67a9e7f1ae8' , 'de109a2b-e36c-4
                    # 0d0-85fc-a67a9e7f1ae8' , '712143d9-e21e-4013-bb3b-3426a21060a8' , 'c5177abd-9465-40d8-861d-3904496
                    # d82b7' , 'c5177abd-9465-40d8-861d-3904496d82b7' , '6af396c2-af3e-436d-ba9a-583637495910' , '6af396
                    # c2-af3e-436d-ba9a-583637495910' , 'e047f3b2-feae-4c5e-9d07-1fefb4c0ec25' , 'e047f3b2-feae-4c5e-9d0
                    # 7-1fefb4c0ec25'
                    'ref_type': DefaultMappings.KEYWORD,
                    # EXAMPLES:
                    # 'FDA' , 'FDA' , 'FDA' , 'FDA' , 'FDA' , 'FDA' , 'FDA' , 'FDA' , 'FDA' , 'FDA'
                    'ref_url': DefaultMappings.KEYWORD,
                    # EXAMPLES:
                    # 'https://api.fda.gov/drug/label.json?search=set_id:de109a2b-e36c-40d0-85fc-a67a9e7f1ae8' , 'https:
                    # //api.fda.gov/drug/label.json?search=set_id:de109a2b-e36c-40d0-85fc-a67a9e7f1ae8' , 'https://api.f
                    # da.gov/drug/label.json?search=set_id:de109a2b-e36c-40d0-85fc-a67a9e7f1ae8' , 'https://api.fda.gov/
                    # drug/label.json?search=set_id:712143d9-e21e-4013-bb3b-3426a21060a8' , 'https://api.fda.gov/drug/la
                    # bel.json?search=set_id:c5177abd-9465-40d8-861d-3904496d82b7' , 'https://api.fda.gov/drug/label.jso
                    # n?search=set_id:c5177abd-9465-40d8-861d-3904496d82b7' , 'https://api.fda.gov/drug/label.json?searc
                    # h=set_id:6af396c2-af3e-436d-ba9a-583637495910' , 'https://api.fda.gov/drug/label.json?search=set_i
                    # d:6af396c2-af3e-436d-ba9a-583637495910' , 'https://api.fda.gov/drug/label.json?search=set_id:e047f
                    # 3b2-feae-4c5e-9d07-1fefb4c0ec25' , 'https://api.fda.gov/drug/label.json?search=set_id:e047f3b2-fea
                    # e-4c5e-9d07-1fefb4c0ec25'
                }
            },
            'warning_type': DefaultMappings.LOWER_CASE_KEYWORD,
            # EXAMPLES:
            # 'Black Box Warning' , 'Black Box Warning' , 'Black Box Warning' , 'Black Box Warning' , 'Black Box Warning
            # ' , 'Black Box Warning' , 'Black Box Warning' , 'Black Box Warning' , 'Black Box Warning' , 'Black Box War
            # ning'
            'warning_year': DefaultMappings.SHORT,
            # EXAMPLES:
            # '2010' , '1991' , '1993' , '2006' , '2007' , '2007' , '2014' , '2001' , '2001' , '2001'
        }
    }

