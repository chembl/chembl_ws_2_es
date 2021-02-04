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
            # 'Not Active' , 'Inactive at solubility limit' , 'Not Determined' , 'Not Active' , 'Not Determined' , 'Not 
            # Determined' , 'Not Determined' , 'Not Determined' , 'Not Active' , 'Not Determined'
            'activity_id': 'NUMERIC',
            # EXAMPLES:
            # '342722' , '335647' , '342724' , '335935' , '335652' , '343013' , '342732' , '338108' , '338378' , '342734
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
                    # 'CHOL (Cholesterol)' , 'WEIGHT (Total Kidney Weight)' , 'TERMBW (Terminal Body Weight)' , 'CHLORID
                    # E (Chloride)' , 'WEIGHT (Total Kidney Weight)' , 'WEIGHT (Liver Weight)' , 'WEIGHT (Right Kidney W
                    # eight)' , 'GGT (Gamma Glutamyl Transferase)' , 'WEIGHT (Liver Weight)' , 'TERMBW (Terminal Body We
                    # ight)'
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
                    # '2000.0' , '300.0' , '300.0' , '450.0' , '300.0' , '300.0' , '0.0' , '450.0' , '5.0' , '300.0'
                    'text_value': 'TEXT',
                    # EXAMPLES:
                    # 'CHOL (Cholesterol)' , 'WEIGHT (Total Kidney Weight)' , 'TERMBW (Terminal Body Weight)' , 'CHLORID
                    # E (Chloride)' , 'WEIGHT (Total Kidney Weight)' , 'WEIGHT (Liver Weight)' , 'WEIGHT (Right Kidney W
                    # eight)' , 'GGT (Gamma Glutamyl Transferase)' , 'WEIGHT (Liver Weight)' , 'TERMBW (Terminal Body We
                    # ight)'
                    'type': 'TEXT',
                    # EXAMPLES:
                    # 'ACTIVITY_TEST' , 'ACTIVITY_TEST' , 'ACTIVITY_TEST' , 'ACTIVITY_TEST' , 'ACTIVITY_TEST' , 'ACTIVIT
                    # Y_TEST' , 'ACTIVITY_TEST' , 'ACTIVITY_TEST' , 'ACTIVITY_TEST' , 'ACTIVITY_TEST'
                    'units': 'TEXT',
                    # EXAMPLES:
                    # 'mg/kg' , 'mg/kg' , 'mg/kg' , 'mg/kg' , 'mg/kg' , 'mg/kg' , 'mg/kg' , 'mg/kg' , 'mg/kg' , 'mg/kg'
                    'value': 'NUMERIC',
                    # EXAMPLES:
                    # '2000.0' , '300.0' , '300.0' , '450.0' , '300.0' , '300.0' , '0.0' , '450.0' , '5.0' , '300.0'
                }
            },
            'assay_chembl_id': 'TEXT',
            # EXAMPLES:
            # 'CHEMBL712523' , 'CHEMBL844043' , 'CHEMBL760277' , 'CHEMBL783082' , 'CHEMBL657879' , 'CHEMBL851341' , 'CHE
            # MBL662561' , 'CHEMBL842068' , 'CHEMBL630163' , 'CHEMBL768069'
            'assay_description': 'TEXT',
            # EXAMPLES:
            # 'In vitro inhibition of Leishmania donovani parasite' , 'Relative inhibition of PDE11 and PDE5' , 'In vitr
            # o antiplasmodial activity against chloroquine-sensitive Plasmodium falciparum Haiti 135' , 'Percentage of 
            # animals failing to escape shock was measured, affording a rough index for nonspecific sedation at 15 mg/kg
            # (ip)' , 'Compound was tested for inherent antifungal geometric minimum inhibitory concentration (GMMIC) ag
            # ainst Candida albicans and Candida tropicalis in serial dilution from 64 to 0.0313 ug/mL' , 'Ratio of IC50
            #  against human plasma renin to that of purified recombinant human renin' , 'Compound was evaluated for fun
            # ctional activity on Cholecystokinin type B receptor (CCK-B) receptor carried out on guinea pig stomach cel
            # ls.' , 'Inhibitory activity against p56 Lck tyrosine kinase' , 'Tested for biodistribution of radioactivit
            # y after 3h of intravenous injection in mice kidneys' , 'In vitro inhibition of ADP-induced platelet aggreg
            # ation in human platelet rich plasma (hPRP)'
            'assay_type': 'TEXT',
            # EXAMPLES:
            # 'F' , 'B' , 'F' , 'F' , 'F' , 'B' , 'B' , 'B' , 'A' , 'F'
            'assay_variant_accession': 'TEXT',
            # EXAMPLES:
            # 'Q9WKE8' , 'P25103' , 'P25103' , 'Q9WKE8' , 'Q9WKE8' , 'P29274' , 'Q9WKE8' , 'Q9WKE8' , 'Q9WJQ2' , 'Q9WKE8
            # '
            'assay_variant_mutation': 'TEXT',
            # EXAMPLES:
            # 'K103N' , 'Q165A' , 'Q165A' , 'K103N' , 'K103N' , 'V84L' , 'K103N' , 'K103N' , 'E233V' , 'K103N'
            'bao_endpoint': 'TEXT',
            # EXAMPLES:
            # 'BAO_0000190' , 'BAO_0000179' , 'BAO_0000190' , 'BAO_0000179' , 'BAO_0000179' , 'BAO_0000179' , 'BAO_00001
            # 90' , 'BAO_0000190' , 'BAO_0000179' , 'BAO_0000190'
            'bao_format': 'TEXT',
            # EXAMPLES:
            # 'BAO_0000218' , 'BAO_0000019' , 'BAO_0000218' , 'BAO_0000218' , 'BAO_0000218' , 'BAO_0000357' , 'BAO_00000
            # 19' , 'BAO_0000357' , 'BAO_0000218' , 'BAO_0000366'
            'bao_label': 'TEXT',
            # EXAMPLES:
            # 'organism-based format' , 'assay format' , 'organism-based format' , 'organism-based format' , 'organism-b
            # ased format' , 'single protein format' , 'assay format' , 'single protein format' , 'organism-based format
            # ' , 'cell-free format'
            'canonical_smiles': 'TEXT',
            # EXAMPLES:
            # 'NS(=O)(=O)c1cc(C(F)(F)F)ccc1Cl' , 'NC(=O)CCN1CC[C@@H](N2CC(=O)N3[C@H](Cc4c([nH]c5ccccc45)[C@H]3c3ccc4c(c3
            # )OCO4)C2=O)C1' , 'CCN(CC)CCNc1ccnc2cc(I)ccc12' , 'COc1ccccc1N1CCN(Cc2ccc(CN3CCCCC3=O)o2)CC1.O=C(O)CCC(=O)O
            # ' , 'CCC(CC)n1ncn(-c2ccc(N3CCN(c4ccc(OC[C@H]5CC[C@](Cn6cncn6)(c6ccc(F)cc6F)O5)cc4)CC3)cc2)c1=O' , 'c1ccc(C
            # OCCCOc2ncc([C@H]3CCNC[C@@H]3OCc3ccc4ccccc4c3)cn2)cc1' , 'CC(C)Oc1cccc(-n2c(NNC(=O)Nc3ccc(Br)cc3)nc3ccccc3c
            # 2=O)c1' , 'N=c1oc2c(O)c(O)ccc2cc1C(=O)Nc1ccccc1' , 'N[C@@H](CSC1CC(=O)N(CCOC(=O)CNC(=O)c2cccc(I)c2)C1=O)C(
            # =O)O' , 'N=C(N)c1ccc(C2=NOC(CC(=O)NC(CC(=O)O)CC(=O)O)C2)cc1.O=C(O)C(F)(F)F'
            'data_validity_comment': 'TEXT',
            # EXAMPLES:
            # 'Outside typical range' , 'Outside typical range' , 'Outside typical range' , 'Non standard unit for type'
            #  , 'Non standard unit for type' , 'Outside typical range' , 'Non standard unit for type' , 'Outside typica
            # l range' , 'Non standard unit for type' , 'Outside typical range'
            'data_validity_description': 'TEXT',
            # EXAMPLES:
            # 'Values for this activity type are unusually large/small, so may not be accurate' , 'Values for this activ
            # ity type are unusually large/small, so may not be accurate' , 'Values for this activity type are unusually
            #  large/small, so may not be accurate' , 'Units for this activity type are unusual and may be incorrect (or
            #  the standard_type may be incorrect)' , 'Units for this activity type are unusual and may be incorrect (or
            #  the standard_type may be incorrect)' , 'Values for this activity type are unusually large/small, so may n
            # ot be accurate' , 'Units for this activity type are unusual and may be incorrect (or the standard_type may
            #  be incorrect)' , 'Values for this activity type are unusually large/small, so may not be accurate' , 'Uni
            # ts for this activity type are unusual and may be incorrect (or the standard_type may be incorrect)' , 'Val
            # ues for this activity type are unusually large/small, so may not be accurate'
            'document_chembl_id': 'TEXT',
            # EXAMPLES:
            # 'CHEMBL1131410' , 'CHEMBL1136701' , 'CHEMBL1131415' , 'CHEMBL1128321' , 'CHEMBL1135167' , 'CHEMBL1131714' 
            # , 'CHEMBL1131373' , 'CHEMBL1152042' , 'CHEMBL1127612' , 'CHEMBL1130078'
            'document_journal': 'TEXT',
            # EXAMPLES:
            # 'J. Med. Chem.' , 'Bioorg. Med. Chem. Lett.' , 'J. Med. Chem.' , 'J. Med. Chem.' , 'Bioorg. Med. Chem. Let
            # t.' , 'Bioorg. Med. Chem. Lett.' , 'J. Med. Chem.' , 'Bioorg. Med. Chem. Lett.' , 'J. Med. Chem.' , 'J. Me
            # d. Chem.'
            'document_year': 'NUMERIC',
            # EXAMPLES:
            # '1998' , '2003' , '1998' , '1995' , '2002' , '1999' , '1998' , '1995' , '1994' , '1997'
            'ligand_efficiency': 
            {
                'properties': 
                {
                    'bei': 'NUMERIC',
                    # EXAMPLES:
                    # '14.30' , '14.61' , '16.00' , '26.18' , '21.26' , '33.02' , '12.73' , '31.35' , '16.16' , '21.98'
                    'le': 'NUMERIC',
                    # EXAMPLES:
                    # '0.30' , '0.27' , '0.30' , '0.49' , '0.39' , '0.64' , '0.24' , '0.59' , '0.30' , '0.45'
                    'lle': 'NUMERIC',
                    # EXAMPLES:
                    # '2.19' , '2.01' , '2.56' , '4.65' , '3.68' , '5.43' , '7.17' , '7.14' , '2.85' , '3.92'
                    'sei': 'NUMERIC',
                    # EXAMPLES:
                    # '7.47' , '6.85' , '8.82' , '6.70' , '7.45' , '11.09' , '4.46' , '18.22' , '5.46' , '11.84'
                }
            },
            'molecule_chembl_id': 'TEXT',
            # EXAMPLES:
            # 'CHEMBL144456' , 'CHEMBL33147' , 'CHEMBL332186' , 'CHEMBL1161070' , 'CHEMBL298899' , 'CHEMBL277738' , 'CHE
            # MBL9422' , 'CHEMBL80091' , 'CHEMBL89596' , 'CHEMBL62827'
            'molecule_pref_name': 'TEXT',
            # EXAMPLES:
            # 'RIFAMPIN' , 'ATROPINE' , '(S)-PIA' , '(S)-PIA' , 'APOMORPHINE' , 'IODOQUINOL' , 'PENCICLOVIR' , 'YM-90K' 
            # , 'TRETINOIN' , 'MEPRYLCAINE'
            'parent_molecule_chembl_id': 'TEXT',
            # EXAMPLES:
            # 'CHEMBL144456' , 'CHEMBL33147' , 'CHEMBL332186' , 'CHEMBL1199896' , 'CHEMBL298899' , 'CHEMBL277738' , 'CHE
            # MBL9422' , 'CHEMBL80091' , 'CHEMBL89596' , 'CHEMBL1179161'
            'pchembl_value': 'NUMERIC',
            # EXAMPLES:
            # '8.22' , '7.27' , '6.68' , '7.30' , '6.92' , '7.82' , '7.21' , '5.40' , '6.00' , '4.77'
            'potential_duplicate': 'BOOLEAN',
            # EXAMPLES:
            # 'False' , 'False' , 'False' , 'False' , 'False' , 'False' , 'False' , 'False' , 'False' , 'False'
            'qudt_units': 'TEXT',
            # EXAMPLES:
            # 'http://www.openphacts.org/units/Nanomolar' , 'http://www.openphacts.org/units/Nanomolar' , 'http://qudt.o
            # rg/vocab/unit#Percent' , 'http://www.openphacts.org/units/MicrogramPerMilliliter' , 'http://www.openphacts
            # .org/units/Nanomolar' , 'http://www.openphacts.org/units/MicrogramPerMilliliter' , 'http://qudt.org/vocab/
            # unit#Percent' , 'http://www.openphacts.org/units/Nanomolar' , 'http://www.openphacts.org/units/Nanomolar' 
            # , 'http://www.openphacts.org/units/Nanomolar'
            'record_id': 'NUMERIC',
            # EXAMPLES:
            # '282421' , '48924' , '283553' , '257307' , '80812' , '46500' , '5461' , '143771' , '160062' , '112765'
            'relation': 'TEXT',
            # EXAMPLES:
            # '>' , '=' , '=' , '=' , '=' , '=' , '=' , '>' , '=' , '='
            'src_id': 'NUMERIC',
            # EXAMPLES:
            # '1' , '1' , '1' , '1' , '1' , '1' , '1' , '1' , '1' , '1'
            'standard_flag': 'BOOLEAN',
            # EXAMPLES:
            # 'True' , 'False' , 'True' , 'False' , 'False' , 'False' , 'True' , 'True' , 'False' , 'True'
            'standard_relation': 'TEXT',
            # EXAMPLES:
            # '>' , '=' , '=' , '=' , '=' , '=' , '=' , '>' , '=' , '='
            'standard_text_value': 'TEXT',
            # EXAMPLES:
            # 'Active' , 'Active' , 'Not Active' , 'Active' , 'Linear Fit' , 'Not Determined' , 'Not Determined' , 'Acti
            # ve' , 'Active' , 'Not Active'
            'standard_type': 'TEXT',
            # EXAMPLES:
            # 'IC50' , 'Selectivity ratio' , 'IC50' , 'Esc loss' , 'GMMIC' , 'Ratio' , 'IC50' , 'IC50' , 'Dose/organ' , 
            # 'IC50'
            'standard_units': 'TEXT',
            # EXAMPLES:
            # 'nM' , 'nM' , '%' , 'ug ml-1' , 'nM' , 'ug.mL-1' , '%' , 'nM' , 'nM' , 'nM'
            'standard_value': 'NUMERIC',
            # EXAMPLES:
            # '450000.0' , '5.7' , '6.0' , '0.0' , '0.02' , '10.0' , '54.0' , '20.0' , '5.0' , '210.0'
            'target_chembl_id': 'TEXT',
            # EXAMPLES:
            # 'CHEMBL367' , 'CHEMBL612545' , 'CHEMBL364' , 'CHEMBL376' , 'CHEMBL612867' , 'CHEMBL286' , 'CHEMBL298' , 'C
            # HEMBL258' , 'CHEMBL375' , 'CHEMBL2093869'
            'target_organism': 'TEXT',
            # EXAMPLES:
            # 'Leishmania donovani' , 'Plasmodium falciparum' , 'Rattus norvegicus' , 'Candida' , 'Homo sapiens' , 'Homo
            #  sapiens' , 'Homo sapiens' , 'Mus musculus' , 'Homo sapiens' , 'Homo sapiens'
            'target_pref_name': 'TEXT',
            # EXAMPLES:
            # 'Leishmania donovani' , 'Unchecked' , 'Plasmodium falciparum' , 'Rattus norvegicus' , 'Candida' , 'Renin' 
            # , 'Cholecystokinin B receptor' , 'Tyrosine-protein kinase LCK' , 'Mus musculus' , 'Integrin alpha-IIb/beta
            # -3'
            'target_tax_id': 'NUMERIC',
            # EXAMPLES:
            # '5661' , '5833' , '10116' , '5475' , '9606' , '9606' , '9606' , '10090' , '9606' , '9606'
            'text_value': 'TEXT',
            # EXAMPLES:
            # 'Active' , 'Active' , 'Not Active' , 'Active' , 'Linear Fit' , 'Not Determined' , 'Not Determined' , 'Acti
            # ve' , 'Active' , 'Not Active'
            'toid': 'NUMERIC',
            # EXAMPLES:
            # '9459' , '6070' , '7033' , '9030' , '7033' , '6071' , '8927' , '9030' , '5384' , '7035'
            'type': 'TEXT',
            # EXAMPLES:
            # 'IC50' , 'Selectivity ratio' , 'IC50' , 'Esc loss' , 'GMMIC' , 'Ratio' , 'IC50' , 'IC50' , 'Dose/organ' , 
            # 'IC50'
            'units': 'TEXT',
            # EXAMPLES:
            # 'uM' , 'nM' , '%' , 'ug ml-1' , 'nM' , 'ug ml-1' , '%' , 'uM' , 'uM' , 'nM'
            'uo_units': 'TEXT',
            # EXAMPLES:
            # 'UO_0000065' , 'UO_0000065' , 'UO_0000187' , 'UO_0000274' , 'UO_0000065' , 'UO_0000274' , 'UO_0000187' , '
            # UO_0000065' , 'UO_0000065' , 'UO_0000065'
            'upper_value': 'NUMERIC',
            # EXAMPLES:
            # '13.0' , '2.0' , '40.0' , '37.4' , '64.0' , '50.7' , '55.0' , '3.0' , '10.0' , '50.0'
            'value': 'NUMERIC',
            # EXAMPLES:
            # '450.0' , '5.7' , '6.0' , '0.0' , '0.02' , '10.0' , '54.0' , '20.0' , '5.0' , '0.21'
        }
    }
