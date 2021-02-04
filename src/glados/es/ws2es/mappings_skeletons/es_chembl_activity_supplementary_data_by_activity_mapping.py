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
            # '17126237' , '17126238' , '17126241' , '17126244' , '17126245' , '17126246' , '17126248' , '17126250' , '1
            # 7126254' , '17126255'
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
                    # 'RBC (Erythrocytes)' , 'HGB (Hemoglobin)' , 'MCH (Ery. Mean Corpuscular Hemoglobin)' , 'PLAT (Plat
                    # elets)' , 'WBC (Leukocytes)' , 'NEUTLE (Neutrophils/Leukocytes)' , 'BASOLE (Basophils/Leukocytes)'
                    #  , 'LYMLE (Lymphocytes/Leukocytes)' , 'RBC (Erythrocytes)' , 'HGB (Hemoglobin)'
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
                    # '0.0' , '0.0' , '0.0' , '0.0' , '0.0' , '0.0' , '0.0' , '0.0' , '0.0' , '0.0'
                    'text_value': 'TEXT',
                    # EXAMPLES:
                    # 'RBC (Erythrocytes)' , 'HGB (Hemoglobin)' , 'MCH (Ery. Mean Corpuscular Hemoglobin)' , 'PLAT (Plat
                    # elets)' , 'WBC (Leukocytes)' , 'NEUTLE (Neutrophils/Leukocytes)' , 'BASOLE (Basophils/Leukocytes)'
                    #  , 'LYMLE (Lymphocytes/Leukocytes)' , 'RBC (Erythrocytes)' , 'HGB (Hemoglobin)'
                    'type': 'TEXT',
                    # EXAMPLES:
                    # 'ACTIVITY_TEST' , 'ACTIVITY_TEST' , 'ACTIVITY_TEST' , 'ACTIVITY_TEST' , 'ACTIVITY_TEST' , 'ACTIVIT
                    # Y_TEST' , 'ACTIVITY_TEST' , 'ACTIVITY_TEST' , 'ACTIVITY_TEST' , 'ACTIVITY_TEST'
                    'units': 'TEXT',
                    # EXAMPLES:
                    # 'mg/kg' , 'mg/kg' , 'mg/kg' , 'mg/kg' , 'mg/kg' , 'mg/kg' , 'mg/kg' , 'mg/kg' , 'mg/kg' , 'mg/kg'
                    'value': 'NUMERIC',
                    # EXAMPLES:
                    # '0.0' , '0.0' , '0.0' , '0.0' , '0.0' , '0.0' , '0.0' , '0.0' , '0.0' , '0.0'
                }
            },
            'assay_chembl_id': 'TEXT',
            # EXAMPLES:
            # 'CHEMBL3885863' , 'CHEMBL3885863' , 'CHEMBL3885863' , 'CHEMBL3885863' , 'CHEMBL3885863' , 'CHEMBL3885863' 
            # , 'CHEMBL3885863' , 'CHEMBL3885863' , 'CHEMBL3885863' , 'CHEMBL3885863'
            'assay_description': 'TEXT',
            # EXAMPLES:
            # 'Open TG-GATES - Regimen: Single' , 'Open TG-GATES - Regimen: Single' , 'Open TG-GATES - Regimen: Single' 
            # , 'Open TG-GATES - Regimen: Single' , 'Open TG-GATES - Regimen: Single' , 'Open TG-GATES - Regimen: Single
            # ' , 'Open TG-GATES - Regimen: Single' , 'Open TG-GATES - Regimen: Single' , 'Open TG-GATES - Regimen: Sing
            # le' , 'Open TG-GATES - Regimen: Single'
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
            # 'CC(=O)Nc1ccc(O)cc1' , 'CC(=O)Nc1ccc(O)cc1' , 'CC(=O)Nc1ccc(O)cc1' , 'CC(=O)Nc1ccc(O)cc1' , 'CC(=O)Nc1ccc(
            # O)cc1' , 'CC(=O)Nc1ccc(O)cc1' , 'CC(=O)Nc1ccc(O)cc1' , 'CC(=O)Nc1ccc(O)cc1' , 'CC(=O)Nc1ccc(O)cc1' , 'CC(=
            # O)Nc1ccc(O)cc1'
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
            # 'CHEMBL112' , 'CHEMBL112' , 'CHEMBL112' , 'CHEMBL112' , 'CHEMBL112' , 'CHEMBL112' , 'CHEMBL112' , 'CHEMBL1
            # 12' , 'CHEMBL112' , 'CHEMBL112'
            'molecule_pref_name': 'TEXT',
            # EXAMPLES:
            # 'ACETAMINOPHEN' , 'ACETAMINOPHEN' , 'ACETAMINOPHEN' , 'ACETAMINOPHEN' , 'ACETAMINOPHEN' , 'ACETAMINOPHEN' 
            # , 'ACETAMINOPHEN' , 'ACETAMINOPHEN' , 'ACETAMINOPHEN' , 'ACETAMINOPHEN'
            'parent_molecule_chembl_id': 'TEXT',
            # EXAMPLES:
            # 'CHEMBL112' , 'CHEMBL112' , 'CHEMBL112' , 'CHEMBL112' , 'CHEMBL112' , 'CHEMBL112' , 'CHEMBL112' , 'CHEMBL1
            # 12' , 'CHEMBL112' , 'CHEMBL112'
            'potential_duplicate': 'BOOLEAN',
            # EXAMPLES:
            # 'False' , 'False' , 'False' , 'False' , 'False' , 'False' , 'False' , 'False' , 'False' , 'False'
            'qudt_units': 'TEXT',
            # EXAMPLES:
            # 'http://www.openphacts.org/units/MicrogramPerMilliliter' , 'http://qudt.org/vocab/unit#Percent' , 'http://
            # qudt.org/vocab/unit#Percent' , 'http://qudt.org/vocab/unit#Percent' , 'http://www.openphacts.org/units/Mic
            # rogramPerMilliliter' , 'http://qudt.org/vocab/unit#Percent' , 'http://qudt.org/vocab/unit#Percent' , 'http
            # ://www.openphacts.org/units/MicrogramPerMilliliter' , 'http://qudt.org/vocab/unit#Percent' , 'http://qudt.
            # org/vocab/unit#Percent'
            'record_id': 'NUMERIC',
            # EXAMPLES:
            # '2834460' , '2834460' , '2834460' , '2834460' , '2834460' , '2834460' , '2834460' , '2834460' , '2834460' 
            # , '2834460'
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
            # 'RBC' , 'HGB' , 'MCH' , 'PLAT' , 'WBC' , 'NEUTLE' , 'BASOLE' , 'LYMLE' , 'RBC' , 'HGB'
            'standard_units': 'TEXT',
            # EXAMPLES:
            # 'cells.uL-1' , 'ug.mL-1' , 'pg' , 'cells.uL-1' , 'cells.uL-1' , '%' , '%' , '%' , 'cells.uL-1' , 'ug.mL-1'
            'standard_value': 'NUMERIC',
            # EXAMPLES:
            # '5554000.0' , '123000.0' , '22.2' , '1230000.0' , '2340.0' , '16.0' , '0.2' , '63.2' , '5406000.0' , '1190
            # 00.0'
            'supplementary_data': 
            {
                'properties': 
                {
                    'as_id': 'NUMERIC',
                    # EXAMPLES:
                    # '12856' , '12840' , '12860' , '12897' , '12847' , '12865' , '12833' , '12835' , '12941' , '12976'
                    'comments': 'TEXT',
                    # EXAMPLES:
                    # 'SAMPLE_ID: 0040013' , 'SAMPLE_ID: 0040012' , 'SAMPLE_ID: 0040013' , 'SAMPLE_ID: 0040015' , 'SAMPL
                    # E_ID: 0040012' , 'SAMPLE_ID: 0040013' , 'SAMPLE_ID: 0040011' , 'SAMPLE_ID: 0040011' , 'SAMPLE_ID: 
                    # 0040023' , 'SAMPLE_ID: 0040025'
                    'relation': 'TEXT',
                    # EXAMPLES:
                    # '=' , '=' , '=' , '=' , '=' , '=' , '=' , '=' , '=' , '='
                    'rgid': 'NUMERIC',
                    # EXAMPLES:
                    # '6820' , '6819' , '6820' , '6822' , '6819' , '6820' , '6818' , '6818' , '6825' , '6827'
                    'standard_relation': 'TEXT',
                    # EXAMPLES:
                    # '=' , '=' , '=' , '=' , '=' , '=' , '=' , '=' , '=' , '='
                    'standard_text_value': 'TEXT',
                    # EXAMPLES:
                    # 'minimal' , 'slight' , 'minimal' , 'moderate' , 'P' , 'slight' , 'P' , 'minimal' , 'P' , 'minimal'
                    'standard_type': 'TEXT',
                    # EXAMPLES:
                    # 'RBC' , 'HGB' , 'MCH' , 'PLAT' , 'WBC' , 'NEUTLE' , 'BASOLE' , 'LYMLE' , 'RBC' , 'HGB'
                    'standard_units': 'TEXT',
                    # EXAMPLES:
                    # 'cells.uL-1' , 'ug.mL-1' , 'pg' , 'cells.uL-1' , 'cells.uL-1' , '%' , '%' , '%' , 'cells.uL-1' , '
                    # ug.mL-1'
                    'standard_value': 'NUMERIC',
                    # EXAMPLES:
                    # '5780000.0' , '126000.0' , '21.3' , '1101000.0' , '1780.0' , '25.0' , '1.0' , '63.0' , '5400000.0'
                    #  , '107000.0'
                    'text_value': 'TEXT',
                    # EXAMPLES:
                    # 'minimal' , 'slight' , 'minimal' , 'moderate' , 'P' , 'slight' , 'P' , 'minimal' , 'P' , 'minimal'
                    'type': 'TEXT',
                    # EXAMPLES:
                    # 'RBC' , 'Hb' , 'MCH' , 'Plat' , 'WBC' , 'Neu' , 'Bas' , 'Lym' , 'RBC' , 'Hb'
                    'units': 'TEXT',
                    # EXAMPLES:
                    # 'x10_4/ul' , 'g/dL' , 'pg' , 'x10_4/uL' , 'x10_2/uL' , '%' , '%' , '%' , 'x10_4/ul' , 'g/dL'
                    'value': 'NUMERIC',
                    # EXAMPLES:
                    # '578.0' , '12.6' , '21.3' , '110.1' , '17.8' , '25.0' , '1.0' , '63.0' , '540.0' , '10.7'
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
            # '4781' , '4781' , '4781' , '4781' , '4781' , '4781' , '4781' , '4781' , '4782' , '4782'
            'type': 'TEXT',
            # EXAMPLES:
            # 'RBC' , 'Hb' , 'MCH' , 'Plat' , 'WBC' , 'Neu' , 'Bas' , 'Lym' , 'RBC' , 'Hb'
            'units': 'TEXT',
            # EXAMPLES:
            # 'x10_4/ul' , 'g/dL' , 'pg' , 'x10_4/uL' , 'x10_2/uL' , '%' , '%' , '%' , 'x10_4/ul' , 'g/dL'
            'uo_units': 'TEXT',
            # EXAMPLES:
            # 'UO_0000274' , 'UO_0000025' , 'UO_0000187' , 'UO_0000187' , 'UO_0000187' , 'UO_0000274' , 'UO_0000187' , '
            # UO_0000187' , 'UO_0000274' , 'UO_0000187'
            'value': 'NUMERIC',
            # EXAMPLES:
            # '555.4' , '12.3' , '22.2' , '123.0' , '23.4' , '16.0' , '0.2' , '63.2' , '540.6' , '11.9'
        }
    }
