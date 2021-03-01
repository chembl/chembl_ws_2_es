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
                    'es_completion': 'TEXT',
                    # EXAMPLES:
                    # '{'input': 'CHEMBL1772953', 'weight': 10}' , '{'input': 'A series of pyridylpiperazines was synthe
                    # sized and analyzed for sigma receptor binding affinity to determine the optimal pyridyl nitrogen p
                    # osition and chain length for the sigma(1) and sigma(2) receptor recognition. The (3-pyridyl)pipera
                    # zines and (4-pyridyl)piperazines favor sigma(1) receptors, while previously studied (2-pyridyl)pip
                    # erazines favor sigma(2) receptors.', 'weight': 60}' , '{'input': '2003', 'weight': 1}' , '{'input'
                    # : 'The effects of replacing the central furan ring of furamidine with indole and benzimidazole on 
                    # their DNA binding affinity, antiparasitic activity and fluorescence are reported. The bis-cyanophe
                    # nylindoles required to make the corresponding amidines were prepared by sequential Stille and/or S
                    # uzuki coupling reactions. The bis-cyanophenylbenzimidazoles were obtained by coupling 4-cyanobenza
                    # ldehydes with the appropriate cyano substituted phenylenediamine. The bis-nitriles were converted 
                    # to the diamidines by reaction with LiN[Si(CH(3))(3)](2) or by Pinner methodology. Specifically, we
                    #  have prepared new series of 2,6- and 2,5-diaryl indoles (6a,b, 12 and 17a-d) and the related benz
                    # imidazoles (24, 30 and 35). The new compounds bind in the DNA minor groove in DNA AT base pair seq
                    # uences and eight of the ten new analogues exhibit ΔT(m) values comparable to or higher than that o
                    # f furamidine. Six of ten of the new compounds exhibit lower IC(50) values against Trypanosoma bruc
                    # ei rhodesiense (T. b. r.) and eight of ten exhibit lower IC(50) values against Plasmodium falcipar
                    # um (P. f.) than furamidine. Four of the ten show greater efficacy than furamidine in the rigorous 
                    # T. b. r. STIB900 mouse model for African trypanosomiasis. Generally, the fluorescence properties o
                    # f the new analogues are similar to that of DAPI.', 'weight': 60}' , '{'input': '2010', 'weight': 1
                    # }' , '{'input': 'The design and synthesis of novel series of 6-methyl-2-oxo-1,2,3,4-tetrahydro-pyr
                    # imidine-5-carboxylic acid (pyrimidone) derivatives that are high affinity ligands for peroxisome p
                    # roliferators activated receptor gamma have been reported as a potential substitute of 2,4-thiazoli
                    # dinedione head group. The FlexX docking and radioligand binding affinity of some promising compoun
                    # ds of this series is comparable to that of thiazolidinedione based antidiabetic drugs currently in
                    #  clinical use.', 'weight': 60}' , '{'input': '10.1021/jm00059a006', 'weight': 10}' , '{'input': 'H
                    # usain K, Bhat AR, Azam A.', 'weight': 100}' , '{'input': 'CHEMBL1128394', 'weight': 10}' , '{'inpu
                    # t': 'In this paper, we describe the SAR of ozonide carboxylic acid OZ78 (1) as the first part of o
                    # ur search for a trematocidal synthetic peroxide drug development candidate. We found that relative
                    # ly small structural changes to 1 resulted most commonly in loss of activity against Fasciola hepat
                    # ica in vivo. A spiroadamantane substructure and acidic functional group (or ester prodrug) were re
                    # quired for activity. Of 26 new compounds administered at single 100 mg/kg oral doses to F. hepatic
                    # a infected rats, 8 had statistically significant worm burden reductions, 7 were partially curative
                    # , and 1 (acylsulfonamide 6) was completely curative and comparable to 1 in flukicidal efficacy. Th
                    # is study also showed that the activity of 1 is peroxide-bond-dependent, suggesting that its flukic
                    # idal efficacy depends upon hemoglobin digestion in F. hepatica.', 'weight': 60}'
                    'related_activities': 
                    {
                        'properties': 
                        {
                            'count': 'NUMERIC',
                            # EXAMPLES:
                            # '5' , '18' , '1' , '108' , '96' , '20' , '68' , '42' , '68' , '47'
                        }
                    },
                    'related_assays': 
                    {
                        'properties': 
                        {
                            'all_chembl_ids': 'TEXT',
                            # EXAMPLES:
                            # 'CHEMBL1775483 CHEMBL1775484 CHEMBL1775482' , 'CHEMBL1111646 CHEMBL1111645 CHEMBL1113414' 
                            # , 'CHEMBL815068' , 'CHEMBL1768089 CHEMBL1768165 CHEMBL1768164 CHEMBL1768088 CHEMBL1768091 
                            # CHEMBL1768090 CHEMBL1768087 CHEMBL1768086' , 'CHEMBL1119011 CHEMBL1119023 CHEMBL1119013 CH
                            # EMBL1119027 CHEMBL1119028 CHEMBL1119018 CHEMBL1119016 CHEMBL1119024 CHEMBL1119026 CHEMBL11
                            # 19020 CHEMBL1119021 CHEMBL1119015 CHEMBL1119012 CHEMBL1119014 CHEMBL1119017 CHEMBL1119022 
                            # CHEMBL1119025 CHEMBL1119019' , 'CHEMBL888894' , 'CHEMBL876077 CHEMBL850534 CHEMBL652109 CH
                            # EMBL850535 CHEMBL845141 CHEMBL801614 CHEMBL632395' , 'CHEMBL979939 CHEMBL979941 CHEMBL9799
                            # 40' , 'CHEMBL755104 CHEMBL814123 CHEMBL755103 CHEMBL679843' , 'CHEMBL1111001 CHEMBL1111003
                            #  CHEMBL1111002'
                            'count': 'NUMERIC',
                            # EXAMPLES:
                            # '3' , '3' , '1' , '8' , '18' , '1' , '7' , '3' , '4' , '3'
                        }
                    },
                    'related_cell_lines': 
                    {
                        'properties': 
                        {
                            'all_chembl_ids': 'TEXT',
                            # EXAMPLES:
                            # 'CHEMBL3307474' , 'CHEMBL3308469' , 'CHEMBL3307639 CHEMBL3308372' , 'CHEMBL3307394' , 'CHE
                            # MBL3307959' , 'CHEMBL3307718 CHEMBL3307715' , 'CHEMBL3308072' , 'CHEMBL3307770 CHEMBL33084
                            # 03' , 'CHEMBL3307651 CHEMBL3307944 CHEMBL3308372' , 'CHEMBL3307574'
                            'count': 'NUMERIC',
                            # EXAMPLES:
                            # '1' , '1' , '2' , '1' , '1' , '2' , '1' , '2' , '3' , '1'
                        }
                    },
                    'related_compounds': 
                    {
                        'properties': 
                        {
                            'all_chembl_ids': 'TEXT',
                            # EXAMPLES:
                            # 'CHEMBL231549 CHEMBL231553 CHEMBL1773153' , 'CHEMBL1090907 CHEMBL143950 CHEMBL1089654 CHEM
                            # BL145867 CHEMBL1090908 CHEMBL1090909' , 'CHEMBL3037893' , 'CHEMBL3217178 CHEMBL3216087 CHE
                            # MBL24057 CHEMBL3216970 CHEMBL3215856 CHEMBL3216088 CHEMBL1765480 CHEMBL3216089 CHEMBL32169
                            # 71 CHEMBL3216295 CHEMBL1232057 CHEMBL3216747 CHEMBL55 CHEMBL3216513 CHEMBL48217' , 'CHEMBL
                            # 1085097 CHEMBL3144166 CHEMBL1086217 CHEMBL1085949 CHEMBL3144168 CHEMBL3216468 CHEMBL314415
                            # 9 CHEMBL3216466 CHEMBL3217134 CHEMBL3144164 CHEMBL3216251 CHEMBL3144165 CHEMBL3216927 CHEM
                            # BL3216467 CHEMBL3144161 CHEMBL3217135 CHEMBL3144157 CHEMBL3144162 CHEMBL3144158 CHEMBL3144
                            # 160 CHEMBL3216053 CHEMBL3144156 CHEMBL3144167 CHEMBL3217137 CHEMBL3216700 CHEMBL3144163 CH
                            # EMBL3216252 CHEMBL3216701 CHEMBL3216256 CHEMBL3216695 CHEMBL3215599 CHEMBL3216048 CHEMBL10
                            # 86216 CHEMBL3215808 CHEMBL3216255' , 'CHEMBL230565 CHEMBL230458 CHEMBL230670 CHEMBL230350 
                            # CHEMBL230672 CHEMBL445151 CHEMBL230460 CHEMBL228492 CHEMBL228548 CHEMBL388561 CHEMBL230567
                            #  CHEMBL394849 CHEMBL228388 CHEMBL228442 CHEMBL394605 CHEMBL396550 CHEMBL228443 CHEMBL39748
                            # 2 CHEMBL230566 CHEMBL595' , 'CHEMBL129 CHEMBL352398 CHEMBL168943 CHEMBL166784 CHEMBL991 CH
                            # EMBL170006 CHEMBL170331 CHEMBL440551 CHEMBL424540 CHEMBL354162 CHEMBL353179 CHEMBL166614 C
                            # HEMBL168236' , 'CHEMBL505120 CHEMBL462440 CHEMBL460708 CHEMBL460707 CHEMBL202752 CHEMBL512
                            # 927 CHEMBL460509 CHEMBL511360 CHEMBL460709 CHEMBL512041 CHEMBL461746 CHEMBL511873 CHEMBL46
                            # 1745 CHEMBL137' , 'CHEMBL67000 CHEMBL68017 CHEMBL304496 CHEMBL85320 CHEMBL479579 CHEMBL697
                            # 93 CHEMBL304939 CHEMBL66712 CHEMBL65903 CHEMBL308333 CHEMBL69745 CHEMBL10247 CHEMBL67348 C
                            # HEMBL2369423 CHEMBL66967 CHEMBL66882 CHEMBL63317 CHEMBL2372437 CHEMBL68128 CHEMBL304736 CH
                            # EMBL303892 CHEMBL66318 CHEMBL303159 CHEMBL66284' , 'CHEMBL1097084 CHEMBL3084739 CHEMBL1097
                            # 092 CHEMBL1096763 CHEMBL1097441 CHEMBL1097099 CHEMBL1094204 CHEMBL1097076 CHEMBL1098011 CH
                            # EMBL1097091 CHEMBL1096762 CHEMBL1096761 CHEMBL361497 CHEMBL1097431 CHEMBL584947 CHEMBL1097
                            # 093 CHEMBL600116 CHEMBL1097663 CHEMBL1096777 CHEMBL1097094 CHEMBL1096779 CHEMBL1097439 CHE
                            # MBL569032 CHEMBL1096783 CHEMBL388806 CHEMBL578617 CHEMBL3084740 CHEMBL1097095'
                            'count': 'NUMERIC',
                            # EXAMPLES:
                            # '3' , '6' , '1' , '15' , '35' , '20' , '13' , '14' , '24' , '28'
                        }
                    },
                    'related_targets': 
                    {
                        'properties': 
                        {
                            'all_chembl_ids': 'TEXT',
                            # EXAMPLES:
                            # 'CHEMBL3879801 CHEMBL612558' , 'CHEMBL3602 CHEMBL612545' , 'CHEMBL615024' , 'CHEMBL612348 
                            # CHEMBL612545 CHEMBL614793 CHEMBL613826 CHEMBL612856' , 'CHEMBL614535 CHEMBL6136' , 'CHEMBL
                            # 235' , 'CHEMBL247 CHEMBL372 CHEMBL612545 CHEMBL614545' , 'CHEMBL3879801 CHEMBL398 CHEMBL61
                            # 2853' , 'CHEMBL3392 CHEMBL4791 CHEMBL3768' , 'CHEMBL612860'
                            'count': 'NUMERIC',
                            # EXAMPLES:
                            # '2' , '2' , '1' , '5' , '2' , '1' , '4' , '3' , '3' , '1'
                        }
                    },
                    'related_tissues': 
                    {
                        'properties': 
                        {
                            'all_chembl_ids': 'TEXT',
                            # EXAMPLES:
                            # 'CHEMBL3559721' , 'CHEMBL3638254' , 'CHEMBL3559721 CHEMBL3559723' , 'CHEMBL3559723' , 'CHE
                            # MBL3638188' , 'CHEMBL3559721' , 'CHEMBL3638261 CHEMBL3559721 CHEMBL3559723' , 'CHEMBL36381
                            # 86 CHEMBL3559721' , 'CHEMBL3559723' , 'CHEMBL3638178'
                            'count': 'NUMERIC',
                            # EXAMPLES:
                            # '1' , '1' , '2' , '1' , '1' , '1' , '3' , '2' , '1' , '1'
                        }
                    },
                    'similar_documents': 
                    {
                        'properties': 
                        {
                            'document_chembl_id': 'TEXT',
                            # EXAMPLES:
                            # 'CHEMBL1921746' , 'CHEMBL2016489' , 'CHEMBL1144254' , 'CHEMBL1914412' , 'CHEMBL1142029' , 
                            # 'CHEMBL3352783' , 'CHEMBL1155264' , 'CHEMBL2074386' , 'CHEMBL1126109' , 'CHEMBL1135794'
                            'doi': 'TEXT',
                            # EXAMPLES:
                            # '10.1016/j.bmcl.2011.09.129' , '10.1021/ml2001505' , '10.1016/j.bmcl.2004.10.052' , '10.10
                            # 16/j.ejmech.2011.09.047' , '10.1016/j.bmcl.2005.01.074' , '10.1016/j.bmcl.2014.10.017' , '
                            # 10.1016/j.ejmech.2009.05.030' , '10.1016/j.ejmech.2010.02.024' , '10.1021/jm00102a015' , '
                            # 10.1021/jm015567k'
                            'first_page': 'NUMERIC',
                            # EXAMPLES:
                            # '7460' , '834' , '435' , '5852' , '1547' , '5814' , '4716' , '1439' , '4608' , '251'
                            'journal': 'TEXT',
                            # EXAMPLES:
                            # 'Bioorg. Med. Chem. Lett.' , 'ACS Med. Chem. Lett.' , 'Bioorg. Med. Chem. Lett.' , 'Eur. J
                            # . Med. Chem.' , 'Bioorg. Med. Chem. Lett.' , 'Bioorg. Med. Chem. Lett.' , 'Eur. J. Med. Ch
                            # em.' , 'J. Pharmacol. Exp. Ther.' , 'J. Med. Chem.' , 'J. Med. Chem.'
                            'last_page': 'NUMERIC',
                            # EXAMPLES:
                            # '7465' , '839' , '438' , '5860' , '1551' , '5817' , '4720' , '1445' , '4612' , '254'
                            'mol_tani': 'NUMERIC',
                            # EXAMPLES:
                            # '0.0' , '0.0' , '0.0' , '0.03' , '0.03' , '0.05' , '0.06' , '0.33' , '0.02' , '0.02'
                            'pubmed_id': 'NUMERIC',
                            # EXAMPLES:
                            # '22071304' , '24900272' , '15603968' , '22005186' , '15745794' , '25455496' , '19560842' ,
                            #  '9732409' , '1361579' , '11784128'
                            'tid_tani': 'NUMERIC',
                            # EXAMPLES:
                            # '1.0' , '1.0' , '1.0' , '0.75' , '1.0' , '1.0' , '1.0' , '1.0' , '1.0' , '1.0'
                            'title': 'TEXT',
                            # EXAMPLES:
                            # 'Chemical constituents of the rhizomes of Hedychium coronarium and their inhibitory effect
                            #  on the pro-inflammatory cytokines production LPS-stimulated in bone marrow-derived dendri
                            # tic cells.' , 'Homology Model and Docking-Based Virtual Screening for Ligands of the σ1 Re
                            # ceptor.' , 'Synthesis and SAR of novel 4,5-diarylimidazolines as potent P2X7 receptor anta
                            # gonists.' , 'Molecular modeling study and synthesis of novel dicationic flexible triaryl g
                            # uanidines and imidamides as antiprotozoal agents.' , 'Design, synthesis, and biological ac
                            # tivity of novel PPARgamma ligands based on rosiglitazone and 15d-PGJ2.' , 'A highly water 
                            # soluble benzimidazole derivative useful for the treatment of fasciolosis.' , 'Synthesis of
                            #  substituted-phenyl-1,2,4-triazol-3-thione analogues with modified D-glucopyranosyl residu
                            # es and their antiproliferative activities.' , 'Saquinavir, an HIV protease inhibitor, is t
                            # ransported by P-glycoprotein.' , 'DL-tetrazol-5-ylglycine, a highly potent NMDA agonist: i
                            # ts synthesis and NMDA receptor efficacy.' , 'Looking for selectivity among cytochrome P450
                            # s inhibitors.'
                            'volume': 'NUMERIC',
                            # EXAMPLES:
                            # '21' , '2' , '15' , '46' , '15' , '24' , '44' , '286' , '35' , '45'
                            'year': 'NUMERIC',
                            # EXAMPLES:
                            # '2011' , '2011' , '2005' , '2011' , '2005' , '2014' , '2009' , '1998' , '1992' , '2002'
                        }
                    },
                    'source': 
                    {
                        'properties': 
                        {
                            'src_description': 'TEXT',
                            # EXAMPLES:
                            # 'Scientific Literature' , 'Scientific Literature' , 'Scientific Literature' , 'Scientific 
                            # Literature' , 'Scientific Literature' , 'Scientific Literature' , 'Scientific Literature' 
                            # , 'Scientific Literature' , 'Scientific Literature' , 'Scientific Literature'
                            'src_id': 'NUMERIC',
                            # EXAMPLES:
                            # '1' , '1' , '1' , '1' , '1' , '1' , '1' , '1' , '1' , '1'
                            'src_short_name': 'TEXT',
                            # EXAMPLES:
                            # 'LITERATURE' , 'LITERATURE' , 'LITERATURE' , 'LITERATURE' , 'LITERATURE' , 'LITERATURE' , 
                            # 'LITERATURE' , 'LITERATURE' , 'LITERATURE' , 'LITERATURE'
                        }
                    }
                }
            },
            'abstract': 'TEXT',
            # EXAMPLES:
            # 'A series of benzodiazepine MMP/TACE inhibitors bearing polar moieties has been synthesized in an effort t
            # o optimize inhibitory activity against LPS-stimulated TNF production in human monocytes and oral activity 
            # in a murine LPS model.' , '' , '' , 'A series of thiophene PLK1 inhibitors was optimized for increased sol
            # ubility and reduced protein binding through the appendage of basic amine functionality. Interesting select
            # ivity between PLK1 and PLK3 was also obtained through these modifications.' , '' , 'A series of potent and
            #  selective 3,4-diamino-1,2,5-thiadiazoles were prepared and found to show excellent binding affinities tow
            # ards CXCR2 receptor.' , 'Tricyclic pyrazole tetrazoles which are potent partial agonists of the high affin
            # ity niacin receptor, GPR109a, have been discovered and optimized. One of these compounds has proven to be 
            # effective at lowering free fatty acids in vitro and in vivo.' , '' , '' , ''
            'authors': 'TEXT',
            # EXAMPLES:
            # 'Igarashi Y, Yanase S, Sugimoto K, Enomoto M, Miyanaga S, Trujillo ME, Saiki I, Kuwahara S.' , 'Stavitskay
            # a L, Seminerio MJ, Matthews-Tsourounis MM, Matsumoto RR, Coop A.' , 'Fernández-Mayoralas A, De La Figuera 
            # N, Zurita M, Vaquero J, Abraham GA, San Román J, Nieto-Sampedro M.' , 'Farahat AA, Paliakov E, Kumar A, Ba
            # rghash AE, Goda FE, Eisa HM, Wenzler T, Brun R, Liu Y, Wilson WD, Boykin DW.' , 'Sharma SK, Wu Y, Steinber
            # gs N, Crowley ML, Hanson AS, Casero RA, Woster PM.' , 'Kumar R, Mittal A, Ramachandran U.' , 'Sergheraert 
            # C, Pierlot C, Tartar A, Henin Y, Lemaitre M.' , 'Husain K, Bhat AR, Azam A.' , 'Bihovsky R, Levinson BL, L
            # oewi RC, Erhardt PW, Polokoff MA.' , 'Zhao Q, Vargas M, Dong Y, Zhou L, Wang X, Sriraghavan K, Keiser J, V
            # ennerstrom JL.'
            'doc_type': 'TEXT',
            # EXAMPLES:
            # 'PUBLICATION' , 'PUBLICATION' , 'PUBLICATION' , 'PUBLICATION' , 'PUBLICATION' , 'PUBLICATION' , 'PUBLICATI
            # ON' , 'PUBLICATION' , 'PUBLICATION' , 'PUBLICATION'
            'document_chembl_id': 'TEXT',
            # EXAMPLES:
            # 'CHEMBL1772953' , 'CHEMBL1156202' , 'CHEMBL1136749' , 'CHEMBL1765028' , 'CHEMBL1155444' , 'CHEMBL1145436' 
            # , 'CHEMBL1126627' , 'CHEMBL1140973' , 'CHEMBL1128394' , 'CHEMBL1157795'
            'doi': 'TEXT',
            # EXAMPLES:
            # '10.1021/np100779t' , '10.1016/j.bmcl.2010.02.087' , '10.1021/jm025620k' , '10.1016/j.bmc.2011.02.045' , '
            # 10.1021/jm100217a' , '10.1016/j.bmcl.2007.05.081' , '10.1021/jm00059a006' , '10.1016/j.ejmech.2007.12.002'
            #  , '10.1021/jm00012a011' , '10.1021/jm100226t'
            'first_page': 'NUMERIC',
            # EXAMPLES:
            # '862' , '2564' , '1286' , '2156' , '5197' , '4613' , '826' , '2016' , '2119' , '4223'
            'issue': 'NUMERIC',
            # EXAMPLES:
            # '4' , '8' , '8' , '7' , '14' , '16' , '7' , '9' , '12' , '10'
            'journal': 'TEXT',
            # EXAMPLES:
            # 'J. Nat. Prod.' , 'Bioorg. Med. Chem. Lett.' , 'J. Med. Chem.' , 'Bioorg. Med. Chem.' , 'J. Med. Chem.' , 
            # 'Bioorg. Med. Chem. Lett.' , 'J. Med. Chem.' , 'Eur. J. Med. Chem.' , 'J. Med. Chem.' , 'J. Med. Chem.'
            'journal_full_title': 'TEXT',
            # EXAMPLES:
            # 'Journal of natural products.' , 'Bioorganic & medicinal chemistry letters.' , 'Journal of medicinal chemi
            # stry.' , 'Bioorganic & medicinal chemistry.' , 'Journal of medicinal chemistry.' , 'Bioorganic & medicinal
            #  chemistry letters.' , 'Journal of medicinal chemistry.' , 'European journal of medicinal chemistry.' , 'J
            # ournal of medicinal chemistry.' , 'Journal of medicinal chemistry.'
            'last_page': 'NUMERIC',
            # EXAMPLES:
            # '865' , '2565' , '1288' , '2167' , '5212' , '4618' , '830' , '2028' , '2129' , '4233'
            'patent_id': 'TEXT',
            # EXAMPLES:
            # 'US-9108951-B2' , 'US-9114126-B2' , 'US-9115102-B2' , 'US-9115116-B2' , 'US-9073940-B2' , 'US-7288556-B2' 
            # , 'US-9115144-B2' , 'US-9120745-B2' , 'US-9120752-B2' , 'US-9238653-B2'
            'pubmed_id': 'NUMERIC',
            # EXAMPLES:
            # '21226490' , '20338757' , '12672228' , '21421317' , '20568780' , '17574414' , '8385224' , '18222017' , '77
            # 83143' , '20423101'
            'src_id': 'NUMERIC',
            # EXAMPLES:
            # '1' , '1' , '1' , '1' , '1' , '1' , '1' , '1' , '1' , '1'
            'title': 'TEXT',
            # EXAMPLES:
            # 'Lupinacidin C, an inhibitor of tumor cell invasion from Micromonospora lupini.' , 'The effect of the pyri
            # dyl nitrogen position in pyridylpiperazine sigma ligands.' , 'Central neural tumor destruction by controll
            # ed release of a synthetic glycoside dispersed in a biodegradable polymeric matrix.' , 'Exploration of larg
            # er central ring linkers in furamidine analogues: synthesis and evaluation of their DNA binding, antiparasi
            # tic and fluorescence properties.' , '(Bis)urea and (bis)thiourea inhibitors of lysine-specific demethylase
            #  1 as epigenetic modulators.' , 'Design and synthesis of 6-methyl-2-oxo-1,2,3,4-tetrahydro-pyrimidine-5-ca
            # rboxylic acid derivatives as PPARgamma activators.' , 'Synthesis and anti-HIV evaluation of D4T and D4T 5'
            # -monophosphate prodrugs.' , 'New Pd(II) complexes of the synthesized 1-N-substituted thiosemicarbazones of
            #  3-indole carboxaldehyde: characterization and antiamoebic assessment against E. histolytica.' , 'Hydroxam
            # ic acids as potent inhibitors of endothelin-converting enzyme from human bronchiolar smooth muscle.' , 'St
            # ructure-activity relationship of an ozonide carboxylic acid (OZ78) against Fasciola hepatica.'
            'volume': 'NUMERIC',
            # EXAMPLES:
            # '74' , '20' , '46' , '19' , '53' , '17' , '36' , '43' , '38' , '53'
            'year': 'NUMERIC',
            # EXAMPLES:
            # '2011' , '2010' , '2003' , '2011' , '2010' , '2007' , '1993' , '2008' , '1995' , '2010'
        }
    }
