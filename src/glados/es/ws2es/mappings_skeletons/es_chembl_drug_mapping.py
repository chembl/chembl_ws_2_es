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
            'applicants': 'TEXT',
            # EXAMPLES:
            # 'Astrazeneca Lp' , 'Sun Pharmaceutical Industries Ltd' , 'Teva Pharmaceuticals Usa' , 'Mylan Pharmaceutica
            # ls Inc' , 'Mylan Pharmaceuticals Inc' , 'Actelion Pharmaceuticals Ltd' , 'Sun Pharmaceutical Industries Lt
            # d' , 'Mylan Pharmaceuticals Inc' , 'King Pharmaceuticals Inc' , 'Vistapharm Inc'
            'atc_classification': 
            {
                'properties': 
                {
                    'code': 'TEXT',
                    # EXAMPLES:
                    # 'N01BB07' , 'V03AB15' , 'G03XC01' , 'L02BA01' , 'N04BC01' , 'B01AC11' , 'L01XX17' , 'N05AX08' , 'R
                    # 03BC01' , 'A03FA01'
                    'description': 'TEXT',
                    # EXAMPLES:
                    # 'NERVOUS SYSTEM: ANESTHETICS: ANESTHETICS, LOCAL: Amide' , 'VARIOUS: ALL OTHER THERAPEUTIC PRODUCT
                    # S: ALL OTHER THERAPEUTIC PRODUCTS: Antidote' , 'GENITO URINARY SYSTEM AND SEX HORMONES: SEX HORMON
                    # ES AND MODULATORS OF THE GENITAL SYSTEM: OTHER SEX HORMONES AND MODULATORS OF THE GENITAL SYSTEM: 
                    # Selective estrogen receptor modulators' , 'ANTINEOPLASTIC AND IMMUNOMODULATING AGENTS: ENDOCRINE T
                    # HERAPY: HORMONE ANTAGONISTS AND RELATED AGENTS: Anti-estrogens' , 'NERVOUS SYSTEM: ANTI-PARKINSON 
                    # DRUGS: DOPAMINERGIC AGENTS: Dopamine agonist' , 'BLOOD AND BLOOD FORMING ORGANS: ANTITHROMBOTIC AG
                    # ENTS: ANTITHROMBOTIC AGENTS: Platelet aggregation inhibitors excl. heparin' , 'ANTINEOPLASTIC AND 
                    # IMMUNOMODULATING AGENTS: ANTINEOPLASTIC AGENTS: OTHER ANTINEOPLASTIC AGENTS: Other antineoplastic 
                    # agents' , 'NERVOUS SYSTEM: PSYCHOLEPTICS: ANTIPSYCHOTICS: Other antipsychotics' , 'RESPIRATORY SYS
                    # TEM: DRUGS FOR OBSTRUCTIVE AIRWAY DISEASES: OTHER DRUGS FOR OBSTRUCTIVE AIRWAY DISEASES, INHALANTS
                    # : Antiallergic agents, excl. corticosteroid' , 'ALIMENTARY TRACT AND METABOLISM: DRUGS FOR FUNCTIO
                    # NAL GASTROINTESTINAL DISORDERS: PROPULSIVES: Propulsives'
                }
            },
            'availability_type': 'NUMERIC',
            # EXAMPLES:
            # '0' , '1' , '1' , '1' , '1' , '1' , '1' , '1' , '2' , '1'
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
                            # '6717' , '6747' , '6551' , '6329' , '6576' , '6480' , '6458' , '6456' , '6289' , '6322'
                            'component_type': 'TEXT',
                            # EXAMPLES:
                            # 'PROTEIN' , 'PROTEIN' , 'PROTEIN' , 'PROTEIN' , 'PROTEIN' , 'PROTEIN' , 'PROTEIN' , 'PROTE
                            # IN' , 'PROTEIN' , 'PROTEIN'
                            'description': 'TEXT',
                            # EXAMPLES:
                            # 'Progonadoliberin I precursor' , 'Enfuvirtide peptide' , 'Icrucumab heavy chain' , 'Indatu
                            # ximab ravtansine heavy chain' , 'Intetumumab heavy chain' , 'Itolizumab heavy chain' , 'Ix
                            # ekizumab heavy chain' , 'Lebrikizumab heavy chain' , 'Lexatumumab heavy chain' , 'Lorvotuz
                            # umab mertansine heavy chain'
                            'organism': 'TEXT',
                            # EXAMPLES:
                            # 'Homo sapiens' , 'Homo sapiens' , 'Homo sapiens' , 'Homo sapiens' , 'Homo sapiens' , 'Homo
                            #  sapiens' , 'Mus musculus' , 'Homo sapiens' , 'Mus musculus' , 'Homo sapiens'
                            'sequence': 'TEXT',
                            # EXAMPLES:
                            # 'MKPIQKLLAGLILLTWCVEGCSSQHWSYGLRPGGKRDAENLIDSFQEIVKEVGQLAETQRFECTTHQPRSPLRDLKGALESLIEEETGQ
                            # KKI' , 'FWNWLSAWKDLELLEQENKEQQNQSEEILSHILSTY' , 'QAQVVESGGGVVQSGRSLRLSCAASGFAFSSYGMHWVRQAP
                            # GKGLEWVAVIWYDGSNKYYADSVRGRFTISRDNSENTLYLQMNSLRAEDTAVYYCARDHYGSGVHHYFYYGLDVWGQGTTVTVSSASTKG
                            # PSVFPLAPSSKSTSGGTAALGCLVKDYFPEPVTVSWNSGALTSGVHTFPAVLQSSGLYSLSSVVTVPSSSLGTQTYICNVNHKPSNTKVD
                            # KRVEPKSCDKTHTCPPCPAPELLGGPSVFLFPPKPKDTLMISRTPEVTCVVVDVSHEDPEVKFNWYVDGVEVHNAKTKPREEQYNSTYRV
                            # VSVLTVLHQDWLNGKEYKCKVSNKALPAPIEKTISKAKGQPREPQVYTLPPSREEMTKNQVSLTCLVKGFYPSDIAVEWESNGQPENNYK
                            # TTPPVLDSDGSFFLYSKLTVDKSRWQQGNVFSCSVMHEALHNHYTQKSLSLSPGK' , 'QVQLQQSGSELMMPGASVKISCKATGYTFS
                            # NYWIEWVKQRPGHGLEWIGEILPGTGRTIYNEKFKGKATFTADISSNTVQMQLSSLTSEDSAVYYCARRDYYGNFYYAMDYWGQGTSVTV
                            # SSASTKGPSVFPLAPCSRSTSESTAALGCLVKDYFPEPVTVSWNSGALTSGVHTFPAVLQSSGLYSLSSVVTVPSSSLGTKTYTCNVDHK
                            # PSNTKVDKRVESKYGPPCPSCPAPEFLGGPSVFLFPPKPKDTLMISRTPEVTCVVVDVSQEDPEVQFNWYVDGVEVHNAKTKPREEQFNS
                            # TYRVVSVLTVLHQDWLNGKEYKCKVSNKGLPSSIEKTISKAKGQPREPQVYTLPPSQEEMTKNQVSLTCLVKGFYPSDIAVEWESNGQPE
                            # NNYKTTPPVLDSDGSFFLYSRLTVDKSRWQEGNVFSCSVMHEALHNHYTQKSLSLSLGK' , 'QVQLVESGGGVVQPGRSRRLSCAASG
                            # FTFSRYTMHWVRQAPGKGLEWVAVISFDGSNKYYVDSVKGRFTISRDNSENTLYLQVNILRAEDTAVYYCAREARGSYAFDIWGQGTMVT
                            # VSSASTKGPSVFPLAPSSKSTSGGTAALGCLVKDYFPEPVTVSWNSGALTSGVHTFPAVLQSSGLYSLSSVVTVPSSSLGTQTYICNVNH
                            # KPSNTKVDKKVEPKSCDKTHTCPPCPAPELLGGPSVFLFPPKPKDTLMISRTPEVTCVVVDVSHEDPEVKFNWYVDGVEVHNAKTKPREE
                            # QYNSTYRVVSVLTVLHQDWLNGKEYKCKVSNKALPAPIEKTISKAKGQPREPQVYTLPPSRDELTKNQVSLTCLVKGFYPSDIAVEWESN
                            # GQPENNYKTTPPVLDSDGSFFLYSKLTVDKSRWQQGNVFSCSVMHEALHNHYTQKSLSLSPGK' , 'EVQLVESGGGLVKPGGSLKLSC
                            # AASGFKFSRYAMSWVRQAPGKRLEWVATISSGGSYIYYPDSVKGRFTISRDNVKNTLYLQMSSLRSEDTAMYYCARRDYDLDYFDSWGQG
                            # TLVTVSSASTKGPSVFPLAPSSKSTSGGTAALGCLVKDYFPEPVTVSWNSGALTSGVHTFPAVLQSSGLYSLSSVVTVPSSSLGTQTYIC
                            # NVNHKPSNTKVDKKVEPKSCDKTHTCPPCPAPELLGGPSVFLFPPKPKDTLMISRTPEVTCVVVDVSHEDPEVKFNWYVDGVEVHNAKTK
                            # PREEQYNSTYRVVSVLTVLHQDWLNGKEYKCKVSNKALPAPIEKTISKAKGQPREPQVYTLPPSRDELTKNQVSLTCLVKGFYPSDIAVE
                            # WESNGQPENNYKTTPPVLDSDGSFFLYSKLTVDKSRWQQGNVFSCSVMHEALHNHYTQKSLSLSPGK' , 'QVQLVQSGAEVKKPGSSV
                            # KVSCKASGYSFTDYHIHWVRQAPGQGLEWMGVINPMYGTTDYNQRFKGRVTITADESTSTAYMELSSLRSEDTAVYYCARYDYFTGTGVY
                            # WGQGTLVTVSSASTKGPSVFPLAPCSRSTSESTAALGCLVKDYFPEPVTVSWNSGALTSGVHTFPAVLQSSGLYSLSSVVTVPSSSLGTK
                            # TYTCNVDHKPSNTKVDKRVESKYGPPCPPCPAPEFLGGPSVFLFPPKPKDTLMISRTPEVTCVVVDVSQEDPEVQFNWYVDGVEVHNAKT
                            # KPREEQFNSTYRVVSVLTVLHQDWLNGKEYKCKVSNKGLPSSIEKTISKAKGQPREPQVYTLPPSQEEMTKNQVSLTCLVKGFYPSDIAV
                            # EWESNGQPENNYKTTPPVLDSDGSFFLYSRLTVDKSRWQEGNVFSCSVMHEALHNHYTQKSLSLSLG' , 'QVTLRESGPALVKPTQTL
                            # TLTCTVSGFSLSAYSVNWIRQPPGKALEWLAMIWGDGKIVYNSALKSRLTISKDTSKNQVVLTMTNMDPVDTATYYCAGDGYYPYAMDNW
                            # GQGSLVTVSSASTKGPSVFPLAPCSRSTSESTAALGCLVKDYFPEPVTVSWNSGALTSGVHTFPAVLQSSGLYSLSSVVTVPSSSLGTKT
                            # YTCNVDHKPSNTKVDKRVESKYGPPCPPCPAPEFLGGPSVFLFPPKPKDTLMISRTPEVTCVVVDVSQEDPEVQFNWYVDGVEVHNAKTK
                            # PREEQFNSTYRVVSVLTVLHQDWLNGKEYKCKVSNKGLPSSIEKTISKAKGQPREPQVYTLPPSQEEMTKNQVSLTCLVKGFYPSDIAVE
                            # WESNGQPENNYKTTPPVLDSDGSFFLYSRLTVDKSRWQEGNVFSCSVMHEALHNHYTQKSLSLSLGK' , 'EVQLVQSGGGVERPGGSL
                            # RLSCAASGFTFDDYGMSWVRQAPGKGLEWVSGINWNGGSTGYADSVKGRVTISRDNAKNSLYLQMNSLRAEDTAVYYCAKILGAGRGWYF
                            # DLWGKGTTVTVSSASTKGPSVFPLAPSSKSTSGGTAALGCLVKDYFPEPVTVSWNSGALTSGVHTFPAVLQSSGLYSLSSVVTVPSSSLG
                            # TQTYICNVNHKPSNTKVDKRVEPKSCDKTHTCPPCPAPELLGGPSVFLFPPKPKDTLMISRTPEVTCVVVDVSHEDPEVKFNWYVDGVEV
                            # HNAKTKPREEQYNSTYRVVSVLTVLHQDWLNGKEYKCKVSNKALPAPIEKTISKAKGQPREPQVYTLPPSREEMTKNQVSLTCLVKGFYP
                            # SDIAVEWESNGQPENNYKTTPPVLDSDGSFFLYSKLTVDKSRWQQGNVFSCSVMHEALHNHYTQKSLSLSPGK' , 'QVQLVESGGGVV
                            # QPGRSLRLSCAASGFTFSSFGMHWVRQAPGKGLEWVAYISSGSFTIYYADSVKGRFTISRDNSKNTLYLQMNSLRAEDTAVYYCARMRKG
                            # YAMDYWGQGTLVTVSSASTKGPSVFPLAPSSKSTSGGTAALGCLVKDYFPEPVTVSWNSGALTSGVHTFPAVLQSSGLYSLSSVVTVPSS
                            # SLGTQTYICNVNHKPSNTKVDKKVEPKSCDKTHTCPPCPAPELLGGPSVFLFPPKPKDTLMISRTPEVTCVVVDVSHEDPEVKFNWYVDG
                            # VEVHNAKTKPREEQYNSTYRVVSVLTVLHQDWLNGKEYKCKVSNKALPAPIEKTISKAKGQPREPQVYTLPPSRDELTKNQVSLTCLVKG
                            # FYPSDIAVEWESNGQPENNYKTTPPVLDSDGSFFLYSKLTVDKSRWQQGNVFSCSVMHEALHNHYTQKSLSLSPGK'
                            'tax_id': 'NUMERIC',
                            # EXAMPLES:
                            # '9606' , '9606' , '9606' , '9606' , '9606' , '9606' , '10090' , '9606' , '10090' , '9606'
                        }
                    },
                    'description': 'TEXT',
                    # EXAMPLES:
                    # 'INTERMEDINE' , 'GLUCAGON' , 'TEPROTIDE' , 'GANIRELIX ACETATE' , 'PRAZARELIX' , 'ABARELIX' , 'THYM
                    # OPENTIN' , 'PENETRATIN' , 'GRAMICIDIN S' , 'ELEDOISIN'
                    'helm_notation': 'TEXT',
                    # EXAMPLES:
                    # 'PEPTIDE1{[ac].S.Y.S.M.E.H.F.R.W.G.K.P.V.[am]}$$$$' , 'PEPTIDE1{H.S.Q.G.T.F.T.S.D.Y.S.K.Y.L.D.S.R.
                    # R.A.Q.D.F.V.Q.W.L.M.N.T}$$$$' , 'PEPTIDE1{[Glp].W.P.R.P.Q.I.P.P}$$$$' , 'PEPTIDE1{[ac].[dNal].[dPh
                    # e(4-Cl)].[d3-Pal].S.Y.[X18].L.[X17].P.[dA].[am]}$$$$' , 'PEPTIDE1{[ac].[dNal].[dPhe(4-Cl)].[d3-Pal
                    # ].S.[X569].[X570].L.[X4].P.[dA].[am]}$$$$' , 'PEPTIDE1{[ac].[dNal].[dPhe(4-Cl)].[d3-Pal].S.[meY].[
                    # dN].L.[X4].P.[dA].[am]}$$$$' , 'PEPTIDE1{R.K.D.V.Y}$$$$' , 'PEPTIDE1{A.S.T.T.T.N.Y.T}$$$$' , 'PEPT
                    # IDE1{G.[X298].E}$$$$' , 'PEPTIDE1{R.Q.I.K.I.W.F.Q.N.R.R.M.K.W.K.K.[am]}$$$$'
                    'molecule_chembl_id': 'TEXT',
                    # EXAMPLES:
                    # 'CHEMBL214332' , 'CHEMBL266481' , 'CHEMBL408983' , 'CHEMBL1251' , 'CHEMBL409018' , 'CHEMBL1252' , 
                    # 'CHEMBL156025' , 'CHEMBL180971' , 'CHEMBL197084' , 'CHEMBL439448'
                }
            },
            'black_box': 'BOOLEAN',
            # EXAMPLES:
            # 'False' , 'False' , 'False' , 'True' , 'True' , 'False' , 'False' , 'False' , 'False' , 'False'
            'chirality': 'NUMERIC',
            # EXAMPLES:
            # '0' , '0' , '1' , '2' , '2' , '1' , '2' , '1' , '2' , '2'
            'development_phase': 'NUMERIC',
            # EXAMPLES:
            # '0' , '4' , '4' , '4' , '4' , '4' , '3' , '2' , '0' , '0'
            'drug_type': 'NUMERIC',
            # EXAMPLES:
            # '1' , '1' , '7' , '1' , '1' , '7' , '1' , '7' , '1' , '1'
            'drug_warnings': 
            {
                'properties': 
                {
                    'warning_class': 'TEXT',
                    # EXAMPLES:
                    # 'Hematological toxicity' , 'Immune system toxicity' , 'Neurotoxicity' , 'Cardiotoxicity' , 'Hemato
                    # logical toxicity' , 'Carcinogenicity' , 'Gastrotoxicity' , 'Hepatotoxicity' , 'Misuse' , 'Cardioto
                    # xicity'
                    'warning_country': 'TEXT',
                    # EXAMPLES:
                    # 'United Kingdom; United States; Germany; France; Japan' , 'United Kingdom; Germany; Italy; Ireland
                    # ; Netherlands; European Union' , 'France' , 'France; unapproved in United States' , 'Germany' , 'E
                    # uropean Union; Never approved in the United States' , 'United Kingdom; United States; Germany; Den
                    # mark' , 'United Kingdom' , 'France' , 'United Kingdom; Spain; Germany'
                    'warning_description': 'TEXT',
                    # EXAMPLES:
                    # 'Neurotoxicity' , 'Arrhythmias and Sudden Cardiac Death (Arrhythmias and Sudden)' , 'Hepatotoxicit
                    # y' , 'Abuse' , 'Off-Label Abuse; Hematologic Toxicity' , 'Psychiatric effects, especially depressi
                    # on' , 'Nephropathy' , 'Cutaneous Reactions; Animal Carcinogenicity' , 'Agranulocytosis' , 'Animal 
                    # Carcinogenicity (rodent); Gastrointestinal Toxicity'
                    'warning_id': 'NUMERIC',
                    # EXAMPLES:
                    # '2783' , '2704' , '1416' , '2299' , '2065' , '2308' , '2148' , '1092' , '337' , '910'
                    'warning_refs': 
                    {
                        'properties': 
                        {
                            'ref_id': 'TEXT',
                            # EXAMPLES:
                            # 'None' , 'None' , 'None' , 'None' , 'None' , 'None' , 'None' , 'None' , 'None' , 'None'
                            'ref_type': 'TEXT',
                            # EXAMPLES:
                            # 'None' , 'None' , 'None' , 'None' , 'None' , 'None' , 'None' , 'None' , 'None' , 'None'
                            'ref_url': 'TEXT',
                            # EXAMPLES:
                            # 'None' , 'None' , 'None' , 'None' , 'None' , 'None' , 'None' , 'None' , 'None' , 'None'
                        }
                    },
                    'warning_type': 'TEXT',
                    # EXAMPLES:
                    # 'Black Box Warning' , 'Black Box Warning' , 'Black Box Warning' , 'Black Box Warning' , 'Withdrawn
                    # ' , 'Black Box Warning' , 'Withdrawn' , 'Black Box Warning' , 'Black Box Warning' , 'Black Box War
                    # ning'
                    'warning_year': 'NUMERIC',
                    # EXAMPLES:
                    # '1973' , '1998' , '1987' , '1996' , '1985' , '2008' , '1980' , '1984' , '1985' , '1983'
                }
            },
            'first_approval': 'NUMERIC',
            # EXAMPLES:
            # '1976' , '1971' , '1997' , '1977' , '1978' , '2004' , '1996' , '1993' , '1982' , '1979'
            'first_in_class': 'BOOLEAN',
            # EXAMPLES:
            # 'False' , 'False' , 'False' , 'False' , 'False' , 'False' , 'False' , 'False' , 'False' , 'False'
            'helm_notation': 'TEXT',
            # EXAMPLES:
            # 'PEPTIDE1{[ac].S.Y.S.M.E.H.F.R.W.G.K.P.V.[am]}$$$$' , 'PEPTIDE1{H.S.Q.G.T.F.T.S.D.Y.S.K.Y.L.D.S.R.R.A.Q.D.
            # F.V.Q.W.L.M.N.T}$$$$' , 'PEPTIDE1{[Glp].W.P.R.P.Q.I.P.P}$$$$' , 'PEPTIDE1{[ac].[dNal].[dPhe(4-Cl)].[d3-Pal
            # ].S.Y.[X18].L.[X17].P.[dA].[am]}$$$$' , 'PEPTIDE1{[ac].[dNal].[dPhe(4-Cl)].[d3-Pal].S.[X569].[X570].L.[X4]
            # .P.[dA].[am]}$$$$' , 'PEPTIDE1{[ac].[dNal].[dPhe(4-Cl)].[d3-Pal].S.[meY].[dN].L.[X4].P.[dA].[am]}$$$$' , '
            # PEPTIDE1{R.K.D.V.Y}$$$$' , 'PEPTIDE1{A.S.T.T.T.N.Y.T}$$$$' , 'PEPTIDE1{G.[X298].E}$$$$' , 'PEPTIDE1{R.Q.I.
            # K.I.W.F.Q.N.R.R.M.K.W.K.K.[am]}$$$$'
            'indication_class': 'TEXT',
            # EXAMPLES:
            # 'Anticholinergic' , 'Anesthetic (local)' , 'Antagonist (to narcotics)' , 'Anti-Estrogen' , 'Anti-Estrogen'
            #  , 'Enzyme Inhibitor (prolactin)' , 'Antifihrinolytic; Anticoagulant' , 'Antineoplastic (DNA topoisomerase
            #  I Inhibitor)' , 'Inhibitor (aldose reductase); Antidiabetic' , 'Inhibitor (aldose reductase)'
            'molecule_chembl_id': 'TEXT',
            # EXAMPLES:
            # 'CHEMBL10272' , 'CHEMBL492' , 'CHEMBL80' , 'CHEMBL81' , 'CHEMBL83' , 'CHEMBL493' , 'CHEMBL273264' , 'CHEMB
            # L274070' , 'CHEMBL269455' , 'CHEMBL10445'
            'molecule_properties': 
            {
                'properties': 
                {
                    'alogp': 'NUMERIC',
                    # EXAMPLES:
                    # '3.27' , '3.75' , '1.30' , '6.08' , '6.00' , '3.19' , '2.65' , '1.66' , '2.03' , '4.09'
                    'aromatic_rings': 'NUMERIC',
                    # EXAMPLES:
                    # '2' , '1' , '1' , '4' , '3' , '2' , '3' , '3' , '2' , '2'
                    'cx_logd': 'NUMERIC',
                    # EXAMPLES:
                    # '2.10' , '3.25' , '1.04' , '5.34' , '4.97' , '3.80' , '-0.28' , '0.39' , '2.08' , '1.94'
                    'cx_logp': 'NUMERIC',
                    # EXAMPLES:
                    # '3.38' , '4.46' , '1.62' , '5.69' , '6.35' , '3.89' , '2.52' , '0.39' , '2.11' , '3.58'
                    'cx_most_apka': 'NUMERIC',
                    # EXAMPLES:
                    # '11.69' , '13.62' , '10.07' , '8.89' , '9.69' , '11.69' , '8.65' , '11.39' , '9.65' , '3.41'
                    'cx_most_bpka': 'NUMERIC',
                    # EXAMPLES:
                    # '8.66' , '8.59' , '7.84' , '7.95' , '8.76' , '6.71' , '11.32' , '3.91' , '9.04' , '3.17'
                    'full_molformula': 'TEXT',
                    # EXAMPLES:
                    # 'C23H26N2O2' , 'C17H28N2O' , 'C19H21NO4' , 'C28H27NO4S' , 'C26H29NO' , 'C32H40BrN5O5' , 'C19H17N5O
                    # 2' , 'C20H17N3O4' , 'C15H8F2N2O2' , 'C22H27Cl2N3O4'
                    'full_mwt': 'NUMERIC',
                    # EXAMPLES:
                    # '362.47' , '276.42' , '327.38' , '473.59' , '371.52' , '654.61' , '347.38' , '363.37' , '286.24' ,
                    #  '468.38'
                    'hba': 'NUMERIC',
                    # EXAMPLES:
                    # '3' , '2' , '5' , '6' , '2' , '6' , '4' , '7' , '2' , '5'
                    'hba_lipinski': 'NUMERIC',
                    # EXAMPLES:
                    # '4' , '3' , '5' , '5' , '2' , '10' , '7' , '7' , '4' , '7'
                    'hbd': 'NUMERIC',
                    # EXAMPLES:
                    # '1' , '1' , '2' , '2' , '0' , '3' , '5' , '2' , '2' , '2'
                    'hbd_lipinski': 'NUMERIC',
                    # EXAMPLES:
                    # '1' , '1' , '2' , '2' , '0' , '3' , '7' , '3' , '2' , '2'
                    'heavy_atoms': 'NUMERIC',
                    # EXAMPLES:
                    # '27' , '20' , '24' , '34' , '28' , '43' , '26' , '27' , '21' , '31'
                    'molecular_species': 'TEXT',
                    # EXAMPLES:
                    # 'BASE' , 'BASE' , 'NEUTRAL' , 'NEUTRAL' , 'BASE' , 'NEUTRAL' , 'BASE' , 'NEUTRAL' , 'NEUTRAL' , 'B
                    # ASE'
                    'mw_freebase': 'NUMERIC',
                    # EXAMPLES:
                    # '362.47' , '276.42' , '327.38' , '473.59' , '371.52' , '654.61' , '347.38' , '363.37' , '286.24' ,
                    #  '468.38'
                    'mw_monoisotopic': 'NUMERIC',
                    # EXAMPLES:
                    # '362.1994' , '276.2202' , '327.1471' , '473.1661' , '371.2249' , '653.2213' , '347.1382' , '363.12
                    # 19' , '286.0554' , '467.1379'
                    'num_lipinski_ro5_violations': 'NUMERIC',
                    # EXAMPLES:
                    # '0' , '0' , '0' , '1' , '1' , '1' , '1' , '0' , '0' , '0'
                    'num_ro5_violations': 'NUMERIC',
                    # EXAMPLES:
                    # '0' , '0' , '0' , '1' , '1' , '1' , '0' , '0' , '0' , '0'
                    'psa': 'NUMERIC',
                    # EXAMPLES:
                    # '49.41' , '32.34' , '70.00' , '70.00' , '12.47' , '118.21' , '138.07' , '107.44' , '58.20' , '79.9
                    # 0'
                    'qed_weighted': 'NUMERIC',
                    # EXAMPLES:
                    # '0.85' , '0.82' , '0.80' , '0.32' , '0.45' , '0.46' , '0.21' , '0.39' , '0.73' , '0.52'
                    'ro3_pass': 'TEXT',
                    # EXAMPLES:
                    # 'N' , 'N' , 'N' , 'N' , 'N' , 'N' , 'N' , 'N' , 'Y' , 'N'
                    'rtb': 'NUMERIC',
                    # EXAMPLES:
                    # '4' , '7' , '2' , '7' , '8' , '5' , '4' , '1' , '0' , '11'
                }
            },
            'molecule_structures': 
            {
                'properties': 
                {
                    'canonical_smiles': 'TEXT',
                    # EXAMPLES:
                    # 'O=C1CCC(c2ccccc2)(C2CCN(Cc3ccccc3)CC2)C(=O)N1' , 'CCCN(CC)C(CC)C(=O)Nc1c(C)cccc1C' , 'C=CCN1CC[C@
                    # ]23c4c5ccc(O)c4O[C@H]2C(=O)CC[C@@]3(O)[C@H]1C5' , 'O=C(c1ccc(OCCN2CCCCC2)cc1)c1c(-c2ccc(O)cc2)sc2c
                    # c(O)ccc12' , 'CC/C(=C(\c1ccccc1)c1ccc(OCCN(C)C)cc1)c1ccccc1' , 'CC(C)C[C@H]1C(=O)N2CCC[C@H]2[C@]2(
                    # O)O[C@](NC(=O)[C@@H]3C=C4c5cccc6[nH]c(Br)c(c56)C[C@H]4N(C)C3)(C(C)C)C(=O)N12' , 'N=C(N)Nc1ccc(C(=O
                    # )Oc2ccc3cc(C(=N)N)ccc3c2)cc1' , 'CC[C@@]1(O)C(=O)OCc2c1cc1n(c2=O)Cc2cc3c(N)cccc3nc2-1' , 'O=C1NC(=
                    # O)C2(N1)c1cc(F)ccc1-c1ccc(F)cc12' , 'CCN(CC)CCNC(=O)c1cc(Cl)c(NC(=O)COc2ccc(Cl)cc2)cc1OC'
                    'standard_inchi': 'TEXT',
                    # EXAMPLES:
                    # 'InChI=1S/C23H26N2O2/c26-21-11-14-23(22(27)24-21,19-9-5-2-6-10-19)20-12-15-25(16-13-20)17-18-7-3-1
                    # -4-8-18/h1-10,20H,11-17H2,(H,24,26,27)' , 'InChI=1S/C17H28N2O/c1-6-12-19(8-3)15(7-2)17(20)18-16-13
                    # (4)10-9-11-14(16)5/h9-11,15H,6-8,12H2,1-5H3,(H,18,20)' , 'InChI=1S/C19H21NO4/c1-2-8-20-9-7-18-15-1
                    # 1-3-4-12(21)16(15)24-17(18)13(22)5-6-19(18,23)14(20)10-11/h2-4,14,17,21,23H,1,5-10H2/t14-,17+,18+,
                    # 19-/m1/s1' , 'InChI=1S/C28H27NO4S/c30-21-8-4-20(5-9-21)28-26(24-13-10-22(31)18-25(24)34-28)27(32)1
                    # 9-6-11-23(12-7-19)33-17-16-29-14-2-1-3-15-29/h4-13,18,30-31H,1-3,14-17H2' , 'InChI=1S/C26H29NO/c1-
                    # 4-25(21-11-7-5-8-12-21)26(22-13-9-6-10-14-22)23-15-17-24(18-16-23)28-20-19-27(2)3/h5-18H,4,19-20H2
                    # ,1-3H3/b26-25-' , 'InChI=1S/C32H40BrN5O5/c1-16(2)12-24-29(40)37-11-7-10-25(37)32(42)38(24)30(41)31
                    # (43-32,17(3)4)35-28(39)18-13-20-19-8-6-9-22-26(19)21(27(33)34-22)14-23(20)36(5)15-18/h6,8-9,13,16-
                    # 18,23-25,34,42H,7,10-12,14-15H2,1-5H3,(H,35,39)/t18-,23-,24+,25+,31-,32+/m1/s1' , 'InChI=1S/C19H17
                    # N5O2/c20-17(21)14-2-1-13-10-16(8-5-12(13)9-14)26-18(25)11-3-6-15(7-4-11)24-19(22)23/h1-10H,(H3,20,
                    # 21)(H4,22,23,24)' , 'InChI=1S/C20H17N3O4/c1-2-20(26)13-7-16-17-10(6-11-14(21)4-3-5-15(11)22-17)8-2
                    # 3(16)18(24)12(13)9-27-19(20)25/h3-7,26H,2,8-9,21H2,1H3/t20-/m0/s1' , 'InChI=1S/C15H8F2N2O2/c16-7-1
                    # -3-9-10-4-2-8(17)6-12(10)15(11(9)5-7)13(20)18-14(21)19-15/h1-6H,(H2,18,19,20,21)' , 'InChI=1S/C22H
                    # 27Cl2N3O4/c1-4-27(5-2)11-10-25-22(29)17-12-18(24)19(13-20(17)30-3)26-21(28)14-31-16-8-6-15(23)7-9-
                    # 16/h6-9,12-13H,4-5,10-11,14H2,1-3H3,(H,25,29)(H,26,28)'
                    'standard_inchi_key': 'TEXT',
                    # EXAMPLES:
                    # 'LQQIVYSCPWCSSD-UHFFFAOYSA-N' , 'VTUSIVBDOCDNHS-UHFFFAOYSA-N' , 'UZHSEJADLWPNLE-GRGSLBFTSA-N' , 'G
                    # ZUITABIAKMVPG-UHFFFAOYSA-N' , 'NKANXQFJJICGDU-QPLCGJKRSA-N' , 'OZVBMTJYIDMWIL-AYFBDAFISA-N' , 'MQQ
                    # NFDZXWVTQEH-UHFFFAOYSA-N' , 'FUXVKZWTXQUGMW-FQEVSTJZSA-N' , 'QCCHBHSAIQIQGO-UHFFFAOYSA-N' , 'VZNJZ
                    # QAFQDEJOO-UHFFFAOYSA-N'
                }
            },
            'molecule_synonyms': 
            {
                'properties': 
                {
                    'molecule_synonym': 'TEXT',
                    # EXAMPLES:
                    # 'Benzetimide' , 'Duranest [as hydrochloride]' , 'Nalone' , 'Evista' , 'ICI-46474' , 'Bromocriptine
                    # ' , 'Nafamostat' , '9-aminocamptothecin' , 'Imirestat' , 'Cloxacepride'
                    'syn_type': 'TEXT',
                    # EXAMPLES:
                    # 'INN' , 'TRADE_NAME' , 'TRADE_NAME' , 'OTHER' , 'RESEARCH_CODE' , 'FDA' , 'INN' , 'MERCK_INDEX' , 
                    # 'OTHER' , 'OTHER'
                    'synonyms': 'TEXT',
                    # EXAMPLES:
                    # 'BENZETIMIDE' , 'Duranest [as hydrochloride]' , 'Nalone' , 'Evista' , 'ICI-46474' , 'Bromocriptine
                    # ' , 'NAFAMOSTAT' , '9-AMINOCAMPTOTHECIN' , 'Imirestat' , 'Cloxacepride'
                }
            },
            'ob_patent': 'NUMERIC',
            # EXAMPLES:
            # '7579019' , '7888310' , '8158645' , '6667061' , '6770262' , '7758891' , '7030149' , '6465463' , '6153635' 
            # , '8940786'
            'oral': 'BOOLEAN',
            # EXAMPLES:
            # 'False' , 'False' , 'True' , 'True' , 'True' , 'True' , 'False' , 'False' , 'False' , 'False'
            'parenteral': 'BOOLEAN',
            # EXAMPLES:
            # 'False' , 'True' , 'True' , 'False' , 'False' , 'False' , 'False' , 'False' , 'False' , 'False'
            'prodrug': 'BOOLEAN',
            # EXAMPLES:
            # 'False' , 'False' , 'False' , 'False' , 'True' , 'False' , 'False' , 'False' , 'False' , 'False'
            'research_codes': 'TEXT',
            # EXAMPLES:
            # 'JANSSEN R 4929' , 'W-19053 [AS HYDROCHLORIDE]' , 'EN-15304' , 'LY156758' , 'ICI 46,474' , 'CB-154' , 'FUT
            # -175' , 'NSC-603071' , 'NSC-107124' , 'FK-366'
            'rule_of_five': 'BOOLEAN',
            # EXAMPLES:
            # 'True' , 'True' , 'True' , 'False' , 'False' , 'False' , 'True' , 'True' , 'True' , 'True'
            'sc_patent': 'TEXT',
            # EXAMPLES:
            # 'US-7579019-B2' , 'US-7888310-B2' , 'US-8158645-B2' , 'US-6667061-B2' , 'US-6770262-B2' , 'US-7758891-B2' 
            # , 'US-7030149-B2' , 'US-6465463-B1' , 'US-6153635-A' , 'US-8940786-B2'
            'synonyms': 'TEXT',
            # EXAMPLES:
            # 'Benzetimide (INN)' , 'Etidocaine hydrochloride (FDA)' , 'Naloxone hydrochloride (FDA, JAN, MI, USAN, USP)
            # ' , 'Raloxifene (BAN, INN, MI)' , 'Tamoxifen (BAN, INN, MI)' , 'Bromocriptine mesilate (JAN)' , 'Nafamosta
            # t dimethanesulfonate (MI)' , '9-aminocamptothecin (MI)' , 'Imirestat (INN)' , 'Cloxacepride (INN)'
            'topical': 'BOOLEAN',
            # EXAMPLES:
            # 'False' , 'False' , 'True' , 'False' , 'False' , 'False' , 'False' , 'False' , 'False' , 'False'
            'usan_stem': 'TEXT',
            # EXAMPLES:
            # '-caine' , 'nal-' , '-ifene' , '-stat' , '-stat' , '-pride' , '-stat' , '-prost' , '-tecan' , '-stat'
            'usan_stem_definition': 'TEXT',
            # EXAMPLES:
            # 'local anesthetics' , 'narcotic agonists/antagonists (normorphine type)' , 'antiestrogens of the clomifene
            #  and tamoxifen groups' , 'enzyme inhibitors: proteolytic enzyme inhibitors' , 'enzyme inhibitors: aldose-r
            # eductase inhibitors' , 'sulpride derivatives' , 'enzyme inhibitors: aldose-reductase inhibitors' , 'prosta
            # glandins' , 'antineoplastics (camptothecine derivatives)' , 'enzyme inhibitors: aldose-reductase inhibitor
            # s'
            'usan_stem_substem': 'TEXT',
            # EXAMPLES:
            # '-caine(-caine)' , 'nal-(nal-)' , '-ifene(-ifene)' , '-stat(-stat (-mostat))' , '-stat(-stat (-restat))' ,
            #  '-pride(-pride)' , '-stat(-stat (-restat))' , '-prost(-prost)' , '-tecan(-tecan)' , '-stat(-stat (-restat
            # ))'
            'usan_year': 'NUMERIC',
            # EXAMPLES:
            # '1969' , '1973' , '1963' , '1988' , '1976' , '1976' , '1992' , '1998' , '2004' , '1990'
            'withdrawn_class': 'TEXT',
            # EXAMPLES:
            # 'Neurotoxicity' , 'Cardiotoxicity' , 'Hepatotoxicity' , 'Misuse' , 'Hematological toxicity; Misuse' , 'Car
            # diotoxicity' , 'Hematological toxicity; Hepatotoxicity; Immune system toxicity; Nephrotoxicity' , 'Psychia
            # tric toxicity' , 'Hematological toxicity; Hepatotoxicity' , 'Nephrotoxicity'
            'withdrawn_country': 'TEXT',
            # EXAMPLES:
            # 'United Kingdom; United States; Germany; France; Japan' , 'United Kingdom; Germany; Italy; Ireland; Nether
            # lands; European Union' , 'United States' , 'France' , 'France; unapproved in United States' , 'Germany' , 
            # 'United States' , 'United States; United Kingdom; Germany' , 'European Union; Never approved in the United
            #  States' , 'United States; United Kingdom; United States; Spain; Germany; France'
            'withdrawn_reason': 'TEXT',
            # EXAMPLES:
            # 'Neurotoxicity' , 'Arrhythmias and Sudden Cardiac Death (Arrhythmias and Sudden)' , 'Hepatotoxicity' , 'Ab
            # use' , 'Off-Label Abuse; Hematologic Toxicity' , 'Risk for heart valve damage' , 'Low blood sugar; hemolyt
            # ic anemia; kidney, liver dysfunction; allergic reactions' , 'Psychiatric effects, especially depression' ,
            #  'Serious hypersensitive reactions; Hemolytic Anemia; Hepatotoxicity' , 'Nephropathy'
            'withdrawn_year': 'NUMERIC',
            # EXAMPLES:
            # '1973' , '1998' , '1987' , '1996' , '1985' , '2007' , '1992' , '2008' , '1986' , '1980'
        }
    }
