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
                    'compound_records': 
                    {
                        'properties': 
                        {
                        }
                    },
                    'drug': 
                    {
                        'properties': 
                        {
                            'drug_data': 
                            {
                                'properties': 
                                {
                                    'atc_classification': 
                                    {
                                        'properties': 
                                        {
                                        }
                                    },
                                    'biotherapeutic': 
                                    {
                                        'properties': 
                                        {
                                            'biocomponents': 
                                            {
                                                'properties': 
                                                {
                                                }
                                            },
                                        }
                                    },
                                    'drug_warnings': 
                                    {
                                        'properties': 
                                        {
                                            'warning_refs': 
                                            {
                                                'properties': 
                                                {
                                                }
                                            },
                                        }
                                    },
                                    'molecule_properties': 
                                    {
                                        'properties': 
                                        {
                                        }
                                    },
                                    'molecule_structures': 
                                    {
                                        'properties': 
                                        {
                                        }
                                    },
                                    'molecule_synonyms': 
                                    {
                                        'properties': 
                                        {
                                        }
                                    },
                                }
                            },
                        }
                    },
                    'es_completion': 'TEXT',
                    # EXAMPLES:
                    # '{'input': 'HDTTZGYLHRXEKT-UHFFFAOYSA-N', 'weight': 30}' , '{'input': 'CHEMBL1517685', 'weight': 1
                    # 0}' , '{'input': 'InChI=1S/C20H20FN3O6S/c1-24-16(11-15(23-31(24,26)27)12-5-7-13(21)8-6-12)20(25)22
                    # -14-9-17(28-2)19(30-4)18(10-14)29-3/h5-11H,1-4H3,(H,22,25)', 'weight': 30}' , '{'input': 'C21H26N4
                    # O6S', 'weight': 90}' , '{'input': 'InChI=1S/C21H20N2O5S/c1-4-23-17-10-11-19(14-6-5-7-15(20(14)17)2
                    # 1(23)24)29(25,26)22-16-9-8-13(27-2)12-18(16)28-3/h5-12,22H,4H2,1-3H3', 'weight': 30}' , '{'input':
                    #  'N#Cc1ccccc1-c1cncnc1NCc1cccnc1', 'weight': 30}' , '{'input': 'CHEMBL1551087', 'weight': 10}' , '
                    # {'input': 'C21H19N5O3', 'weight': 90}' , '{'input': 'C24H37N3O4S', 'weight': 90}' , '{'input': 'CH
                    # EMBL1540139', 'weight': 10}'
                    'related_targets': 
                    {
                        'properties': 
                        {
                        }
                    },
                }
            },
            'atc_classifications': 'TEXT',
            # EXAMPLES:
            # 'C01EB13' , 'P03BA03' , 'J01DF02' , 'A02BX14' , 'L01XC12' , 'M01AA02' , 'L01XE10' , 'C04AA31' , 'C08CA15' 
            # , 'R01AA13'
            'availability_type': 'NUMERIC',
            # EXAMPLES:
            # '-1' , '-1' , '-1' , '-1' , '-1' , '-1' , '-1' , '-1' , '-1' , '-1'
            'biotherapeutic': 
            {
                'properties': 
                {
                    'biocomponents': 
                    {
                        'properties': 
                        {
                            'component_id': 'NUMERIC',
                            # EXAMPLES:
                            # '6335' , '6341' , '6416' , '6503' , '8385' , '6363' , '6710' , '6478' , '6691' , '6677'
                            'component_type': 'TEXT',
                            # EXAMPLES:
                            # 'PROTEIN' , 'PROTEIN' , 'PROTEIN' , 'PROTEIN' , 'PROTEIN' , 'PROTEIN' , 'PROTEIN' , 'PROTE
                            # IN' , 'PROTEIN' , 'PROTEIN'
                            'description': 'TEXT',
                            # EXAMPLES:
                            # 'Brentuximab vedotin heavy chain' , 'Gantenerumab heavy chain' , 'Patritumab heavy chain' 
                            # , 'Fasinumab heavy chain' , 'Varlilumab heavy chain' , 'Rituximab heavy chain' , 'Serum al
                            # bumin precursor' , 'Alemtuzumab heavy chain' , 'Corticotropin-lipotropin precursor' , 'Pur
                            # ified semisynthetic human insulin zinc suspension'
                            'organism': 'TEXT',
                            # EXAMPLES:
                            # 'Homo sapiens' , 'Homo sapiens' , 'Homo sapiens' , 'Homo sapiens' , 'Homo sapiens' , 'Homo
                            #  sapiens' , 'Homo sapiens' , 'Homo sapiens' , 'Bos taurus' , 'Homo sapiens'
                            'sequence': 'TEXT',
                            # EXAMPLES:
                            # 'QIQLQQSGPEVVKPGASVKISCKASGYTFTDYYITWVKQKPGQGLEWIGWIYPGSGNTKYNEKFKGKATLTVDTSSSTAFMQLSSLTSE
                            # DTAVYFCANYGNYWFAYWGQGTQVTVSAASTKGPSVFPLAPSSKSTSGGTAALGCLVKDYFPEPVTVSWNSGALTSGVHTFPAVLQSSGL
                            # YSLSSVVTVPSSSLGTQTYICNVNHKPSNTKVDKKVEPKSCDKTHTCPPCPAPELLGGPSVFLFPPKPKDTLMISRTPEVTCVVVDVSHE
                            # DPEVKFNWYVDGVEVHNAKTKPREEQYNSTYRVVSVLTVLHQDWLNGKEYKCKVSNKALPAPIEKTISKAKGQPREPQVYTLPPSRDELT
                            # KNQVSLTCLVKGFYPSDIAVEWESNGQPENNYKTTPPVLDSDGSFFLYSKLTVDKSRWQQGNVFSCSVMHEALHNHYTQKSLSLSPG' ,
                            #  'QVELVESGGGLVQPGGSLRLSCAASGFTFSSYAMSWVRQAPGKGLEWVSAINASGTRTYYADSVKGRFTISRDNSKNTLYLQMNSLRA
                            # EDTAVYYCARGKGNTHKPYGYVRYFDVWGQGTLVTVSSASTKGPSVFPLAPSSKSTSGGTAALGCLVKDYFPEPVTVSWNSGALTSGVHT
                            # FPAVLQSSGLYSLSSVVTVPSSSLGTQTYICNVNHKPSNTKVDKKVEPKSCDKTHTCPPCPAPELLGGPSVFLFPPKPKDTLMISRTPEV
                            # TCVVVDVSHEDPEVKFNWYVDGVEVHNAKTKPREEQYNSTYRVVSVLTVLHQDWLNGKEYKCKVSNKALPAPIEKTISKAKGQPREPQVY
                            # TLPPSRDELTKNQVSLTCLVKGFYPSDIAVEWESNGQPENNYKTTPPVLDSDGSFFLYSKLTVDKSRWQQGNVFSCSVMHEALHNHYTQK
                            # SLSLSPGK' , 'QVQLQQWGAGLLKPSETLSLTCAVYGGSFSGYYWSWIRQPPGKGLEWIGEINHSGSTNYNPSLKSRVTISVETSKNQ
                            # FSLKLSSVTAADTAVYYCARDKWTWYFDLWGRGTLVTVSSASTKGPSVFPLAPSSKSTSGGTAALGCLVKDYFPEPVTVSWNSGALTSGV
                            # HTFPAVLQSSGLYSLSSVVTVPSSSLGTQTYICNVNHKPSNTKVDKRVEPKSCDKTHTCPPCPAPELLGGPSVFLFPPKPKDTLMISRTP
                            # EVTCVVVDVSHEDPEVKFNWYVDGVEVHNAKTKPREEQYNSTYRVVSVLTVLHQDWLNGKEYKCKVSNKALPAPIEKTISKAKGQPREPQ
                            # VYTLPPSREEMTKNQVSLTCLVKGFYPSDIAVEWESNGQPENNYKTTPPVLDSDGSFFLYSKLTVDKSRWQQGNVFSCSVMHEALHNHYT
                            # QKSLSLSPGK' , 'QVQLVQSGAEVKKPGASVKVSCKVSGFTLTELSIHWVRQAPGKGLEWMGGFDPEDGETIYAQKFQGRVTMTEDTS
                            # TDTAYMELTSLRSEDTAVYYCSTIFGVVTNFDNWGQGTLVTVSSASTKGPSVFPLAPCSRSTSESTAALGCLVKDYFPEPVTVSWNSGAL
                            # TSGVHTFPAVLQSSGLYSLSSVVTVPSSSLGTKTYTCNVDHKPSNTKVDKRVESKYGPPCPPCPAPEFLGGPSVFLFPPKPKDTLMISRT
                            # PEVTCVVVDVSQEDPEVQFNWYVDGVEVHNAKTKPREEQFNSTYRVVSVLTVLHQDWLNGKEYKCKVSNKGLPSSIEKTISKAKGQPREP
                            # QVYTLPPSQEEMTKNQVSLTCLVKGFYPSDIAVEWESNGQPENNYKTTPPVLDSDGSFFLYSRLTVDKSRWQEGNVFSCSVMHEALHNHY
                            # TQKSLSLSLGK' , 'QVQLVESGGGVVQPGRSLRLSCAASGFTFSSYDMHWVRQAPGKGLEWVAVIWYDGSNKYYADSVKGRFTISRDN
                            # SKNTLYLQMNSLRAEDTAVYYCARGSGNWGFFDYWGQGTLVTVSSASTKGPSVFPLAPSSKSTSGGTAALGCLVKDYFPEPVTVSWNSGA
                            # LTSGVHTFPAVLQSSGLYSLSSVVTVPSSSLGTQTYICNVNHKPSNTKVDKKVEPKSCDKTHTCPPCPAPELLGGPSVFLFPPKPKDTLM
                            # ISRTPEVTCVVVDVSHEDPEVKFNWYVDGVEVHNAKTKPREEQYNSTYRVVSVLTVLHQDWLNGKEYKCKVSNKALPAPIEKTISKAKGQ
                            # PREPQVYTLPPSRDELTKNQVSLTCLVKGFYPSDIAVEWESNGQPENNYKTTPPVLDSDGSFFLYSKLTVDKSRWQQGNVFSCSVMHEAL
                            # HNHYTQKSLSLSPGKGSS' , 'QVQLQQPGAELVKPGASVKMSCKASGYTFTSYNMHWVKQTPGRGLEWIGAIYPGNGDTSYNQKFKGK
                            # ATLTADKSSSTAYMQLSSLTSEDSAVYYCARSTYYGGDWYFNVWGAGTTVTVSAASTKGPSVFPLAPSSKSTSGGTAALGCLVKDYFPEP
                            # VTVSWNSGALTSGVHTFPAVLQSSGLYSLSSVVTVPSSSLGTQTYICNVNHKPSNTKVDKKVEPKSCDKTHTCPPCPAPELLGGPSVFLF
                            # PPKPKDTLMISRTPEVTCVVVDVSHEDPEVKFNWYVDGVEVHNAKTKPREEQYNSTYRVVSVLTVLHQDWLNGKEYKCKVSNKALPAPIE
                            # KTISKAKGQPREPQVYTLPPSRDELTKNQVSLTCLVKGFYPSDIAVEWESNGQPENNYKTTPPVLDSDGSFFLYSKLTVDKSRWQQGNVF
                            # SCSVMHEALHNHYTQKSLSLSPGK' , 'MKWVTFISLLFLFSSAYSRGVFRRDAHKSEVAHRFKDLGEENFKALVLIAFAQYLQQCPFE
                            # DHVKLVNEVTEFAKTCVADESAENCDKSLHTLFGDKLCTVATLRETYGEMADCCAKQEPERNECFLQHKDDNPNLPRLVRPEVDVMCTAF
                            # HDNEETFLKKYLYEIARRHPYFYAPELLFFAKRYKAAFTECCQAADKAACLLPKLDELRDEGKASSAKQRLKCASLQKFGERAFKAWAVA
                            # RLSQRFPKAEFAEVSKLVTDLTKVHTECCHGDLLECADDRADLAKYICENQDSISSKLKECCEKPLLEKSHCIAEVENDEMPADLPSLAA
                            # DFVESKDVCKNYAEAKDVFLGMFLYEYARRHPDYSVVLLLRLAKTYETTLEKCCAAADPHECYAKVFDEFKPLVEEPQNLIKQNCELFEQ
                            # LGEYKFQNALLVRYTKKVPQVSTPTLVEVSRNLGKVGSKCCKHPEAKRMPCAEDYLSVVLNQLCVLHEKTPVSDRVTKCCTESLVNRRPC
                            # FSALEVDETYVPKEFNAETFTFHADICTLSEKERQIKKQTALVELVKHKPKATKEQLKAVMDDFAAFVEKCCKADDKETCFAEEGKKLVA
                            # ASQAALGL' , 'QVQLQESGPGLVRPSQTLSLTCTVSGFTFTDFYMNWVRQPPGRGLEWIGFIRDKAKGYTTEYNPSVKGRVTMLVDTS
                            # KNQFSLRLSSVTAADTAVYYCAREGHTAAPFDYWGQGSLVTVSSASTKGPSVFPLAPSSKSTSGGTAALGCLVKDYFPEPVTVSWNSGAL
                            # TSGVHTFPAVLQSSGLYSLSSVVTVPSSSLGTQTYICNVNHKPSNTKVDKKVEPKSCDKTHTCPPCPAPELLGGPSVFLFPPKPKDTLMI
                            # SRTPEVTCVVVDVSHEDPEVKFNWYVDGVEVHNAKTKPREEQYNSTYRVVSVLTVLHQDWLNGKEYKCKVSNKALPAPIEKTISKAKGQP
                            # REPQVYTLPPSRDELTKNQVSLTCLVKGFYPSDIAVEWESNGQPENNYKTTPPVLDSDGSFFLYSKLTVDKSRWQQGNVFSCSVMHEALH
                            # NHYTQKSLSLSPGK' , 'MPRSCCSRSGALLLALLLQASMEVRGWCLESSQCQDLTTESNLLECIRACKPDLSAETPMFPGNGDEQPLT
                            # ENPRKYVMGHFRWDRFGRRNSSSSGSSGAGQKREDVSAGEDCGPLPEGGPEPRSDGAKPGPREGKRSYSMEHFRWGKPVGKKRRPVKVYP
                            # NGAEDESAEAFPLEFKRELTGQRLREGDGPDGPADDGAGAQADLEHSLLVAAEKKDEGPYRMEHFRWGSPPKDKRYGGFMTSEKSQTPLV
                            # TLFKNAIIKNAYKKGE' , 'MALWMRLLPLLALLALWGPDPAAAFVNQHLCGSHLVEALYLVCGERGFFYTPKTRREAEDLQVGQVELG
                            # GGPGAGSLQPLALEGSLQKRGIVEQCCTSICSLYQLENYCN'
                            'tax_id': 'NUMERIC',
                            # EXAMPLES:
                            # '9606' , '9606' , '9606' , '9606' , '9606' , '9606' , '9606' , '9606' , '9913' , '9606'
                        }
                    },
                    'description': 'TEXT',
                    # EXAMPLES:
                    # 'Brentuximab Vedotin (chimeric mab)' , 'Gantenerumab (human mab)' , 'BREMELANOTIDE' , 'Lenercept (
                    # immunoadhesin)' , 'Rovelizumab (humanized mab)' , 'Telimomab aritox (mouse Fab)' , 'SEMPARATIDE' ,
                    #  'CP-870893 (mab)' , 'AHN-12 (mab)' , 'ImmuRAIT-LL2 (mouse mab)'
                    'helm_notation': 'TEXT',
                    # EXAMPLES:
                    # 'PEPTIDE1{[Cbz_L].[dL].[L_Me]}$$$$' , 'PEPTIDE1{[X894].L.P}$$$$' , 'PEPTIDE1{[X856].L.G}$$$$' , 'P
                    # EPTIDE1{Y.I.I.K.G.V.F.W.D.P.A.[X1619]}$$$$' , 'PEPTIDE1{[ac].P.V.L.D.E.F.R.E.K.L.N.E.E.L.E.A.[X222
                    # ].K.Q.K.L.K.[am]}$$$$' , 'PEPTIDE1{[ac].P.V.L.D.E.F.R.E.K.L.N.E.[X857].L.E.A.L.K.Q.K.L.K.[am]}$$$$
                    # ' , 'PEPTIDE1{[X320].D.K.G.S.Y.L.P.R.P.T.P.P.R.P.I.Y.N.[meR].N}|PEPTIDE2{[X320].D.K.G.S.Y.L.P.R.P.
                    # T.P.P.R.P.I.Y.N.[meR].N.[Dab].[am]}$PEPTIDE2,PEPTIDE1,21:R3-20:R2$$$' , 'PEPTIDE1{V.[Orn].A.[dF].P
                    # .[dY].V.[Orn].A.[dF].P.[dY]}$PEPTIDE1,PEPTIDE1,12:R2-1:R1$$$' , 'PEPTIDE1{[ac].P.[X222].L.D.E.[X22
                    # 2].R.E.K.L.N.E.[X222].L.E.A.L.K.Q.K.L.K.[am]}$$$$' , 'PEPTIDE1{A.G.[dA].G.A.G.C.Y.I.Q.N.[dC].P.L.G
                    # }$PEPTIDE1,PEPTIDE1,12:R3-7:R3|PEPTIDE1,PEPTIDE1,15:R2-1:R1$$$'
                    'molecule_chembl_id': 'TEXT',
                    # EXAMPLES:
                    # 'CHEMBL1536007' , 'CHEMBL1611100' , 'CHEMBL1651876' , 'CHEMBL1652309' , 'CHEMBL1630184' , 'CHEMBL1
                    # 630191' , 'CHEMBL1630214' , 'CHEMBL1643494' , 'CHEMBL1630526' , 'CHEMBL1630533'
                }
            },
            'black_box_warning': 'NUMERIC',
            # EXAMPLES:
            # '0' , '0' , '0' , '0' , '0' , '0' , '0' , '0' , '0' , '0'
            'chebi_par_id': 'NUMERIC',
            # EXAMPLES:
            # '3245' , '83851' , '48567' , '78901' , '28498' , '29115' , '81838' , '81935' , '16076' , '6407'
            'chirality': 'NUMERIC',
            # EXAMPLES:
            # '-1' , '-1' , '-1' , '-1' , '-1' , '-1' , '-1' , '-1' , '-1' , '-1'
            'cross_references': 
            {
                'properties': 
                {
                    'xref_id': 'NUMERIC',
                    # EXAMPLES:
                    # '22414485' , '4258421' , '24394952' , '57266327' , '4249259' , '4237541' , '24394771' , '7974009' 
                    # , '24784738' , '24791638'
                    'xref_name': 'TEXT',
                    # EXAMPLES:
                    # 'SID: 22414485' , 'SID: 4258421' , 'SID: 24394952' , 'SID: 57266327' , 'SID: 4249259' , 'SID: 4237
                    # 541' , 'SID: 24394771' , 'SID: 7974009' , 'SID: 24784738' , 'SID: 24791638'
                    'xref_src': 'TEXT',
                    # EXAMPLES:
                    # 'PubChem' , 'PubChem' , 'PubChem' , 'PubChem' , 'PubChem' , 'PubChem' , 'PubChem' , 'PubChem' , 'P
                    # ubChem' , 'PubChem'
                }
            },
            'dosed_ingredient': 'BOOLEAN',
            # EXAMPLES:
            # 'False' , 'False' , 'False' , 'False' , 'False' , 'False' , 'False' , 'False' , 'False' , 'False'
            'drug_warnings': 
            {
                'properties': 
                {
                    'warning_class': 'TEXT',
                    # EXAMPLES:
                    # 'Infections' , 'Hepatotoxicity' , 'Hepatotoxicity' , 'Immune system toxicity' , 'Cardiotoxicity' ,
                    #  'Nephrotoxicity' , 'Cardiotoxicity' , 'Respiratory toxicity' , 'Neurotoxicity' , 'Carcinogenicity
                    # '
                    'warning_country': 'TEXT',
                    # EXAMPLES:
                    # 'United Kingdom; United States' , 'Australia' , 'United Kingdom; Germany; Italy; Ireland; Netherla
                    # nds; European Union' , 'United States' , 'United Kingdom' , 'France; United States' , 'European Un
                    # ion; Canada; Ireland; Portugal; Australia' , 'Spain; Germany; France' , 'United States' , 'France;
                    #  Norway'
                    'warning_description': 'TEXT',
                    # EXAMPLES:
                    # 'Jaundice; Elevated Hepatic Enzymes' , 'Hepatotoxicity' , 'Arrhythmias and Sudden Cardiac Death (A
                    # rrhythmias and Sudden)' , 'Cutaneous Reactions; Animal Carcinogenicity' , 'Neuropsychiatric Reacti
                    # on' , 'Hepatotoxicity' , 'Gastrointestinal Toxicity; Hepatotoxicity' , 'Progressive multifocal leu
                    # koencephalopathy' , 'Self-poisoning' , 'Animal carcinogenicity (rodents)'
                    'warning_id': 'NUMERIC',
                    # EXAMPLES:
                    # '2354' , '2235' , '2279' , '712' , '1226' , '380' , '1598' , '2148' , '1404' , '668'
                    'warning_refs': 
                    {
                        'properties': 
                        {
                            'ref_id': 'TEXT',
                            # EXAMPLES:
                            # '3904f8dd-1aef-3490-e48f-bd55f32ed67f' , '10.1177/009286150103500134' , '10.1177/009286150
                            # 103500134' , 'e082a024-7850-400b-a5c2-2a140612562a' , '6d00e5cc-72b4-41af-8833-bf787310f90
                            # a' , 'a32820f7-9ff6-4c13-a96a-4483a943fe82' , '0b296555-c32f-42db-b5f3-ea981a3dd2f8' , '10
                            # .1177/009286150103500134' , 'b0a5ded2-8ee2-49ca-a86c-2b28ae40f60c' , '87bb0e2f-9fa6-438b-9
                            # d5f-d0a90af770ed'
                            'ref_type': 'TEXT',
                            # EXAMPLES:
                            # 'FDA' , 'DOI' , 'DOI' , 'FDA' , 'FDA' , 'FDA' , 'FDA' , 'DOI' , 'FDA' , 'FDA'
                            'ref_url': 'TEXT',
                            # EXAMPLES:
                            # 'https://api.fda.gov/drug/label.json?search=set_id:3904f8dd-1aef-3490-e48f-bd55f32ed67f' ,
                            #  'https://doi.org/10.1177/009286150103500134' , 'https://doi.org/10.1177/00928615010350013
                            # 4' , 'https://api.fda.gov/drug/label.json?search=set_id:e082a024-7850-400b-a5c2-2a14061256
                            # 2a' , 'https://api.fda.gov/drug/label.json?search=set_id:6d00e5cc-72b4-41af-8833-bf787310f
                            # 90a' , 'https://api.fda.gov/drug/label.json?search=set_id:a32820f7-9ff6-4c13-a96a-4483a943
                            # fe82' , 'https://api.fda.gov/drug/label.json?search=set_id:0b296555-c32f-42db-b5f3-ea981a3
                            # dd2f8' , 'https://doi.org/10.1177/009286150103500134' , 'https://api.fda.gov/drug/label.js
                            # on?search=set_id:b0a5ded2-8ee2-49ca-a86c-2b28ae40f60c' , 'https://api.fda.gov/drug/label.j
                            # son?search=set_id:87bb0e2f-9fa6-438b-9d5f-d0a90af770ed'
                        }
                    },
                    'warning_type': 'TEXT',
                    # EXAMPLES:
                    # 'Black Box Warning' , 'Withdrawn' , 'Withdrawn' , 'Black Box Warning' , 'Black Box Warning' , 'Bla
                    # ck Box Warning' , 'Black Box Warning' , 'Withdrawn' , 'Black Box Warning' , 'Black Box Warning'
                    'warning_year': 'NUMERIC',
                    # EXAMPLES:
                    # '1970' , '1971' , '1998' , '1984' , '1972' , '1998' , '1990' , '2009' , '1980' , '1979'
                }
            },
            'first_approval': 'NUMERIC',
            # EXAMPLES:
            # '2003' , '1982' , '2011' , '2009' , '2010' , '2019' , '1978' , '2001' , '1982' , '1993'
            'first_in_class': 'NUMERIC',
            # EXAMPLES:
            # '-1' , '-1' , '-1' , '-1' , '-1' , '-1' , '-1' , '-1' , '-1' , '-1'
            'helm_notation': 'TEXT',
            # EXAMPLES:
            # 'PEPTIDE1{[Cbz_L].[dL].[L_Me]}$$$$' , 'PEPTIDE1{[X894].L.P}$$$$' , 'PEPTIDE1{[X856].L.G}$$$$' , 'PEPTIDE1{
            # Y.I.I.K.G.V.F.W.D.P.A.[X1619]}$$$$' , 'PEPTIDE1{[ac].P.V.L.D.E.F.R.E.K.L.N.E.E.L.E.A.[X222].K.Q.K.L.K.[am]
            # }$$$$' , 'PEPTIDE1{[ac].P.V.L.D.E.F.R.E.K.L.N.E.[X857].L.E.A.L.K.Q.K.L.K.[am]}$$$$' , 'PEPTIDE1{[X320].D.K
            # .G.S.Y.L.P.R.P.T.P.P.R.P.I.Y.N.[meR].N}|PEPTIDE2{[X320].D.K.G.S.Y.L.P.R.P.T.P.P.R.P.I.Y.N.[meR].N.[Dab].[a
            # m]}$PEPTIDE2,PEPTIDE1,21:R3-20:R2$$$' , 'PEPTIDE1{V.[Orn].A.[dF].P.[dY].V.[Orn].A.[dF].P.[dY]}$PEPTIDE1,PE
            # PTIDE1,12:R2-1:R1$$$' , 'PEPTIDE1{[ac].P.[X222].L.D.E.[X222].R.E.K.L.N.E.[X222].L.E.A.L.K.Q.K.L.K.[am]}$$$
            # $' , 'PEPTIDE1{A.G.[dA].G.A.G.C.Y.I.Q.N.[dC].P.L.G}$PEPTIDE1,PEPTIDE1,12:R3-7:R3|PEPTIDE1,PEPTIDE1,15:R2-1
            # :R1$$$'
            'indication_class': 'TEXT',
            # EXAMPLES:
            # 'Pharmaceutic Aid (emulsifying agent)' , 'Platelet Aggregation Inhibitor' , 'Antihistaminic' , 'Pharmaceut
            # ic Aid (alkalizing agent)' , 'Antibacterial' , 'Pharmaceutic Aid (gelling agent)' , 'Antihistaminic' , 'An
            # tibacterial (veterinary)' , 'Vasoconstrictor' , 'Vasodilator (peripheral)'
            'inorganic_flag': 'NUMERIC',
            # EXAMPLES:
            # '-1' , '-1' , '-1' , '-1' , '-1' , '-1' , '-1' , '-1' , '-1' , '-1'
            'max_phase': 'NUMERIC',
            # EXAMPLES:
            # '0' , '0' , '0' , '0' , '0' , '0' , '0' , '0' , '0' , '0'
            'molecule_chembl_id': 'TEXT',
            # EXAMPLES:
            # 'CHEMBL1529844' , 'CHEMBL1517685' , 'CHEMBL1512973' , 'CHEMBL1551086' , 'CHEMBL1529845' , 'CHEMBL1556045' 
            # , 'CHEMBL1551087' , 'CHEMBL1540138' , 'CHEMBL1520375' , 'CHEMBL1540139'
            'molecule_hierarchy': 
            {
                'properties': 
                {
                    'molecule_chembl_id': 'TEXT',
                    # EXAMPLES:
                    # 'CHEMBL1529844' , 'CHEMBL1517685' , 'CHEMBL1512973' , 'CHEMBL1551086' , 'CHEMBL1529845' , 'CHEMBL1
                    # 556045' , 'CHEMBL1551087' , 'CHEMBL1540138' , 'CHEMBL1520375' , 'CHEMBL1540139'
                    'parent_chembl_id': 'TEXT',
                    # EXAMPLES:
                    # 'CHEMBL1529844' , 'CHEMBL1517685' , 'CHEMBL1512973' , 'CHEMBL1551086' , 'CHEMBL1529845' , 'CHEMBL1
                    # 556045' , 'CHEMBL1551087' , 'CHEMBL1540138' , 'CHEMBL1520375' , 'CHEMBL1540139'
                }
            },
            'molecule_properties': 
            {
                'properties': 
                {
                    'alogp': 'NUMERIC',
                    # EXAMPLES:
                    # '1.52' , '4.16' , '2.35' , '3.14' , '3.64' , '3.02' , '5.61' , '2.06' , '3.15' , '2.36'
                    'aromatic_rings': 'NUMERIC',
                    # EXAMPLES:
                    # '2' , '3' , '2' , '2' , '3' , '3' , '3' , '4' , '1' , '2'
                    'cx_logd': 'NUMERIC',
                    # EXAMPLES:
                    # '0.55' , '1.96' , '1.59' , '2.56' , '2.04' , '2.12' , '4.78' , '1.49' , '2.34' , '1.34'
                    'cx_logp': 'NUMERIC',
                    # EXAMPLES:
                    # '0.55' , '2.32' , '1.59' , '2.56' , '2.47' , '2.13' , '4.78' , '1.50' , '2.37' , '1.48'
                    'cx_most_apka': 'NUMERIC',
                    # EXAMPLES:
                    # '10.21' , '9.46' , '12.97' , '12.43' , '6.99' , '13.35' , '8.60' , '7.73' , '7.19' , '12.43'
                    'cx_most_bpka': 'NUMERIC',
                    # EXAMPLES:
                    # '4.81' , '7.75' , '0.97' , '5.60' , '5.92' , '8.32' , '6.44' , '3.54' , '1.02' , '7.46'
                    'full_molformula': 'TEXT',
                    # EXAMPLES:
                    # 'C14H15N3O3S' , 'C24H25N3O4S' , 'C20H20FN3O6S' , 'C21H26N4O6S' , 'C21H20N2O5S' , 'C17H13N5' , 'C21
                    # H21ClN2O2S' , 'C21H19N5O3' , 'C24H37N3O4S' , 'C15H15N3O6S'
                    'full_mwt': 'NUMERIC',
                    # EXAMPLES:
                    # '305.36' , '451.55' , '449.46' , '462.53' , '412.47' , '287.33' , '400.93' , '389.42' , '463.64' ,
                    #  '365.37'
                    'hba': 'NUMERIC',
                    # EXAMPLES:
                    # '4' , '7' , '6' , '7' , '5' , '5' , '3' , '8' , '4' , '6'
                    'hba_lipinski': 'NUMERIC',
                    # EXAMPLES:
                    # '6' , '7' , '9' , '10' , '7' , '5' , '4' , '8' , '7' , '9'
                    'hbd': 'NUMERIC',
                    # EXAMPLES:
                    # '2' , '1' , '1' , '2' , '1' , '1' , '1' , '1' , '2' , '2'
                    'hbd_lipinski': 'NUMERIC',
                    # EXAMPLES:
                    # '2' , '1' , '1' , '2' , '1' , '1' , '1' , '1' , '2' , '2'
                    'heavy_atoms': 'NUMERIC',
                    # EXAMPLES:
                    # '21' , '32' , '31' , '32' , '29' , '22' , '27' , '29' , '32' , '25'
                    'molecular_species': 'TEXT',
                    # EXAMPLES:
                    # 'NEUTRAL' , 'NEUTRAL' , 'NEUTRAL' , 'NEUTRAL' , 'NEUTRAL' , 'NEUTRAL' , 'NEUTRAL' , 'NEUTRAL' , 'N
                    # EUTRAL' , 'NEUTRAL'
                    'mw_freebase': 'NUMERIC',
                    # EXAMPLES:
                    # '305.36' , '451.55' , '449.46' , '462.53' , '412.47' , '287.33' , '400.93' , '389.42' , '463.64' ,
                    #  '365.37'
                    'mw_monoisotopic': 'NUMERIC',
                    # EXAMPLES:
                    # '305.0834' , '451.1566' , '449.1057' , '462.1573' , '412.1093' , '287.1171' , '400.1012' , '389.14
                    # 88' , '463.2505' , '365.0682'
                    'num_lipinski_ro5_violations': 'NUMERIC',
                    # EXAMPLES:
                    # '0' , '0' , '0' , '0' , '0' , '0' , '1' , '0' , '0' , '0'
                    'num_ro5_violations': 'NUMERIC',
                    # EXAMPLES:
                    # '0' , '0' , '0' , '0' , '0' , '0' , '1' , '0' , '0' , '0'
                    'psa': 'NUMERIC',
                    # EXAMPLES:
                    # '88.16' , '86.88' , '106.53' , '130.88' , '84.94' , '74.49' , '45.33' , '102.34' , '95.58' , '127.
                    # 64'
                    'qed_weighted': 'NUMERIC',
                    # EXAMPLES:
                    # '0.88' , '0.54' , '0.73' , '0.46' , '0.67' , '0.80' , '0.62' , '0.43' , '0.62' , '0.60'
                    'ro3_pass': 'TEXT',
                    # EXAMPLES:
                    # 'N' , 'N' , 'N' , 'N' , 'N' , 'N' , 'N' , 'N' , 'N' , 'N'
                    'rtb': 'NUMERIC',
                    # EXAMPLES:
                    # '5' , '7' , '6' , '8' , '6' , '4' , '4' , '4' , '8' , '6'
                }
            },
            'molecule_structures': 
            {
                'properties': 
                {
                    'canonical_smiles': 'TEXT',
                    # EXAMPLES:
                    # 'CC(=O)Nc1ccc(S(=O)(=O)NCc2cccnc2)cc1' , 'Cc1ccc(C2C(C(=O)c3sc(-c4ccccc4)nc3C)=C(O)C(=O)N2CCN(C)C)
                    # o1' , 'COc1cc(NC(=O)C2=CC(c3ccc(F)cc3)=NS(=O)(=O)N2C)cc(OC)c1OC' , 'COc1ccc([N+](=O)[O-])cc1NCC(=O
                    # )Nc1cc(S(=O)(=O)N2CCCCC2)ccc1C' , 'CCN1C(=O)c2cccc3c(S(=O)(=O)Nc4ccc(OC)cc4OC)ccc1c23' , 'N#Cc1ccc
                    # cc1-c1cncnc1NCc1cccnc1' , 'COc1ccc2c(Sc3ccc(Cl)cc3)c(C(=O)N3CCCCC3)[nH]c2c1' , 'CCOC(=O)c1cc2c(=O)
                    # n3cc(C)ccc3nc2n(Cc2cccnc2)c1=N' , 'Cc1ccc(NC(=O)C[S+]([O-])CC(=O)N(C(C)C(=O)NC2CCCCC2)C(C)(C)C)cc1
                    # ' , 'COc1ccc(S(=O)(=O)Nc2ccc(NC(C)=O)cc2)cc1[N+](=O)[O-]'
                    'standard_inchi': 'TEXT',
                    # EXAMPLES:
                    # 'InChI=1S/C14H15N3O3S/c1-11(18)17-13-4-6-14(7-5-13)21(19,20)16-10-12-3-2-8-15-9-12/h2-9,16H,10H2,1
                    # H3,(H,17,18)' , 'InChI=1S/C24H25N3O4S/c1-14-10-11-17(31-14)19-18(21(29)24(30)27(19)13-12-26(3)4)20
                    # (28)22-15(2)25-23(32-22)16-8-6-5-7-9-16/h5-11,19,29H,12-13H2,1-4H3' , 'InChI=1S/C20H20FN3O6S/c1-24
                    # -16(11-15(23-31(24,26)27)12-5-7-13(21)8-6-12)20(25)22-14-9-17(28-2)19(30-4)18(10-14)29-3/h5-11H,1-
                    # 4H3,(H,22,25)' , 'InChI=1S/C21H26N4O6S/c1-15-6-8-17(32(29,30)24-10-4-3-5-11-24)13-18(15)23-21(26)1
                    # 4-22-19-12-16(25(27)28)7-9-20(19)31-2/h6-9,12-13,22H,3-5,10-11,14H2,1-2H3,(H,23,26)' , 'InChI=1S/C
                    # 21H20N2O5S/c1-4-23-17-10-11-19(14-6-5-7-15(20(14)17)21(23)24)29(25,26)22-16-9-8-13(27-2)12-18(16)2
                    # 8-3/h5-12,22H,4H2,1-3H3' , 'InChI=1S/C17H13N5/c18-8-14-5-1-2-6-15(14)16-11-20-12-22-17(16)21-10-13
                    # -4-3-7-19-9-13/h1-7,9,11-12H,10H2,(H,20,21,22)' , 'InChI=1S/C21H21ClN2O2S/c1-26-15-7-10-17-18(13-1
                    # 5)23-19(21(25)24-11-3-2-4-12-24)20(17)27-16-8-5-14(22)6-9-16/h5-10,13,23H,2-4,11-12H2,1H3' , 'InCh
                    # I=1S/C21H19N5O3/c1-3-29-21(28)15-9-16-19(24-17-7-6-13(2)11-25(17)20(16)27)26(18(15)22)12-14-5-4-8-
                    # 23-10-14/h4-11,22H,3,12H2,1-2H3' , 'InChI=1S/C24H37N3O4S/c1-17-11-13-20(14-12-17)25-21(28)15-32(31
                    # )16-22(29)27(24(3,4)5)18(2)23(30)26-19-9-7-6-8-10-19/h11-14,18-19H,6-10,15-16H2,1-5H3,(H,25,28)(H,
                    # 26,30)' , 'InChI=1S/C15H15N3O6S/c1-10(19)16-11-3-5-12(6-4-11)17-25(22,23)13-7-8-15(24-2)14(9-13)18
                    # (20)21/h3-9,17H,1-2H3,(H,16,19)'
                    'standard_inchi_key': 'TEXT',
                    # EXAMPLES:
                    # 'HDTTZGYLHRXEKT-UHFFFAOYSA-N' , 'GBYRSEMZAJOZQB-UHFFFAOYSA-N' , 'VGIZYGQUZZAUFF-UHFFFAOYSA-N' , 'H
                    # DRZXKBDOCTHLP-UHFFFAOYSA-N' , 'AVOMNAQODOXAKO-UHFFFAOYSA-N' , 'SJVWVKDOEBSGKD-UHFFFAOYSA-N' , 'OAT
                    # KBIYJFOCWED-UHFFFAOYSA-N' , 'VQGDCICFXJACPE-UHFFFAOYSA-N' , 'JBDCQOUPPHYZOE-UHFFFAOYSA-N' , 'IHFNB
                    # YIEAVFRKS-UHFFFAOYSA-N'
                }
            },
            'molecule_synonyms': 
            {
                'properties': 
                {
                    'molecule_synonym': 'TEXT',
                    # EXAMPLES:
                    # 'Propylene glycol monostearate' , 'Acadesine' , 'Indocate' , 'GNF-Pf-1859' , 'H 168/68 MAGNESIUM' 
                    # , 'RP-49356' , '2-Cinnamamidobenzamide' , 'Chartreusin' , '(-)-Asarinin' , 'NSC-60340'
                    'syn_type': 'TEXT',
                    # EXAMPLES:
                    # 'NATIONAL_FORMULARY' , 'ATC' , 'INN' , 'RESEARCH_CODE' , 'RESEARCH_CODE' , 'RESEARCH_CODE' , 'OTHE
                    # R' , 'OTHER' , 'OTHER' , 'RESEARCH_CODE'
                    'synonyms': 'TEXT',
                    # EXAMPLES:
                    # 'PROPYLENE GLYCOL MONOSTEARATE' , 'ACADESINE' , 'INDOCATE' , 'GNF-Pf-1859' , 'H 168/68 MAGNESIUM' 
                    # , 'RP-49356' , '2-Cinnamamidobenzamide' , 'Chartreusin' , '(-)-Asarinin' , 'NSC-60340'
                }
            },
            'molecule_type': 'TEXT',
            # EXAMPLES:
            # 'Small molecule' , 'Small molecule' , 'Small molecule' , 'Small molecule' , 'Small molecule' , 'Small mole
            # cule' , 'Small molecule' , 'Small molecule' , 'Small molecule' , 'Small molecule'
            'natural_product': 'NUMERIC',
            # EXAMPLES:
            # '-1' , '-1' , '-1' , '-1' , '-1' , '-1' , '-1' , '-1' , '-1' , '-1'
            'oral': 'BOOLEAN',
            # EXAMPLES:
            # 'False' , 'False' , 'False' , 'False' , 'False' , 'False' , 'False' , 'False' , 'False' , 'False'
            'parenteral': 'BOOLEAN',
            # EXAMPLES:
            # 'False' , 'False' , 'False' , 'False' , 'False' , 'False' , 'False' , 'False' , 'False' , 'False'
            'polymer_flag': 'BOOLEAN',
            # EXAMPLES:
            # 'False' , 'False' , 'False' , 'False' , 'False' , 'False' , 'False' , 'False' , 'False' , 'False'
            'pref_name': 'TEXT',
            # EXAMPLES:
            # 'BISABOLOL' , 'PROPYLENE GLYCOL MONOSTEARATE' , 'BITERTANOL' , 'ACADESINE' , 'INDOCATE' , 'PYRAZON' , 'NIT
            # RAPYRIN' , 'OMEPRAZOLE MAGNESIUM' , 'LENACIL' , 'ROTOXAMINE'
            'prodrug': 'NUMERIC',
            # EXAMPLES:
            # '-1' , '-1' , '-1' , '-1' , '-1' , '-1' , '-1' , '-1' , '-1' , '-1'
            'structure_type': 'TEXT',
            # EXAMPLES:
            # 'MOL' , 'MOL' , 'MOL' , 'MOL' , 'MOL' , 'MOL' , 'MOL' , 'MOL' , 'MOL' , 'MOL'
            'therapeutic_flag': 'BOOLEAN',
            # EXAMPLES:
            # 'False' , 'False' , 'False' , 'False' , 'False' , 'False' , 'False' , 'False' , 'False' , 'False'
            'topical': 'BOOLEAN',
            # EXAMPLES:
            # 'False' , 'False' , 'False' , 'False' , 'False' , 'False' , 'False' , 'False' , 'False' , 'False'
            'usan_stem': 'TEXT',
            # EXAMPLES:
            # '-prazole' , '-caine' , '-monam' , '-ium' , '-ium; io-' , '-dotin; -mab' , '-mab' , '-profen' , '-butazone
            # ' , '-penem'
            'usan_stem_definition': 'TEXT',
            # EXAMPLES:
            # 'antiulcer agents (benzimidazole derivatives)' , 'local anesthetics' , 'monobactam antibiotics' , 'quatern
            # ary ammonium derivatives' , 'quaternary ammonium derivatives; iodine-containing contrast media' , 'synthet
            # ic analogs of the dolastatin series; monoclonal antibodies: chimeric, tumors as target' , 'monoclonal anti
            # bodies: neurologic indications' , 'anti-inflammatory/analgesic agents (ibuprofen type)' , 'anti-inflammato
            # ry analgesics (phenylbutazone type)' , 'antibacterial antibiotics, carbapenem derivatives'
            'usan_substem': 'TEXT',
            # EXAMPLES:
            # '-prazole' , '-caine' , '-monam' , '-ium' , '-ium; io-' , '-dotin; -mab (-tuximab)' , '-mab (-ner-)' , '-p
            # rofen' , '-butazone' , '-penem'
            'usan_year': 'NUMERIC',
            # EXAMPLES:
            # '1992' , '2000' , '1983' , '1985' , '2009' , '2009' , '1963' , '1976' , '1992' , '2003'
            'withdrawn_class': 'TEXT',
            # EXAMPLES:
            # 'Hepatotoxicity' , 'Hepatotoxicity' , 'Hematological toxicity; Hepatotoxicity; Immune system toxicity; Nep
            # hrotoxicity' , 'Cardiotoxicity' , 'Carcinogenicity; Dermatological toxicity' , 'Neurotoxicity; Psychiatric
            #  toxicity' , 'Hepatotoxicity' , 'Gastrotoxicity; Hepatotoxicity' , 'Neurotoxicity; Psychiatric toxicity' ,
            #  'Neurotoxicity'
            'withdrawn_country': 'TEXT',
            # EXAMPLES:
            # 'United Kingdom; United States' , 'Australia' , 'United States; United Kingdom; Germany' , 'United Kingdom
            # ; Germany; Italy; Ireland; Netherlands; European Union' , 'United States' , 'United States' , 'United King
            # dom' , 'France; United States' , 'European Union; Canada; Ireland; Portugal; Australia' , 'Spain; Germany;
            #  France'
            'withdrawn_flag': 'BOOLEAN',
            # EXAMPLES:
            # 'False' , 'False' , 'False' , 'False' , 'False' , 'False' , 'False' , 'False' , 'False' , 'False'
            'withdrawn_reason': 'TEXT',
            # EXAMPLES:
            # 'Jaundice; Elevated Hepatic Enzymes' , 'Hepatotoxicity' , 'Low blood sugar; hemolytic anemia; kidney, live
            # r dysfunction; allergic reactions' , 'Arrhythmias and Sudden Cardiac Death (Arrhythmias and Sudden)' , 'Cu
            # taneous Reactions; Animal Carcinogenicity' , 'Neuropsychiatric Reaction' , 'Hepatotoxicity' , 'Gastrointes
            # tinal Toxicity; Hepatotoxicity' , 'Neuropsychiatric Reaction' , 'Progressive multifocal leukoencephalopath
            # y'
            'withdrawn_year': 'NUMERIC',
            # EXAMPLES:
            # '1970' , '1971' , '1992' , '1998' , '1984' , '1972' , '1998' , '1990' , '1972' , '2009'
        }
    }
