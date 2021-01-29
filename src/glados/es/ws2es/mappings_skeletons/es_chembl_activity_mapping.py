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
            # 'Not Active' , 'Not Active' , 'Not Active' , 'Not Active' , 'Agonist' , 'Not Determined' , 'Active' , 'Vir
            # tual activity' , 'Not Determined' , 'Not Determined'
            'activity_id': 'NUMERIC',
            # EXAMPLES:
            # '868708' , '868712' , '874116' , '874117' , '868733' , '874125' , '874127' , '874130' , '874134' , '874147
            # '
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
                    # 'MCH (Ery. Mean Corpuscular Hemoglobin)' , 'NEUTLE (Neutrophils/Leukocytes)' , 'MCV (Ery. Mean Cor
                    # puscular Volume)' , 'MCHC (Ery. Mean Corpuscular HGB Concentration)' , 'HCT (Hematocrit)' , 'WBC (
                    # Leukocytes)' , 'RBC (Erythrocytes)' , 'PLAT (Platelets)' , 'MONOLE (Monocytes/Leukocytes)' , 'HCT 
                    # (Hematocrit)'
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
                    # '600.0' , '600.0' , '600.0' , '600.0' , '1000.0' , '1000.0' , '1000.0' , '1000.0' , '1000.0' , '10
                    # 00.0'
                    'text_value': 'TEXT',
                    # EXAMPLES:
                    # 'MCH (Ery. Mean Corpuscular Hemoglobin)' , 'NEUTLE (Neutrophils/Leukocytes)' , 'MCV (Ery. Mean Cor
                    # puscular Volume)' , 'MCHC (Ery. Mean Corpuscular HGB Concentration)' , 'HCT (Hematocrit)' , 'WBC (
                    # Leukocytes)' , 'RBC (Erythrocytes)' , 'PLAT (Platelets)' , 'MONOLE (Monocytes/Leukocytes)' , 'HCT 
                    # (Hematocrit)'
                    'type': 'TEXT',
                    # EXAMPLES:
                    # 'ACTIVITY_TEST' , 'ACTIVITY_TEST' , 'ACTIVITY_TEST' , 'ACTIVITY_TEST' , 'ACTIVITY_TEST' , 'ACTIVIT
                    # Y_TEST' , 'ACTIVITY_TEST' , 'ACTIVITY_TEST' , 'ACTIVITY_TEST' , 'ACTIVITY_TEST'
                    'units': 'TEXT',
                    # EXAMPLES:
                    # 'mg/kg' , 'mg/kg' , 'mg/kg' , 'mg/kg' , 'mg/kg' , 'mg/kg' , 'mg/kg' , 'mg/kg' , 'mg/kg' , 'mg/kg'
                    'value': 'NUMERIC',
                    # EXAMPLES:
                    # '600.0' , '600.0' , '600.0' , '600.0' , '1000.0' , '1000.0' , '1000.0' , '1000.0' , '1000.0' , '10
                    # 00.0'
                }
            },
            'assay_chembl_id': 'TEXT',
            # EXAMPLES:
            # 'CHEMBL662302' , 'CHEMBL641101' , 'CHEMBL787305' , 'CHEMBL669303' , 'CHEMBL717165' , 'CHEMBL852149' , 'CHE
            # MBL816795' , 'CHEMBL729879' , 'CHEMBL753046' , 'CHEMBL718465'
            'assay_description': 'TEXT',
            # EXAMPLES:
            # 'Cytotoxicity against Chinese hamster ovary cells' , 'Dissociation constant (pKa)' , 'Antihypertensive act
            # ivity in spontaneously hypertensive rats (SHR) at 5 mg/kg dose (po) after 6 h' , 'Inhibitory activity agai
            # nst dihydrofolate reductase(DHFR)' , 'In vivo antimalarial activity to reduce parasitaemia in mice (Mus mu
            # sculus) infected with Plasmodium berghei by 50% of the control' , 'Selective toxicity against Plasmodium f
            # alciparum compared to FM3A cytotoxicity' , 'Inhibition of trypsin ' , 'Antinociceptive activity was determ
            # ined using the phenylquinone writhing assay by intravenous administration' , 'Displacement of [3H]ouabain 
            # binding from Na+,K+ -ATPase receptor isolated from dog kidney' , 'Evaluated for antimalarial activity agai
            # nst Plasmodium berghei in mice (Mus musculus) at 90 mg/kg; inactive'
            'assay_type': 'TEXT',
            # EXAMPLES:
            # 'A' , 'P' , 'F' , 'B' , 'F' , 'F' , 'B' , 'F' , 'B' , 'F'
            'assay_variant_accession': 'TEXT',
            # EXAMPLES:
            # 'P41145' , 'P41145' , 'P41145' , 'P0DMS8' , 'P29274' , 'Q9WKE8' , 'P41145' , 'P41145' , 'P56221' , 'P0DMS8
            # '
            'assay_variant_mutation': 'TEXT',
            # EXAMPLES:
            # 'E297K' , 'E297A' , 'E297K' , 'H95A' , 'S277E' , 'K103N' , 'E297K' , 'E297A' , 'N131A' , 'H95A'
            'bao_endpoint': 'TEXT',
            # EXAMPLES:
            # 'BAO_0000179' , 'BAO_0002131' , 'BAO_0000082' , 'BAO_0000190' , 'BAO_0003036' , 'BAO_0000179' , 'BAO_00001
            # 90' , 'BAO_0000181' , 'BAO_0000190' , 'BAO_0000375'
            'bao_format': 'TEXT',
            # EXAMPLES:
            # 'BAO_0000219' , 'BAO_0000100' , 'BAO_0000218' , 'BAO_0000357' , 'BAO_0000218' , 'BAO_0000219' , 'BAO_00000
            # 19' , 'BAO_0000218' , 'BAO_0000019' , 'BAO_0000218'
            'bao_label': 'TEXT',
            # EXAMPLES:
            # 'cell-based format' , 'small-molecule physicochemical format' , 'organism-based format' , 'single protein 
            # format' , 'organism-based format' , 'cell-based format' , 'assay format' , 'organism-based format' , 'assa
            # y format' , 'organism-based format'
            'canonical_smiles': 'TEXT',
            # EXAMPLES:
            # 'CC1C2c3ccccc3C(c3ccccc32)C1CN(C)C' , 'CC1C2c3ccccc3C(c3ccccc32)C1CN(C)C' , 'COc1cc2nc(N3CCC(OCCOC4CCCC4)C
            # C3)nc(N)c2cc1OC' , 'CN(Cc1cnc2nc(N)nc(N)c2n1)c1ccc(C(=O)NC(C/C=C/C(=O)O)C(=O)O)cc1' , 'CC1(OCc2ccccc2)CCC2
            # CC1OO[C@]2(C)CS(=O)(=O)c1ccccc1' , 'COC(=O)[C@]12OC[C@@]34[C@H]1[C@@H](OC(C)=O)C(=O)O[C@@H]3C[C@H]1C(C)=C(
            # O)C(=O)C[C@]1(C)[C@H]4[C@@H](O)[C@@H]2O' , 'Cc1ccc(NS(=O)(=O)Cc2ccccc2)c(=O)n1CC(=O)NCCC(=O)N=C(N)N' , 'CC
            # [C@H](C)[C@H](NC(=O)[C@H](Cc1ccc(O)cc1)NC(=O)[C@@H]1CCCN1C(=O)[C@H](CCCN)NC(=O)OC(C)(C)C)C(=O)N[C@@H](CC(C
            # )C)C(=O)O' , 'C[C@]12CC[C@H](SCCCN3CCCC3)C[C@H]1CC[C@@H]1[C@@H]2CC[C@]2(C)[C@@H](C3=CC(=O)OC3)CC[C@]12O' ,
            #  'C=C(c1ccc(OC)cc1)C1COC2(CCCCC2)OO1'
            'data_validity_comment': 'TEXT',
            # EXAMPLES:
            # 'Non standard unit for type' , 'Outside typical range' , 'Outside typical range' , 'Outside typical range'
            #  , 'Outside typical range' , 'Outside typical range' , 'Outside typical range' , 'Outside typical range' ,
            #  'Outside typical range' , 'Outside typical range'
            'data_validity_description': 'TEXT',
            # EXAMPLES:
            # 'Units for this activity type are unusual and may be incorrect (or the standard_type may be incorrect)' , 
            # 'Values for this activity type are unusually large/small, so may not be accurate' , 'Values for this activ
            # ity type are unusually large/small, so may not be accurate' , 'Values for this activity type are unusually
            #  large/small, so may not be accurate' , 'Values for this activity type are unusually large/small, so may n
            # ot be accurate' , 'Values for this activity type are unusually large/small, so may not be accurate' , 'Val
            # ues for this activity type are unusually large/small, so may not be accurate' , 'Values for this activity 
            # type are unusually large/small, so may not be accurate' , 'Values for this activity type are unusually lar
            # ge/small, so may not be accurate' , 'Values for this activity type are unusually large/small, so may not b
            # e accurate'
            'document_chembl_id': 'TEXT',
            # EXAMPLES:
            # 'CHEMBL1135512' , 'CHEMBL1135512' , 'CHEMBL1124050' , 'CHEMBL1124079' , 'CHEMBL1148317' , 'CHEMBL1130760' 
            # , 'CHEMBL1130715' , 'CHEMBL1126486' , 'CHEMBL1129845' , 'CHEMBL1128628'
            'document_journal': 'TEXT',
            # EXAMPLES:
            # 'J. Med. Chem.' , 'J. Med. Chem.' , 'J. Med. Chem.' , 'J. Med. Chem.' , 'J. Med. Chem.' , 'Bioorg. Med. Ch
            # em. Lett.' , 'Bioorg. Med. Chem. Lett.' , 'Bioorg. Med. Chem. Lett.' , 'Bioorg. Med. Chem. Lett.' , 'Bioor
            # g. Med. Chem. Lett.'
            'document_year': 'NUMERIC',
            # EXAMPLES:
            # '2002' , '2002' , '1988' , '1988' , '2004' , '1998' , '1998' , '1993' , '1997' , '1995'
            'ligand_efficiency': 
            {
                'properties': 
                {
                    'bei': 'NUMERIC',
                    # EXAMPLES:
                    # '9.64' , '18.43' , '22.60' , '22.42' , '20.00' , '14.32' , '24.98' , '19.03' , '20.01' , '22.61'
                    'le': 'NUMERIC',
                    # EXAMPLES:
                    # '0.18' , '0.36' , '0.41' , '0.42' , '0.37' , '0.27' , '0.49' , '0.39' , '0.36' , '0.45'
                    'lle': 'NUMERIC',
                    # EXAMPLES:
                    # '4.06' , '6.00' , '4.05' , '2.92' , '2.13' , '4.76' , '11.88' , '5.32' , '2.45' , '5.30'
                    'sei': 'NUMERIC',
                    # EXAMPLES:
                    # '2.13' , '5.93' , '9.25' , '13.06' , '11.65' , '4.41' , '4.19' , '7.43' , '18.27' , '12.08'
                }
            },
            'molecule_chembl_id': 'TEXT',
            # EXAMPLES:
            # 'CHEMBL324180' , 'CHEMBL324180' , 'CHEMBL149666' , 'CHEMBL164765' , 'CHEMBL85891' , 'CHEMBL140809' , 'CHEM
            # BL421057' , 'CHEMBL427656' , 'CHEMBL2068953' , 'CHEMBL56262'
            'molecule_pref_name': 'TEXT',
            # EXAMPLES:
            # 'BRUCEINE B' , 'CISPLATIN' , 'CISPLATIN' , 'DOXORUBICIN' , 'ZANAMIVIR' , 'ZANAMIVIR' , 'ZANAMIVIR' , 'ZANA
            # MIVIR' , 'GLYCINE' , 'DIMINAZENE'
            'parent_molecule_chembl_id': 'TEXT',
            # EXAMPLES:
            # 'CHEMBL324180' , 'CHEMBL324180' , 'CHEMBL149666' , 'CHEMBL164765' , 'CHEMBL85891' , 'CHEMBL140809' , 'CHEM
            # BL421057' , 'CHEMBL427656' , 'CHEMBL2068953' , 'CHEMBL56262'
            'pchembl_value': 'NUMERIC',
            # EXAMPLES:
            # '4.50' , '5.72' , '6.80' , '7.09' , '6.23' , '8.02' , '6.25' , '5.77' , '7.37' , '6.57'
            'potential_duplicate': 'BOOLEAN',
            # EXAMPLES:
            # 'False' , 'False' , 'False' , 'False' , 'False' , 'False' , 'False' , 'False' , 'False' , 'False'
            'qudt_units': 'TEXT',
            # EXAMPLES:
            # 'http://www.openphacts.org/units/Micromolar' , 'http://qudt.org/vocab/unit#Percent' , 'http://www.openphac
            # ts.org/units/Nanomolar' , 'http://www.openphacts.org/units/Nanomolar' , 'http://www.openphacts.org/units/N
            # anomolar' , 'http://www.openphacts.org/units/Nanomolar' , 'http://www.openphacts.org/units/Nanomolar' , 'h
            # ttp://www.openphacts.org/units/Nanomolar' , 'http://qudt.org/vocab/unit#Percent' , 'http://qudt.org/vocab/
            # unit#Percent'
            'record_id': 'NUMERIC',
            # EXAMPLES:
            # '205023' , '205023' , '290877' , '323748' , '187056' , '274315' , '228035' , '4545' , '277381' , '97456'
            'relation': 'TEXT',
            # EXAMPLES:
            # '=' , '=' , '=' , '=' , '=' , '=' , '=' , '=' , '=' , '='
            'src_id': 'NUMERIC',
            # EXAMPLES:
            # '1' , '1' , '1' , '1' , '1' , '1' , '1' , '1' , '1' , '1'
            'standard_flag': 'BOOLEAN',
            # EXAMPLES:
            # 'False' , 'False' , 'False' , 'True' , 'True' , 'False' , 'True' , 'False' , 'True' , 'False'
            'standard_relation': 'TEXT',
            # EXAMPLES:
            # '=' , '=' , '=' , '=' , '=' , '=' , '=' , '=' , '=' , '='
            'standard_text_value': 'TEXT',
            # EXAMPLES:
            # 'Active' , 'Active' , 'Not Active' , 'Active' , 'Linear Fit' , 'Not Determined' , 'Not Determined' , 'Acti
            # ve' , 'Not Active' , 'Not Determined'
            'standard_type': 'TEXT',
            # EXAMPLES:
            # 'Cytotoxicity' , 'pKa' , 'Reduction' , 'IC50' , 'ED50' , 'Ratio' , 'IC50' , 'Activity' , 'IC50' , 'Activit
            # y'
            'standard_units': 'TEXT',
            # EXAMPLES:
            # 'uM' , '%' , 'nM' , 'mg.kg-1' , 'nM' , 'mg kg-1' , 'nM' , 'nM' , 'nM' , 'nM'
            'standard_value': 'NUMERIC',
            # EXAMPLES:
            # '711.0' , '8.99' , '11.0' , '32000.0' , '0.43' , '333.0' , '1900.0' , '0.74' , '158.49' , '82.0'
            'target_chembl_id': 'TEXT',
            # EXAMPLES:
            # 'CHEMBL612558' , 'CHEMBL2362975' , 'CHEMBL376' , 'CHEMBL4564' , 'CHEMBL375' , 'CHEMBL614297' , 'CHEMBL6125
            # 45' , 'CHEMBL375' , 'CHEMBL612545' , 'CHEMBL375'
            'target_organism': 'TEXT',
            # EXAMPLES:
            # 'Rattus norvegicus' , 'Mus musculus' , 'Mus musculus' , 'Mus musculus' , 'Mus musculus' , 'Mus musculus' ,
            #  'Homo sapiens' , 'Homo sapiens' , 'Homo sapiens' , 'Mus musculus'
            'target_pref_name': 'TEXT',
            # EXAMPLES:
            # 'ADMET' , 'No relevant target' , 'Rattus norvegicus' , 'Dihydrofolate reductase' , 'Mus musculus' , 'FM3A'
            #  , 'Unchecked' , 'Mus musculus' , 'Unchecked' , 'Mus musculus'
            'target_tax_id': 'NUMERIC',
            # EXAMPLES:
            # '10116' , '10090' , '10090' , '10090' , '10090' , '10090' , '9606' , '9606' , '9606' , '10090'
            'text_value': 'TEXT',
            # EXAMPLES:
            # 'Active' , 'Active' , 'Not Active' , 'Active' , 'Linear Fit' , 'Not Determined' , 'Not Determined' , 'Acti
            # ve' , 'Not Active' , 'Not Determined'
            'toid': 'NUMERIC',
            # EXAMPLES:
            # '4790' , '4791' , '4792' , '4792' , '4793' , '4793' , '4794' , '4794' , '4794' , '4795'
            'type': 'TEXT',
            # EXAMPLES:
            # 'Cytotoxicity' , 'pKa' , 'Reduction' , 'IC50' , 'ED50' , 'Ratio' , 'IC50' , 'Activity' , '-Log IC50' , 'Ac
            # tivity'
            'units': 'TEXT',
            # EXAMPLES:
            # 'uM' , '%' , 'uM' , 'mg kg-1' , 'uM' , 'mg kg-1' , 'nM' , '%' , '%' , 'uM'
            'uo_units': 'TEXT',
            # EXAMPLES:
            # 'UO_0000064' , 'UO_0000187' , 'UO_0000065' , 'UO_0000308' , 'UO_0000065' , 'UO_0000308' , 'UO_0000065' , '
            # UO_0000065' , 'UO_0000065' , 'UO_0000065'
            'upper_value': 'NUMERIC',
            # EXAMPLES:
            # '32.0' , '13.1' , '5.0' , '63.0' , '3.36' , '1.8' , '40.0' , '3.0' , '109.0' , '14.0'
            'value': 'NUMERIC',
            # EXAMPLES:
            # '711.0' , '8.99' , '11.0' , '32.0' , '0.43' , '333.0' , '1.9' , '0.74' , '6.8' , '82.0'
        }
    }
