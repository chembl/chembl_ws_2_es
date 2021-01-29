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
                    # '{'input': 'C28H30F2N2O2', 'weight': 90}' , '{'input': 'Nc1c(CC(=O)[O-])cccc1C(=O)c1ccccc1Cl.[Na+]
                    # ', 'weight': 30}' , '{'input': 'InChI=1S/C11H14N4O4/c1-3-4-15-9-8(10(18)13(2)11(15)19)14(6-12-9)5-
                    # 7(16)17/h6H,3-5H2,1-2H3,(H,16,17)', 'weight': 30}' , '{'input': 'InChI=1S/C13H18N4O2/c1-4-6-8-16-9
                    # -14-11-10(16)12(18)15(3)13(19)17(11)7-5-2/h4,9H,1,5-8H2,2-3H3', 'weight': 30}' , '{'input': 'InChI
                    # =1S/C12H16N4O2/c1-4-6-15-8-13-10-9(15)11(17)14(3)12(18)16(10)7-5-2/h4,8H,1,5-7H2,2-3H3', 'weight':
                    #  30}' , '{'input': 'C16H14NNaO3', 'weight': 90}' , '{'input': 'AIRMFERKNRDUKD-WPNIJPGZSA-N', 'weig
                    # ht': 30}' , '{'input': 'C23H23N5O6', 'weight': 90}' , '{'input': 'CHEMBL286267', 'weight': 10}' , 
                    # '{'input': 'CHEMBL29030', 'weight': 10}'
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
            # 'A10BB03' , 'A10BX03' , 'R03DC04' , 'N07BA01' , 'J01MA01' , 'J01CG02' , 'J01MA02' , 'J01MA06' , 'C01DA58' 
            # , 'C07AB02'
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
                            # '6691' , '6713' , '6710' , '6710' , '6385' , '6691' , '6677' , '6710' , '6672' , '6731'
                            'component_type': 'TEXT',
                            # EXAMPLES:
                            # 'PROTEIN' , 'PROTEIN' , 'PROTEIN' , 'PROTEIN' , 'PROTEIN' , 'PROTEIN' , 'PROTEIN' , 'PROTE
                            # IN' , 'PROTEIN' , 'PROTEIN'
                            'description': 'TEXT',
                            # EXAMPLES:
                            # 'Corticotropin-lipotropin precursor' , 'Antithrombin-III precursor' , 'Serum albumin precu
                            # rsor' , 'Serum albumin precursor' , 'Basiliximab heavy chain' , 'Corticotropin-lipotropin 
                            # precursor' , 'Purified semisynthetic human insulin zinc suspension' , 'Serum albumin precu
                            # rsor' , 'Erythropoietin precursor' , 'Urokinase-type plasminogen activator precursor'
                            'organism': 'TEXT',
                            # EXAMPLES:
                            # 'Homo sapiens' , 'Homo sapiens' , 'Homo sapiens' , 'Homo sapiens' , 'Homo sapiens' , 'Homo
                            #  sapiens' , 'Homo sapiens' , 'Homo sapiens' , 'Homo sapiens' , 'Bos taurus'
                            'sequence': 'TEXT',
                            # EXAMPLES:
                            # 'MPRSCCSRSGALLLALLLQASMEVRGWCLESSQCQDLTTESNLLECIRACKPDLSAETPMFPGNGDEQPLTENPRKYVMGHFRWDRFGR
                            # RNSSSSGSSGAGQKREDVSAGEDCGPLPEGGPEPRSDGAKPGPREGKRSYSMEHFRWGKPVGKKRRPVKVYPNGAEDESAEAFPLEFKRE
                            # LTGQRLREGDGPDGPADDGAGAQADLEHSLLVAAEKKDEGPYRMEHFRWGSPPKDKRYGGFMTSEKSQTPLVTLFKNAIIKNAYKKGE' 
                            # , 'MYSNVIGTVTSGKRKVYLLSLLLIGFWDCVTCHGSPVDICTAKPRDIPMNPMCIYRSPEKKATEDEGSEQKIPEATNRRVWELSKAN
                            # SRFATTFYQHLADSKNDNDNIFLSPLSISTAFAMTKLGACNDTLQQLMEVFKFDTISEKTSDQIHFFFAKLNCRLYRKANKSSKLVSANR
                            # LFGDKSLTFNETYQDISELVYGAKLQPLDFKENAEQSRAAINKWVSNKTEGRITDVIPSEAINELTVLVLVNTIYFKGLWKSKFSPENTR
                            # KELFYKADGESCSASMMYQEGKFRYRRVAEGTQVLELPFKGDDITMVLILPKPEKSLAKVEKELTPEVLQEWLDELEEMMLVVHMPRFRI
                            # EDGFSLKEQLQDMGLVDLFSPEKSKLPGIVAEGRDDLYVSDAFHKAFLEVNEEGSEAAASTAVVIAGRSLNPNRVTFKANRPFLVFIREV
                            # PLNTIIFMGRVANPCVK' , 'MKWVTFISLLFLFSSAYSRGVFRRDAHKSEVAHRFKDLGEENFKALVLIAFAQYLQQCPFEDHVKLVN
                            # EVTEFAKTCVADESAENCDKSLHTLFGDKLCTVATLRETYGEMADCCAKQEPERNECFLQHKDDNPNLPRLVRPEVDVMCTAFHDNEETF
                            # LKKYLYEIARRHPYFYAPELLFFAKRYKAAFTECCQAADKAACLLPKLDELRDEGKASSAKQRLKCASLQKFGERAFKAWAVARLSQRFP
                            # KAEFAEVSKLVTDLTKVHTECCHGDLLECADDRADLAKYICENQDSISSKLKECCEKPLLEKSHCIAEVENDEMPADLPSLAADFVESKD
                            # VCKNYAEAKDVFLGMFLYEYARRHPDYSVVLLLRLAKTYETTLEKCCAAADPHECYAKVFDEFKPLVEEPQNLIKQNCELFEQLGEYKFQ
                            # NALLVRYTKKVPQVSTPTLVEVSRNLGKVGSKCCKHPEAKRMPCAEDYLSVVLNQLCVLHEKTPVSDRVTKCCTESLVNRRPCFSALEVD
                            # ETYVPKEFNAETFTFHADICTLSEKERQIKKQTALVELVKHKPKATKEQLKAVMDDFAAFVEKCCKADDKETCFAEEGKKLVAASQAALG
                            # L' , 'MKWVTFISLLFLFSSAYSRGVFRRDAHKSEVAHRFKDLGEENFKALVLIAFAQYLQQCPFEDHVKLVNEVTEFAKTCVADESAE
                            # NCDKSLHTLFGDKLCTVATLRETYGEMADCCAKQEPERNECFLQHKDDNPNLPRLVRPEVDVMCTAFHDNEETFLKKYLYEIARRHPYFY
                            # APELLFFAKRYKAAFTECCQAADKAACLLPKLDELRDEGKASSAKQRLKCASLQKFGERAFKAWAVARLSQRFPKAEFAEVSKLVTDLTK
                            # VHTECCHGDLLECADDRADLAKYICENQDSISSKLKECCEKPLLEKSHCIAEVENDEMPADLPSLAADFVESKDVCKNYAEAKDVFLGMF
                            # LYEYARRHPDYSVVLLLRLAKTYETTLEKCCAAADPHECYAKVFDEFKPLVEEPQNLIKQNCELFEQLGEYKFQNALLVRYTKKVPQVST
                            # PTLVEVSRNLGKVGSKCCKHPEAKRMPCAEDYLSVVLNQLCVLHEKTPVSDRVTKCCTESLVNRRPCFSALEVDETYVPKEFNAETFTFH
                            # ADICTLSEKERQIKKQTALVELVKHKPKATKEQLKAVMDDFAAFVEKCCKADDKETCFAEEGKKLVAASQAALGL' , 'QLQQSGTVLA
                            # RPGASVKMSCKASGYSFTRYWMHWIKQRPGQGLEWIGAIYPGNSDTSYNQKFEGKAKLTAVTSASTAYMELSSLTHEDSAVYYCSRDYGY
                            # YFDFWGQGTTLTVSSASTKGPSVFPLAPSSKSTSGGTAALGCLVKDYFPEPVTVSWNSGALTSGVHTFPAVLQSSGLYSLSSVVTVPSSS
                            # LGTQTYICNVNHKPSNTKVDKRVEPPKSCDKTHTCPPCPAPELLGGPSVFLFPPKPKDTLMISRTPEVTCVVVDVSHEDPEVKFNWYVDG
                            # VEVHNAKTKPREEQYNSTYRVVSVLTVLHQDWLNGKEYKCKVSNKALPAPIEKTISKAKGQPREPQVYTLPPSRDELTKNQVSLTCLVKG
                            # FYPSDIAVEWESNGQPENNYKTTPPVLDSDGSFFLYSKLTVDKSRWQQGNVFSCSVMHEALHNHYTQKSLSLSPGK' , 'MPRSCCSRS
                            # GALLLALLLQASMEVRGWCLESSQCQDLTTESNLLECIRACKPDLSAETPMFPGNGDEQPLTENPRKYVMGHFRWDRFGRRNSSSSGSSG
                            # AGQKREDVSAGEDCGPLPEGGPEPRSDGAKPGPREGKRSYSMEHFRWGKPVGKKRRPVKVYPNGAEDESAEAFPLEFKRELTGQRLREGD
                            # GPDGPADDGAGAQADLEHSLLVAAEKKDEGPYRMEHFRWGSPPKDKRYGGFMTSEKSQTPLVTLFKNAIIKNAYKKGE' , 'MALWMRL
                            # LPLLALLALWGPDPAAAFVNQHLCGSHLVEALYLVCGERGFFYTPKTRREAEDLQVGQVELGGGPGAGSLQPLALEGSLQKRGIVEQCCT
                            # SICSLYQLENYCN' , 'MKWVTFISLLFLFSSAYSRGVFRRDAHKSEVAHRFKDLGEENFKALVLIAFAQYLQQCPFEDHVKLVNEVTE
                            # FAKTCVADESAENCDKSLHTLFGDKLCTVATLRETYGEMADCCAKQEPERNECFLQHKDDNPNLPRLVRPEVDVMCTAFHDNEETFLKKY
                            # LYEIARRHPYFYAPELLFFAKRYKAAFTECCQAADKAACLLPKLDELRDEGKASSAKQRLKCASLQKFGERAFKAWAVARLSQRFPKAEF
                            # AEVSKLVTDLTKVHTECCHGDLLECADDRADLAKYICENQDSISSKLKECCEKPLLEKSHCIAEVENDEMPADLPSLAADFVESKDVCKN
                            # YAEAKDVFLGMFLYEYARRHPDYSVVLLLRLAKTYETTLEKCCAAADPHECYAKVFDEFKPLVEEPQNLIKQNCELFEQLGEYKFQNALL
                            # VRYTKKVPQVSTPTLVEVSRNLGKVGSKCCKHPEAKRMPCAEDYLSVVLNQLCVLHEKTPVSDRVTKCCTESLVNRRPCFSALEVDETYV
                            # PKEFNAETFTFHADICTLSEKERQIKKQTALVELVKHKPKATKEQLKAVMDDFAAFVEKCCKADDKETCFAEEGKKLVAASQAALGL' ,
                            #  'MGVHECPAWLWLLLSLLSLPLGLPVLGAPPRLICDSRVLERYLLEAKEAENITTGCAEHCSLNENITVPDTKVNFYAWKRMEVGQQAV
                            # EVWQGLALLSEAVLRGQALLVNSSQPWEPLQLHVDKAVSGLRSLTTLLRALGAQKEAISPPDAASAAPLRTITADTFRKLFRVYSNFLRG
                            # KLKLYTGEACRTGDR' , 'MRALLARLLLCVLVVSDSKGSNELHQVPSNCDCLNGGTCVSNKYFSNIHWCNCPKKFGGQHCEIDKSKTC
                            # YEGNGHFYRGKASTDTMGRPCLPWNSATVLQQTYHAHRSDALQLGLGKHNYCRNPDNRRRPWCYVQVGLKPLVQECMVHDCADGKKPSSP
                            # PEELKFQCGQKTLRPRFKIIGGEFTTIENQPWFAAIYRRHRGGSVTYVCGGSLMSPCWVISATHCFIDYPKKEDYIVYLGRSRLNSNTQG
                            # EMKFEVENLILHKDYSADTLAHHNDIALLKIRSKEGRCAQPSRTIQTICLPSMYNDPQFGTSCEITGFGKENSTDYLYPEQLKMTVVKLI
                            # SHRECQQPHYYGSEVTTKMLCAADPQWKTDSCQGDSGGPLVCSLQGRMTLTGIVSWGRGCALKDKPGVYTRVSHFLPWIRSHTKEENGLA
                            # L'
                            'tax_id': 'NUMERIC',
                            # EXAMPLES:
                            # '9606' , '9606' , '9606' , '9606' , '9606' , '9606' , '9606' , '9606' , '9606' , '9913'
                        }
                    },
                    'description': 'TEXT',
                    # EXAMPLES:
                    # 'ENKEPHALIN' , 'VENORPHIN' , 'TEPROTIDE' , 'DERMORPHIN' , 'SPYSSDTTPA' , 'NPY[TYR32,LEU34]' , 'GOR
                    # ALATIDE' , 'SARALASIN' , 'RIP' , 'PROLYLPROLYLTHREONYLPROLINAMIDE(PPTPNH2)'
                    'helm_notation': 'TEXT',
                    # EXAMPLES:
                    # 'PEPTIDE1{[dP].H.[dP].F.H.F.F.V.Y.[dK]}$$$$' , 'PEPTIDE1{P.[1-Nal].[dW].[X3].[dalloT].F}$PEPTIDE1,
                    # PEPTIDE1,6:R2-1:R1$$$' , 'PEPTIDE1{Y.C.F.[dD].[dC].[dV].G.[am]}$PEPTIDE1,PEPTIDE1,5:R3-2:R3$$$' , 
                    # 'PEPTIDE1{Y.G.G.F.D.R.R.I.R.P.K.L.K}$$$$' , 'PEPTIDE1{[X958].V.N.D.L}$$$$' , 'PEPTIDE1{[dL].[dE].[
                    # dA].[dI].P.M}$$$$' , 'PEPTIDE1{[dM].[dF].[dL].[dE]}$$$$' , 'PEPTIDE1{[X833].[dP].W.[Tle].[X454]}$$
                    # $$' , 'PEPTIDE1{[X12].[dP].Y.[Tle].L}$$$$' , 'PEPTIDE1{Y.A.G}$$$$'
                    'molecule_chembl_id': 'TEXT',
                    # EXAMPLES:
                    # 'CHEMBL438719' , 'CHEMBL281971' , 'CHEMBL289006' , 'CHEMBL406899' , 'CHEMBL276044' , 'CHEMBL21201'
                    #  , 'CHEMBL20698' , 'CHEMBL268600' , 'CHEMBL6508' , 'CHEMBL274367'
                }
            },
            'black_box_warning': 'NUMERIC',
            # EXAMPLES:
            # '0' , '0' , '0' , '0' , '0' , '0' , '0' , '0' , '0' , '0'
            'chebi_par_id': 'NUMERIC',
            # EXAMPLES:
            # '35052' , '75918' , '27999' , '31897' , '141059' , '17598' , '10304' , '2268' , '17509' , '17688'
            'chirality': 'NUMERIC',
            # EXAMPLES:
            # '-1' , '-1' , '-1' , '-1' , '-1' , '-1' , '-1' , '-1' , '-1' , '-1'
            'cross_references': 
            {
                'properties': 
                {
                    'xref_id': 'TEXT',
                    # EXAMPLES:
                    # '496265' , '496566' , '461603' , '144206567' , '11110691' , 'tolbutamide' , 'nateglinide' , '26756
                    # 988' , '530046' , '87335404'
                    'xref_name': 'TEXT',
                    # EXAMPLES:
                    # 'SID: 496265' , 'SID: 496566' , 'SID: 461603' , 'SID: 144206567' , 'SID: 11110691' , 'tolbutamide'
                    #  , 'nateglinide' , 'SID: 26756988' , 'SID: 530046' , 'SID: 87335404'
                    'xref_src': 'TEXT',
                    # EXAMPLES:
                    # 'PubChem' , 'PubChem' , 'PubChem' , 'PubChem' , 'PubChem' , 'DailyMed' , 'DailyMed' , 'PubChem' , 
                    # 'PubChem' , 'PubChem'
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
                    # 'Neurotoxicity' , 'Neurotoxicity' , 'Misuse' , 'Immune system toxicity' , 'Hematological toxicity'
                    #  , 'Hematological toxicity' , 'Neurotoxicity' , 'Cardiotoxicity' , 'Neurotoxicity' , 'Nephrotoxici
                    # ty'
                    'warning_country': 'TEXT',
                    # EXAMPLES:
                    # 'United States' , 'Norway' , 'Germany' , 'France; United States' , 'United States' , 'United State
                    # s' , 'United Kingdom; Germany; Italy; Ireland; Netherlands; European Union' , 'United Kingdom' , '
                    # France' , 'United Kingdom; Spain; Germany'
                    'warning_description': 'TEXT',
                    # EXAMPLES:
                    # 'Self-Poisonings' , 'Off-Label Abuse; Hematologic Toxicity' , 'Risk for birth defects' , 'Arrhythm
                    # ias and Sudden Cardiac Death (Arrhythmias and Sudden)' , 'Cutaneous Reactions; Animal Carcinogenic
                    # ity' , 'Agranulocytosis' , 'Animal Carcinogenicity (rodent); Gastrointestinal Toxicity' , 'Agranul
                    # ocytosis' , 'Animal carcinogenicity (dogs)' , 'Gastrointestinal Toxicity; Hepatotoxicity'
                    'warning_id': 'NUMERIC',
                    # EXAMPLES:
                    # '1364' , '373' , '1350' , '2110' , '2172' , '1416' , '2783' , '2497' , '2222' , '2603'
                    'warning_refs': 
                    {
                        'properties': 
                        {
                            'ref_id': 'TEXT',
                            # EXAMPLES:
                            # 'ee1bf431-97fa-4aba-9cc3-0cfcea779ca2' , '7049f870-6741-4a67-8033-398c36126a06' , 'CFR-201
                            # 9-title21-vol4/pdf/CFR-2019-title21-vol4-sec216-24.pdf' , '10.1177/009286150103500134' , '
                            # a6c24189-293f-42ca-b969-75870bb55af0' , '7636bc1e-77b6-46ad-9df0-c8bb1c5e503f' , '5c50b5a3
                            # -9b39-4cad-8be5-c2a8dd3f7df5' , '10.1177/009286150103500134' , 'ce512844-5220-4661-809f-56
                            # d088699c9c' , 'dff10e66-a577-451d-ba75-1889458ca833'
                            'ref_type': 'TEXT',
                            # EXAMPLES:
                            # 'FDA' , 'FDA' , 'USGPO' , 'DOI' , 'FDA' , 'FDA' , 'FDA' , 'DOI' , 'FDA' , 'FDA'
                            'ref_url': 'TEXT',
                            # EXAMPLES:
                            # 'https://api.fda.gov/drug/label.json?search=set_id:ee1bf431-97fa-4aba-9cc3-0cfcea779ca2' ,
                            #  'https://api.fda.gov/drug/label.json?search=set_id:7049f870-6741-4a67-8033-398c36126a06' 
                            # , 'https://www.govinfo.gov/content/pkg/CFR-2019-title21-vol4/pdf/CFR-2019-title21-vol4-sec
                            # 216-24.pdf' , 'https://doi.org/10.1177/009286150103500134' , 'https://api.fda.gov/drug/lab
                            # el.json?search=set_id:a6c24189-293f-42ca-b969-75870bb55af0' , 'https://api.fda.gov/drug/la
                            # bel.json?search=set_id:7636bc1e-77b6-46ad-9df0-c8bb1c5e503f' , 'https://api.fda.gov/drug/l
                            # abel.json?search=set_id:5c50b5a3-9b39-4cad-8be5-c2a8dd3f7df5' , 'https://doi.org/10.1177/0
                            # 09286150103500134' , 'https://api.fda.gov/drug/label.json?search=set_id:ce512844-5220-4661
                            # -809f-56d088699c9c' , 'https://api.fda.gov/drug/label.json?search=set_id:dff10e66-a577-451
                            # d-ba75-1889458ca833'
                        }
                    },
                    'warning_type': 'TEXT',
                    # EXAMPLES:
                    # 'Black Box Warning' , 'Black Box Warning' , 'Black Box Warning' , 'Withdrawn' , 'Withdrawn' , 'Bla
                    # ck Box Warning' , 'Black Box Warning' , 'Black Box Warning' , 'Withdrawn' , 'Black Box Warning'
                    'warning_year': 'NUMERIC',
                    # EXAMPLES:
                    # '1980' , '1985' , '1989' , '1998' , '1984' , '1985' , '1983' , '1970' , '1970' , '1990'
                }
            },
            'first_approval': 'NUMERIC',
            # EXAMPLES:
            # '1961' , '2000' , '1960' , '1984' , '1990' , '1993' , '1987' , '1986' , '1986' , '1978'
            'first_in_class': 'NUMERIC',
            # EXAMPLES:
            # '-1' , '-1' , '-1' , '-1' , '-1' , '-1' , '-1' , '-1' , '-1' , '-1'
            'helm_notation': 'TEXT',
            # EXAMPLES:
            # 'PEPTIDE1{[dP].H.[dP].F.H.F.F.V.Y.[dK]}$$$$' , 'PEPTIDE1{P.[1-Nal].[dW].[X3].[dalloT].F}$PEPTIDE1,PEPTIDE1
            # ,6:R2-1:R1$$$' , 'PEPTIDE1{Y.C.F.[dD].[dC].[dV].G.[am]}$PEPTIDE1,PEPTIDE1,5:R3-2:R3$$$' , 'PEPTIDE1{Y.G.G.
            # F.D.R.R.I.R.P.K.L.K}$$$$' , 'PEPTIDE1{[X958].V.N.D.L}$$$$' , 'PEPTIDE1{[dL].[dE].[dA].[dI].P.M}$$$$' , 'PE
            # PTIDE1{[dM].[dF].[dL].[dE]}$$$$' , 'PEPTIDE1{[X833].[dP].W.[Tle].[X454]}$$$$' , 'PEPTIDE1{[X12].[dP].Y.[Tl
            # e].L}$$$$' , 'PEPTIDE1{Y.A.G}$$$$'
            'indication_class': 'TEXT',
            # EXAMPLES:
            # 'Anti-Inflammatory' , 'Antidiabetic,Diagnostic Aid (diabetes)' , 'Antihyperlipoproteinemic' , 'Adrenergic 
            # (vasoconstrictor)' , 'Smoking Cessation Adjunct' , 'Antibacterial' , 'Anti-Infective (DNA gyrase inhibitor
            # )' , 'Inhibitor (beta-lactamase)' , 'Antibacterial' , 'Antibacterial'
            'inorganic_flag': 'NUMERIC',
            # EXAMPLES:
            # '-1' , '-1' , '-1' , '-1' , '-1' , '-1' , '-1' , '-1' , '-1' , '-1'
            'max_phase': 'NUMERIC',
            # EXAMPLES:
            # '0' , '0' , '0' , '0' , '0' , '0' , '0' , '0' , '0' , '0'
            'molecule_chembl_id': 'TEXT',
            # EXAMPLES:
            # 'CHEMBL283662' , 'CHEMBL284647' , 'CHEMBL29209' , 'CHEMBL28980' , 'CHEMBL287180' , 'CHEMBL28703' , 'CHEMBL
            # 438719' , 'CHEMBL286266' , 'CHEMBL286267' , 'CHEMBL29030'
            'molecule_hierarchy': 
            {
                'properties': 
                {
                    'molecule_chembl_id': 'TEXT',
                    # EXAMPLES:
                    # 'CHEMBL283662' , 'CHEMBL284647' , 'CHEMBL29209' , 'CHEMBL28980' , 'CHEMBL287180' , 'CHEMBL28703' ,
                    #  'CHEMBL438719' , 'CHEMBL286266' , 'CHEMBL286267' , 'CHEMBL28450'
                    'parent_chembl_id': 'TEXT',
                    # EXAMPLES:
                    # 'CHEMBL283662' , 'CHEMBL1206563' , 'CHEMBL29209' , 'CHEMBL28980' , 'CHEMBL287180' , 'CHEMBL1204828
                    # ' , 'CHEMBL438719' , 'CHEMBL286266' , 'CHEMBL286267' , 'CHEMBL28450'
                }
            },
            'molecule_properties': 
            {
                'properties': 
                {
                    'alogp': 'NUMERIC',
                    # EXAMPLES:
                    # '4.96' , '2.78' , '-0.61' , '0.88' , '0.49' , '2.44' , '2.06' , '4.56' , '2.13' , '-0.36'
                    'aromatic_rings': 'NUMERIC',
                    # EXAMPLES:
                    # '3' , '2' , '2' , '2' , '2' , '2' , '3' , '3' , '1' , '1'
                    'cx_logd': 'NUMERIC',
                    # EXAMPLES:
                    # '5.08' , '0.22' , '-3.57' , '1.35' , '1.06' , '0.22' , '-2.83' , '2.99' , '1.28' , '-0.19'
                    'cx_logp': 'NUMERIC',
                    # EXAMPLES:
                    # '5.25' , '3.50' , '-0.19' , '1.35' , '1.06' , '3.40' , '-0.61' , '4.00' , '1.70' , '-0.10'
                    'cx_most_apka': 'NUMERIC',
                    # EXAMPLES:
                    # '3.77' , '3.47' , '3.98' , '3.97' , '7.98' , '7.42' , '1.17' , '12.31' , '8.71' , '5.72'
                    'cx_most_bpka': 'NUMERIC',
                    # EXAMPLES:
                    # '7.08' , '1.56' , '1.80' , '4.87' , '8.39' , '7.62' , '7.17' , '4.73' , '10.69' , '4.60'
                    'full_molformula': 'TEXT',
                    # EXAMPLES:
                    # 'C28H30F2N2O2' , 'C15H11ClNNaO3' , 'C11H14N4O4' , 'C13H18N4O2' , 'C12H16N4O2' , 'C16H14NNaO3' , 'C
                    # 69H87N15O12' , 'C23H23N5O6' , 'C17H17N3O2S3' , 'C24H31N5O2'
                    'full_mwt': 'NUMERIC',
                    # EXAMPLES:
                    # '464.56' , '311.70' , '266.26' , '262.31' , '248.29' , '291.28' , '1318.55' , '465.47' , '391.54' 
                    # , '421.55'
                    'hba': 'NUMERIC',
                    # EXAMPLES:
                    # '4' , '3' , '7' , '6' , '6' , '3' , '6' , '7' , '6' , '5'
                    'hba_lipinski': 'NUMERIC',
                    # EXAMPLES:
                    # '4' , '4' , '8' , '6' , '6' , '4' , '11' , '5' , '7' , '7'
                    'hbd': 'NUMERIC',
                    # EXAMPLES:
                    # '0' , '2' , '1' , '0' , '0' , '2' , '5' , '2' , '0' , '1'
                    'hbd_lipinski': 'NUMERIC',
                    # EXAMPLES:
                    # '0' , '3' , '1' , '0' , '0' , '3' , '5' , '3' , '0' , '2'
                    'heavy_atoms': 'NUMERIC',
                    # EXAMPLES:
                    # '34' , '20' , '19' , '19' , '18' , '20' , '34' , '25' , '31' , '13'
                    'molecular_species': 'TEXT',
                    # EXAMPLES:
                    # 'NEUTRAL' , 'ACID' , 'ACID' , 'NEUTRAL' , 'NEUTRAL' , 'ACID' , 'ACID' , 'NEUTRAL' , 'NEUTRAL' , 'N
                    # EUTRAL'
                    'mw_freebase': 'NUMERIC',
                    # EXAMPLES:
                    # '464.56' , '289.72' , '266.26' , '262.31' , '248.29' , '269.30' , '1318.55' , '465.47' , '391.54' 
                    # , '421.55'
                    'mw_monoisotopic': 'NUMERIC',
                    # EXAMPLES:
                    # '464.2275' , '289.0506' , '266.1015' , '262.1430' , '248.1273' , '269.1052' , '1317.6659' , '465.1
                    # 648' , '391.0483' , '421.2478'
                    'num_lipinski_ro5_violations': 'NUMERIC',
                    # EXAMPLES:
                    # '0' , '0' , '0' , '0' , '0' , '0' , '1' , '0' , '0' , '0'
                    'num_ro5_violations': 'NUMERIC',
                    # EXAMPLES:
                    # '0' , '0' , '0' , '0' , '0' , '0' , '0' , '0' , '0' , '0'
                    'psa': 'NUMERIC',
                    # EXAMPLES:
                    # '32.78' , '80.39' , '99.12' , '61.82' , '61.82' , '80.39' , '162.66' , '81.22' , '69.64' , '116.19
                    # '
                    'qed_weighted': 'NUMERIC',
                    # EXAMPLES:
                    # '0.40' , '0.67' , '0.80' , '0.75' , '0.74' , '0.66' , '0.31' , '0.37' , '0.40' , '0.52'
                    'ro3_pass': 'TEXT',
                    # EXAMPLES:
                    # 'N' , 'N' , 'N' , 'N' , 'N' , 'N' , 'N' , 'N' , 'N' , 'N'
                    'rtb': 'NUMERIC',
                    # EXAMPLES:
                    # '10' , '4' , '4' , '5' , '4' , '4' , '10' , '6' , '6' , '2'
                }
            },
            'molecule_structures': 
            {
                'properties': 
                {
                    'canonical_smiles': 'TEXT',
                    # EXAMPLES:
                    # 'O=C(CCN1CCN(CCOC(c2ccc(F)cc2)c2ccc(F)cc2)CC1)c1ccccc1' , 'Nc1c(CC(=O)[O-])cccc1C(=O)c1ccccc1Cl.[N
                    # a+]' , 'CCCn1c(=O)n(C)c(=O)c2c1ncn2CC(=O)O' , 'C=CCCn1cnc2c1c(=O)n(C)c(=O)n2CCC' , 'C=CCn1cnc2c1c(
                    # =O)n(C)c(=O)n2CCC' , 'Cc1ccc(C(=O)c2cccc(CC(=O)[O-])c2N)cc1.[Na+]' , 'CC(C)[C@H](NC(=O)[C@H](Cc1cc
                    # ccc1)NC(=O)[C@H](Cc1ccccc1)NC(=O)[C@H](Cc1c[nH]cn1)NC(=O)[C@H](Cc1ccccc1)NC(=O)[C@H]1CCCN1C(=O)[C@
                    # H](Cc1c[nH]cn1)NC(=O)[C@H]1CCCN1)C(=O)N[C@@H](Cc1ccc(O)cc1)C(=O)N[C@H](CCCCN)C(=O)O' , 'O=C(O)CC(N
                    # C(=O)CNC(=O)c1ccc(NC(=O)NCc2ccccc2)o1)c1cccnc1' , 'COc1ccc(-c2csc(-c3cc(C(=N)N)sc3SC)n2)c(OC)c1' ,
                    #  'CC(C)=C1C2C=CC1C1C(=O)N(CCCCN3CCN(c4ncccn4)CC3)C(=O)C21'
                    'standard_inchi': 'TEXT',
                    # EXAMPLES:
                    # 'InChI=1S/C28H30F2N2O2/c29-25-10-6-23(7-11-25)28(24-8-12-26(30)13-9-24)34-21-20-32-18-16-31(17-19-
                    # 32)15-14-27(33)22-4-2-1-3-5-22/h1-13,28H,14-21H2' , 'InChI=1S/C15H12ClNO3.Na/c16-12-7-2-1-5-10(12)
                    # 15(20)11-6-3-4-9(14(11)17)8-13(18)19;/h1-7H,8,17H2,(H,18,19);/q;+1/p-1' , 'InChI=1S/C11H14N4O4/c1-
                    # 3-4-15-9-8(10(18)13(2)11(15)19)14(6-12-9)5-7(16)17/h6H,3-5H2,1-2H3,(H,16,17)' , 'InChI=1S/C13H18N4
                    # O2/c1-4-6-8-16-9-14-11-10(16)12(18)15(3)13(19)17(11)7-5-2/h4,9H,1,5-8H2,2-3H3' , 'InChI=1S/C12H16N
                    # 4O2/c1-4-6-15-8-13-10-9(15)11(17)14(3)12(18)16(10)7-5-2/h4,8H,1,5-7H2,2-3H3' , 'InChI=1S/C16H15NO3
                    # .Na/c1-10-5-7-11(8-6-10)16(20)13-4-2-3-12(15(13)17)9-14(18)19;/h2-8H,9,17H2,1H3,(H,18,19);/q;+1/p-
                    # 1' , 'InChI=1S/C69H87N15O12/c1-42(2)59(67(93)81-54(35-46-25-27-49(85)28-26-46)61(87)76-51(69(95)96
                    # )22-12-13-29-70)83-65(91)55(34-45-20-10-5-11-21-45)78-62(88)52(32-43-16-6-3-7-17-43)77-64(90)56(36
                    # -47-38-71-40-74-47)79-63(89)53(33-44-18-8-4-9-19-44)80-66(92)58-24-15-31-84(58)68(94)57(37-48-39-7
                    # 2-41-75-48)82-60(86)50-23-14-30-73-50/h3-11,16-21,25-28,38-42,50-59,73,85H,12-15,22-24,29-37,70H2,
                    # 1-2H3,(H,71,74)(H,72,75)(H,76,87)(H,77,90)(H,78,88)(H,79,89)(H,80,92)(H,81,93)(H,82,86)(H,83,91)(H
                    # ,95,96)/t50-,51-,52+,53+,54+,55+,56+,57+,58-,59+/m1/s1' , 'InChI=1S/C23H23N5O6/c29-19(27-17(11-21(
                    # 30)31)16-7-4-10-24-13-16)14-25-22(32)18-8-9-20(34-18)28-23(33)26-12-15-5-2-1-3-6-15/h1-10,13,17H,1
                    # 1-12,14H2,(H,25,32)(H,27,29)(H,30,31)(H2,26,28,33)' , 'InChI=1S/C17H17N3O2S3/c1-21-9-4-5-10(13(6-9
                    # )22-2)12-8-24-16(20-12)11-7-14(15(18)19)25-17(11)23-3/h4-8H,1-3H3,(H3,18,19)' , 'InChI=1S/C24H31N5
                    # O2/c1-16(2)19-17-6-7-18(19)21-20(17)22(30)29(23(21)31)11-4-3-10-27-12-14-28(15-13-27)24-25-8-5-9-2
                    # 6-24/h5-9,17-18,20-21H,3-4,10-15H2,1-2H3'
                    'standard_inchi_key': 'TEXT',
                    # EXAMPLES:
                    # 'OSLVNNRVAWCDKE-UHFFFAOYSA-N' , 'SCIHPJKZCBCCBB-UHFFFAOYSA-M' , 'BWFPSXHKZDKRAO-UHFFFAOYSA-N' , 'C
                    # DPLOYJOJXNIRU-UHFFFAOYSA-N' , 'IKFVHDFFKFNFKJ-UHFFFAOYSA-N' , 'BMAGEWWAMCCBDD-UHFFFAOYSA-M' , 'AIR
                    # MFERKNRDUKD-WPNIJPGZSA-N' , 'UFJUFUWNIIBKKK-UHFFFAOYSA-N' , 'OUPJOWDHCXNNFZ-UHFFFAOYSA-N' , 'XNBIJ
                    # YRQZOUYPD-UHFFFAOYSA-N'
                }
            },
            'molecule_synonyms': 
            {
                'properties': 
                {
                    'molecule_synonym': 'TEXT',
                    # EXAMPLES:
                    # 'Hexadecanoic Acid Phenylamide' , 'Zindoxifene' , 'AHR-5850D' , 'Homohypotaurine' , 'Cis-4-Aminocr
                    # otonic Acid' , 'Glyconon' , 'A-4166' , 'CGS-26582' , '[3H]-Phorbol 12,13-Dibutyrate' , 'L-703605'
                    'syn_type': 'TEXT',
                    # EXAMPLES:
                    # 'OTHER' , 'INN' , 'RESEARCH_CODE' , 'OTHER' , 'OTHER' , 'TRADE_NAME' , 'RESEARCH_CODE' , 'RESEARCH
                    # _CODE' , 'OTHER' , 'RESEARCH_CODE'
                    'synonyms': 'TEXT',
                    # EXAMPLES:
                    # 'Hexadecanoic Acid Phenylamide' , 'ZINDOXIFENE' , 'AHR-5850D' , 'Homohypotaurine' , 'Cis-4-Aminocr
                    # otonic Acid' , 'GLYCONON' , 'A-4166' , 'CGS-26582' , '[3H]-Phorbol 12,13-Dibutyrate' , 'L-703605'
                }
            },
            'molecule_type': 'TEXT',
            # EXAMPLES:
            # 'Small molecule' , 'Small molecule' , 'Small molecule' , 'Small molecule' , 'Small molecule' , 'Small mole
            # cule' , 'Protein' , 'Small molecule' , 'Small molecule' , 'Small molecule'
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
            # 'HEXADECANOIC ACID PHENYLAMIDE' , 'ZINDOXIFENE' , 'AMFENAC SODIUM' , 'Bis [1,2-bis(dipyridine-4-ylphosphin
            # o)ethane] gold (I) Chloride Hydrate; chloride' , 'Bis [1,2-bis(diphenylphosphino)ethane] gold (I) Methanes
            # ulfonate' , 'HOMOHYPOTAURINE' , 'TOLBUTAMIDE' , 'NATEGLINIDE' , 'N-(3-HYDROXYPROPYL)PALMITAMIDE' , '2,3,4,
            # 4'-TETRAMETHOXYBIPHENYL'
            'prodrug': 'NUMERIC',
            # EXAMPLES:
            # '-1' , '-1' , '-1' , '-1' , '-1' , '-1' , '-1' , '-1' , '-1' , '-1'
            'structure_type': 'TEXT',
            # EXAMPLES:
            # 'MOL' , 'MOL' , 'MOL' , 'MOL' , 'MOL' , 'MOL' , 'BOTH' , 'MOL' , 'MOL' , 'MOL'
            'therapeutic_flag': 'BOOLEAN',
            # EXAMPLES:
            # 'False' , 'False' , 'False' , 'False' , 'False' , 'False' , 'False' , 'False' , 'False' , 'False'
            'topical': 'BOOLEAN',
            # EXAMPLES:
            # 'False' , 'False' , 'False' , 'False' , 'False' , 'False' , 'False' , 'False' , 'False' , 'False'
            'usan_stem': 'TEXT',
            # EXAMPLES:
            # '-ifene' , '-ac' , '-glinide' , '-ast; -dil-' , '-micin' , '-prim' , '-oxacin' , '-oxacin' , '-bactam' , '
            # -oxacin'
            'usan_stem_definition': 'TEXT',
            # EXAMPLES:
            # 'antiestrogens of the clomifene and tamoxifen groups' , 'anti-inflammatory agents (acetic acid derivatives
            # )' , 'antidiabetic, SGLT2 inhibitors, not phlorozin derivatives' , 'antiasthmatics/antiallergics (not acti
            # ng primarily as antihistamines); vasodilators (undefined group)' , 'antibiotics (Micromonospora strains)' 
            # , 'antibacterials (trimethoprim type)' , 'antibacterials (quinolone derivatives)' , 'antibacterials (quino
            # lone derivatives)' , 'beta-lactamase inhibitors' , 'antibacterials (quinolone derivatives)'
            'usan_substem': 'TEXT',
            # EXAMPLES:
            # '-ifene' , '-ac' , '-glinide' , '-ast; -dil-' , '-micin' , '-prim' , '-oxacin' , '-oxacin' , '-bactam' , '
            # -oxacin'
            'usan_year': 'NUMERIC',
            # EXAMPLES:
            # '1977' , '2000' , '1978' , '1999' , '1985' , '1984' , '1986' , '1989' , '1987' , '1984'
            'withdrawn_class': 'TEXT',
            # EXAMPLES:
            # 'Misuse' , 'Hematological toxicity; Misuse' , 'Hematological toxicity; Hepatotoxicity; Immune system toxic
            # ity; Nephrotoxicity' , 'Teratogenicity' , 'Cardiotoxicity' , 'Carcinogenicity; Dermatological toxicity' , 
            # 'Hematological toxicity' , 'Carcinogenicity; Gastrotoxicity' , 'Cardiotoxicity' , 'Hematological toxicity'
            'withdrawn_country': 'TEXT',
            # EXAMPLES:
            # 'United States' , 'Norway' , 'Germany' , 'United States; United Kingdom; Germany' , 'France; United States
            # ' , 'United States' , 'United States' , 'United States' , 'United Kingdom; Germany; Italy; Ireland; Nether
            # lands; European Union' , 'United Kingdom'
            'withdrawn_flag': 'BOOLEAN',
            # EXAMPLES:
            # 'False' , 'False' , 'False' , 'False' , 'False' , 'False' , 'False' , 'False' , 'False' , 'False'
            'withdrawn_reason': 'TEXT',
            # EXAMPLES:
            # 'Self-Poisonings' , 'Off-Label Abuse; Hematologic Toxicity' , 'Low blood sugar; hemolytic anemia; kidney, 
            # liver dysfunction; allergic reactions' , 'Risk for birth defects' , 'Arrhythmias and Sudden Cardiac Death 
            # (Arrhythmias and Sudden)' , 'Cutaneous Reactions; Animal Carcinogenicity' , 'Agranulocytosis' , 'Animal Ca
            # rcinogenicity (rodent); Gastrointestinal Toxicity' , 'Cardiac repolarization; QTc interval prolongation' ,
            #  'Agranulocytosis'
            'withdrawn_year': 'NUMERIC',
            # EXAMPLES:
            # '1980' , '1985' , '1992' , '1989' , '1998' , '1984' , '1985' , '1983' , '1999' , '1970'
        }
    }
