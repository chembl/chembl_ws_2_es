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
            'assay_class_id': 'NUMERIC',
            # EXAMPLES:
            # '1' , '2' , '3' , '4' , '5' , '6' , '7' , '8' , '9' , '10'
            'class_type': 'TEXT',
            # EXAMPLES:
            # 'In vivo efficacy' , 'In vivo efficacy' , 'In vivo efficacy' , 'In vivo efficacy' , 'In vivo efficacy' , '
            # In vivo efficacy' , 'In vivo efficacy' , 'In vivo efficacy' , 'In vivo efficacy' , 'In vivo efficacy'
            'l1': 'TEXT',
            # EXAMPLES:
            # 'ALIMENTARY TRACT AND METABOLISM' , 'ALIMENTARY TRACT AND METABOLISM' , 'ALIMENTARY TRACT AND METABOLISM' 
            # , 'ALIMENTARY TRACT AND METABOLISM' , 'ALIMENTARY TRACT AND METABOLISM' , 'ALIMENTARY TRACT AND METABOLISM
            # ' , 'ALIMENTARY TRACT AND METABOLISM' , 'ALIMENTARY TRACT AND METABOLISM' , 'ALIMENTARY TRACT AND METABOLI
            # SM' , 'ALIMENTARY TRACT AND METABOLISM'
            'l2': 'TEXT',
            # EXAMPLES:
            # 'Anti-Obesity Activity' , 'Anti-Obesity Activity' , 'Anti-Obesity Activity' , 'Anti-Obesity Activity' , 'E
            # xperimental Diabetes Mellitus' , 'Experimental Diabetes Mellitus' , 'Experimental Diabetes Mellitus' , 'Ex
            # perimental Diabetes Mellitus' , 'Experimental Obesity' , 'Experimental Obesity'
            'l3': 'TEXT',
            # EXAMPLES:
            # 'Computer-Assisted Measurement of Food Consumption in Rats Anorectic Activity' , 'Food Consumption in Rats
            #  Anorectic Activity' , 'General Anti-Obesity activity' , 'Resting Metabolic Rate Anti-Obesity' , 'Alloxan 
            # Induced Diabetes' , 'Corticosteroid Induced Diabetes' , 'Streptozotocin Induced Diabetes' , 'Virus Induced
            #  Diabetes' , 'Diet Induced Obesity' , 'Goldthioglucose Induced Obesity'
            'source': 'TEXT',
            # EXAMPLES:
            # 'Vogel_2008' , 'Vogel_2008' , 'phenotype' , 'Vogel_2008' , 'Vogel_2008' , 'Vogel_2008' , 'Vogel_2008' , 'V
            # ogel_2008' , 'Hock_2016' , 'Vogel_2008'
        }
    }
