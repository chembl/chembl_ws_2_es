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
            # 'Teva Pharmaceuticals Usa' , 'Emmaus Medical Inc' , 'Halocarbon Laboratories Div Halocarbon Products Corp'
            #  , 'Serb Sa' , 'Sun Pharmaceutical Industries Ltd' , 'Hra Pharma Rare Diseases' , 'Fresenius Kabi Usa Llc'
            #  , 'Sun Pharmaceutical Industries Ltd' , 'Procter And Gamble Pharmaceuticals Inc Sub Procter And Gamble Co
            # ' , 'Astrazeneca Ab'
            'atc_classification': 
            {
                'properties': 
                {
                    'code': 'TEXT',
                    # EXAMPLES:
                    # 'J01DD15' , 'N06AX02' , 'R03DA06' , 'J01CA07' , 'A16AA03' , 'M02AA26' , 'N01AB01' , 'V03AB33' , 'B
                    # 01AC07' , 'V04CD01'
                    'description': 'TEXT',
                    # EXAMPLES:
                    # 'ANTIINFECTIVES FOR SYSTEMIC USE: ANTIBACTERIALS FOR SYSTEMIC USE: OTHER BETA-LACTAM ANTIBACTERIAL
                    # S: Third-generation cephalosporins' , 'NERVOUS SYSTEM: PSYCHOANALEPTICS: ANTIDEPRESSANTS: Other an
                    # tidepressants' , 'RESPIRATORY SYSTEM: DRUGS FOR OBSTRUCTIVE AIRWAY DISEASES: OTHER SYSTEMIC DRUGS 
                    # FOR OBSTRUCTIVE AIRWAY DISEASES: Xanthines' , 'ANTIINFECTIVES FOR SYSTEMIC USE: ANTIBACTERIALS FOR
                    #  SYSTEMIC USE: BETA-LACTAM ANTIBACTERIALS, PENICILLINS: Penicillins with extended spectrum' , 'ALI
                    # MENTARY TRACT AND METABOLISM: OTHER ALIMENTARY TRACT AND METABOLISM PRODUCTS: OTHER ALIMENTARY TRA
                    # CT AND METABOLISM PRODUCTS: Amino acids and derivatives' , 'MUSCULO-SKELETAL SYSTEM: TOPICAL PRODU
                    # CTS FOR JOINT AND MUSCULAR PAIN: TOPICAL PRODUCTS FOR JOINT AND MUSCULAR PAIN: Antiinflammatory pr
                    # eparations, non-steroids for topical us' , 'NERVOUS SYSTEM: ANESTHETICS: ANESTHETICS, GENERAL: Hal
                    # ogenated hydrocarbons' , 'VARIOUS: ALL OTHER THERAPEUTIC PRODUCTS: ALL OTHER THERAPEUTIC PRODUCTS:
                    #  Antidote' , 'BLOOD AND BLOOD FORMING ORGANS: ANTITHROMBOTIC AGENTS: ANTITHROMBOTIC AGENTS: Platel
                    # et aggregation inhibitors excl. heparin' , 'VARIOUS: DIAGNOSTIC AGENTS: OTHER DIAGNOSTIC AGENTS: T
                    # ests for pituitary function'
                }
            },
            'availability_type': 'NUMERIC',
            # EXAMPLES:
            # '1' , '-2' , '-1' , '1' , '-1' , '0' , '1' , '1' , '1' , '1'
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
                            # '9874' , '8639' , '8642' , '8644' , '8647' , '8649' , '9880' , '9882' , '9884' , '8659'
                            'component_type': 'TEXT',
                            # EXAMPLES:
                            # 'PROTEIN' , 'PROTEIN' , 'PROTEIN' , 'PROTEIN' , 'PROTEIN' , 'PROTEIN' , 'PROTEIN' , 'PROTE
                            # IN' , 'PROTEIN' , 'PROTEIN'
                            'description': 'TEXT',
                            # EXAMPLES:
                            # 'EVINACUMAB HEAVY CHAIN' , 'Ipafricept' , 'Enfortumab heavy chain' , 'Fletikumab heavy cha
                            # in' , 'Polatuzumab vedotin heavy chain' , 'Andexanet alfa' , 'LIFASTUZUMAB HEAVY CHAIN' , 
                            # 'BRONTICTUZUMAB HEAVY CHAIN' , 'SACITUZUMAB GOVITECAN HEAVY CHAIN' , 'Enfortumab vedotin h
                            # eavy chain'
                            'organism': 'TEXT',
                            # EXAMPLES:
                            # 'Homo sapiens' , 'Homo sapiens' , 'Homo sapiens' , 'Homo sapiens' , 'Conus magus' , 'Homo 
                            # sapiens' , 'Homo sapiens' , 'Homo sapiens' , 'Homo sapiens' , 'Homo sapiens'
                            'sequence': 'TEXT',
                            # EXAMPLES:
                            # 'EVQLVESGGGVIQPGGSLRLSCAASGFTFDDYAMNWVRQGPGKGLEWVSAISGDGGSTYYADSVKGRFTISRDNSKNSLYLQMNSLRAE
                            # DTAFFYCAKDLRNTIFGVVIPDAFDIWGQGTMVTVSSASTKGPSVFPLAPCSRSTSESTAALGCLVKDYFPEPVTVSWNSGALTSGVHTF
                            # PAVLQSSGLYSLSSVVTVPSSSLGTKTYTCNVDHKPSNTKVDKRVESKYGPPCPPCPAPEFLGGPSVFLFPPKPKDTLMISRTPEVTCVV
                            # VDVSQEDPEVQFNWYVDGVEVHNAKTKPREEQFNSTYRVVSVLTVLHQDWLNGKEYKCKVSNKGLPSSIEKTISKAKGQPREPQVYTLPP
                            # SQEEMTKNQVSLTCLVKGFYPSDIAVEWESNGQPENNYKTTPPVLDSDGSFFLYSRLTVDKSRWQEGNVFSCSVMHEALHNHYTQKSLSL
                            # SLGK' , 'ASAKELACQEITVPLCKGIGYNYTYMPNQFNHDTQDEAGLEVHQFWPLVEIQCSPDLKFFLCSMYTPICLEDYKKPLPPCR
                            # SVCERAKAGCAPLMRQYGFAWPDRMRCDRLPEQGNPDTLCMDYNRTDLTTEPKSSDKTHTCPPCPAPELLGGPSVFLFPPKPKDTLMISR
                            # TPEVTCVVVDVSHEDPEVKFNWYVDGVEVHNAKTKPREEQYNSTYRVVSVLTVLHQDWLNGKEYKCKVSNKALPAPIEKTISKAKGQPRE
                            # PQVYTLPPSRDELTKNQVSLTCLVKGFYPSDIAVEWESNGQPENNYKTTPPVLDSDGSFFLYSKLTVDKSRWQQGNVFSCSVMHEALHNH
                            # YTQKSLSLSPG' , 'EVQLVESGGGLVQPGGSLRLSCAASGFTFSSYNMNWVRQAPGKGLEWVSYISSSSSTIYYADSVKGRFTISRDN
                            # AKNSLSLQMNSLRDEDTAVYYCARAYYYGMDVWGQGTTVTVSSASTKGPSVFPLAPSSKSTSGGTAALGCLVKDYFPEPVTVSWNSGALT
                            # SGVHTFPAVLQSSGLYSLSSVVTVPSSSLGTQTYICNVNHKPSNTKVDKRVEPKSCDKTHTCPPCPAPELLGGPSVFLFPPKPKDTLMIS
                            # RTPEVTCVVVDVSHEDPEVKFNWYVDGVEVHNAKTKPREEQYNSTYRVVSVLTVLHQDWLNGKEYKCKVSNKALPAPIEKTISKAKGQPR
                            # EPQVYTLPPSREEMTKNQVSLTCLVKGFYPSDIAVEWESNGQPENNYKTTPPVLDSDGSFFLYSKLTVDKSRWQQGNVFSCSVMHEALHN
                            # HYTQKSLSLSPGK' , 'QVQLVQSGAEVKRPGASVKVSCKASGYTFTNDIIHWVRQAPGQRLEWMGWINAGYGNTQYSQNFQDRVSITR
                            # DTSASTAYMELISLRSEDTAVYYCAREPLWFGESSPHDYYGMDVWGQGTTVTVSSASTKGPSVFPLAPCSRSTSESTAALGCLVKDYFPE
                            # PVTVSWNSGALTSGVHTFPAVLQSSGLYSLSSVVTVPSSSLGTKTYTCNVDHKPSNTKVDKRVESKYGPPCPPCPAPEFLGGPSVFLFPP
                            # KPKDTLMISRTPEVTCVVVDVSQEDPEVQFNWYVDGVEVHNAKTKPREEQFNSTYRVVSVLTVLHQDWLNGKEYKCKVSNKGLPSSIEKT
                            # ISKAKGQPREPQVYTLPPSQEEMTKNQVSLTCLVKGFYPSDIAVEWESNGQPENNYKTTPPVLDSDGSFFLYSRLTVDKSRWQEGNVFSC
                            # SVMHEALHNHYTQKSLSLSLGK' , 'EVQLVESGGGLVQPGGSLRLSCAASGYTFSSYWIEWVRQAPGKGLEWIGEILPGGGDTNYNEI
                            # FKGRATFSADTSKNTAYLQMNSLRAEDTAVYYCTRRVPIRLDYWGQGTLVTVSSASTKGPSVFPLAPSSKSTSGGTAALGCLVKDYFPEP
                            # VTVSWNSGALTSGVHTFPAVLQSSGLYSLSSVVTVPSSSLGTQTYICNVNHKPSNTKVDKKVEPKSCDKTHTCPPCPAPELLGGPSVFLF
                            # PPKPKDTLMISRTPEVTCVVVDVSHEDPEVKFNWYVDGVEVHNAKTKPREEQYNSTYRVVSVLTVLHQDWLNGKEYKCKVSNKALPAPIE
                            # KTISKAKGQPREPQVYTLPPSREEMTKNQVSLTCLVKGFYPSDIAVEWESNGQPENNYKTTPPVLDSDGSFFLYSKLTVDKSRWQQGNVF
                            # SCSVMHEALHNHYTQKSLSLSPGK' , 'ANSFLFWNKYKDGDQCETSPCQNQGKCKDGLGEYTCTCLEGFEGKNCELFTRKLCSLDNGD
                            # CDQFCHEEQNSVVCSCARGYTLADNGKACIPTGPYPCGKQTLERIVGGQECKDGECPWQALLINEENEGFCGGTILSEFYILTAAHCLYQ
                            # AKRFKVRVGDRNTEQEEGGEAVHEVEVVIKHNRFTKETYDFDIAVLRLKTPITFRMNVAPACLPERDWAESTLMTQKTGIVSGFGRTHEK
                            # GRQSTRLKMLEVPYVDRNSCKLSSSFIITQNMFCAGYDTKQEDACQGDAGGPHVTRFKDTYFVTGIVSWGEGCARKGKYGIYTKVTAFLK
                            # WIDRSMKTRGLPKAKSHAPEVITSSPLK' , 'EVQLVESGGGLVQPGGSLRLSCAASGFSFSDFAMSWVRQAPGKGLEWVATIGRVAFH
                            # TYYPDSMKGRFTISRDNSKNTLYLQMNSLRAEDTAVYYCARHRGFDVGHFDFWGQGTLVTVSSASTKGPSVFPLAPSSKSTSGGTAALGC
                            # LVKDYFPEPVTVSWNSGALTSGVHTFPAVLQSSGLYSLSSVVTVPSSSLGTQTYICNVNHKPSNTKVDKKVEPKSCDKTHTCPPCPAPEL
                            # LGGPSVFLFPPKPKDTLMISRTPEVTCVVVDVSHEDPEVKFNWYVDGVEVHNAKTKPREEQYNSTYRVVSVLTVLHQDWLNGKEYKCKVS
                            # NKALPAPIEKTISKAKGQPREPQVYTLPPSREEMTKNQVSLTCLVKGFYPSDIAVEWESNGQPENNYKTTPPVLDSDGSFFLYSKLTVDK
                            # SRWQQGNVFSCSVMHEALHNHYTQKSLSLSPGK' , 'QVQLVQSGAEVKKPGASVKISCKVSGYTLRGYWIEWVRQAPGKGLEWIGQIL
                            # PGTGRTNYNEKFKGRVTMTADTSTDTAYMELSSLRSEDTAVYYCARFDGNYGYYAMDYWGQGTTVTVSSASTKGPSVFPLAPCSRSTSES
                            # TAALGCLVKDYFPEPVTVSWNSGALTSGVHTFPAVLQSSGLYSLSSVVTVPSSNFGTQTYTCNVDHKPSNTKVDKTVERKCCVECPPCPA
                            # PPVAGPSVFLFPPKPKDTLMISRTPEVTCVVVDVSHEDPEVQFNWYVDGVEVHNAKTKPREEQFNSTFRVVSVLTVVHQDWLNGKEYKCK
                            # VSNKGLPAPIEKTISKTKGQPREPQVYTLPPSREEMTKNQVSLTCLVKGFYPSDIAVEWESNGQPENNYKTTPPMLDSDGSFFLYSKLTV
                            # DKSRWQQGNVFSCSVMHEALHNHYTQKSLSLSPGK' , 'QVQLQQSGSELKKPGASVKVSCKASGYTFTNYGMNWVKQAPGQGLKWMGW
                            # INTYTGEPTYTDDFKGRFAFSLDTSVSTAYLQISSLKADDTAVYFCARGGFGSSYWYFDVWGQGSLVTVSSASTKGPSVFPLAPSSKSTS
                            # GGTAALGCLVKDYFPEPVTVSWNSGALTSGVHTFPAVLQSSGLYSLSSVVTVPSSSLGTQTYICNVNHKPSNTKVDKRVEPKSCDKTHTC
                            # PPCPAPELLGGPSVFLFPPKPKDTLMISRTPEVTCVVVDVSHEDPEVKFNWYVDGVEVHNAKTKPREEQYNSTYRVVSVLTVLHQDWLNG
                            # KEYKCKVSNKALPAPIEKTISKAKGQPREPQVYTLPPSREEMTKNQVSLTCLVKGFYPSDIAVEWESNGQPENNYKTTPPVLDSDGSFFL
                            # YSKLTVDKSRWQQGNVFSCSVMHEALHNHYTQKSLSLSPGK' , 'EVQLVESGGGLVQPGGSLRLSCAASGFTFSSYNMNWVRQAPGKG
                            # LEWVSYISSSSSTIYYADSVKGRFTISRDNAKNSLSLQMNSLRDEDTAVYYCARAYYYGMDVWGQGTTVTVSSASTKGPSVFPLAPSSKS
                            # TSGGTAALGCLVKDYFPEPVTVSWNSGALTSGVHTFPAVLQSSGLYSLSSVVTVPSSSLGTQTYICNVNHKPSNTKVDKRVEPKSCDKTH
                            # TCPPCPAPELLGGPSVFLFPPKPKDTLMISRTPEVTCVVVDVSHEDPEVKFNWYVDGVEVHNAKTKPREEQYNSTYRVVSVLTVLHQDWL
                            # NGKEYKCKVSNKALPAPIEKTISKAKGQPREPQVYTLPPSREEMTKNQVSLTCLVKGFYPSDIAVEWESNGQPENNYKTTPPVLDSDGSF
                            # FLYSKLTVDKSRWQQGNVFSCSVMHEALHNHYTQKSLSLSPG'
                            'tax_id': 'NUMERIC',
                            # EXAMPLES:
                            # '9606' , '9606' , '9606' , '9606' , '6492' , '9606' , '9606' , '9606' , '9606' , '9606'
                        }
                    },
                    'description': 'TEXT',
                    # EXAMPLES:
                    # 'BIVALIRUDIN' , 'SARALASIN' , 'PRAMLINTIDE' , 'IPAMORELIN' , 'Ipafricept' , 'Enfortumab (human mab
                    # )' , 'Fletikumab (human mab)' , 'Polatuzumab vedotin (humanized mab)' , 'Andexanet alfa' , 'COSYNT
                    # ROPIN'
                    'helm_notation': 'TEXT',
                    # EXAMPLES:
                    # 'PEPTIDE1{[dF].P.R.P.G.G.G.G.N.G.D.F.E.E.I.P.E.E.Y.L}$$$$' , 'PEPTIDE1{[Sar].R.V.Y.V.H.P.A}$$$$' ,
                    #  'PEPTIDE1{K.C.N.T.A.T.C.A.T.Q.R.L.A.N.F.L.V.H.S.S.N.N.F.G.P.I.L.P.P.T.N.V.G.S.N.T.Y.[am]}$PEPTIDE
                    # 1,PEPTIDE1,7:R3-2:R3$$$' , 'PEPTIDE1{[Aib].H.[dNal].[dF].K.[am]}$$$$' , 'PEPTIDE1{D.I.Q.M.T.Q.S.P.
                    # S.S.V.S.A.S.V.G.D.R.V.T.I.T.C.R.A.S.Q.G.I.S.G.W.L.A.W.Y.Q.Q.K.P.G.K.A.P.K.F.L.I.Y.A.A.S.T.L.Q.S.G.
                    # V.P.S.R.F.S.G.S.G.S.G.T.D.F.T.L.T.I.S.S.L.Q.P.E.D.F.A.T.Y.Y.C.Q.Q.A.N.S.F.P.P.T.F.G.G.G.T.K.V.E.I.
                    # K.R.T.V.A.A.P.S.V.F.I.F.P.P.S.D.E.Q.L.K.S.G.T.A.S.V.V.C.L.L.N.N.F.Y.P.R.E.A.K.V.Q.W.K.V.D.N.A.L.Q.
                    # S.G.N.S.Q.E.S.V.T.E.Q.D.S.K.D.S.T.Y.S.L.S.S.T.L.T.L.S.K.A.D.Y.E.K.H.K.V.Y.A.C.E.V.T.H.Q.G.L.S.S.P.
                    # V.T.K.S.F.N.R.G.E.C}|PEPTIDE2{E.V.Q.L.V.E.S.G.G.G.L.V.Q.P.G.G.S.L.R.L.S.C.A.A.S.G.F.T.F.S.S.Y.N.M.
                    # N.W.V.R.Q.A.P.G.K.G.L.E.W.V.S.Y.I.S.S.S.S.S.T.I.Y.Y.A.D.S.V.K.G.R.F.T.I.S.R.D.N.A.K.N.S.L.S.L.Q.M.
                    # N.S.L.R.D.E.D.T.A.V.Y.Y.C.A.R.A.Y.Y.Y.G.M.D.V.W.G.Q.G.T.T.V.T.V.S.S.A.S.T.K.G.P.S.V.F.P.L.A.P.S.S.
                    # K.S.T.S.G.G.T.A.A.L.G.C.L.V.K.D.Y.F.P.E.P.V.T.V.S.W.N.S.G.A.L.T.S.G.V.H.T.F.P.A.V.L.Q.S.S.G.L.Y.S.
                    # L.S.S.V.V.T.V.P.S.S.S.L.G.T.Q.T.Y.I.C.N.V.N.H.K.P.S.N.T.K.V.D.K.R.V.E.P.K.S.C.D.K.T.H.T.C.P.P.C.P.
                    # A.P.E.L.L.G.G.P.S.V.F.L.F.P.P.K.P.K.D.T.L.M.I.S.R.T.P.E.V.T.C.V.V.V.D.V.S.H.E.D.P.E.V.K.F.N.W.Y.V.
                    # D.G.V.E.V.H.N.A.K.T.K.P.R.E.E.Q.Y.N.S.T.Y.R.V.V.S.V.L.T.V.L.H.Q.D.W.L.N.G.K.E.Y.K.C.K.V.S.N.K.A.L.
                    # P.A.P.I.E.K.T.I.S.K.A.K.G.Q.P.R.E.P.Q.V.Y.T.L.P.P.S.R.E.E.M.T.K.N.Q.V.S.L.T.C.L.V.K.G.F.Y.P.S.D.I.
                    # A.V.E.W.E.S.N.G.Q.P.E.N.N.Y.K.T.T.P.P.V.L.D.S.D.G.S.F.F.L.Y.S.K.L.T.V.D.K.S.R.W.Q.Q.G.N.V.F.S.C.S.
                    # V.M.H.E.A.L.H.N.H.Y.T.Q.K.S.L.S.L.S.P.G.K}|PEPTIDE3{E.V.Q.L.V.E.S.G.G.G.L.V.Q.P.G.G.S.L.R.L.S.C.A.
                    # A.S.G.F.T.F.S.S.Y.N.M.N.W.V.R.Q.A.P.G.K.G.L.E.W.V.S.Y.I.S.S.S.S.S.T.I.Y.Y.A.D.S.V.K.G.R.F.T.I.S.R.
                    # D.N.A.K.N.S.L.S.L.Q.M.N.S.L.R.D.E.D.T.A.V.Y.Y.C.A.R.A.Y.Y.Y.G.M.D.V.W.G.Q.G.T.T.V.T.V.S.S.A.S.T.K.
                    # G.P.S.V.F.P.L.A.P.S.S.K.S.T.S.G.G.T.A.A.L.G.C.L.V.K.D.Y.F.P.E.P.V.T.V.S.W.N.S.G.A.L.T.S.G.V.H.T.F.
                    # P.A.V.L.Q.S.S.G.L.Y.S.L.S.S.V.V.T.V.P.S.S.S.L.G.T.Q.T.Y.I.C.N.V.N.H.K.P.S.N.T.K.V.D.K.R.V.E.P.K.S.
                    # C.D.K.T.H.T.C.P.P.C.P.A.P.E.L.L.G.G.P.S.V.F.L.F.P.P.K.P.K.D.T.L.M.I.S.R.T.P.E.V.T.C.V.V.V.D.V.S.H.
                    # E.D.P.E.V.K.F.N.W.Y.V.D.G.V.E.V.H.N.A.K.T.K.P.R.E.E.Q.Y.N.S.T.Y.R.V.V.S.V.L.T.V.L.H.Q.D.W.L.N.G.K.
                    # E.Y.K.C.K.V.S.N.K.A.L.P.A.P.I.E.K.T.I.S.K.A.K.G.Q.P.R.E.P.Q.V.Y.T.L.P.P.S.R.E.E.M.T.K.N.Q.V.S.L.T.
                    # C.L.V.K.G.F.Y.P.S.D.I.A.V.E.W.E.S.N.G.Q.P.E.N.N.Y.K.T.T.P.P.V.L.D.S.D.G.S.F.F.L.Y.S.K.L.T.V.D.K.S.
                    # R.W.Q.Q.G.N.V.F.S.C.S.V.M.H.E.A.L.H.N.H.Y.T.Q.K.S.L.S.L.S.P.G.K}|PEPTIDE4{D.I.Q.M.T.Q.S.P.S.S.V.S.
                    # A.S.V.G.D.R.V.T.I.T.C.R.A.S.Q.G.I.S.G.W.L.A.W.Y.Q.Q.K.P.G.K.A.P.K.F.L.I.Y.A.A.S.T.L.Q.S.G.V.P.S.R.
                    # F.S.G.S.G.S.G.T.D.F.T.L.T.I.S.S.L.Q.P.E.D.F.A.T.Y.Y.C.Q.Q.A.N.S.F.P.P.T.F.G.G.G.T.K.V.E.I.K.R.T.V.
                    # A.A.P.S.V.F.I.F.P.P.S.D.E.Q.L.K.S.G.T.A.S.V.V.C.L.L.N.N.F.Y.P.R.E.A.K.V.Q.W.K.V.D.N.A.L.Q.S.G.N.S.
                    # Q.E.S.V.T.E.Q.D.S.K.D.S.T.Y.S.L.S.S.T.L.T.L.S.K.A.D.Y.E.K.H.K.V.Y.A.C.E.V.T.H.Q.G.L.S.S.P.V.T.K.S.
                    # F.N.R.G.E.C}$PEPTIDE2,PEPTIDE3,229:R3-229:R3|PEPTIDE2,PEPTIDE2,367:R3-425:R3|PEPTIDE2,PEPTIDE3,226
                    # :R3-226:R3|PEPTIDE3,PEPTIDE3,261:R3-321:R3|PEPTIDE3,PEPTIDE4,220:R3-214:R3|PEPTIDE2,PEPTIDE2,22:R3
                    # -96:R3|PEPTIDE3,PEPTIDE3,367:R3-425:R3|PEPTIDE1,PEPTIDE1,134:R3-194:R3|PEPTIDE4,PEPTIDE4,134:R3-19
                    # 4:R3|PEPTIDE4,PEPTIDE4,23:R3-88:R3|PEPTIDE1,PEPTIDE1,23:R3-88:R3|PEPTIDE3,PEPTIDE3,22:R3-96:R3|PEP
                    # TIDE3,PEPTIDE3,144:R3-200:R3|PEPTIDE2,PEPTIDE2,144:R3-200:R3|PEPTIDE2,PEPTIDE2,261:R3-321:R3|PEPTI
                    # DE2,PEPTIDE1,220:R3-214:R3$$$' , 'PEPTIDE1{S.Y.S.M.E.H.F.R.W.G.K.P.V.G.K.K.R.R.P.V.K.V.Y.P}$$$$' ,
                    #  'PEPTIDE1{R.Q.I.K.I.W.F.Q.N.R.R.M.K.W.K.K.[am]}$$$$' , 'PEPTIDE1{[ac].[dNal].[Phe(4-Cl)].W.S.Y.[X
                    # 17].L.R.P.[dA].[am]}$$$$' , 'PEPTIDE1{[Glp].E.Q.L.E.R.A.L.N.S.S}$$$$' , 'PEPTIDE1{S.N.L.S}|PEPTIDE
                    # 2{T.[Asu].V.L.G.K.L.S.Q.E.L.H.K.L.Q.T.Y.P.R.T.D.V.G.A.G.T.P.[am]}$PEPTIDE2,PEPTIDE1,2:R3-1:R1|PEPT
                    # IDE1,PEPTIDE2,4:R2-1:R1$$$'
                    'molecule_chembl_id': 'TEXT',
                    # EXAMPLES:
                    # 'CHEMBL3545191' , 'CHEMBL3545192' , 'CHEMBL2103749' , 'CHEMBL938' , 'CHEMBL2103758' , 'CHEMBL58547
                    # ' , 'CHEMBL3301577' , 'CHEMBL3301579' , 'CHEMBL3301580' , 'CHEMBL3301582'
                }
            },
            'black_box': 'BOOLEAN',
            # EXAMPLES:
            # 'False' , 'False' , 'False' , 'False' , 'False' , 'False' , 'False' , 'False' , 'False' , 'False'
            'black_box_warning': 'NUMERIC',
            # EXAMPLES:
            # '0' , '0' , '0' , '0' , '0' , '0' , '0' , '0' , '0' , '0'
            'chirality': 'NUMERIC',
            # EXAMPLES:
            # '1' , '1' , '1' , '1' , '2' , '1' , '1' , '2' , '1' , '1'
            'development_phase': 'NUMERIC',
            # EXAMPLES:
            # '3' , '0' , '3' , '0' , '0' , '1' , '1' , '0' , '3' , '1'
            'drug_type': 'NUMERIC',
            # EXAMPLES:
            # '6' , '1' , '1' , '6' , '1' , '1' , '1' , '1' , '1' , '1'
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
            'first_approval': 'NUMERIC',
            # EXAMPLES:
            # '1997' , '2004' , '1958' , '1961' , '1961' , '2000' , '1991' , '1982' , '2005' , '2019'
            'first_in_class': 'BOOLEAN',
            # EXAMPLES:
            # 'False' , 'False' , 'False' , 'False' , 'False' , 'False' , 'False' , 'False' , 'False' , 'False'
            'helm_notation': 'TEXT',
            # EXAMPLES:
            # 'PEPTIDE1{[dF].P.R.P.G.G.G.G.N.G.D.F.E.E.I.P.E.E.Y.L}$$$$' , 'PEPTIDE1{[Sar].R.V.Y.V.H.P.A}$$$$' , 'PEPTID
            # E1{K.C.N.T.A.T.C.A.T.Q.R.L.A.N.F.L.V.H.S.S.N.N.F.G.P.I.L.P.P.T.N.V.G.S.N.T.Y.[am]}$PEPTIDE1,PEPTIDE1,7:R3-
            # 2:R3$$$' , 'PEPTIDE1{[Aib].H.[dNal].[dF].K.[am]}$$$$' , 'PEPTIDE1{D.I.Q.M.T.Q.S.P.S.S.V.S.A.S.V.G.D.R.V.T.
            # I.T.C.R.A.S.Q.G.I.S.G.W.L.A.W.Y.Q.Q.K.P.G.K.A.P.K.F.L.I.Y.A.A.S.T.L.Q.S.G.V.P.S.R.F.S.G.S.G.S.G.T.D.F.T.L.
            # T.I.S.S.L.Q.P.E.D.F.A.T.Y.Y.C.Q.Q.A.N.S.F.P.P.T.F.G.G.G.T.K.V.E.I.K.R.T.V.A.A.P.S.V.F.I.F.P.P.S.D.E.Q.L.K.
            # S.G.T.A.S.V.V.C.L.L.N.N.F.Y.P.R.E.A.K.V.Q.W.K.V.D.N.A.L.Q.S.G.N.S.Q.E.S.V.T.E.Q.D.S.K.D.S.T.Y.S.L.S.S.T.L.
            # T.L.S.K.A.D.Y.E.K.H.K.V.Y.A.C.E.V.T.H.Q.G.L.S.S.P.V.T.K.S.F.N.R.G.E.C}|PEPTIDE2{E.V.Q.L.V.E.S.G.G.G.L.V.Q.
            # P.G.G.S.L.R.L.S.C.A.A.S.G.F.T.F.S.S.Y.N.M.N.W.V.R.Q.A.P.G.K.G.L.E.W.V.S.Y.I.S.S.S.S.S.T.I.Y.Y.A.D.S.V.K.G.
            # R.F.T.I.S.R.D.N.A.K.N.S.L.S.L.Q.M.N.S.L.R.D.E.D.T.A.V.Y.Y.C.A.R.A.Y.Y.Y.G.M.D.V.W.G.Q.G.T.T.V.T.V.S.S.A.S.
            # T.K.G.P.S.V.F.P.L.A.P.S.S.K.S.T.S.G.G.T.A.A.L.G.C.L.V.K.D.Y.F.P.E.P.V.T.V.S.W.N.S.G.A.L.T.S.G.V.H.T.F.P.A.
            # V.L.Q.S.S.G.L.Y.S.L.S.S.V.V.T.V.P.S.S.S.L.G.T.Q.T.Y.I.C.N.V.N.H.K.P.S.N.T.K.V.D.K.R.V.E.P.K.S.C.D.K.T.H.T.
            # C.P.P.C.P.A.P.E.L.L.G.G.P.S.V.F.L.F.P.P.K.P.K.D.T.L.M.I.S.R.T.P.E.V.T.C.V.V.V.D.V.S.H.E.D.P.E.V.K.F.N.W.Y.
            # V.D.G.V.E.V.H.N.A.K.T.K.P.R.E.E.Q.Y.N.S.T.Y.R.V.V.S.V.L.T.V.L.H.Q.D.W.L.N.G.K.E.Y.K.C.K.V.S.N.K.A.L.P.A.P.
            # I.E.K.T.I.S.K.A.K.G.Q.P.R.E.P.Q.V.Y.T.L.P.P.S.R.E.E.M.T.K.N.Q.V.S.L.T.C.L.V.K.G.F.Y.P.S.D.I.A.V.E.W.E.S.N.
            # G.Q.P.E.N.N.Y.K.T.T.P.P.V.L.D.S.D.G.S.F.F.L.Y.S.K.L.T.V.D.K.S.R.W.Q.Q.G.N.V.F.S.C.S.V.M.H.E.A.L.H.N.H.Y.T.
            # Q.K.S.L.S.L.S.P.G.K}|PEPTIDE3{E.V.Q.L.V.E.S.G.G.G.L.V.Q.P.G.G.S.L.R.L.S.C.A.A.S.G.F.T.F.S.S.Y.N.M.N.W.V.R.
            # Q.A.P.G.K.G.L.E.W.V.S.Y.I.S.S.S.S.S.T.I.Y.Y.A.D.S.V.K.G.R.F.T.I.S.R.D.N.A.K.N.S.L.S.L.Q.M.N.S.L.R.D.E.D.T.
            # A.V.Y.Y.C.A.R.A.Y.Y.Y.G.M.D.V.W.G.Q.G.T.T.V.T.V.S.S.A.S.T.K.G.P.S.V.F.P.L.A.P.S.S.K.S.T.S.G.G.T.A.A.L.G.C.
            # L.V.K.D.Y.F.P.E.P.V.T.V.S.W.N.S.G.A.L.T.S.G.V.H.T.F.P.A.V.L.Q.S.S.G.L.Y.S.L.S.S.V.V.T.V.P.S.S.S.L.G.T.Q.T.
            # Y.I.C.N.V.N.H.K.P.S.N.T.K.V.D.K.R.V.E.P.K.S.C.D.K.T.H.T.C.P.P.C.P.A.P.E.L.L.G.G.P.S.V.F.L.F.P.P.K.P.K.D.T.
            # L.M.I.S.R.T.P.E.V.T.C.V.V.V.D.V.S.H.E.D.P.E.V.K.F.N.W.Y.V.D.G.V.E.V.H.N.A.K.T.K.P.R.E.E.Q.Y.N.S.T.Y.R.V.V.
            # S.V.L.T.V.L.H.Q.D.W.L.N.G.K.E.Y.K.C.K.V.S.N.K.A.L.P.A.P.I.E.K.T.I.S.K.A.K.G.Q.P.R.E.P.Q.V.Y.T.L.P.P.S.R.E.
            # E.M.T.K.N.Q.V.S.L.T.C.L.V.K.G.F.Y.P.S.D.I.A.V.E.W.E.S.N.G.Q.P.E.N.N.Y.K.T.T.P.P.V.L.D.S.D.G.S.F.F.L.Y.S.K.
            # L.T.V.D.K.S.R.W.Q.Q.G.N.V.F.S.C.S.V.M.H.E.A.L.H.N.H.Y.T.Q.K.S.L.S.L.S.P.G.K}|PEPTIDE4{D.I.Q.M.T.Q.S.P.S.S.
            # V.S.A.S.V.G.D.R.V.T.I.T.C.R.A.S.Q.G.I.S.G.W.L.A.W.Y.Q.Q.K.P.G.K.A.P.K.F.L.I.Y.A.A.S.T.L.Q.S.G.V.P.S.R.F.S.
            # G.S.G.S.G.T.D.F.T.L.T.I.S.S.L.Q.P.E.D.F.A.T.Y.Y.C.Q.Q.A.N.S.F.P.P.T.F.G.G.G.T.K.V.E.I.K.R.T.V.A.A.P.S.V.F.
            # I.F.P.P.S.D.E.Q.L.K.S.G.T.A.S.V.V.C.L.L.N.N.F.Y.P.R.E.A.K.V.Q.W.K.V.D.N.A.L.Q.S.G.N.S.Q.E.S.V.T.E.Q.D.S.K.
            # D.S.T.Y.S.L.S.S.T.L.T.L.S.K.A.D.Y.E.K.H.K.V.Y.A.C.E.V.T.H.Q.G.L.S.S.P.V.T.K.S.F.N.R.G.E.C}$PEPTIDE2,PEPTID
            # E3,229:R3-229:R3|PEPTIDE2,PEPTIDE2,367:R3-425:R3|PEPTIDE2,PEPTIDE3,226:R3-226:R3|PEPTIDE3,PEPTIDE3,261:R3-
            # 321:R3|PEPTIDE3,PEPTIDE4,220:R3-214:R3|PEPTIDE2,PEPTIDE2,22:R3-96:R3|PEPTIDE3,PEPTIDE3,367:R3-425:R3|PEPTI
            # DE1,PEPTIDE1,134:R3-194:R3|PEPTIDE4,PEPTIDE4,134:R3-194:R3|PEPTIDE4,PEPTIDE4,23:R3-88:R3|PEPTIDE1,PEPTIDE1
            # ,23:R3-88:R3|PEPTIDE3,PEPTIDE3,22:R3-96:R3|PEPTIDE3,PEPTIDE3,144:R3-200:R3|PEPTIDE2,PEPTIDE2,144:R3-200:R3
            # |PEPTIDE2,PEPTIDE2,261:R3-321:R3|PEPTIDE2,PEPTIDE1,220:R3-214:R3$$$' , 'PEPTIDE1{S.Y.S.M.E.H.F.R.W.G.K.P.V
            # .G.K.K.R.R.P.V.K.V.Y.P}$$$$' , 'PEPTIDE1{R.Q.I.K.I.W.F.Q.N.R.R.M.K.W.K.K.[am]}$$$$' , 'PEPTIDE1{[ac].[dNal
            # ].[Phe(4-Cl)].W.S.Y.[X17].L.R.P.[dA].[am]}$$$$' , 'PEPTIDE1{[Glp].E.Q.L.E.R.A.L.N.S.S}$$$$' , 'PEPTIDE1{S.
            # N.L.S}|PEPTIDE2{T.[Asu].V.L.G.K.L.S.Q.E.L.H.K.L.Q.T.Y.P.R.T.D.V.G.A.G.T.P.[am]}$PEPTIDE2,PEPTIDE1,2:R3-1:R
            # 1|PEPTIDE1,PEPTIDE2,4:R2-1:R1$$$'
            'indication_class': 'TEXT',
            # EXAMPLES:
            # 'Amino Acid' , 'Amino Acid' , 'Antibacterial' , 'Amino Acid' , 'Amino Acid' , 'Antibacterial' , 'Antihyper
            # tensive; Diuretic' , 'Antagonist (to histamine-H2 receptors)' , 'Anesthetic (inhalation)' , 'Vitamin (hema
            # topoietic)'
            'molecule_chembl_id': 'TEXT',
            # EXAMPLES:
            # 'CHEMBL3545191' , 'CHEMBL2104246' , 'CHEMBL301523' , 'CHEMBL3545192' , 'CHEMBL2104247' , 'CHEMBL294029' , 
            # 'CHEMBL3545193' , 'CHEMBL2104248' , 'CHEMBL291962' , 'CHEMBL3545194'
            'molecule_properties': 
            {
                'properties': 
                {
                    'alogp': 'NUMERIC',
                    # EXAMPLES:
                    # '0.06' , '0.64' , '5.29' , '4.24' , '3.99' , '0.44' , '2.04' , '-0.17' , '5.67' , '1.12'
                    'aromatic_rings': 'NUMERIC',
                    # EXAMPLES:
                    # '1' , '1' , '3' , '4' , '3' , '0' , '3' , '1' , '3' , '2'
                    'cx_logd': 'NUMERIC',
                    # EXAMPLES:
                    # '0.32' , '-1.19' , '5.46' , '4.14' , '0.83' , '-1.59' , '2.09' , '-3.70' , '6.51' , '-1.09'
                    'cx_logp': 'NUMERIC',
                    # EXAMPLES:
                    # '-0.62' , '-1.18' , '5.46' , '4.14' , '4.43' , '-1.59' , '2.09' , '-0.89' , '6.51' , '-1.09'
                    'cx_most_apka': 'NUMERIC',
                    # EXAMPLES:
                    # '6.37' , '2.47' , '12.67' , '3.49' , '2.79' , '2.73' , '2.54' , '1.94' , '12.70' , '8.85'
                    'cx_most_bpka': 'NUMERIC',
                    # EXAMPLES:
                    # '2.08' , '9.45' , '1.73' , '2.32' , '9.52' , '3.74' , '3.61' , '9.40' , '8.02' , '11.33'
                    'full_molformula': 'TEXT',
                    # EXAMPLES:
                    # 'C9H16N4O' , 'C9H11NO2' , 'C17H11Br2NO2' , 'C22H17F2N5OS' , 'C20H14O4' , 'C6H13NO2' , 'C15H14N4O' 
                    # , 'C14H13N5O5S2' , 'C27H25ClN2O4' , 'C11H12N2O2'
                    'full_mwt': 'NUMERIC',
                    # EXAMPLES:
                    # '196.25' , '165.19' , '421.09' , '437.48' , '318.33' , '131.18' , '266.30' , '395.42' , '476.96' ,
                    #  '204.23'
                    'hba': 'NUMERIC',
                    # EXAMPLES:
                    # '4' , '2' , '3' , '7' , '3' , '2' , '5' , '9' , '4' , '2'
                    'hba_lipinski': 'NUMERIC',
                    # EXAMPLES:
                    # '5' , '3' , '3' , '6' , '4' , '3' , '5' , '10' , '6' , '4'
                    'hbd': 'NUMERIC',
                    # EXAMPLES:
                    # '1' , '2' , '0' , '1' , '2' , '2' , '1' , '4' , '0' , '3'
                    'hbd_lipinski': 'NUMERIC',
                    # EXAMPLES:
                    # '1' , '3' , '0' , '1' , '2' , '3' , '1' , '5' , '0' , '4'
                    'heavy_atoms': 'NUMERIC',
                    # EXAMPLES:
                    # '14' , '12' , '22' , '31' , '24' , '9' , '20' , '26' , '34' , '15'
                    'molecular_species': 'TEXT',
                    # EXAMPLES:
                    # 'ACID' , 'ZWITTERION' , 'NEUTRAL' , 'NEUTRAL' , 'ACID' , 'ZWITTERION' , 'NEUTRAL' , 'ACID' , 'ZWIT
                    # TERION' , 'NEUTRAL'
                    'mw_freebase': 'NUMERIC',
                    # EXAMPLES:
                    # '196.25' , '165.19' , '421.09' , '437.48' , '318.33' , '131.18' , '266.30' , '395.42' , '476.96' ,
                    #  '204.23'
                    'mw_monoisotopic': 'NUMERIC',
                    # EXAMPLES:
                    # '196.1324' , '165.0790' , '418.9157' , '437.1122' , '318.0892' , '131.0946' , '266.1168' , '395.03
                    # 58' , '476.1503' , '204.0899'
                    'num_lipinski_ro5_violations': 'NUMERIC',
                    # EXAMPLES:
                    # '0' , '0' , '1' , '0' , '0' , '0' , '0' , '0' , '1' , '0'
                    'num_ro5_violations': 'NUMERIC',
                    # EXAMPLES:
                    # '0' , '0' , '1' , '0' , '0' , '0' , '0' , '0' , '1' , '0'
                    'psa': 'NUMERIC',
                    # EXAMPLES:
                    # '57.00' , '63.32' , '39.19' , '87.62' , '74.60' , '63.32' , '63.83' , '158.21' , '66.92' , '79.11'
                    'qed_weighted': 'NUMERIC',
                    # EXAMPLES:
                    # '0.51' , '0.69' , '0.42' , '0.49' , '0.71' , '0.58' , '0.79' , '0.23' , '0.31' , '0.70'
                    'ro3_pass': 'TEXT',
                    # EXAMPLES:
                    # 'N' , 'N' , 'N' , 'N' , 'N' , 'N' , 'N' , 'N' , 'N' , 'N'
                    'rtb': 'NUMERIC',
                    # EXAMPLES:
                    # '1' , '3' , '2' , '6' , '4' , '3' , '3' , '5' , '8' , '3'
                }
            },
            'molecule_structures': 
            {
                'properties': 
                {
                    'canonical_smiles': 'TEXT',
                    # EXAMPLES:
                    # 'C[C@H]1CCC[C@@H](C)N1[n+]1[cH-]c(=N)on1' , 'N[C@@H](Cc1ccccc1)C(=O)O' , 'Cc1ccc2c(Br)cc(Br)c(OC(=
                    # O)c3ccccc3)c2n1' , 'C[C@@H](c1nc(-c2ccc(C#N)cc2)cs1)[C@](O)(Cn1cncn1)c1ccc(F)cc1F' , 'O=C(O)c1cccc
                    # c1C(=O)c1ccc(O)c(-c2ccccc2)c1' , 'CC(C)C[C@H](N)C(=O)O' , 'Cn1nc(-c2cccnc2)nc1-c1ccccc1CO' , 'C=CC
                    # 1=C(C(=O)O)N2C(=O)[C@@H](NC(=O)/C(=N\O)c3csc(N)n3)[C@H]2SC1' , 'CCCCC1(COC(=O)c2ccc(Cl)cc2)C(=O)N(
                    # c2ccccc2)N(c2ccccc2)C1=O' , 'N[C@@H](Cc1c[nH]c2ccccc12)C(=O)O'
                    'standard_inchi': 'TEXT',
                    # EXAMPLES:
                    # 'InChI=1S/C9H16N4O/c1-7-4-3-5-8(2)13(7)12-6-9(10)14-11-12/h6-8,10H,3-5H2,1-2H3/t7-,8+' , 'InChI=1S
                    # /C9H11NO2/c10-8(9(11)12)6-7-4-2-1-3-5-7/h1-5,8H,6,10H2,(H,11,12)/t8-/m0/s1' , 'InChI=1S/C17H11Br2N
                    # O2/c1-10-7-8-12-13(18)9-14(19)16(15(12)20-10)22-17(21)11-5-3-2-4-6-11/h2-9H,1H3' , 'InChI=1S/C22H1
                    # 7F2N5OS/c1-14(21-28-20(10-31-21)16-4-2-15(9-25)3-5-16)22(30,11-29-13-26-12-27-29)18-7-6-17(23)8-19
                    # (18)24/h2-8,10,12-14,30H,11H2,1H3/t14-,22+/m0/s1' , 'InChI=1S/C20H14O4/c21-18-11-10-14(12-17(18)13
                    # -6-2-1-3-7-13)19(22)15-8-4-5-9-16(15)20(23)24/h1-12,21H,(H,23,24)' , 'InChI=1S/C6H13NO2/c1-4(2)3-5
                    # (7)6(8)9/h4-5H,3,7H2,1-2H3,(H,8,9)/t5-/m0/s1' , 'InChI=1S/C15H14N4O/c1-19-15(13-7-3-2-5-12(13)10-2
                    # 0)17-14(18-19)11-6-4-8-16-9-11/h2-9,20H,10H2,1H3' , 'InChI=1S/C14H13N5O5S2/c1-2-5-3-25-12-8(11(21)
                    # 19(12)9(5)13(22)23)17-10(20)7(18-24)6-4-26-14(15)16-6/h2,4,8,12,24H,1,3H2,(H2,15,16)(H,17,20)(H,22
                    # ,23)/b18-7-/t8-,12-/m1/s1' , 'InChI=1S/C27H25ClN2O4/c1-2-3-18-27(19-34-24(31)20-14-16-21(28)17-15-
                    # 20)25(32)29(22-10-6-4-7-11-22)30(26(27)33)23-12-8-5-9-13-23/h4-17H,2-3,18-19H2,1H3' , 'InChI=1S/C1
                    # 1H12N2O2/c12-9(11(14)15)5-7-6-13-10-4-2-1-3-8(7)10/h1-4,6,9,13H,5,12H2,(H,14,15)/t9-/m0/s1'
                    'standard_inchi_key': 'TEXT',
                    # EXAMPLES:
                    # 'VBBUFAXMBDEROK-OCAPTIKFSA-N' , 'COLNVLDHVKWLRT-QMMMGPOBSA-N' , 'IJTPLVAAROHGGB-UHFFFAOYSA-N' , 'O
                    # PAHEYNNJWPQPX-RCDICMHDSA-N' , 'PKHPZNKXOBWFCX-UHFFFAOYSA-N' , 'ROHFNLRQFUQHCH-YFKPBYRVSA-N' , 'UDB
                    # QGHIODMCIFZ-UHFFFAOYSA-N' , 'RTXOFQZKPXMALH-GHXIOONMSA-N' , 'OZKQTMYKYQGCME-UHFFFAOYSA-N' , 'QIVBC
                    # DIJIAJPQS-VIFPVBQESA-N'
                }
            },
            'molecule_synonyms': 
            {
                'properties': 
                {
                    'molecule_synonym': 'TEXT',
                    # EXAMPLES:
                    # 'Evinacumab' , 'Darsidomine' , 'FEMA NO. 3585' , 'M9346A' , 'Brobenzoxaldine' , 'BMS-207147' , 'Ms
                    # c-2364447' , 'Fendizoate' , 'E641' , 'LGH447'
                    'syn_type': 'TEXT',
                    # EXAMPLES:
                    # 'INN' , 'INN' , 'RESEARCH_CODE' , 'RESEARCH_CODE' , 'OTHER' , 'RESEARCH_CODE' , 'OTHER' , 'INN' , 
                    # 'E_NUMBER' , 'RESEARCH_CODE'
                    'synonyms': 'TEXT',
                    # EXAMPLES:
                    # 'EVINACUMAB' , 'DARSIDOMINE' , 'FEMA NO. 3585' , 'M9346A' , 'BROBENZOXALDINE' , 'BMS-207147' , 'MS
                    # C-2364447' , 'FENDIZOATE' , 'E641' , 'LGH447'
                }
            },
            'ob_patent': 'TEXT',
            # EXAMPLES:
            # '7582727' , '6753445' , '6488962' , 'RE38551' , '6613355' , '6239180' , '8501758' , '8440715' , '7582621' 
            # , '6750237'
            'oral': 'BOOLEAN',
            # EXAMPLES:
            # 'False' , 'False' , 'False' , 'False' , 'False' , 'False' , 'False' , 'False' , 'False' , 'False'
            'parenteral': 'BOOLEAN',
            # EXAMPLES:
            # 'False' , 'False' , 'False' , 'False' , 'False' , 'False' , 'False' , 'False' , 'False' , 'False'
            'prodrug': 'BOOLEAN',
            # EXAMPLES:
            # 'False' , 'False' , 'False' , 'False' , 'False' , 'False' , 'False' , 'False' , 'False' , 'False'
            'research_codes': 'TEXT',
            # EXAMPLES:
            # 'REGN1500' , 'NSC-79477' , 'M9346A' , 'BMS-207147' , 'NSC-46709' , 'LGH447' , 'FK 482' , 'DP-4978' , 'AE-9
            # ' , 'NSC-13119'
            'rule_of_five': 'BOOLEAN',
            # EXAMPLES:
            # 'False' , 'True' , 'True' , 'False' , 'False' , 'True' , 'False' , 'True' , 'True' , 'False'
            'sc_patent': 'TEXT',
            # EXAMPLES:
            # 'US-7582727-B1' , 'US-6753445-B2' , 'US-6488962-B1' , 'US-RE38551-E1' , 'US-6613355-B2' , 'US-6239180-B1' 
            # , 'US-8501758-B2' , 'US-8440715-B2' , 'US-7582621-B2' , 'US-6750237-B1'
            'synonyms': 'TEXT',
            # EXAMPLES:
            # 'Evinacumab (INN, USAN)' , 'Darsidomine (INN)' , 'L-phenylalanine (JAN, USP)' , 'Mirvetuximab (INN, USAN)'
            #  , 'Broxaldine (DCF, INN)' , 'Ravuconazole (INN, MI)' , 'Msc-2364447' , 'Fendizoate (INN)' , 'L-leucine (J
            # AN, USP)' , 'Lgh-447'
            'topical': 'BOOLEAN',
            # EXAMPLES:
            # 'False' , 'False' , 'False' , 'False' , 'False' , 'False' , 'False' , 'False' , 'False' , 'False'
            'usan_stem': 'TEXT',
            # EXAMPLES:
            # '-mab; -vin-' , '-sidomine' , '-mab' , '-conazole' , 'cef-' , '-eridine' , '-azepam' , '-farnib' , '-tide'
            #  , '-sal-'
            'usan_stem_definition': 'TEXT',
            # EXAMPLES:
            # 'monoclonal antibodies: fully human, cardiovascular indications; vinca alkaloids' , 'antianginals (sydnone
            #  derivatives)' , 'monoclonal antibodies: chimeric, tumors as target' , 'systemic antifungals (miconazole t
            # ype)' , 'cephalosporins' , 'analgesics (meperidine type)' , 'antianxiety agents (diazepam type)' , 'farnes
            # yl transferase inhibitor' , 'peptides: neurologic indications' , 'anti-inflammatory agents (salicylic acid
            #  derivatives)'
            'usan_stem_substem': 'TEXT',
            # EXAMPLES:
            # '-mab(-mab (-cumab)); -vin-(-vin-)' , '-sidomine(-sidomine)' , '-mab(-mab (-tuximab))' , '-conazole(-conaz
            # ole)' , 'cef-(cef-)' , '-eridine(-eridine)' , '-azepam(-azepam)' , '-farnib(-farnib)' , '-tide(-tide (-net
            # ide))' , '-sal-(-sal-)'
            'usan_year': 'NUMERIC',
            # EXAMPLES:
            # '2014' , '1980' , '2015' , '1979' , '1991' , '1979' , '1979' , '2002' , '2002' , '1970'
            'withdrawn_class': 'TEXT',
            # EXAMPLES:
            # 'Hematological toxicity' , 'Hepatotoxicity' , 'Musculoskeletal toxicity; Nephrotoxicity' , 'Immune system 
            # toxicity' , 'Hepatotoxicity' , 'Hepatotoxicity; Nephrotoxicity' , 'Gastrotoxicity; Hepatotoxicity' , 'Derm
            # atological toxicity; Opthalmic toxicity' , 'Misuse' , 'Opthalmic toxicity'
            'withdrawn_country': 'TEXT',
            # EXAMPLES:
            # 'United Kingdom; Germany' , 'United Kingdom, Germany' , 'United States; United Kingdom; Spain' , 'Germany'
            #  , 'United Kingdom' , 'European Union; Canada; Ireland; Portugal; Australia' , 'United States' , 'Spain; G
            # ermany; France' , 'France; United States' , 'France'
            'withdrawn_flag': 'NUMERIC',
            # EXAMPLES:
            # '0' , '0' , '0' , '0' , '0' , '0' , '0' , '0' , '0' , '0'
            'withdrawn_reason': 'TEXT',
            # EXAMPLES:
            # 'Eosinophilic Myalgia Syndrome' , 'Guillan-Barre Syndrome, hepatotoxicity' , 'Flank pain, decreased kidney
            #  function' , 'Multi-Organ Toxicities' , 'Allergy' , 'Hepatotoxicity' , 'Serious, irreversible, and even fa
            # tal nephrotoxicity and hepatotoxicity' , 'Gastrointestinal Toxicity; Hepatotoxicity' , 'Cataracts, Alopeci
            # a, lchthyosis' , 'Misuse and abuse'
            'withdrawn_year': 'NUMERIC',
            # EXAMPLES:
            # '1989' , '1983' , '1987' , '1986' , '1983' , '1998' , '2001' , '1990' , '1962' , '1979'
        }
    }
