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
            # '17161621' , '17161624' , '17166666' , '17161627' , '17166673' , '17161631' , '17166677' , '17166679' , '1
            # 7166680' , '17166681'
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
                    # 'PLAT (Platelets)' , 'EOSLE (Eosinophils/Leukocytes)' , 'MCV (Ery. Mean Corpuscular Volume)' , 'LY
                    # MLE (Lymphocytes/Leukocytes)' , 'EOSLE (Eosinophils/Leukocytes)' , 'RBC (Erythrocytes)' , 'PT (Pro
                    # thrombin Time)' , 'FIBRINO (Fibrinogen)' , 'RBC (Erythrocytes)' , 'HGB (Hemoglobin)'
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
                    # '0.0' , '0.0' , '300.0' , '0.0' , '300.0' , '0.0' , '300.0' , '300.0' , '300.0' , '300.0'
                    'text_value': 'TEXT',
                    # EXAMPLES:
                    # 'PLAT (Platelets)' , 'EOSLE (Eosinophils/Leukocytes)' , 'MCV (Ery. Mean Corpuscular Volume)' , 'LY
                    # MLE (Lymphocytes/Leukocytes)' , 'EOSLE (Eosinophils/Leukocytes)' , 'RBC (Erythrocytes)' , 'PT (Pro
                    # thrombin Time)' , 'FIBRINO (Fibrinogen)' , 'RBC (Erythrocytes)' , 'HGB (Hemoglobin)'
                    'type': 'TEXT',
                    # EXAMPLES:
                    # 'ACTIVITY_TEST' , 'ACTIVITY_TEST' , 'ACTIVITY_TEST' , 'ACTIVITY_TEST' , 'ACTIVITY_TEST' , 'ACTIVIT
                    # Y_TEST' , 'ACTIVITY_TEST' , 'ACTIVITY_TEST' , 'ACTIVITY_TEST' , 'ACTIVITY_TEST'
                    'units': 'TEXT',
                    # EXAMPLES:
                    # 'mg/kg' , 'mg/kg' , 'mg/kg' , 'mg/kg' , 'mg/kg' , 'mg/kg' , 'mg/kg' , 'mg/kg' , 'mg/kg' , 'mg/kg'
                    'value': 'NUMERIC',
                    # EXAMPLES:
                    # '0.0' , '0.0' , '300.0' , '0.0' , '300.0' , '0.0' , '300.0' , '300.0' , '300.0' , '300.0'
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
            # 'NC(N)=Nc1nc(CSCC/C(N)=N/S(N)(=O)=O)cs1' , 'NC(N)=Nc1nc(CSCC/C(N)=N/S(N)(=O)=O)cs1' , 'O=C(OC[C@H]1O[C@@H]
            # (OC(=O)c2cc(O)c(O)c(OC(=O)c3cc(O)c(O)c(O)c3)c2)[C@H](OC(=O)c2cc(O)c(O)c(OC(=O)c3cc(O)c(O)c(O)c3)c2)[C@@H](
            # OC(=O)c2cc(O)c(O)c(OC(=O)c3cc(O)c(O)c(O)c3)c2)[C@@H]1OC(=O)c1cc(O)c(O)c(OC(=O)c2cc(O)c(O)c(O)c2)c1)c1cc(O)
            # c(O)c(OC(=O)c2cc(O)c(O)c(O)c2)c1' , 'NC(N)=Nc1nc(CSCC/C(N)=N/S(N)(=O)=O)cs1' , 'O=C(OC[C@H]1O[C@@H](OC(=O)
            # c2cc(O)c(O)c(OC(=O)c3cc(O)c(O)c(O)c3)c2)[C@H](OC(=O)c2cc(O)c(O)c(OC(=O)c3cc(O)c(O)c(O)c3)c2)[C@@H](OC(=O)c
            # 2cc(O)c(O)c(OC(=O)c3cc(O)c(O)c(O)c3)c2)[C@@H]1OC(=O)c1cc(O)c(O)c(OC(=O)c2cc(O)c(O)c(O)c2)c1)c1cc(O)c(O)c(O
            # C(=O)c2cc(O)c(O)c(O)c2)c1' , 'NC(N)=Nc1nc(CSCC/C(N)=N/S(N)(=O)=O)cs1' , 'O=C(OC[C@H]1O[C@@H](OC(=O)c2cc(O)
            # c(O)c(OC(=O)c3cc(O)c(O)c(O)c3)c2)[C@H](OC(=O)c2cc(O)c(O)c(OC(=O)c3cc(O)c(O)c(O)c3)c2)[C@@H](OC(=O)c2cc(O)c
            # (O)c(OC(=O)c3cc(O)c(O)c(O)c3)c2)[C@@H]1OC(=O)c1cc(O)c(O)c(OC(=O)c2cc(O)c(O)c(O)c2)c1)c1cc(O)c(O)c(OC(=O)c2
            # cc(O)c(O)c(O)c2)c1' , 'O=C(OC[C@H]1O[C@@H](OC(=O)c2cc(O)c(O)c(OC(=O)c3cc(O)c(O)c(O)c3)c2)[C@H](OC(=O)c2cc(
            # O)c(O)c(OC(=O)c3cc(O)c(O)c(O)c3)c2)[C@@H](OC(=O)c2cc(O)c(O)c(OC(=O)c3cc(O)c(O)c(O)c3)c2)[C@@H]1OC(=O)c1cc(
            # O)c(O)c(OC(=O)c2cc(O)c(O)c(O)c2)c1)c1cc(O)c(O)c(OC(=O)c2cc(O)c(O)c(O)c2)c1' , 'O=C(OC[C@H]1O[C@@H](OC(=O)c
            # 2cc(O)c(O)c(OC(=O)c3cc(O)c(O)c(O)c3)c2)[C@H](OC(=O)c2cc(O)c(O)c(OC(=O)c3cc(O)c(O)c(O)c3)c2)[C@@H](OC(=O)c2
            # cc(O)c(O)c(OC(=O)c3cc(O)c(O)c(O)c3)c2)[C@@H]1OC(=O)c1cc(O)c(O)c(OC(=O)c2cc(O)c(O)c(O)c2)c1)c1cc(O)c(O)c(OC
            # (=O)c2cc(O)c(O)c(O)c2)c1' , 'O=C(OC[C@H]1O[C@@H](OC(=O)c2cc(O)c(O)c(OC(=O)c3cc(O)c(O)c(O)c3)c2)[C@H](OC(=O
            # )c2cc(O)c(O)c(OC(=O)c3cc(O)c(O)c(O)c3)c2)[C@@H](OC(=O)c2cc(O)c(O)c(OC(=O)c3cc(O)c(O)c(O)c3)c2)[C@@H]1OC(=O
            # )c1cc(O)c(O)c(OC(=O)c2cc(O)c(O)c(O)c2)c1)c1cc(O)c(O)c(OC(=O)c2cc(O)c(O)c(O)c2)c1'
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
            # 'CHEMBL902' , 'CHEMBL902' , 'CHEMBL506247' , 'CHEMBL902' , 'CHEMBL506247' , 'CHEMBL902' , 'CHEMBL506247' ,
            #  'CHEMBL506247' , 'CHEMBL506247' , 'CHEMBL506247'
            'molecule_pref_name': 'TEXT',
            # EXAMPLES:
            # 'FAMOTIDINE' , 'FAMOTIDINE' , 'TANNIC ACID' , 'FAMOTIDINE' , 'TANNIC ACID' , 'FAMOTIDINE' , 'TANNIC ACID' 
            # , 'TANNIC ACID' , 'TANNIC ACID' , 'TANNIC ACID'
            'parent_molecule_chembl_id': 'TEXT',
            # EXAMPLES:
            # 'CHEMBL902' , 'CHEMBL902' , 'CHEMBL506247' , 'CHEMBL902' , 'CHEMBL506247' , 'CHEMBL902' , 'CHEMBL506247' ,
            #  'CHEMBL506247' , 'CHEMBL506247' , 'CHEMBL506247'
            'potential_duplicate': 'BOOLEAN',
            # EXAMPLES:
            # 'False' , 'False' , 'False' , 'False' , 'False' , 'False' , 'False' , 'False' , 'False' , 'False'
            'qudt_units': 'TEXT',
            # EXAMPLES:
            # 'http://qudt.org/vocab/unit#Percent' , 'http://qudt.org/vocab/unit#Percent' , 'http://qudt.org/vocab/unit#
            # Percent' , 'http://qudt.org/vocab/unit#SecondTime' , 'http://www.openphacts.org/units/MicrogramPerMillilit
            # er' , 'http://www.openphacts.org/units/MicrogramPerMilliliter' , 'http://qudt.org/vocab/unit#Percent' , 'h
            # ttp://qudt.org/vocab/unit#Percent' , 'http://qudt.org/vocab/unit#Percent' , 'http://qudt.org/vocab/unit#Se
            # condTime'
            'record_id': 'NUMERIC',
            # EXAMPLES:
            # '2834522' , '2834522' , '2834593' , '2834522' , '2834593' , '2834522' , '2834593' , '2834593' , '2834593' 
            # , '2834593'
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
            # 'PLAT' , 'EOSLE' , 'MCV' , 'LYMLE' , 'EOSLE' , 'RBC' , 'PT' , 'FIBRINO' , 'RBC' , 'HGB'
            'standard_units': 'TEXT',
            # EXAMPLES:
            # 'cells.uL-1' , '%' , 'fL' , '%' , '%' , 'cells.uL-1' , 's' , 'ug.mL-1' , 'cells.uL-1' , 'ug.mL-1'
            'standard_value': 'NUMERIC',
            # EXAMPLES:
            # '1196000.0' , '0.8' , '65.9' , '79.4' , '1.0' , '5808000.0' , '12.1' , '2198.0' , '5916000.0' , '130000.0'
            'supplementary_data': 
            {
                'properties': 
                {
                    'as_id': 'NUMERIC',
                    # EXAMPLES:
                    # '188155' , '188192' , '213311' , '188144' , '213267' , '188267' , '213254' , '213324' , '213325' ,
                    #  '213377'
                    'comments': 'TEXT',
                    # EXAMPLES:
                    # 'SAMPLE_ID: 0379022' , 'SAMPLE_ID: 0379024' , 'SAMPLE_ID: 0418115' , 'SAMPLE_ID: 0379021' , 'SAMPL
                    # E_ID: 0418112' , 'SAMPLE_ID: 0379034' , 'SAMPLE_ID: 0418111' , 'SAMPLE_ID: 0418115' , 'SAMPLE_ID: 
                    # 0418121' , 'SAMPLE_ID: 0418124'
                    'relation': 'TEXT',
                    # EXAMPLES:
                    # '=' , '=' , '=' , '=' , '=' , '=' , '=' , '=' , '=' , '='
                    'rgid': 'NUMERIC',
                    # EXAMPLES:
                    # '14090' , '14092' , '6252' , '14089' , '6254' , '14097' , '15323' , '6252' , '6255' , '6256'
                    'standard_relation': 'TEXT',
                    # EXAMPLES:
                    # '=' , '=' , '=' , '=' , '=' , '=' , '=' , '=' , '=' , '='
                    'standard_text_value': 'TEXT',
                    # EXAMPLES:
                    # 'slight' , 'minimal' , 'minimal' , 'minimal' , 'minimal' , 'minimal' , 'slight' , 'P' , 'minimal' 
                    # , 'slight'
                    'standard_type': 'TEXT',
                    # EXAMPLES:
                    # 'PLAT' , 'EOSLE' , 'MCV' , 'LYMLE' , 'EOSLE' , 'RBC' , 'PT' , 'FIBRINO' , 'RBC' , 'HGB'
                    'standard_units': 'TEXT',
                    # EXAMPLES:
                    # 'cells.uL-1' , '%' , 'fL' , '%' , '%' , 'cells.uL-1' , 's' , 'ug.mL-1' , 'cells.uL-1' , 'ug.mL-1'
                    'standard_value': 'NUMERIC',
                    # EXAMPLES:
                    # '1343000.0' , '1.0' , '65.6' , '74.0' , '1.0' , '5800000.0' , '11.9' , '2240.0' , '6250000.0' , '1
                    # 29000.0'
                    'text_value': 'TEXT',
                    # EXAMPLES:
                    # 'slight' , 'minimal' , 'minimal' , 'minimal' , 'minimal' , 'minimal' , 'slight' , 'P' , 'minimal' 
                    # , 'slight'
                    'type': 'TEXT',
                    # EXAMPLES:
                    # 'Plat' , 'Eos' , 'MCV' , 'Lym' , 'Eos' , 'RBC' , 'PT' , 'Fbg' , 'RBC' , 'Hb'
                    'units': 'TEXT',
                    # EXAMPLES:
                    # 'x10_4/uL' , '%' , 'fL' , '%' , '%' , 'x10_4/ul' , 's' , 'mg/dL' , 'x10_4/ul' , 'g/dL'
                    'value': 'NUMERIC',
                    # EXAMPLES:
                    # '134.3' , '1.0' , '65.6' , '74.0' , '1.0' , '580.0' , '11.9' , '224.0' , '625.0' , '12.9'
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
            # '6862' , '6862' , '7159' , '6862' , '7159' , '6863' , '7159' , '7159' , '7160' , '7160'
            'type': 'TEXT',
            # EXAMPLES:
            # 'Plat' , 'Eos' , 'MCV' , 'Lym' , 'Eos' , 'RBC' , 'PT' , 'Fbg' , 'RBC' , 'Hb'
            'units': 'TEXT',
            # EXAMPLES:
            # 'x10_4/uL' , '%' , 'fL' , '%' , '%' , 'x10_4/ul' , 's' , 'mg/dL' , 'x10_4/ul' , 'g/dL'
            'uo_units': 'TEXT',
            # EXAMPLES:
            # 'UO_0000187' , 'UO_0000187' , 'UO_0000187' , 'UO_0000010' , 'UO_0000274' , 'UO_0000274' , 'UO_0000187' , '
            # UO_0000187' , 'UO_0000187' , 'UO_0000010'
            'value': 'NUMERIC',
            # EXAMPLES:
            # '119.6' , '0.8' , '65.9' , '79.4' , '1.0' , '580.8' , '12.1' , '219.8' , '591.6' , '13.0'
        }
    }
