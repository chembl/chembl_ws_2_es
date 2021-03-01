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
            'activity_comment': 'TEXT',
            # EXAMPLES:
            # 'See Activity_Supp For Individual Animal Data' , 'See Activity_Supp For Individual Animal Data' , 'See Act
            # ivity_Supp For Individual Animal Data' , 'See Activity_Supp For Individual Animal Data' , 'See Activity_Su
            # pp For Individual Animal Data' , 'See Activity_Supp For Individual Animal Data' , 'See Activity_Supp For I
            # ndividual Animal Data' , 'See Activity_Supp For Individual Animal Data' , 'See Activity_Supp For Individua
            # l Animal Data' , 'See Activity_Supp For Individual Animal Data'
            'activity_id': 'NUMERIC',
            # EXAMPLES:
            # '17131431' , '17127047' , '17127048' , '17131433' , '17127049' , '17127051' , '17131437' , '17131438' , '1
            # 7131439' , '17127055'
            'activity_properties': 
            {
                'properties': 
                {
                    'relation': 'TEXT',
                    # EXAMPLES:
                    # '=' , '=' , '=' , '=' , '=' , '=' , '=' , '=' , '=' , '='
                    'result_flag': 'NUMERIC',
                    # EXAMPLES:
                    # '0' , '0' , '0' , '0' , '0' , '0' , '0' , '0' , '0' , '0'
                    'standard_relation': 'TEXT',
                    # EXAMPLES:
                    # '=' , '=' , '=' , '=' , '=' , '=' , '=' , '=' , '=' , '='
                    'standard_text_value': 'TEXT',
                    # EXAMPLES:
                    # 'NEUTLE (Neutrophils/Leukocytes)' , 'BASOLE (Basophils/Leukocytes)' , 'MONOLE (Monocytes/Leukocyte
                    # s)' , 'BASOLE (Basophils/Leukocytes)' , 'LYMLE (Lymphocytes/Leukocytes)' , 'APTT (Activated Partia
                    # l Thromboplastin Time)' , 'APTT (Activated Partial Thromboplastin Time)' , 'FIBRINO (Fibrinogen)' 
                    # , 'RBC (Erythrocytes)' , 'HCT (Hematocrit)'
                    'standard_type': 'TEXT',
                    # EXAMPLES:
                    # 'ACTIVITY_TEST' , 'ACTIVITY_TEST' , 'ACTIVITY_TEST' , 'ACTIVITY_TEST' , 'ACTIVITY_TEST' , 'ACTIVIT
                    # Y_TEST' , 'ACTIVITY_TEST' , 'ACTIVITY_TEST' , 'ACTIVITY_TEST' , 'ACTIVITY_TEST'
                    'standard_units': 'TEXT',
                    # EXAMPLES:
                    # 'mg.kg-1' , 'mg.kg-1' , 'mg.kg-1' , 'mg.kg-1' , 'mg.kg-1' , 'mg.kg-1' , 'mg.kg-1' , 'mg.kg-1' , 'm
                    # g.kg-1' , 'mg.kg-1'
                    'standard_value': 'NUMERIC',
                    # EXAMPLES:
                    # '0.0' , '200.0' , '200.0' , '0.0' , '200.0' , '200.0' , '0.0' , '0.0' , '0.0' , '0.0'
                    'text_value': 'TEXT',
                    # EXAMPLES:
                    # 'NEUTLE (Neutrophils/Leukocytes)' , 'BASOLE (Basophils/Leukocytes)' , 'MONOLE (Monocytes/Leukocyte
                    # s)' , 'BASOLE (Basophils/Leukocytes)' , 'LYMLE (Lymphocytes/Leukocytes)' , 'APTT (Activated Partia
                    # l Thromboplastin Time)' , 'APTT (Activated Partial Thromboplastin Time)' , 'FIBRINO (Fibrinogen)' 
                    # , 'RBC (Erythrocytes)' , 'HCT (Hematocrit)'
                    'type': 'TEXT',
                    # EXAMPLES:
                    # 'ACTIVITY_TEST' , 'ACTIVITY_TEST' , 'ACTIVITY_TEST' , 'ACTIVITY_TEST' , 'ACTIVITY_TEST' , 'ACTIVIT
                    # Y_TEST' , 'ACTIVITY_TEST' , 'ACTIVITY_TEST' , 'ACTIVITY_TEST' , 'ACTIVITY_TEST'
                    'units': 'TEXT',
                    # EXAMPLES:
                    # 'mg/kg' , 'mg/kg' , 'mg/kg' , 'mg/kg' , 'mg/kg' , 'mg/kg' , 'mg/kg' , 'mg/kg' , 'mg/kg' , 'mg/kg'
                    'value': 'NUMERIC',
                    # EXAMPLES:
                    # '0.0' , '200.0' , '200.0' , '0.0' , '200.0' , '200.0' , '0.0' , '0.0' , '0.0' , '0.0'
                }
            },
            'assay_chembl_id': 'TEXT',
            # EXAMPLES:
            # 'CHEMBL3885862' , 'CHEMBL3885862' , 'CHEMBL3885862' , 'CHEMBL3885862' , 'CHEMBL3885862' , 'CHEMBL3885862' 
            # , 'CHEMBL3885862' , 'CHEMBL3885862' , 'CHEMBL3885862' , 'CHEMBL3885863'
            'assay_description': 'TEXT',
            # EXAMPLES:
            # 'Open TG-GATES - Regimen: Daily Repeat' , 'Open TG-GATES - Regimen: Daily Repeat' , 'Open TG-GATES - Regim
            # en: Daily Repeat' , 'Open TG-GATES - Regimen: Daily Repeat' , 'Open TG-GATES - Regimen: Daily Repeat' , 'O
            # pen TG-GATES - Regimen: Daily Repeat' , 'Open TG-GATES - Regimen: Daily Repeat' , 'Open TG-GATES - Regimen
            # : Daily Repeat' , 'Open TG-GATES - Regimen: Daily Repeat' , 'Open TG-GATES - Regimen: Single'
            'assay_type': 'TEXT',
            # EXAMPLES:
            # 'T' , 'T' , 'T' , 'T' , 'T' , 'T' , 'T' , 'T' , 'T' , 'T'
            'bao_endpoint': 'TEXT',
            # EXAMPLES:
            # 'BAO_0000179' , 'BAO_0000179' , 'BAO_0000179' , 'BAO_0000179' , 'BAO_0000179' , 'BAO_0000179' , 'BAO_00001
            # 79' , 'BAO_0000179' , 'BAO_0000179' , 'BAO_0000179'
            'bao_format': 'TEXT',
            # EXAMPLES:
            # 'BAO_0000218' , 'BAO_0000218' , 'BAO_0000218' , 'BAO_0000218' , 'BAO_0000218' , 'BAO_0000218' , 'BAO_00002
            # 18' , 'BAO_0000218' , 'BAO_0000218' , 'BAO_0000218'
            'bao_label': 'TEXT',
            # EXAMPLES:
            # 'organism-based format' , 'organism-based format' , 'organism-based format' , 'organism-based format' , 'o
            # rganism-based format' , 'organism-based format' , 'organism-based format' , 'organism-based format' , 'org
            # anism-based format' , 'organism-based format'
            'canonical_smiles': 'TEXT',
            # EXAMPLES:
            # 'CN(C)CCCN1c2ccccc2Sc2ccc(Cl)cc21' , 'NNC(=O)c1ccncc1' , 'NNC(=O)c1ccncc1' , 'CN(C)CCCN1c2ccccc2Sc2ccc(Cl)
            # cc21' , 'NNC(=O)c1ccncc1' , 'NNC(=O)c1ccncc1' , 'CN(C)CCCN1c2ccccc2Sc2ccc(Cl)cc21' , 'CN(C)CCCN1c2ccccc2Sc
            # 2ccc(Cl)cc21' , 'CN(C)CCCN1c2ccccc2Sc2ccc(Cl)cc21' , 'ClC(Cl)(Cl)Cl'
            'data_validity_comment': 'TEXT',
            # EXAMPLES:
            # 'Non standard unit for type' , 'Non standard unit for type' , 'Non standard unit for type' , 'Non standard
            #  unit for type' , 'Non standard unit for type' , 'Non standard unit for type' , 'Non standard unit for typ
            # e' , 'Non standard unit for type' , 'Non standard unit for type' , 'Non standard unit for type'
            'data_validity_description': 'TEXT',
            # EXAMPLES:
            # 'Units for this activity type are unusual and may be incorrect (or the standard_type may be incorrect)' , 
            # 'Units for this activity type are unusual and may be incorrect (or the standard_type may be incorrect)' , 
            # 'Units for this activity type are unusual and may be incorrect (or the standard_type may be incorrect)' , 
            # 'Units for this activity type are unusual and may be incorrect (or the standard_type may be incorrect)' , 
            # 'Units for this activity type are unusual and may be incorrect (or the standard_type may be incorrect)' , 
            # 'Units for this activity type are unusual and may be incorrect (or the standard_type may be incorrect)' , 
            # 'Units for this activity type are unusual and may be incorrect (or the standard_type may be incorrect)' , 
            # 'Units for this activity type are unusual and may be incorrect (or the standard_type may be incorrect)' , 
            # 'Units for this activity type are unusual and may be incorrect (or the standard_type may be incorrect)' , 
            # 'Units for this activity type are unusual and may be incorrect (or the standard_type may be incorrect)'
            'document_chembl_id': 'TEXT',
            # EXAMPLES:
            # 'CHEMBL3885861' , 'CHEMBL3885861' , 'CHEMBL3885861' , 'CHEMBL3885861' , 'CHEMBL3885861' , 'CHEMBL3885861' 
            # , 'CHEMBL3885861' , 'CHEMBL3885861' , 'CHEMBL3885861' , 'CHEMBL3885861'
            'document_year': 'NUMERIC',
            # EXAMPLES:
            # '2019' , '2019' , '2019' , '2019' , '2019' , '2019' , '2019' , '2019' , '2019' , '2019'
            'ligand_efficiency': 
            {
                'properties': 
                {
                }
            },
            'molecule_chembl_id': 'TEXT',
            # EXAMPLES:
            # 'CHEMBL71' , 'CHEMBL64' , 'CHEMBL64' , 'CHEMBL71' , 'CHEMBL64' , 'CHEMBL64' , 'CHEMBL71' , 'CHEMBL71' , 'C
            # HEMBL71' , 'CHEMBL44814'
            'molecule_pref_name': 'TEXT',
            # EXAMPLES:
            # 'CHLORPROMAZINE' , 'ISONIAZID' , 'ISONIAZID' , 'CHLORPROMAZINE' , 'ISONIAZID' , 'ISONIAZID' , 'CHLORPROMAZ
            # INE' , 'CHLORPROMAZINE' , 'CHLORPROMAZINE' , 'CARBON TETRACHLORIDE'
            'parent_molecule_chembl_id': 'TEXT',
            # EXAMPLES:
            # 'CHEMBL71' , 'CHEMBL64' , 'CHEMBL64' , 'CHEMBL71' , 'CHEMBL64' , 'CHEMBL64' , 'CHEMBL71' , 'CHEMBL71' , 'C
            # HEMBL71' , 'CHEMBL44814'
            'potential_duplicate': 'BOOLEAN',
            # EXAMPLES:
            # 'False' , 'False' , 'False' , 'False' , 'False' , 'False' , 'False' , 'False' , 'False' , 'False'
            'qudt_units': 'TEXT',
            # EXAMPLES:
            # 'http://qudt.org/vocab/unit#Percent' , 'http://qudt.org/vocab/unit#Percent' , 'http://qudt.org/vocab/unit#
            # Percent' , 'http://qudt.org/vocab/unit#Percent' , 'http://qudt.org/vocab/unit#Percent' , 'http://qudt.org/
            # vocab/unit#SecondTime' , 'http://qudt.org/vocab/unit#SecondTime' , 'http://www.openphacts.org/units/Microg
            # ramPerMilliliter' , 'http://qudt.org/vocab/unit#Percent' , 'http://qudt.org/vocab/unit#Percent'
            'record_id': 'NUMERIC',
            # EXAMPLES:
            # '2834491' , '2834542' , '2834542' , '2834491' , '2834542' , '2834542' , '2834491' , '2834491' , '2834491' 
            # , '2834484'
            'relation': 'TEXT',
            # EXAMPLES:
            # '=' , '=' , '=' , '=' , '=' , '=' , '=' , '=' , '=' , '='
            'src_id': 'NUMERIC',
            # EXAMPLES:
            # '11' , '11' , '11' , '11' , '11' , '11' , '11' , '11' , '11' , '11'
            'standard_flag': 'BOOLEAN',
            # EXAMPLES:
            # 'True' , 'True' , 'True' , 'True' , 'True' , 'True' , 'True' , 'True' , 'True' , 'True'
            'standard_relation': 'TEXT',
            # EXAMPLES:
            # '=' , '=' , '=' , '=' , '=' , '=' , '=' , '=' , '=' , '='
            'standard_type': 'TEXT',
            # EXAMPLES:
            # 'NEUTLE' , 'BASOLE' , 'MONOLE' , 'BASOLE' , 'LYMLE' , 'APTT' , 'APTT' , 'FIBRINO' , 'RBC' , 'HCT'
            'standard_units': 'TEXT',
            # EXAMPLES:
            # '%' , '%' , '%' , '%' , '%' , 's' , 's' , 'ug.mL-1' , 'cells.uL-1' , '%'
            'standard_value': 'NUMERIC',
            # EXAMPLES:
            # '12.6' , '0.0' , '5.5' , '0.0' , '84.2' , '15.9' , '17.4' , '2256.0' , '7402000.0' , '37.3'
            'supplementary_data': 
            {
                'properties': 
                {
                    'as_id': 'NUMERIC',
                    # EXAMPLES:
                    # '38582' , '16765' , '16766' , '38584' , '16767' , '16820' , '38571' , '38555' , '38641' , '16841'
                    'comments': 'TEXT',
                    # EXAMPLES:
                    # 'SAMPLE_ID: 0115024' , 'SAMPLE_ID: 0061201' , 'SAMPLE_ID: 0061201' , 'SAMPLE_ID: 0115024' , 'SAMPL
                    # E_ID: 0061201' , 'SAMPLE_ID: 0061205' , 'SAMPLE_ID: 0115023' , 'SAMPLE_ID: 0115022' , 'SAMPLE_ID: 
                    # 0115033' , 'SAMPLE_ID: 0066012'
                    'relation': 'TEXT',
                    # EXAMPLES:
                    # '=' , '=' , '=' , '=' , '=' , '=' , '=' , '=' , '=' , '='
                    'rgid': 'NUMERIC',
                    # EXAMPLES:
                    # '7823' , '4166' , '4166' , '7823' , '4166' , '4169' , '7822' , '7821' , '7827' , '7013'
                    'standard_relation': 'TEXT',
                    # EXAMPLES:
                    # '=' , '=' , '=' , '=' , '=' , '=' , '=' , '=' , '=' , '='
                    'standard_text_value': 'TEXT',
                    # EXAMPLES:
                    # 'minimal' , 'minimal' , 'minimal' , 'minimal' , 'slight' , 'P' , 'slight' , 'minimal' , 'minimal' 
                    # , 'minimal'
                    'standard_type': 'TEXT',
                    # EXAMPLES:
                    # 'NEUTLE' , 'BASOLE' , 'MONOLE' , 'BASOLE' , 'LYMLE' , 'APTT' , 'APTT' , 'FIBRINO' , 'RBC' , 'HCT'
                    'standard_units': 'TEXT',
                    # EXAMPLES:
                    # '%' , '%' , '%' , '%' , '%' , 's' , 's' , 'ug.mL-1' , 'cells.uL-1' , '%'
                    'standard_value': 'NUMERIC',
                    # EXAMPLES:
                    # '21.0' , '0.0' , '5.0' , '0.0' , '87.0' , '16.3' , '16.9' , '2260.0' , '7850000.0' , '39.0'
                    'text_value': 'TEXT',
                    # EXAMPLES:
                    # 'minimal' , 'minimal' , 'minimal' , 'minimal' , 'slight' , 'P' , 'slight' , 'minimal' , 'minimal' 
                    # , 'minimal'
                    'type': 'TEXT',
                    # EXAMPLES:
                    # 'Neu' , 'Bas' , 'Mono' , 'Bas' , 'Lym' , 'APTT' , 'APTT' , 'Fbg' , 'RBC' , 'Ht'
                    'units': 'TEXT',
                    # EXAMPLES:
                    # '%' , '%' , '%' , '%' , '%' , 's' , 's' , 'mg/dL' , 'x10_4/ul' , '%'
                    'value': 'NUMERIC',
                    # EXAMPLES:
                    # '21.0' , '0.0' , '5.0' , '0.0' , '87.0' , '16.3' , '16.9' , '226.0' , '785.0' , '39.0'
                }
            },
            'target_chembl_id': 'TEXT',
            # EXAMPLES:
            # 'CHEMBL376' , 'CHEMBL376' , 'CHEMBL376' , 'CHEMBL376' , 'CHEMBL376' , 'CHEMBL376' , 'CHEMBL376' , 'CHEMBL3
            # 76' , 'CHEMBL376' , 'CHEMBL376'
            'target_organism': 'TEXT',
            # EXAMPLES:
            # 'Rattus norvegicus' , 'Rattus norvegicus' , 'Rattus norvegicus' , 'Rattus norvegicus' , 'Rattus norvegicus
            # ' , 'Rattus norvegicus' , 'Rattus norvegicus' , 'Rattus norvegicus' , 'Rattus norvegicus' , 'Rattus norveg
            # icus'
            'target_pref_name': 'TEXT',
            # EXAMPLES:
            # 'Rattus norvegicus' , 'Rattus norvegicus' , 'Rattus norvegicus' , 'Rattus norvegicus' , 'Rattus norvegicus
            # ' , 'Rattus norvegicus' , 'Rattus norvegicus' , 'Rattus norvegicus' , 'Rattus norvegicus' , 'Rattus norveg
            # icus'
            'target_tax_id': 'NUMERIC',
            # EXAMPLES:
            # '10116' , '10116' , '10116' , '10116' , '10116' , '10116' , '10116' , '10116' , '10116' , '10116'
            'toid': 'NUMERIC',
            # EXAMPLES:
            # '5086' , '4828' , '4828' , '5086' , '4828' , '4828' , '5086' , '5086' , '5087' , '4829'
            'type': 'TEXT',
            # EXAMPLES:
            # 'Neu' , 'Bas' , 'Mono' , 'Bas' , 'Lym' , 'APTT' , 'APTT' , 'Fbg' , 'RBC' , 'Ht'
            'units': 'TEXT',
            # EXAMPLES:
            # '%' , '%' , '%' , '%' , '%' , 's' , 's' , 'mg/dL' , 'x10_4/ul' , '%'
            'uo_units': 'TEXT',
            # EXAMPLES:
            # 'UO_0000187' , 'UO_0000187' , 'UO_0000187' , 'UO_0000187' , 'UO_0000187' , 'UO_0000010' , 'UO_0000010' , '
            # UO_0000274' , 'UO_0000187' , 'UO_0000187'
            'value': 'NUMERIC',
            # EXAMPLES:
            # '12.6' , '0.0' , '5.5' , '0.0' , '84.2' , '15.9' , '17.4' , '225.6' , '740.2' , '37.3'
        }
    }
