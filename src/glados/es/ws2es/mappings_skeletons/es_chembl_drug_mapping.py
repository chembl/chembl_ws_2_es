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
            # 'Mylan Pharmaceuticals Inc' , 'Perrigo R And D Co' , 'Bedford Laboratories Div Ben Venue Laboratories Inc'
            #  , 'Watson Laboratories Inc' , 'Cosette Pharmaceuticals Inc' , 'Pfizer Laboratories Div Pfizer Inc' , 'Fre
            # senius Kabi Anti Infectives Srl' , 'Mylan Pharmaceuticals Inc' , 'Merck Research Laboratories Div Merck Co
            #  Inc' , 'Mylan Pharmaceuticals Inc'
            'atc_classification': 
            {
                'properties': 
                {
                    'code': 'TEXT',
                    # EXAMPLES:
                    # 'C02CA01' , 'N07BA01' , 'S02AA16' , 'J01MB02' , 'C01EB03' , 'J01CG01' , 'J01CG02' , 'J01MA08' , 'S
                    # 02AA15' , 'J01MA06'
                    'description': 'TEXT',
                    # EXAMPLES:
                    # 'CARDIOVASCULAR SYSTEM: ANTIHYPERTENSIVES: ANTIADRENERGIC AGENTS, PERIPHERALLY ACTING: Alpha-adren
                    # oreceptor antagonists' , 'NERVOUS SYSTEM: OTHER NERVOUS SYSTEM DRUGS: DRUGS USED IN ADDICTIVE DISO
                    # RDERS: Drugs used in nicotine dependence' , 'SENSORY ORGANS: OTOLOGICALS: ANTIINFECTIVES: Antiinfe
                    # ctive' , 'ANTIINFECTIVES FOR SYSTEMIC USE: ANTIBACTERIALS FOR SYSTEMIC USE: QUINOLONE ANTIBACTERIA
                    # LS: Other quinolones' , 'CARDIOVASCULAR SYSTEM: CARDIAC THERAPY: OTHER CARDIAC PREPARATIONS: Other
                    #  cardiac preparation' , 'ANTIINFECTIVES FOR SYSTEMIC USE: ANTIBACTERIALS FOR SYSTEMIC USE: BETA-LA
                    # CTAM ANTIBACTERIALS, PENICILLINS: Beta-lactamase inhibitors' , 'ANTIINFECTIVES FOR SYSTEMIC USE: A
                    # NTIBACTERIALS FOR SYSTEMIC USE: BETA-LACTAM ANTIBACTERIALS, PENICILLINS: Beta-lactamase inhibitors
                    # ' , 'ANTIINFECTIVES FOR SYSTEMIC USE: ANTIBACTERIALS FOR SYSTEMIC USE: QUINOLONE ANTIBACTERIALS: F
                    # luoroquinolones' , 'SENSORY ORGANS: OTOLOGICALS: ANTIINFECTIVES: Antiinfective' , 'ANTIINFECTIVES 
                    # FOR SYSTEMIC USE: ANTIBACTERIALS FOR SYSTEMIC USE: QUINOLONE ANTIBACTERIALS: Fluoroquinolone'
                }
            },
            'availability_type': 'NUMERIC',
            # EXAMPLES:
            # '1' , '2' , '1' , '0' , '1' , '1' , '1' , '1' , '1' , '1'
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
                            # '6354' , '6484' , '6425' , '6526' , '6407' , '6530' , '6324' , '6509' , '6541' , '6345'
                            'component_type': 'TEXT',
                            # EXAMPLES:
                            # 'PROTEIN' , 'PROTEIN' , 'PROTEIN' , 'PROTEIN' , 'PROTEIN' , 'PROTEIN' , 'PROTEIN' , 'PROTE
                            # IN' , 'PROTEIN' , 'PROTEIN'
                            'description': 'TEXT',
                            # EXAMPLES:
                            # 'Mavrilimumab heavy chain' , 'Milatuzumab heavy chain' , 'Namilumab heavy chain' , 'Narnat
                            # umab heavy chain' , 'Necitumumab heavy chain' , 'Onartuzumab heavy chain' , 'Oportuzumab m
                            # onatox single chain variable fragment' , 'Panobacumab heavy chain' , 'Pegsunercept fusion 
                            # protein' , 'Ponezumab heavy chain'
                            'organism': 'TEXT',
                            # EXAMPLES:
                            # 'Homo sapiens' , 'Homo sapiens' , 'Homo sapiens' , 'Homo sapiens' , 'Homo sapiens' , 'Mus 
                            # musculus' , 'Homo sapiens' , 'Homo sapiens' , 'Homo sapiens' , 'Homo sapiens'
                            'sequence': 'TEXT',
                            # EXAMPLES:
                            # 'QVQLVQSGAEVKKPGASVKVSCKVSGYTLTELSIHWVRQAPGKGLEWMGGFDPEENEIVYAQRFQGRVTMTEDTSTDTAYMELSSLRSE
                            # DTAVYYCAIVGSFSPLTLGLWGQGTMVTVSSASTKGPSVFPLAPCSRSTSESTAALGCLVKDYFPEPVTVSWNSGALTSGVHTFPAVLQS
                            # SGLYSLSSVVTVPSSSLGTKTYTCNVDHKPSNTKVDKRVESKYGPPCPSCPAPEFLGGPSVFLFPPKPKDTLMISRTPEVTCVVVDVSQE
                            # DPEVQFNWYVDGVEVHNAKTKPREEQFNSTYRVVSVLTVLHQDWLNGKEYKCKVSNKGLPSSIEKTISKAKGQPREPQVYTLPPSQEEMT
                            # KNQVSLTCLVKGFYPSDIAVEWESNGQPENNYKTTPPVLDSDGSFFLYSRLTVDKSRWQEGNVFSCSVMHEALHNHYTQKSLSLSLGK' 
                            # , 'QVQLQQSGSELKKPGASVKVSCKASGYTFTNYGVNWIKQAPGQGLQWMGWINPNTGEPTFDDDFKGRFAFSLDTSVSTAYLQISSLK
                            # ADDTAVYFCSRSRGKNEAWFAYWGQGTLVTVSSASTKGPSVFPLAPSSKSTSGGTAALGCLVKDYFPEPVTVSWNSGALTSGVHTFPAVL
                            # QSSGLYSLSSVVTVPSSSLGTQTYICNVNHKPSNTKVDKRVEPKSCDKTHTCPPCPAPELLGGPSVFLFPPKPKDTLMISRTPEVTCVVV
                            # DVSHEDPEVKFNWYVDGVEVHNAKTKPREEQYNSTYRVVSVLTVLHQDWLNGKEYKCKVSNKALPAPIEKTISKAKGQPREPQVYTLPPS
                            # REEMTKNQVSLTCLVKGFYPSDIAVEWESNGQPENNYKTTPPVLDSDGSFFLYSKLTVDKSRWQQGNVFSCSVMHEALHNHYTQKSLSLS
                            # PGK' , 'QVQLVQSGAEVKKPGASVKVSCKAFGYPFTDYLLHWVRQAPGQGLEWVGWLNPYSGDTNYAQKFQGRVTMTRDTSISTAYME
                            # LSRLRSDDTAVYYCTRTTLISVYFDYWGQGTMVTVSSASTKGPSVFPLAPSSKSTSGGTAALGCLVKDYFPEPVTVSWNSGALTSGVHTF
                            # PAVLQSSGLYSLSSVVTVPSSSLGTQTYICNVNHKPSNTKVDKKVEPKSCDKTHTCPPCPAPELLGGPSVFLFPPKPKDTLMISRTPEVT
                            # CVVVDVSHEDPEVKFNWYVDGVEVHNAKTKPREEQYNSTYRVVSVLTVLHQDWLNGKEYKCKVSNKALPAPIEKTISKAKGQPREPQVYT
                            # LPPSRDELTKNQVSLTCLVKGFYPSDIAVEWESNGQPENNYKTTPPVLDSDGSFFLYSKLTVDKSRWQQGNVFSCSVMHEALHNHYTQKS
                            # LSLSPGK' , 'EVQLVESGGGLVQPGGSLRLSCAASGFTFSSYLMTWVRQAPGKGLEWVANIKQDGSEKYYVDSVKGRFTISRDNAKNS
                            # LNLQMNSLRAEDTAVYYCTRDGYSSGRHYGMDVWGQGTTVIVSSASTKGPSVFPLAPSSKSTSGGTAALGCLVKDYFPEPVTVSWNSGAL
                            # TSGVHTFPAVLQSSGLYSLSSVVTVPSSSLGTQTYICNVNHKPSNTKVDKRVEPKSCDKTHTCPPCPAPELLGGPSVFLFPPKPKDTLMI
                            # SRTPEVTCVVVDVSHEDPEVKFNWYVDGVEVHNAKTKPREEQYNSTYRVVSVLTVLHQDWLNGKEYKCKVSNKALPAPIEKTISKAKGQP
                            # REPQVYTLPPSREEMTKNQVSLTCLVKGFYPSDIAVEWESNGQPENNYKTTPPVLDSDGSFFLYSKLTVDKSRWQQGNVFSCSVMHEALH
                            # NHYTQKSLSLSPGK' , 'QVQLQESGPGLVKPSQTLSLTCTVSGGSISSGDYYWSWIRQPPGKGLEWIGYIYYSGSTDYNPSLKSRVTM
                            # SVDTSKNQFSLKVNSVTAADTAVYYCARVSIFGVGTFDYWGQGTLVTVSSASTKGPSVLPLAPSSKSTSGGTAALGCLVKDYFPEPVTVS
                            # WNSGALTSGVHTFPAVLQSSGLYSLSSVVTVPSSSLGTQTYICNVNHKPSNTKVDKRVEPKSCDKTHTCPPCPAPELLGGPSVFLFPPKP
                            # KDTLMISRTPEVTCVVVDVSHEDPEVKFNWYVDGVEVHNAKTKPREEQYNSTYRVVSVLTVLHQDWLNGKEYKCKVSNKALPAPIEKTIS
                            # KAKGQPREPQVYTLPPSREEMTKNQVSLTCLVKGFYPSDIAVEWESNGQPENNYKTTPPVLDSDGSFFLYSKLTVDKSRWQQGNVFSCSV
                            # MHEALHNHYTQKSLSLSPGK' , 'EVQLVESGGGLVQPGGSLRLSCAASGYTFTSYWLHWVRQAPGKGLEWVGMIDPSNSDTRFNPNFK
                            # DRFTISADTSKNTAYLQMNSLRAEDTAVYYCATYRSYVTPLDYWGQGTLVTVSSASTKGPSVFPLAPSSKSTSGGTAALGCLVKDYFPEP
                            # VTVSWNSGALTSGVHTFPAVLQSSGLYSLSSVVTVPSSSLGTQTYICNVNHKPSNTKVDKKVEPKSCDKTHTCPPCPAPELLGGPSVFLF
                            # PPKPKDTLMISRTPEVTCVVVDVSHEDPEVKFNWYVDGVEVHNAKTKPREEQYNSTYRVVSVLTVLHQDWLNGKEYKCKVSNKALPAPIE
                            # KTISKAKGQPREPQVYTLPPSREEMTKNQVSLSCAVKGFYPSDIAVEWESNGQPENNYKTTPPVLDSDGSFFLVSKLTVDKSRWQQGNVF
                            # SCSVMHEALHNHYTQKSLSLSPGK' , 'HHHHHHDIQMTQSPSSLSASVGDRVTITCRSTKSLLHSNGITYLYWYQQKPGKAPKLLIYQ
                            # MSNLASGVPSRFSSSGSGTDFTLTISSLQPEDFATYYCAQNLEIPRTFGQGTKVELKRATPSHNSHQVPSAGGPTANSGTSGSEVQLVQS
                            # GPGLVQPGGSVRISCAASGYTFTNYGMNWVKQAPGKGLEWMGWINTYTGESTYADSFKGRFTFSLDTSASAAYLQINSLRAEDTAVYYCA
                            # RFAIKGDYWGQGTLLTVSSEFGGAPEFPKPSTPPGSSGLEGGSLAALTAHQACHLPLETFTRHRQPRGWEQLEQCGYPVQRLVALYLAAR
                            # LSWNQVDQVIRNALASPGSGGDLGEAIREQPEQARLALTLAAAESERFVRQGTGNDEAGAASADVVSLTCPVAAGECAGPADSGDALLER
                            # NYPTGAEFLGDGGDVSFSTRGTQNWTVERLLQAHRQLEERGYVFVGYHGTFLEAAQSIVFGGVRARSQDLDAIWRGFYIAGDPALAYGYA
                            # QDQEPDARGRIRNGALLRVYVPRSSLPGFYRTGLTLAAPEAAGEVERLIGHPLPLRLDAITGPEEEGGRLETILGWPLAERTVVIPSAIP
                            # TDPRNVGGDLDPSSIPDKEQAISALPDYASQPGKPPHHHHHHKDEL' , 'EEQVVESGGGFVQPGGSLRLSCAASGFTFSPYWMHWVRQ
                            # APGKGLVWVSRINSDGSTYYADSVKGRFTISRDNARNTLYLQMNSLRAEDTAVYYCARDRYYGPEMWGQGTMVTVSSGSASAPTLFPLVS
                            # CENSPSDTSSVAVGCLAQDFLPDSITFSWKYKNNSDISSTRGFPSVLRGGKYAATSQVLLPSKDVMQGTDEHVVCKVQHPNGNKEKNVPL
                            # PVIAELPPKVSVFVPPRDGFFGNPRKSKLICQATGFSPRQIQVSWLREGKQVGSGVTTDQVQAEAKESGPTTYKVTSTLTIKESDWLSQS
                            # MFTCRVDHRGLTFQQNASSMCVPDQDTAIRVFAIPPSFASIFLTKSTKLTCLVTDLTTYDSVTISWTRQNGEAVKTHTNISESHPNATFS
                            # AVGEASICEDDWNSGERFTCTVTHTDLPSPLKQTISRPKGVALHRPDVYLLPPAREQLNLRESATITCLVTGFSPADVFVQWMQRGQPLS
                            # PEKYVTSAPMPEPQAPGRYFAHSILTVSEEEWNTGETYTCVVAHEALPNRVTERTVDKSTGKPTLYNVSLVMSDTAGTCY' , 'MDSVC
                            # PQGKYIHPQNNSICCTKCHKGTYLYNDCPGPGQDTDCRECESGSFTASENHLRHCLSCSKCRKEMGQVEISSCTVDRDTVCGCRKNQYRH
                            # YWSENLFQCFN' , 'QVQLVQSGAEVKKPGASVKVSCKASGYYTEAYYIHWVRQAPGQGLEWMGRIDPATGNTKYAPRLQDRVTMTRDT
                            # STSTVYMELSSLRSEDTAVYYCASLYSLPVYWGQGTTVTVSSASTKGPSVFPLAPCSRSTSESTAALGCLVKDYFPEPVTVSWNSGALTS
                            # GVHTFPAVLQSSGLYSLSSVVTVPSSNFGTQTYTCNVDHKPSNTKVDKTVERKCCVECPPCPAPPVAGPSVFLFPPKPKDTLMISRTPEV
                            # TCVVVDVSHEDPEVQFNWYVDGVEVHNAKTKPREEQFNSTFRVVSVLTVVHQDWLNGKEYKCKVSNKGLPSSIEKTISKTKGQPREPQVY
                            # TLPPSREEMTKNQVSLTCLVKGFYPSDIAVEWESNGQPENNYKTTPPMLDSDGSFFLYSKLTVDKSRWQQGNVFSCSVMHEALHNHYTQK
                            # SLSLSPGK'
                            'tax_id': 'NUMERIC',
                            # EXAMPLES:
                            # '9606' , '9606' , '9606' , '9606' , '9606' , '10090' , '9606' , '9606' , '9606' , '9606'
                        }
                    },
                    'description': 'TEXT',
                    # EXAMPLES:
                    # 'Mavrilimumab (human mab)' , 'Milatuzumab (humanized mab)' , 'Namilumab (human mab)' , 'Narnatumab
                    #  (human mab)' , 'Necitumumab (human mab)' , 'Onartuzumab (humanized mab)' , 'Oportuzumab monatox (
                    # humanized scFv)' , 'Panobacumab (human mab)' , 'Pegsunercept (immunoadhesin)' , 'Ponezumab (humani
                    # zed mab)'
                    'helm_notation': 'TEXT',
                    # EXAMPLES:
                    # 'PEPTIDE1{D.I.Q.L.T.Q.S.P.L.S.L.P.V.T.L.G.Q.P.A.S.I.S.C.R.S.S.Q.S.L.V.H.R.N.G.N.T.Y.L.H.W.F.Q.Q.R.
                    # P.G.Q.S.P.R.L.L.I.Y.T.V.S.N.R.F.S.G.V.P.D.R.F.S.G.S.G.S.G.T.D.F.T.L.K.I.S.R.V.E.A.E.D.V.G.V.Y.F.C.
                    # S.Q.S.S.H.V.P.P.T.F.G.A.G.T.R.L.E.I.K.R.T.V.A.A.P.S.V.F.I.F.P.P.S.D.E.Q.L.K.S.G.T.A.S.V.V.C.L.L.N.
                    # N.F.Y.P.R.E.A.K.V.Q.W.K.V.D.N.A.L.Q.S.G.N.S.Q.E.S.V.T.E.Q.D.S.K.D.S.T.Y.S.L.S.S.T.L.T.L.S.K.A.D.Y.
                    # E.K.H.K.V.Y.A.C.E.V.T.H.Q.G.L.S.S.P.V.T.K.S.F.N.R.G.E.C}|PEPTIDE2{Q.V.Q.L.Q.Q.S.G.S.E.L.K.K.P.G.A.
                    # S.V.K.V.S.C.K.A.S.G.Y.T.F.T.N.Y.G.V.N.W.I.K.Q.A.P.G.Q.G.L.Q.W.M.G.W.I.N.P.N.T.G.E.P.T.F.D.D.D.F.K.
                    # G.R.F.A.F.S.L.D.T.S.V.S.T.A.Y.L.Q.I.S.S.L.K.A.D.D.T.A.V.Y.F.C.S.R.S.R.G.K.N.E.A.W.F.A.Y.W.G.Q.G.T.
                    # L.V.T.V.S.S.A.S.T.K.G.P.S.V.F.P.L.A.P.S.S.K.S.T.S.G.G.T.A.A.L.G.C.L.V.K.D.Y.F.P.E.P.V.T.V.S.W.N.S.
                    # G.A.L.T.S.G.V.H.T.F.P.A.V.L.Q.S.S.G.L.Y.S.L.S.S.V.V.T.V.P.S.S.S.L.G.T.Q.T.Y.I.C.N.V.N.H.K.P.S.N.T.
                    # K.V.D.K.R.V.E.P.K.S.C.D.K.T.H.T.C.P.P.C.P.A.P.E.L.L.G.G.P.S.V.F.L.F.P.P.K.P.K.D.T.L.M.I.S.R.T.P.E.
                    # V.T.C.V.V.V.D.V.S.H.E.D.P.E.V.K.F.N.W.Y.V.D.G.V.E.V.H.N.A.K.T.K.P.R.E.E.Q.Y.N.S.T.Y.R.V.V.S.V.L.T.
                    # V.L.H.Q.D.W.L.N.G.K.E.Y.K.C.K.V.S.N.K.A.L.P.A.P.I.E.K.T.I.S.K.A.K.G.Q.P.R.E.P.Q.V.Y.T.L.P.P.S.R.E.
                    # E.M.T.K.N.Q.V.S.L.T.C.L.V.K.G.F.Y.P.S.D.I.A.V.E.W.E.S.N.G.Q.P.E.N.N.Y.K.T.T.P.P.V.L.D.S.D.G.S.F.F.
                    # L.Y.S.K.L.T.V.D.K.S.R.W.Q.Q.G.N.V.F.S.C.S.V.M.H.E.A.L.H.N.H.Y.T.Q.K.S.L.S.L.S.P.G.K}|PEPTIDE3{Q.V.
                    # Q.L.Q.Q.S.G.S.E.L.K.K.P.G.A.S.V.K.V.S.C.K.A.S.G.Y.T.F.T.N.Y.G.V.N.W.I.K.Q.A.P.G.Q.G.L.Q.W.M.G.W.I.
                    # N.P.N.T.G.E.P.T.F.D.D.D.F.K.G.R.F.A.F.S.L.D.T.S.V.S.T.A.Y.L.Q.I.S.S.L.K.A.D.D.T.A.V.Y.F.C.S.R.S.R.
                    # G.K.N.E.A.W.F.A.Y.W.G.Q.G.T.L.V.T.V.S.S.A.S.T.K.G.P.S.V.F.P.L.A.P.S.S.K.S.T.S.G.G.T.A.A.L.G.C.L.V.
                    # K.D.Y.F.P.E.P.V.T.V.S.W.N.S.G.A.L.T.S.G.V.H.T.F.P.A.V.L.Q.S.S.G.L.Y.S.L.S.S.V.V.T.V.P.S.S.S.L.G.T.
                    # Q.T.Y.I.C.N.V.N.H.K.P.S.N.T.K.V.D.K.R.V.E.P.K.S.C.D.K.T.H.T.C.P.P.C.P.A.P.E.L.L.G.G.P.S.V.F.L.F.P.
                    # P.K.P.K.D.T.L.M.I.S.R.T.P.E.V.T.C.V.V.V.D.V.S.H.E.D.P.E.V.K.F.N.W.Y.V.D.G.V.E.V.H.N.A.K.T.K.P.R.E.
                    # E.Q.Y.N.S.T.Y.R.V.V.S.V.L.T.V.L.H.Q.D.W.L.N.G.K.E.Y.K.C.K.V.S.N.K.A.L.P.A.P.I.E.K.T.I.S.K.A.K.G.Q.
                    # P.R.E.P.Q.V.Y.T.L.P.P.S.R.E.E.M.T.K.N.Q.V.S.L.T.C.L.V.K.G.F.Y.P.S.D.I.A.V.E.W.E.S.N.G.Q.P.E.N.N.Y.
                    # K.T.T.P.P.V.L.D.S.D.G.S.F.F.L.Y.S.K.L.T.V.D.K.S.R.W.Q.Q.G.N.V.F.S.C.S.V.M.H.E.A.L.H.N.H.Y.T.Q.K.S.
                    # L.S.L.S.P.G.K}|PEPTIDE4{D.I.Q.L.T.Q.S.P.L.S.L.P.V.T.L.G.Q.P.A.S.I.S.C.R.S.S.Q.S.L.V.H.R.N.G.N.T.Y.
                    # L.H.W.F.Q.Q.R.P.G.Q.S.P.R.L.L.I.Y.T.V.S.N.R.F.S.G.V.P.D.R.F.S.G.S.G.S.G.T.D.F.T.L.K.I.S.R.V.E.A.E.
                    # D.V.G.V.Y.F.C.S.Q.S.S.H.V.P.P.T.F.G.A.G.T.R.L.E.I.K.R.T.V.A.A.P.S.V.F.I.F.P.P.S.D.E.Q.L.K.S.G.T.A.
                    # S.V.V.C.L.L.N.N.F.Y.P.R.E.A.K.V.Q.W.K.V.D.N.A.L.Q.S.G.N.S.Q.E.S.V.T.E.Q.D.S.K.D.S.T.Y.S.L.S.S.T.L.
                    # T.L.S.K.A.D.Y.E.K.H.K.V.Y.A.C.E.V.T.H.Q.G.L.S.S.P.V.T.K.S.F.N.R.G.E.C}$PEPTIDE4,PEPTIDE4,23:R3-93:
                    # R3|PEPTIDE2,PEPTIDE3,232:R3-232:R3|PEPTIDE3,PEPTIDE3,22:R3-96:R3|PEPTIDE2,PEPTIDE2,147:R3-203:R3|P
                    # EPTIDE2,PEPTIDE2,370:R3-428:R3|PEPTIDE3,PEPTIDE3,147:R3-203:R3|PEPTIDE3,PEPTIDE3,370:R3-428:R3|PEP
                    # TIDE1,PEPTIDE1,23:R3-93:R3|PEPTIDE3,PEPTIDE3,264:R3-324:R3|PEPTIDE2,PEPTIDE2,22:R3-96:R3|PEPTIDE2,
                    # PEPTIDE2,264:R3-324:R3|PEPTIDE3,PEPTIDE4,223:R3-219:R3|PEPTIDE2,PEPTIDE1,223:R3-219:R3|PEPTIDE4,PE
                    # PTIDE4,139:R3-199:R3|PEPTIDE2,PEPTIDE3,229:R3-229:R3|PEPTIDE1,PEPTIDE1,139:R3-199:R3$$$' , 'PEPTID
                    # E1{D.I.Q.M.T.Q.S.P.S.S.V.S.A.S.V.G.D.R.V.T.I.A.C.R.A.S.Q.N.I.R.N.I.L.N.W.Y.Q.Q.R.P.G.K.A.P.Q.L.L.I
                    # .Y.A.A.S.N.L.Q.S.G.V.P.S.R.F.S.G.S.G.S.G.T.D.F.T.L.T.I.N.S.L.Q.P.E.D.F.A.T.Y.Y.C.Q.Q.S.Y.S.M.P.R.T
                    # .F.G.G.G.T.K.L.E.I.K.R.T.V.A.A.P.S.V.F.I.F.P.P.S.D.E.Q.L.K.S.G.T.A.S.V.V.C.L.L.N.N.F.Y.P.R.E.A.K.V
                    # .Q.W.K.V.D.N.A.L.Q.S.G.N.S.Q.E.S.V.T.E.Q.D.S.K.D.S.T.Y.S.L.S.S.T.L.T.L.S.K.A.D.Y.E.K.H.K.V.Y.A.C.E
                    # .V.T.H.Q.G.L.S.S.P.V.T.K.S.F.N.R.G.E.C}|PEPTIDE2{Q.V.Q.L.V.Q.S.G.A.E.V.K.K.P.G.A.S.V.K.V.S.C.K.A.F
                    # .G.Y.P.F.T.D.Y.L.L.H.W.V.R.Q.A.P.G.Q.G.L.E.W.V.G.W.L.N.P.Y.S.G.D.T.N.Y.A.Q.K.F.Q.G.R.V.T.M.T.R.D.T
                    # .S.I.S.T.A.Y.M.E.L.S.R.L.R.S.D.D.T.A.V.Y.Y.C.T.R.T.T.L.I.S.V.Y.F.D.Y.W.G.Q.G.T.M.V.T.V.S.S.A.S.T.K
                    # .G.P.S.V.F.P.L.A.P.S.S.K.S.T.S.G.G.T.A.A.L.G.C.L.V.K.D.Y.F.P.E.P.V.T.V.S.W.N.S.G.A.L.T.S.G.V.H.T.F
                    # .P.A.V.L.Q.S.S.G.L.Y.S.L.S.S.V.V.T.V.P.S.S.S.L.G.T.Q.T.Y.I.C.N.V.N.H.K.P.S.N.T.K.V.D.K.K.V.E.P.K.S
                    # .C.D.K.T.H.T.C.P.P.C.P.A.P.E.L.L.G.G.P.S.V.F.L.F.P.P.K.P.K.D.T.L.M.I.S.R.T.P.E.V.T.C.V.V.V.D.V.S.H
                    # .E.D.P.E.V.K.F.N.W.Y.V.D.G.V.E.V.H.N.A.K.T.K.P.R.E.E.Q.Y.N.S.T.Y.R.V.V.S.V.L.T.V.L.H.Q.D.W.L.N.G.K
                    # .E.Y.K.C.K.V.S.N.K.A.L.P.A.P.I.E.K.T.I.S.K.A.K.G.Q.P.R.E.P.Q.V.Y.T.L.P.P.S.R.D.E.L.T.K.N.Q.V.S.L.T
                    # .C.L.V.K.G.F.Y.P.S.D.I.A.V.E.W.E.S.N.G.Q.P.E.N.N.Y.K.T.T.P.P.V.L.D.S.D.G.S.F.F.L.Y.S.K.L.T.V.D.K.S
                    # .R.W.Q.Q.G.N.V.F.S.C.S.V.M.H.E.A.L.H.N.H.Y.T.Q.K.S.L.S.L.S.P.G.K}|PEPTIDE3{Q.V.Q.L.V.Q.S.G.A.E.V.K
                    # .K.P.G.A.S.V.K.V.S.C.K.A.F.G.Y.P.F.T.D.Y.L.L.H.W.V.R.Q.A.P.G.Q.G.L.E.W.V.G.W.L.N.P.Y.S.G.D.T.N.Y.A
                    # .Q.K.F.Q.G.R.V.T.M.T.R.D.T.S.I.S.T.A.Y.M.E.L.S.R.L.R.S.D.D.T.A.V.Y.Y.C.T.R.T.T.L.I.S.V.Y.F.D.Y.W.G
                    # .Q.G.T.M.V.T.V.S.S.A.S.T.K.G.P.S.V.F.P.L.A.P.S.S.K.S.T.S.G.G.T.A.A.L.G.C.L.V.K.D.Y.F.P.E.P.V.T.V.S
                    # .W.N.S.G.A.L.T.S.G.V.H.T.F.P.A.V.L.Q.S.S.G.L.Y.S.L.S.S.V.V.T.V.P.S.S.S.L.G.T.Q.T.Y.I.C.N.V.N.H.K.P
                    # .S.N.T.K.V.D.K.K.V.E.P.K.S.C.D.K.T.H.T.C.P.P.C.P.A.P.E.L.L.G.G.P.S.V.F.L.F.P.P.K.P.K.D.T.L.M.I.S.R
                    # .T.P.E.V.T.C.V.V.V.D.V.S.H.E.D.P.E.V.K.F.N.W.Y.V.D.G.V.E.V.H.N.A.K.T.K.P.R.E.E.Q.Y.N.S.T.Y.R.V.V.S
                    # .V.L.T.V.L.H.Q.D.W.L.N.G.K.E.Y.K.C.K.V.S.N.K.A.L.P.A.P.I.E.K.T.I.S.K.A.K.G.Q.P.R.E.P.Q.V.Y.T.L.P.P
                    # .S.R.D.E.L.T.K.N.Q.V.S.L.T.C.L.V.K.G.F.Y.P.S.D.I.A.V.E.W.E.S.N.G.Q.P.E.N.N.Y.K.T.T.P.P.V.L.D.S.D.G
                    # .S.F.F.L.Y.S.K.L.T.V.D.K.S.R.W.Q.Q.G.N.V.F.S.C.S.V.M.H.E.A.L.H.N.H.Y.T.Q.K.S.L.S.L.S.P.G.K}|PEPTID
                    # E4{D.I.Q.M.T.Q.S.P.S.S.V.S.A.S.V.G.D.R.V.T.I.A.C.R.A.S.Q.N.I.R.N.I.L.N.W.Y.Q.Q.R.P.G.K.A.P.Q.L.L.I
                    # .Y.A.A.S.N.L.Q.S.G.V.P.S.R.F.S.G.S.G.S.G.T.D.F.T.L.T.I.N.S.L.Q.P.E.D.F.A.T.Y.Y.C.Q.Q.S.Y.S.M.P.R.T
                    # .F.G.G.G.T.K.L.E.I.K.R.T.V.A.A.P.S.V.F.I.F.P.P.S.D.E.Q.L.K.S.G.T.A.S.V.V.C.L.L.N.N.F.Y.P.R.E.A.K.V
                    # .Q.W.K.V.D.N.A.L.Q.S.G.N.S.Q.E.S.V.T.E.Q.D.S.K.D.S.T.Y.S.L.S.S.T.L.T.L.S.K.A.D.Y.E.K.H.K.V.Y.A.C.E
                    # .V.T.H.Q.G.L.S.S.P.V.T.K.S.F.N.R.G.E.C}$PEPTIDE3,PEPTIDE4,222:R3-214:R3|PEPTIDE1,PEPTIDE1,134:R3-1
                    # 94:R3|PEPTIDE2,PEPTIDE3,231:R3-231:R3|PEPTIDE4,PEPTIDE4,23:R3-88:R3|PEPTIDE3,PEPTIDE3,369:R3-427:R
                    # 3|PEPTIDE2,PEPTIDE2,369:R3-427:R3|PEPTIDE1,PEPTIDE1,23:R3-88:R3|PEPTIDE2,PEPTIDE2,146:R3-202:R3|PE
                    # PTIDE4,PEPTIDE4,134:R3-194:R3|PEPTIDE2,PEPTIDE2,22:R3-96:R3|PEPTIDE3,PEPTIDE3,263:R3-323:R3|PEPTID
                    # E3,PEPTIDE3,22:R3-96:R3|PEPTIDE2,PEPTIDE1,222:R3-214:R3|PEPTIDE3,PEPTIDE3,146:R3-202:R3|PEPTIDE2,P
                    # EPTIDE3,228:R3-228:R3|PEPTIDE2,PEPTIDE2,263:R3-323:R3$$$' , 'PEPTIDE1{E.I.V.L.T.Q.S.P.A.T.L.S.L.S.
                    # P.G.E.R.A.T.L.S.C.R.A.S.Q.S.V.S.R.Y.L.A.W.Y.Q.Q.K.P.G.Q.A.P.R.L.L.I.Y.D.A.S.N.R.A.T.G.I.P.A.R.F.S.
                    # G.S.G.S.G.T.D.F.T.L.T.I.S.S.L.E.P.E.D.F.A.V.Y.Y.C.Q.Q.R.S.N.W.P.R.T.F.G.Q.G.T.K.V.E.I.K.R.T.V.A.A.
                    # P.S.V.F.I.F.P.P.S.D.E.Q.L.K.S.G.T.A.S.V.V.C.L.L.N.N.F.Y.P.R.E.A.K.V.Q.W.K.V.D.N.A.L.Q.S.G.N.S.Q.E.
                    # S.V.T.E.Q.D.S.K.D.S.T.Y.S.L.S.S.T.L.T.L.S.K.A.D.Y.E.K.H.K.V.Y.A.C.E.V.T.H.Q.G.L.S.S.P.V.T.K.S.F.N.
                    # R.G.E.C}|PEPTIDE2{E.V.Q.L.V.E.S.G.G.G.L.V.Q.P.G.G.S.L.R.L.S.C.A.A.S.G.F.T.F.S.S.Y.L.M.T.W.V.R.Q.A.
                    # P.G.K.G.L.E.W.V.A.N.I.K.Q.D.G.S.E.K.Y.Y.V.D.S.V.K.G.R.F.T.I.S.R.D.N.A.K.N.S.L.N.L.Q.M.N.S.L.R.A.E.
                    # D.T.A.V.Y.Y.C.T.R.D.G.Y.S.S.G.R.H.Y.G.M.D.V.W.G.Q.G.T.T.V.I.V.S.S.A.S.T.K.G.P.S.V.F.P.L.A.P.S.S.K.
                    # S.T.S.G.G.T.A.A.L.G.C.L.V.K.D.Y.F.P.E.P.V.T.V.S.W.N.S.G.A.L.T.S.G.V.H.T.F.P.A.V.L.Q.S.S.G.L.Y.S.L.
                    # S.S.V.V.T.V.P.S.S.S.L.G.T.Q.T.Y.I.C.N.V.N.H.K.P.S.N.T.K.V.D.K.R.V.E.P.K.S.C.D.K.T.H.T.C.P.P.C.P.A.
                    # P.E.L.L.G.G.P.S.V.F.L.F.P.P.K.P.K.D.T.L.M.I.S.R.T.P.E.V.T.C.V.V.V.D.V.S.H.E.D.P.E.V.K.F.N.W.Y.V.D.
                    # G.V.E.V.H.N.A.K.T.K.P.R.E.E.Q.Y.N.S.T.Y.R.V.V.S.V.L.T.V.L.H.Q.D.W.L.N.G.K.E.Y.K.C.K.V.S.N.K.A.L.P.
                    # A.P.I.E.K.T.I.S.K.A.K.G.Q.P.R.E.P.Q.V.Y.T.L.P.P.S.R.E.E.M.T.K.N.Q.V.S.L.T.C.L.V.K.G.F.Y.P.S.D.I.A.
                    # V.E.W.E.S.N.G.Q.P.E.N.N.Y.K.T.T.P.P.V.L.D.S.D.G.S.F.F.L.Y.S.K.L.T.V.D.K.S.R.W.Q.Q.G.N.V.F.S.C.S.V.
                    # M.H.E.A.L.H.N.H.Y.T.Q.K.S.L.S.L.S.P.G.K}|PEPTIDE3{E.V.Q.L.V.E.S.G.G.G.L.V.Q.P.G.G.S.L.R.L.S.C.A.A.
                    # S.G.F.T.F.S.S.Y.L.M.T.W.V.R.Q.A.P.G.K.G.L.E.W.V.A.N.I.K.Q.D.G.S.E.K.Y.Y.V.D.S.V.K.G.R.F.T.I.S.R.D.
                    # N.A.K.N.S.L.N.L.Q.M.N.S.L.R.A.E.D.T.A.V.Y.Y.C.T.R.D.G.Y.S.S.G.R.H.Y.G.M.D.V.W.G.Q.G.T.T.V.I.V.S.S.
                    # A.S.T.K.G.P.S.V.F.P.L.A.P.S.S.K.S.T.S.G.G.T.A.A.L.G.C.L.V.K.D.Y.F.P.E.P.V.T.V.S.W.N.S.G.A.L.T.S.G.
                    # V.H.T.F.P.A.V.L.Q.S.S.G.L.Y.S.L.S.S.V.V.T.V.P.S.S.S.L.G.T.Q.T.Y.I.C.N.V.N.H.K.P.S.N.T.K.V.D.K.R.V.
                    # E.P.K.S.C.D.K.T.H.T.C.P.P.C.P.A.P.E.L.L.G.G.P.S.V.F.L.F.P.P.K.P.K.D.T.L.M.I.S.R.T.P.E.V.T.C.V.V.V.
                    # D.V.S.H.E.D.P.E.V.K.F.N.W.Y.V.D.G.V.E.V.H.N.A.K.T.K.P.R.E.E.Q.Y.N.S.T.Y.R.V.V.S.V.L.T.V.L.H.Q.D.W.
                    # L.N.G.K.E.Y.K.C.K.V.S.N.K.A.L.P.A.P.I.E.K.T.I.S.K.A.K.G.Q.P.R.E.P.Q.V.Y.T.L.P.P.S.R.E.E.M.T.K.N.Q.
                    # V.S.L.T.C.L.V.K.G.F.Y.P.S.D.I.A.V.E.W.E.S.N.G.Q.P.E.N.N.Y.K.T.T.P.P.V.L.D.S.D.G.S.F.F.L.Y.S.K.L.T.
                    # V.D.K.S.R.W.Q.Q.G.N.V.F.S.C.S.V.M.H.E.A.L.H.N.H.Y.T.Q.K.S.L.S.L.S.P.G.K}|PEPTIDE4{E.I.V.L.T.Q.S.P.
                    # A.T.L.S.L.S.P.G.E.R.A.T.L.S.C.R.A.S.Q.S.V.S.R.Y.L.A.W.Y.Q.Q.K.P.G.Q.A.P.R.L.L.I.Y.D.A.S.N.R.A.T.G.
                    # I.P.A.R.F.S.G.S.G.S.G.T.D.F.T.L.T.I.S.S.L.E.P.E.D.F.A.V.Y.Y.C.Q.Q.R.S.N.W.P.R.T.F.G.Q.G.T.K.V.E.I.
                    # K.R.T.V.A.A.P.S.V.F.I.F.P.P.S.D.E.Q.L.K.S.G.T.A.S.V.V.C.L.L.N.N.F.Y.P.R.E.A.K.V.Q.W.K.V.D.N.A.L.Q.
                    # S.G.N.S.Q.E.S.V.T.E.Q.D.S.K.D.S.T.Y.S.L.S.S.T.L.T.L.S.K.A.D.Y.E.K.H.K.V.Y.A.C.E.V.T.H.Q.G.L.S.S.P.
                    # V.T.K.S.F.N.R.G.E.C}$PEPTIDE4,PEPTIDE4,23:R3-88:R3|PEPTIDE1,PEPTIDE1,23:R3-88:R3|PEPTIDE3,PEPTIDE3
                    # ,372:R3-430:R3|PEPTIDE4,PEPTIDE4,134:R3-194:R3|PEPTIDE2,PEPTIDE2,22:R3-96:R3|PEPTIDE2,PEPTIDE2,149
                    # :R3-205:R3|PEPTIDE2,PEPTIDE2,266:R3-326:R3|PEPTIDE3,PEPTIDE3,149:R3-205:R3|PEPTIDE2,PEPTIDE2,372:R
                    # 3-430:R3|PEPTIDE2,PEPTIDE3,231:R3-231:R3|PEPTIDE2,PEPTIDE1,225:R3-214:R3|PEPTIDE3,PEPTIDE3,266:R3-
                    # 326:R3|PEPTIDE3,PEPTIDE4,225:R3-214:R3|PEPTIDE3,PEPTIDE3,22:R3-96:R3|PEPTIDE1,PEPTIDE1,134:R3-194:
                    # R3|PEPTIDE2,PEPTIDE3,234:R3-234:R3$$$' , 'PEPTIDE1{E.I.V.M.T.Q.S.P.A.T.L.S.L.S.P.G.E.R.A.T.L.S.C.R
                    # .A.S.Q.S.V.S.S.Y.L.A.W.Y.Q.Q.K.P.G.Q.A.P.R.L.L.I.Y.D.A.S.N.R.A.T.G.I.P.A.R.F.S.G.S.G.S.G.T.D.F.T.L
                    # .T.I.S.S.L.E.P.E.D.F.A.V.Y.Y.C.H.Q.Y.G.S.T.P.L.T.F.G.G.G.T.K.A.E.I.K.R.T.V.A.A.P.S.V.F.I.F.P.P.S.D
                    # .E.Q.L.K.S.G.T.A.S.V.V.C.L.L.N.N.F.Y.P.R.E.A.K.V.Q.W.K.V.D.N.A.L.Q.S.G.N.S.Q.E.S.V.T.E.Q.D.S.K.D.S
                    # .T.Y.S.L.S.S.T.L.T.L.S.K.A.D.Y.E.K.H.K.V.Y.A.C.E.V.T.H.Q.G.L.S.S.P.V.T.K.S.F.N.R.G.E.C}|PEPTIDE2{Q
                    # .V.Q.L.Q.E.S.G.P.G.L.V.K.P.S.Q.T.L.S.L.T.C.T.V.S.G.G.S.I.S.S.G.D.Y.Y.W.S.W.I.R.Q.P.P.G.K.G.L.E.W.I
                    # .G.Y.I.Y.Y.S.G.S.T.D.Y.N.P.S.L.K.S.R.V.T.M.S.V.D.T.S.K.N.Q.F.S.L.K.V.N.S.V.T.A.A.D.T.A.V.Y.Y.C.A.R
                    # .V.S.I.F.G.V.G.T.F.D.Y.W.G.Q.G.T.L.V.T.V.S.S.A.S.T.K.G.P.S.V.L.P.L.A.P.S.S.K.S.T.S.G.G.T.A.A.L.G.C
                    # .L.V.K.D.Y.F.P.E.P.V.T.V.S.W.N.S.G.A.L.T.S.G.V.H.T.F.P.A.V.L.Q.S.S.G.L.Y.S.L.S.S.V.V.T.V.P.S.S.S.L
                    # .G.T.Q.T.Y.I.C.N.V.N.H.K.P.S.N.T.K.V.D.K.R.V.E.P.K.S.C.D.K.T.H.T.C.P.P.C.P.A.P.E.L.L.G.G.P.S.V.F.L
                    # .F.P.P.K.P.K.D.T.L.M.I.S.R.T.P.E.V.T.C.V.V.V.D.V.S.H.E.D.P.E.V.K.F.N.W.Y.V.D.G.V.E.V.H.N.A.K.T.K.P
                    # .R.E.E.Q.Y.N.S.T.Y.R.V.V.S.V.L.T.V.L.H.Q.D.W.L.N.G.K.E.Y.K.C.K.V.S.N.K.A.L.P.A.P.I.E.K.T.I.S.K.A.K
                    # .G.Q.P.R.E.P.Q.V.Y.T.L.P.P.S.R.E.E.M.T.K.N.Q.V.S.L.T.C.L.V.K.G.F.Y.P.S.D.I.A.V.E.W.E.S.N.G.Q.P.E.N
                    # .N.Y.K.T.T.P.P.V.L.D.S.D.G.S.F.F.L.Y.S.K.L.T.V.D.K.S.R.W.Q.Q.G.N.V.F.S.C.S.V.M.H.E.A.L.H.N.H.Y.T.Q
                    # .K.S.L.S.L.S.P.G.K}|PEPTIDE3{Q.V.Q.L.Q.E.S.G.P.G.L.V.K.P.S.Q.T.L.S.L.T.C.T.V.S.G.G.S.I.S.S.G.D.Y.Y
                    # .W.S.W.I.R.Q.P.P.G.K.G.L.E.W.I.G.Y.I.Y.Y.S.G.S.T.D.Y.N.P.S.L.K.S.R.V.T.M.S.V.D.T.S.K.N.Q.F.S.L.K.V
                    # .N.S.V.T.A.A.D.T.A.V.Y.Y.C.A.R.V.S.I.F.G.V.G.T.F.D.Y.W.G.Q.G.T.L.V.T.V.S.S.A.S.T.K.G.P.S.V.L.P.L.A
                    # .P.S.S.K.S.T.S.G.G.T.A.A.L.G.C.L.V.K.D.Y.F.P.E.P.V.T.V.S.W.N.S.G.A.L.T.S.G.V.H.T.F.P.A.V.L.Q.S.S.G
                    # .L.Y.S.L.S.S.V.V.T.V.P.S.S.S.L.G.T.Q.T.Y.I.C.N.V.N.H.K.P.S.N.T.K.V.D.K.R.V.E.P.K.S.C.D.K.T.H.T.C.P
                    # .P.C.P.A.P.E.L.L.G.G.P.S.V.F.L.F.P.P.K.P.K.D.T.L.M.I.S.R.T.P.E.V.T.C.V.V.V.D.V.S.H.E.D.P.E.V.K.F.N
                    # .W.Y.V.D.G.V.E.V.H.N.A.K.T.K.P.R.E.E.Q.Y.N.S.T.Y.R.V.V.S.V.L.T.V.L.H.Q.D.W.L.N.G.K.E.Y.K.C.K.V.S.N
                    # .K.A.L.P.A.P.I.E.K.T.I.S.K.A.K.G.Q.P.R.E.P.Q.V.Y.T.L.P.P.S.R.E.E.M.T.K.N.Q.V.S.L.T.C.L.V.K.G.F.Y.P
                    # .S.D.I.A.V.E.W.E.S.N.G.Q.P.E.N.N.Y.K.T.T.P.P.V.L.D.S.D.G.S.F.F.L.Y.S.K.L.T.V.D.K.S.R.W.Q.Q.G.N.V.F
                    # .S.C.S.V.M.H.E.A.L.H.N.H.Y.T.Q.K.S.L.S.L.S.P.G.K}|PEPTIDE4{E.I.V.M.T.Q.S.P.A.T.L.S.L.S.P.G.E.R.A.T
                    # .L.S.C.R.A.S.Q.S.V.S.S.Y.L.A.W.Y.Q.Q.K.P.G.Q.A.P.R.L.L.I.Y.D.A.S.N.R.A.T.G.I.P.A.R.F.S.G.S.G.S.G.T
                    # .D.F.T.L.T.I.S.S.L.E.P.E.D.F.A.V.Y.Y.C.H.Q.Y.G.S.T.P.L.T.F.G.G.G.T.K.A.E.I.K.R.T.V.A.A.P.S.V.F.I.F
                    # .P.P.S.D.E.Q.L.K.S.G.T.A.S.V.V.C.L.L.N.N.F.Y.P.R.E.A.K.V.Q.W.K.V.D.N.A.L.Q.S.G.N.S.Q.E.S.V.T.E.Q.D
                    # .S.K.D.S.T.Y.S.L.S.S.T.L.T.L.S.K.A.D.Y.E.K.H.K.V.Y.A.C.E.V.T.H.Q.G.L.S.S.P.V.T.K.S.F.N.R.G.E.C}$PE
                    # PTIDE3,PEPTIDE4,224:R3-214:R3|PEPTIDE3,PEPTIDE3,22:R3-97:R3|PEPTIDE3,PEPTIDE3,148:R3-204:R3|PEPTID
                    # E3,PEPTIDE3,265:R3-325:R3|PEPTIDE2,PEPTIDE2,371:R3-429:R3|PEPTIDE1,PEPTIDE1,134:R3-194:R3|PEPTIDE2
                    # ,PEPTIDE3,233:R3-233:R3|PEPTIDE4,PEPTIDE4,23:R3-88:R3|PEPTIDE2,PEPTIDE1,224:R3-214:R3|PEPTIDE2,PEP
                    # TIDE2,148:R3-204:R3|PEPTIDE2,PEPTIDE2,22:R3-97:R3|PEPTIDE2,PEPTIDE2,265:R3-325:R3|PEPTIDE2,PEPTIDE
                    # 3,230:R3-230:R3|PEPTIDE4,PEPTIDE4,134:R3-194:R3|PEPTIDE3,PEPTIDE3,371:R3-429:R3|PEPTIDE1,PEPTIDE1,
                    # 23:R3-88:R3$$$' , 'PEPTIDE1{D.I.Q.M.T.Q.T.T.S.S.L.S.A.S.L.G.D.R.V.T.I.S.C.R.A.S.Q.D.I.S.N.Y.L.N.W.
                    # Y.Q.Q.K.P.D.G.T.V.K.L.L.I.Y.Y.T.S.R.L.H.S.G.V.P.S.R.F.S.G.S.G.S.G.T.D.Y.S.L.T.I.S.N.L.E.Q.E.D.I.A.
                    # T.Y.F.C.Q.Q.G.N.T.L.P.W.T.F.G.G.G.T.K.L.E.I.K.R.A.D.A.A.P.T.V.S.I.F.P.P.S.S.E.Q.L.T.S.G.G.A.S.V.V.
                    # C.F.L.N.N.F.Y.P.K.D.I.N.V.K.W.K.I.D.G.S.E.R.Q.N.G.V.L.N.S.W.T.D.Q.D.S.K.D.S.T.Y.S.M.S.S.T.L.T.L.T.
                    # K.D.E.Y.E.R.H.N.S.Y.T.C.E.A.T.H.K.T.S.T.S.P.I.V.K.S.F.N.R.N.E.C}|PEPTIDE2{Q.V.Q.L.Q.Q.S.G.A.E.L.V.
                    # K.P.G.A.S.V.K.L.S.C.K.A.S.G.Y.T.F.T.S.Y.D.I.N.W.V.R.Q.R.P.E.Q.G.L.E.W.I.G.W.I.F.P.G.D.G.S.T.K.Y.N.
                    # E.K.F.K.G.K.A.T.L.T.T.D.K.S.S.S.T.A.Y.M.Q.L.S.R.L.T.S.E.D.S.A.V.Y.F.C.A.R.E.D.Y.Y.D.N.S.Y.Y.F.D.Y.
                    # W.G.Q.G.T.T.L.T.V.S.S.A.K.T.T.P.P.S.V.Y.P.L.A.P.G.S.A.A.Q.T.N.S.M.V.T.L.G.C.L.V.K.G.Y.F.P.E.P.V.T.
                    # V.T.W.N.S.G.S.L.S.S.G.V.H.T.F.P.A.V.L.Q.S.D.L.Y.T.L.S.S.S.V.T.V.P.S.S.P.R.P.S.E.T.V.T.C.N.V.A.H.P.
                    # A.S.S.T.K.V.D.K.K.I.V.P.R.D.C.G.C.K.P.C.I.C.T.V.P.E.V.S.S.V.F.I.F.P.P.K.P.K.D.V.L.T.I.T.L.T.P.K.V.
                    # T.C.V.V.V.D.I.S.K.D.D.P.E.V.Q.F.S.W.F.V.D.D.V.E.V.H.T.A.Q.T.Q.P.R.E.E.Q.F.N.S.T.F.R.S.V.S.E.L.P.I.
                    # M.H.Q.D.W.L.N.G.K.E.F.K.C.R.V.N.S.A.A.F.P.A.P.I.E.K.T.I.S.K.T.K.G.R.P.K.A.P.Q.V.Y.T.I.P.P.P.K.E.Q.
                    # M.A.K.D.K.V.S.L.T.C.M.I.T.D.F.F.P.E.D.I.T.V.E.W.Q.W.N.G.Q.P.A.E.N.Y.K.N.T.Q.P.I.M.N.T.N.G.S.Y.F.V.
                    # Y.S.K.L.N.V.Q.K.S.N.W.E.A.G.N.T.F.T.C.S.V.L.H.E.G.L.H.N.H.H.T.E.K.S.L.S.H.S.P.G.K}|PEPTIDE3{Q.V.Q.
                    # L.Q.Q.S.G.A.E.L.V.K.P.G.A.S.V.K.L.S.C.K.A.S.G.Y.T.F.T.S.Y.D.I.N.W.V.R.Q.R.P.E.Q.G.L.E.W.I.G.W.I.F.
                    # P.G.D.G.S.T.K.Y.N.E.K.F.K.G.K.A.T.L.T.T.D.K.S.S.S.T.A.Y.M.Q.L.S.R.L.T.S.E.D.S.A.V.Y.F.C.A.R.E.D.Y.
                    # Y.D.N.S.Y.Y.F.D.Y.W.G.Q.G.T.T.L.T.V.S.S.A.K.T.T.P.P.S.V.Y.P.L.A.P.G.S.A.A.Q.T.N.S.M.V.T.L.G.C.L.V.
                    # K.G.Y.F.P.E.P.V.T.V.T.W.N.S.G.S.L.S.S.G.V.H.T.F.P.A.V.L.Q.S.D.L.Y.T.L.S.S.S.V.T.V.P.S.S.P.R.P.S.E.
                    # T.V.T.C.N.V.A.H.P.A.S.S.T.K.V.D.K.K.I.V.P.R.D.C.G.C.K.P.C.I.C.T.V.P.E.V.S.S.V.F.I.F.P.P.K.P.K.D.V.
                    # L.T.I.T.L.T.P.K.V.T.C.V.V.V.D.I.S.K.D.D.P.E.V.Q.F.S.W.F.V.D.D.V.E.V.H.T.A.Q.T.Q.P.R.E.E.Q.F.N.S.T.
                    # F.R.S.V.S.E.L.P.I.M.H.Q.D.W.L.N.G.K.E.F.K.C.R.V.N.S.A.A.F.P.A.P.I.E.K.T.I.S.K.T.K.G.R.P.K.A.P.Q.V.
                    # Y.T.I.P.P.P.K.E.Q.M.A.K.D.K.V.S.L.T.C.M.I.T.D.F.F.P.E.D.I.T.V.E.W.Q.W.N.G.Q.P.A.E.N.Y.K.N.T.Q.P.I.
                    # M.N.T.N.G.S.Y.F.V.Y.S.K.L.N.V.Q.K.S.N.W.E.A.G.N.T.F.T.C.S.V.L.H.E.G.L.H.N.H.H.T.E.K.S.L.S.H.S.P.G.
                    # K}|PEPTIDE4{D.I.Q.M.T.Q.T.T.S.S.L.S.A.S.L.G.D.R.V.T.I.S.C.R.A.S.Q.D.I.S.N.Y.L.N.W.Y.Q.Q.K.P.D.G.T.
                    # V.K.L.L.I.Y.Y.T.S.R.L.H.S.G.V.P.S.R.F.S.G.S.G.S.G.T.D.Y.S.L.T.I.S.N.L.E.Q.E.D.I.A.T.Y.F.C.Q.Q.G.N.
                    # T.L.P.W.T.F.G.G.G.T.K.L.E.I.K.R.A.D.A.A.P.T.V.S.I.F.P.P.S.S.E.Q.L.T.S.G.G.A.S.V.V.C.F.L.N.N.F.Y.P.
                    # K.D.I.N.V.K.W.K.I.D.G.S.E.R.Q.N.G.V.L.N.S.W.T.D.Q.D.S.K.D.S.T.Y.S.M.S.S.T.L.T.L.T.K.D.E.Y.E.R.H.N.
                    # S.Y.T.C.E.A.T.H.K.T.S.T.S.P.I.V.K.S.F.N.R.N.E.C}$PEPTIDE2,PEPTIDE3,225:R3-225:R3|PEPTIDE2,PEPTIDE2
                    # ,365:R3-423:R3|PEPTIDE3,PEPTIDE3,365:R3-423:R3|PEPTIDE1,PEPTIDE1,23:R3-88:R3|PEPTIDE3,PEPTIDE3,259
                    # :R3-319:R3|PEPTIDE2,PEPTIDE1,223:R3-214:R3|PEPTIDE2,PEPTIDE2,148:R3-203:R3|PEPTIDE1,PEPTIDE1,134:R
                    # 3-194:R3|PEPTIDE3,PEPTIDE4,223:R3-214:R3|PEPTIDE2,PEPTIDE2,22:R3-96:R3|PEPTIDE4,PEPTIDE4,134:R3-19
                    # 4:R3|PEPTIDE3,PEPTIDE3,22:R3-96:R3|PEPTIDE2,PEPTIDE2,259:R3-319:R3|PEPTIDE2,PEPTIDE3,230:R3-230:R3
                    # |PEPTIDE3,PEPTIDE3,148:R3-203:R3|PEPTIDE4,PEPTIDE4,23:R3-88:R3|PEPTIDE2,PEPTIDE3,228:R3-228:R3$$$'
                    #  , 'PEPTIDE1{D.I.Q.M.T.Q.S.P.S.S.V.S.A.S.I.G.D.R.V.T.I.T.C.R.A.S.Q.G.I.D.N.W.L.G.W.Y.Q.Q.K.P.G.K.A
                    # .P.K.L.L.I.Y.D.A.S.N.L.D.T.G.V.P.S.R.F.S.G.S.G.S.G.T.Y.F.T.L.T.I.S.S.L.Q.A.E.D.F.A.V.Y.F.C.Q.Q.A.K
                    # .A.F.P.P.T.F.G.G.G.T.K.V.D.I.K.G.T.V.A.A.P.S.V.F.I.F.P.P.S.D.E.Q.L.K.S.G.T.A.S.V.V.C.L.L.N.N.F.Y.P
                    # .R.E.A.K.V.Q.W.K.V.D.N.A.L.Q.S.G.N.S.Q.E.S.V.T.E.Q.D.S.K.D.S.T.Y.S.L.S.S.T.L.T.L.S.K.A.D.Y.E.K.H.K
                    # .V.Y.A.C.E.V.T.H.Q.G.L.S.S.P.V.T.K.S.F.N.R.G.E.C}|PEPTIDE2{E.V.Q.L.V.Q.S.G.G.G.L.V.K.P.G.G.S.L.R.L
                    # .S.C.A.A.S.G.F.T.F.S.S.Y.S.M.N.W.V.R.Q.A.P.G.K.G.L.E.W.V.S.S.I.S.S.S.S.S.Y.I.Y.Y.A.D.S.V.K.G.R.F.T
                    # .I.S.R.D.N.A.K.N.S.L.Y.L.Q.M.N.S.L.R.A.E.D.T.A.V.Y.Y.C.A.R.V.T.D.A.F.D.I.W.G.Q.G.T.M.V.T.V.S.S.A.S
                    # .T.K.G.P.S.V.F.P.L.A.P.S.S.K.S.T.S.G.G.T.A.A.L.G.C.L.V.K.D.Y.F.P.E.P.V.T.V.S.W.N.S.G.A.L.T.S.G.V.H
                    # .T.F.P.A.V.L.Q.S.S.G.L.Y.S.L.S.S.V.V.T.V.P.S.S.S.L.G.T.Q.T.Y.I.C.N.V.N.H.K.P.S.N.T.K.V.D.K.K.V.E.P
                    # .K.S.C.D.K.T.H.T.C.P.P.C.P.A.P.E.L.L.G.G.P.S.V.F.L.F.P.P.K.P.K.D.T.L.M.I.S.R.T.P.E.V.T.C.V.V.V.D.V
                    # .S.H.E.D.P.E.V.K.F.N.W.Y.V.D.G.V.E.V.H.N.A.K.T.K.P.R.E.E.Q.Y.N.S.T.Y.R.V.V.S.V.L.T.V.L.H.Q.D.W.L.N
                    # .G.K.E.Y.K.C.K.V.S.N.K.A.L.P.A.P.I.E.K.T.I.S.K.A.K.G.Q.P.R.E.P.Q.V.Y.T.L.P.P.S.R.E.E.M.T.K.N.Q.V.S
                    # .L.T.C.L.V.K.G.F.Y.P.S.D.I.A.V.E.W.E.S.N.G.Q.P.E.N.N.Y.K.T.T.P.P.V.L.D.S.D.G.S.F.F.L.Y.S.K.L.T.V.D
                    # .K.S.R.W.Q.Q.G.N.V.F.S.C.S.V.M.H.E.A.L.H.N.H.Y.T.Q.K.S.L.S.L.S.P.G.K}|PEPTIDE3{E.V.Q.L.V.Q.S.G.G.G
                    # .L.V.K.P.G.G.S.L.R.L.S.C.A.A.S.G.F.T.F.S.S.Y.S.M.N.W.V.R.Q.A.P.G.K.G.L.E.W.V.S.S.I.S.S.S.S.S.Y.I.Y
                    # .Y.A.D.S.V.K.G.R.F.T.I.S.R.D.N.A.K.N.S.L.Y.L.Q.M.N.S.L.R.A.E.D.T.A.V.Y.Y.C.A.R.V.T.D.A.F.D.I.W.G.Q
                    # .G.T.M.V.T.V.S.S.A.S.T.K.G.P.S.V.F.P.L.A.P.S.S.K.S.T.S.G.G.T.A.A.L.G.C.L.V.K.D.Y.F.P.E.P.V.T.V.S.W
                    # .N.S.G.A.L.T.S.G.V.H.T.F.P.A.V.L.Q.S.S.G.L.Y.S.L.S.S.V.V.T.V.P.S.S.S.L.G.T.Q.T.Y.I.C.N.V.N.H.K.P.S
                    # .N.T.K.V.D.K.K.V.E.P.K.S.C.D.K.T.H.T.C.P.P.C.P.A.P.E.L.L.G.G.P.S.V.F.L.F.P.P.K.P.K.D.T.L.M.I.S.R.T
                    # .P.E.V.T.C.V.V.V.D.V.S.H.E.D.P.E.V.K.F.N.W.Y.V.D.G.V.E.V.H.N.A.K.T.K.P.R.E.E.Q.Y.N.S.T.Y.R.V.V.S.V
                    # .L.T.V.L.H.Q.D.W.L.N.G.K.E.Y.K.C.K.V.S.N.K.A.L.P.A.P.I.E.K.T.I.S.K.A.K.G.Q.P.R.E.P.Q.V.Y.T.L.P.P.S
                    # .R.E.E.M.T.K.N.Q.V.S.L.T.C.L.V.K.G.F.Y.P.S.D.I.A.V.E.W.E.S.N.G.Q.P.E.N.N.Y.K.T.T.P.P.V.L.D.S.D.G.S
                    # .F.F.L.Y.S.K.L.T.V.D.K.S.R.W.Q.Q.G.N.V.F.S.C.S.V.M.H.E.A.L.H.N.H.Y.T.Q.K.S.L.S.L.S.P.G.K}|PEPTIDE4
                    # {D.I.Q.M.T.Q.S.P.S.S.V.S.A.S.I.G.D.R.V.T.I.T.C.R.A.S.Q.G.I.D.N.W.L.G.W.Y.Q.Q.K.P.G.K.A.P.K.L.L.I.Y
                    # .D.A.S.N.L.D.T.G.V.P.S.R.F.S.G.S.G.S.G.T.Y.F.T.L.T.I.S.S.L.Q.A.E.D.F.A.V.Y.F.C.Q.Q.A.K.A.F.P.P.T.F
                    # .G.G.G.T.K.V.D.I.K.G.T.V.A.A.P.S.V.F.I.F.P.P.S.D.E.Q.L.K.S.G.T.A.S.V.V.C.L.L.N.N.F.Y.P.R.E.A.K.V.Q
                    # .W.K.V.D.N.A.L.Q.S.G.N.S.Q.E.S.V.T.E.Q.D.S.K.D.S.T.Y.S.L.S.S.T.L.T.L.S.K.A.D.Y.E.K.H.K.V.Y.A.C.E.V
                    # .T.H.Q.G.L.S.S.P.V.T.K.S.F.N.R.G.E.C}$PEPTIDE3,PEPTIDE4,219:R3-214:R3|PEPTIDE2,PEPTIDE2,143:R3-199
                    # :R3|PEPTIDE1,PEPTIDE1,23:R3-88:R3|PEPTIDE3,PEPTIDE3,366:R3-424:R3|PEPTIDE3,PEPTIDE3,260:R3-320:R3|
                    # PEPTIDE2,PEPTIDE3,225:R3-225:R3|PEPTIDE2,PEPTIDE2,366:R3-424:R3|PEPTIDE3,PEPTIDE3,143:R3-199:R3|PE
                    # PTIDE4,PEPTIDE4,134:R3-194:R3|PEPTIDE2,PEPTIDE2,260:R3-320:R3|PEPTIDE2,PEPTIDE1,219:R3-214:R3|PEPT
                    # IDE1,PEPTIDE1,134:R3-194:R3|PEPTIDE2,PEPTIDE2,22:R3-96:R3|PEPTIDE3,PEPTIDE3,22:R3-96:R3|PEPTIDE2,P
                    # EPTIDE3,228:R3-228:R3|PEPTIDE4,PEPTIDE4,23:R3-88:R3$$$' , 'PEPTIDE1{E.I.V.L.T.Q.S.P.G.T.L.S.V.S.P.
                    # G.E.R.A.T.L.S.C.R.A.S.Q.S.I.G.S.S.L.H.W.Y.Q.Q.K.P.G.Q.A.P.R.L.L.I.K.Y.A.S.Q.S.L.S.G.I.P.D.R.F.S.G.
                    # S.G.S.G.T.D.F.T.L.T.I.S.R.L.E.P.E.D.F.A.V.Y.Y.C.H.Q.S.S.R.L.P.H.T.F.G.Q.G.T.K.V.E.I.K.R.T.V.A.A.P.
                    # S.V.F.I.F.P.P.S.D.E.Q.L.K.S.G.T.A.S.V.V.C.L.L.N.N.F.Y.P.R.E.A.K.V.Q.W.K.V.D.N.A.L.Q.S.G.N.S.Q.E.S.
                    # V.T.E.Q.D.S.K.D.S.T.Y.S.L.S.S.T.L.T.L.S.K.A.D.Y.E.K.H.K.V.Y.A.C.E.V.T.H.Q.G.L.S.S.P.V.T.K.S.F.N.R.
                    # G.E.C}|PEPTIDE2{E.V.Q.L.V.Q.S.G.G.G.L.V.K.P.G.G.S.L.R.L.S.C.A.A.S.G.F.T.F.S.S.F.A.M.H.W.V.R.Q.A.P.
                    # G.K.G.L.E.W.I.S.V.I.D.T.R.G.A.T.Y.Y.A.D.S.V.K.G.R.F.T.I.S.R.D.N.A.K.N.S.L.Y.L.Q.M.N.S.L.R.A.E.D.T.
                    # A.V.Y.Y.C.A.R.L.G.N.F.Y.Y.G.M.D.V.W.G.Q.G.T.T.V.T.V.S.S.A.S.T.K.G.P.S.V.F.P.L.A.P.S.S.K.S.T.S.G.G.
                    # T.A.A.L.G.C.L.V.K.D.Y.F.P.E.P.V.T.V.S.W.N.S.G.A.L.T.S.G.V.H.T.F.P.A.V.L.Q.S.S.G.L.Y.S.L.S.S.V.V.T.
                    # V.P.S.S.S.L.G.T.Q.T.Y.I.C.N.V.N.H.K.P.S.N.T.K.V.D.K.K.V.E.P.K.S.C.D.K.T.H.T.C.P.P.C.P.A.P.E.L.L.G.
                    # G.P.S.V.F.L.F.P.P.K.P.K.D.T.L.M.I.S.R.T.P.E.V.T.C.V.V.V.D.V.S.H.E.D.P.E.V.K.F.N.W.Y.V.D.G.V.E.V.H.
                    # N.A.K.T.K.P.R.E.E.Q.Y.N.S.T.Y.R.V.V.S.V.L.T.V.L.H.Q.D.W.L.N.G.K.E.Y.K.C.K.V.S.N.K.A.L.P.A.P.I.E.K.
                    # T.I.S.K.A.K.G.Q.P.R.E.P.Q.V.Y.T.L.P.P.S.R.D.E.L.T.K.N.Q.V.S.L.T.C.L.V.K.G.F.Y.P.S.D.I.A.V.E.W.E.S.
                    # N.G.Q.P.E.N.N.Y.K.T.T.P.P.V.L.D.S.D.G.S.F.F.L.Y.S.K.L.T.V.D.K.S.R.W.Q.Q.G.N.V.F.S.C.S.V.M.H.E.A.L.
                    # H.N.H.Y.T.Q.K.S.L.S.L.S.P.G.K}|PEPTIDE3{E.V.Q.L.V.Q.S.G.G.G.L.V.K.P.G.G.S.L.R.L.S.C.A.A.S.G.F.T.F.
                    # S.S.F.A.M.H.W.V.R.Q.A.P.G.K.G.L.E.W.I.S.V.I.D.T.R.G.A.T.Y.Y.A.D.S.V.K.G.R.F.T.I.S.R.D.N.A.K.N.S.L.
                    # Y.L.Q.M.N.S.L.R.A.E.D.T.A.V.Y.Y.C.A.R.L.G.N.F.Y.Y.G.M.D.V.W.G.Q.G.T.T.V.T.V.S.S.A.S.T.K.G.P.S.V.F.
                    # P.L.A.P.S.S.K.S.T.S.G.G.T.A.A.L.G.C.L.V.K.D.Y.F.P.E.P.V.T.V.S.W.N.S.G.A.L.T.S.G.V.H.T.F.P.A.V.L.Q.
                    # S.S.G.L.Y.S.L.S.S.V.V.T.V.P.S.S.S.L.G.T.Q.T.Y.I.C.N.V.N.H.K.P.S.N.T.K.V.D.K.K.V.E.P.K.S.C.D.K.T.H.
                    # T.C.P.P.C.P.A.P.E.L.L.G.G.P.S.V.F.L.F.P.P.K.P.K.D.T.L.M.I.S.R.T.P.E.V.T.C.V.V.V.D.V.S.H.E.D.P.E.V.
                    # K.F.N.W.Y.V.D.G.V.E.V.H.N.A.K.T.K.P.R.E.E.Q.Y.N.S.T.Y.R.V.V.S.V.L.T.V.L.H.Q.D.W.L.N.G.K.E.Y.K.C.K.
                    # V.S.N.K.A.L.P.A.P.I.E.K.T.I.S.K.A.K.G.Q.P.R.E.P.Q.V.Y.T.L.P.P.S.R.D.E.L.T.K.N.Q.V.S.L.T.C.L.V.K.G.
                    # F.Y.P.S.D.I.A.V.E.W.E.S.N.G.Q.P.E.N.N.Y.K.T.T.P.P.V.L.D.S.D.G.S.F.F.L.Y.S.K.L.T.V.D.K.S.R.W.Q.Q.G.
                    # N.V.F.S.C.S.V.M.H.E.A.L.H.N.H.Y.T.Q.K.S.L.S.L.S.P.G.K}|PEPTIDE4{E.I.V.L.T.Q.S.P.G.T.L.S.V.S.P.G.E.
                    # R.A.T.L.S.C.R.A.S.Q.S.I.G.S.S.L.H.W.Y.Q.Q.K.P.G.Q.A.P.R.L.L.I.K.Y.A.S.Q.S.L.S.G.I.P.D.R.F.S.G.S.G.
                    # S.G.T.D.F.T.L.T.I.S.R.L.E.P.E.D.F.A.V.Y.Y.C.H.Q.S.S.R.L.P.H.T.F.G.Q.G.T.K.V.E.I.K.R.T.V.A.A.P.S.V.
                    # F.I.F.P.P.S.D.E.Q.L.K.S.G.T.A.S.V.V.C.L.L.N.N.F.Y.P.R.E.A.K.V.Q.W.K.V.D.N.A.L.Q.S.G.N.S.Q.E.S.V.T.
                    # E.Q.D.S.K.D.S.T.Y.S.L.S.S.T.L.T.L.S.K.A.D.Y.E.K.H.K.V.Y.A.C.E.V.T.H.Q.G.L.S.S.P.V.T.K.S.F.N.R.G.E.
                    # C}$PEPTIDE2,PEPTIDE3,230:R3-230:R3|PEPTIDE3,PEPTIDE3,22:R3-95:R3|PEPTIDE4,PEPTIDE4,23:R3-88:R3|PEP
                    # TIDE2,PEPTIDE2,145:R3-201:R3|PEPTIDE1,PEPTIDE1,23:R3-88:R3|PEPTIDE2,PEPTIDE2,368:R3-426:R3|PEPTIDE
                    # 2,PEPTIDE3,227:R3-227:R3|PEPTIDE3,PEPTIDE3,368:R3-426:R3|PEPTIDE3,PEPTIDE4,221:R3-214:R3|PEPTIDE4,
                    # PEPTIDE4,134:R3-194:R3|PEPTIDE1,PEPTIDE1,134:R3-194:R3|PEPTIDE2,PEPTIDE1,221:R3-214:R3|PEPTIDE2,PE
                    # PTIDE2,262:R3-322:R3|PEPTIDE2,PEPTIDE2,22:R3-95:R3|PEPTIDE3,PEPTIDE3,262:R3-322:R3|PEPTIDE3,PEPTID
                    # E3,145:R3-201:R3$$$' , 'PEPTIDE1{E.I.V.L.T.Q.S.P.G.T.L.S.L.S.P.G.E.R.A.T.L.S.C.R.A.S.Q.S.V.S.S.T.Y
                    # .L.A.W.Y.Q.Q.K.P.G.Q.A.P.R.L.L.I.Y.G.A.S.S.R.A.T.G.I.P.D.R.F.S.G.S.G.S.G.T.D.F.T.L.T.I.S.R.L.E.P.E
                    # .D.F.A.V.Y.Y.C.Q.Q.Y.G.S.S.P.R.T.F.G.Q.G.T.K.V.E.I.K.R.T.V.A.A.P.S.V.F.I.F.P.P.S.D.E.Q.L.K.S.G.T.A
                    # .S.V.V.C.L.L.N.N.F.Y.P.R.E.A.K.V.Q.W.K.V.D.N.A.L.Q.S.G.N.S.Q.E.S.V.T.E.Q.D.S.K.D.S.T.Y.S.L.S.S.T.L
                    # .T.L.S.K.A.D.Y.E.K.H.K.V.Y.A.C.E.V.T.H.Q.G.L.S.S.P.V.T.K.S.F.N.R.G.E.C}|PEPTIDE2{Q.V.Q.L.V.Q.S.G.A
                    # .E.V.K.K.P.G.A.S.V.K.V.S.C.K.A.S.G.Y.T.F.T.S.Y.S.I.S.W.V.R.Q.A.P.G.Q.G.L.E.W.M.G.W.I.S.V.Y.N.G.N.T
                    # .N.Y.A.Q.K.F.Q.G.R.V.T.M.T.T.D.T.S.T.S.T.A.Y.L.E.L.R.S.L.R.S.D.D.T.A.V.Y.Y.C.A.R.D.P.I.A.A.G.Y.W.G
                    # .Q.G.T.L.V.T.V.S.S.A.S.T.K.G.P.S.V.F.P.L.A.P.S.S.K.S.T.S.G.G.T.A.A.L.G.C.L.V.K.D.Y.F.P.E.P.V.T.V.S
                    # .W.N.S.G.A.L.T.S.G.V.H.T.F.P.A.V.L.Q.S.S.G.L.Y.S.L.S.S.V.V.T.V.P.S.S.S.L.G.T.Q.T.Y.I.C.N.V.N.H.K.P
                    # .S.N.T.K.V.D.K.K.V.E.P.K.S.C.D.K.T.H.T.C.P.P.C.P.A.P.E.L.L.G.G.P.S.V.F.L.F.P.P.K.P.K.D.T.L.M.I.S.R
                    # .T.P.E.V.T.C.V.V.V.D.V.S.H.E.D.P.E.V.K.F.N.W.Y.V.D.G.V.E.V.H.N.A.K.T.K.P.R.E.E.Q.Y.N.S.T.Y.R.V.V.S
                    # .V.L.T.V.L.H.Q.D.W.L.N.G.K.E.Y.K.C.K.V.S.N.K.A.L.P.A.P.I.E.K.T.I.S.K.A.K.G.Q.P.R.E.P.Q.V.Y.T.L.P.P
                    # .S.R.E.E.M.T.K.N.Q.V.S.L.T.C.L.V.K.G.F.Y.P.S.D.I.A.V.E.W.E.S.N.G.Q.P.E.N.N.Y.K.T.T.P.P.V.L.D.S.D.G
                    # .S.F.F.L.Y.S.K.L.T.V.D.K.S.R.W.Q.Q.G.N.V.F.S.C.S.V.M.H.E.A.L.H.N.H.Y.T.Q.K.S.L.S.L.S.P.G.K}|PEPTID
                    # E3{Q.V.Q.L.V.Q.S.G.A.E.V.K.K.P.G.A.S.V.K.V.S.C.K.A.S.G.Y.T.F.T.S.Y.S.I.S.W.V.R.Q.A.P.G.Q.G.L.E.W.M
                    # .G.W.I.S.V.Y.N.G.N.T.N.Y.A.Q.K.F.Q.G.R.V.T.M.T.T.D.T.S.T.S.T.A.Y.L.E.L.R.S.L.R.S.D.D.T.A.V.Y.Y.C.A
                    # .R.D.P.I.A.A.G.Y.W.G.Q.G.T.L.V.T.V.S.S.A.S.T.K.G.P.S.V.F.P.L.A.P.S.S.K.S.T.S.G.G.T.A.A.L.G.C.L.V.K
                    # .D.Y.F.P.E.P.V.T.V.S.W.N.S.G.A.L.T.S.G.V.H.T.F.P.A.V.L.Q.S.S.G.L.Y.S.L.S.S.V.V.T.V.P.S.S.S.L.G.T.Q
                    # .T.Y.I.C.N.V.N.H.K.P.S.N.T.K.V.D.K.K.V.E.P.K.S.C.D.K.T.H.T.C.P.P.C.P.A.P.E.L.L.G.G.P.S.V.F.L.F.P.P
                    # .K.P.K.D.T.L.M.I.S.R.T.P.E.V.T.C.V.V.V.D.V.S.H.E.D.P.E.V.K.F.N.W.Y.V.D.G.V.E.V.H.N.A.K.T.K.P.R.E.E
                    # .Q.Y.N.S.T.Y.R.V.V.S.V.L.T.V.L.H.Q.D.W.L.N.G.K.E.Y.K.C.K.V.S.N.K.A.L.P.A.P.I.E.K.T.I.S.K.A.K.G.Q.P
                    # .R.E.P.Q.V.Y.T.L.P.P.S.R.E.E.M.T.K.N.Q.V.S.L.T.C.L.V.K.G.F.Y.P.S.D.I.A.V.E.W.E.S.N.G.Q.P.E.N.N.Y.K
                    # .T.T.P.P.V.L.D.S.D.G.S.F.F.L.Y.S.K.L.T.V.D.K.S.R.W.Q.Q.G.N.V.F.S.C.S.V.M.H.E.A.L.H.N.H.Y.T.Q.K.S.L
                    # .S.L.S.P.G.K}|PEPTIDE4{E.I.V.L.T.Q.S.P.G.T.L.S.L.S.P.G.E.R.A.T.L.S.C.R.A.S.Q.S.V.S.S.T.Y.L.A.W.Y.Q
                    # .Q.K.P.G.Q.A.P.R.L.L.I.Y.G.A.S.S.R.A.T.G.I.P.D.R.F.S.G.S.G.S.G.T.D.F.T.L.T.I.S.R.L.E.P.E.D.F.A.V.Y
                    # .Y.C.Q.Q.Y.G.S.S.P.R.T.F.G.Q.G.T.K.V.E.I.K.R.T.V.A.A.P.S.V.F.I.F.P.P.S.D.E.Q.L.K.S.G.T.A.S.V.V.C.L
                    # .L.N.N.F.Y.P.R.E.A.K.V.Q.W.K.V.D.N.A.L.Q.S.G.N.S.Q.E.S.V.T.E.Q.D.S.K.D.S.T.Y.S.L.S.S.T.L.T.L.S.K.A
                    # .D.Y.E.K.H.K.V.Y.A.C.E.V.T.H.Q.G.L.S.S.P.V.T.K.S.F.N.R.G.E.C}$PEPTIDE2,PEPTIDE2,143:R3-199:R3|PEPT
                    # IDE2,PEPTIDE1,219:R3-215:R3|PEPTIDE3,PEPTIDE4,219:R3-215:R3|PEPTIDE3,PEPTIDE3,260:R3-320:R3|PEPTID
                    # E2,PEPTIDE2,22:R3-96:R3|PEPTIDE3,PEPTIDE3,366:R3-424:R3|PEPTIDE4,PEPTIDE4,135:R3-195:R3|PEPTIDE1,P
                    # EPTIDE1,23:R3-89:R3|PEPTIDE2,PEPTIDE2,260:R3-320:R3|PEPTIDE2,PEPTIDE3,225:R3-225:R3|PEPTIDE1,PEPTI
                    # DE1,135:R3-195:R3|PEPTIDE2,PEPTIDE2,366:R3-424:R3|PEPTIDE3,PEPTIDE3,143:R3-199:R3|PEPTIDE4,PEPTIDE
                    # 4,23:R3-89:R3|PEPTIDE3,PEPTIDE3,22:R3-96:R3|PEPTIDE2,PEPTIDE3,228:R3-228:R3$$$' , 'PEPTIDE1{E.I.V.
                    # L.T.Q.S.P.A.T.L.S.L.S.P.G.E.R.A.T.L.S.C.S.A.S.I.S.V.S.Y.M.Y.W.Y.Q.Q.K.P.G.Q.A.P.R.L.L.I.Y.D.M.S.N.
                    # L.A.S.G.I.P.A.R.F.S.G.S.G.S.G.T.D.F.T.L.T.I.S.S.L.E.P.E.D.F.A.V.Y.Y.C.M.Q.W.S.G.Y.P.Y.T.F.G.G.G.T.
                    # K.V.E.I.K.R.T.V.A.A.P.S.V.F.I.F.P.P.S.D.E.Q.L.K.S.G.T.A.S.V.V.C.L.L.N.N.F.Y.P.R.E.A.K.V.Q.W.K.V.D.
                    # N.A.L.Q.S.G.N.S.Q.E.S.V.T.E.Q.D.S.K.D.S.T.Y.S.L.S.S.T.L.T.L.S.K.A.D.Y.E.K.H.K.V.Y.A.C.E.V.T.H.Q.G.
                    # L.S.S.P.V.T.K.S.F.N.R.G.E.C}|PEPTIDE2{E.V.Q.L.V.E.S.G.G.G.L.V.Q.P.G.G.S.L.R.L.S.C.A.A.S.G.F.T.F.S.
                    # P.F.A.M.S.W.V.R.Q.A.P.G.K.G.L.E.W.V.A.K.I.S.P.G.G.S.W.T.Y.Y.S.D.T.V.T.G.R.F.T.I.S.R.D.N.A.K.N.S.L.
                    # Y.L.Q.M.N.S.L.R.A.E.D.T.A.V.Y.Y.C.A.R.Q.L.W.G.Y.Y.A.L.D.I.W.G.Q.G.T.T.V.T.V.S.S.A.S.T.K.G.P.S.V.F.
                    # P.L.A.P.S.S.K.S.T.S.G.G.T.A.A.L.G.C.L.V.K.D.Y.F.P.E.P.V.T.V.S.W.N.S.G.A.L.T.S.G.V.H.T.F.P.A.V.L.Q.
                    # S.S.G.L.Y.S.L.S.S.V.V.T.V.P.S.S.S.L.G.T.Q.T.Y.I.C.N.V.N.H.K.P.S.N.T.K.V.D.K.K.V.E.P.K.S.C.D.K.T.H.
                    # T.C.P.P.C.P.A.P.E.L.L.G.G.P.S.V.F.L.F.P.P.K.P.K.D.T.L.M.I.S.R.T.P.E.V.T.C.V.V.V.D.V.S.H.E.D.P.E.V.
                    # K.F.N.W.Y.V.D.G.V.E.V.H.N.A.K.T.K.P.R.E.E.Q.Y.N.S.T.Y.R.V.V.S.V.L.T.V.L.H.Q.D.W.L.N.G.K.E.Y.K.C.K.
                    # V.S.N.K.A.L.P.A.P.I.E.K.T.I.S.K.A.K.G.Q.P.R.E.P.Q.V.Y.T.L.P.P.S.R.D.E.L.T.K.N.Q.V.S.L.T.C.L.V.K.G.
                    # F.Y.P.S.D.I.A.V.E.W.E.S.N.G.Q.P.E.N.N.Y.K.T.T.P.P.V.L.D.S.D.G.S.F.F.L.Y.S.K.L.T.V.D.K.S.R.W.Q.Q.G.
                    # N.V.F.S.C.S.V.M.H.E.A.L.H.N.H.Y.T.Q.K.S.L.S.L.S.P.G.K}|PEPTIDE3{E.V.Q.L.V.E.S.G.G.G.L.V.Q.P.G.G.S.
                    # L.R.L.S.C.A.A.S.G.F.T.F.S.P.F.A.M.S.W.V.R.Q.A.P.G.K.G.L.E.W.V.A.K.I.S.P.G.G.S.W.T.Y.Y.S.D.T.V.T.G.
                    # R.F.T.I.S.R.D.N.A.K.N.S.L.Y.L.Q.M.N.S.L.R.A.E.D.T.A.V.Y.Y.C.A.R.Q.L.W.G.Y.Y.A.L.D.I.W.G.Q.G.T.T.V.
                    # T.V.S.S.A.S.T.K.G.P.S.V.F.P.L.A.P.S.S.K.S.T.S.G.G.T.A.A.L.G.C.L.V.K.D.Y.F.P.E.P.V.T.V.S.W.N.S.G.A.
                    # L.T.S.G.V.H.T.F.P.A.V.L.Q.S.S.G.L.Y.S.L.S.S.V.V.T.V.P.S.S.S.L.G.T.Q.T.Y.I.C.N.V.N.H.K.P.S.N.T.K.V.
                    # D.K.K.V.E.P.K.S.C.D.K.T.H.T.C.P.P.C.P.A.P.E.L.L.G.G.P.S.V.F.L.F.P.P.K.P.K.D.T.L.M.I.S.R.T.P.E.V.T.
                    # C.V.V.V.D.V.S.H.E.D.P.E.V.K.F.N.W.Y.V.D.G.V.E.V.H.N.A.K.T.K.P.R.E.E.Q.Y.N.S.T.Y.R.V.V.S.V.L.T.V.L.
                    # H.Q.D.W.L.N.G.K.E.Y.K.C.K.V.S.N.K.A.L.P.A.P.I.E.K.T.I.S.K.A.K.G.Q.P.R.E.P.Q.V.Y.T.L.P.P.S.R.D.E.L.
                    # T.K.N.Q.V.S.L.T.C.L.V.K.G.F.Y.P.S.D.I.A.V.E.W.E.S.N.G.Q.P.E.N.N.Y.K.T.T.P.P.V.L.D.S.D.G.S.F.F.L.Y.
                    # S.K.L.T.V.D.K.S.R.W.Q.Q.G.N.V.F.S.C.S.V.M.H.E.A.L.H.N.H.Y.T.Q.K.S.L.S.L.S.P.G.K}|PEPTIDE4{E.I.V.L.
                    # T.Q.S.P.A.T.L.S.L.S.P.G.E.R.A.T.L.S.C.S.A.S.I.S.V.S.Y.M.Y.W.Y.Q.Q.K.P.G.Q.A.P.R.L.L.I.Y.D.M.S.N.L.
                    # A.S.G.I.P.A.R.F.S.G.S.G.S.G.T.D.F.T.L.T.I.S.S.L.E.P.E.D.F.A.V.Y.Y.C.M.Q.W.S.G.Y.P.Y.T.F.G.G.G.T.K.
                    # V.E.I.K.R.T.V.A.A.P.S.V.F.I.F.P.P.S.D.E.Q.L.K.S.G.T.A.S.V.V.C.L.L.N.N.F.Y.P.R.E.A.K.V.Q.W.K.V.D.N.
                    # A.L.Q.S.G.N.S.Q.E.S.V.T.E.Q.D.S.K.D.S.T.Y.S.L.S.S.T.L.T.L.S.K.A.D.Y.E.K.H.K.V.Y.A.C.E.V.T.H.Q.G.L.
                    # S.S.P.V.T.K.S.F.N.R.G.E.C}$PEPTIDE1,PEPTIDE1,23:R3-87:R3|PEPTIDE3,PEPTIDE4,222:R3-213:R3|PEPTIDE2,
                    # PEPTIDE2,22:R3-96:R3|PEPTIDE1,PEPTIDE1,133:R3-193:R3|PEPTIDE4,PEPTIDE4,133:R3-193:R3|PEPTIDE2,PEPT
                    # IDE2,146:R3-202:R3|PEPTIDE3,PEPTIDE3,369:R3-427:R3|PEPTIDE2,PEPTIDE1,222:R3-213:R3|PEPTIDE3,PEPTID
                    # E3,146:R3-202:R3|PEPTIDE3,PEPTIDE3,22:R3-96:R3|PEPTIDE3,PEPTIDE3,263:R3-323:R3|PEPTIDE2,PEPTIDE2,2
                    # 63:R3-323:R3|PEPTIDE2,PEPTIDE3,228:R3-228:R3|PEPTIDE4,PEPTIDE4,23:R3-87:R3|PEPTIDE2,PEPTIDE2,369:R
                    # 3-427:R3|PEPTIDE2,PEPTIDE3,231:R3-231:R3$$$' , 'PEPTIDE1{D.V.V.M.T.Q.S.P.L.S.L.P.V.T.L.G.Q.P.A.S.I
                    # .S.C.R.S.S.Q.S.L.I.Y.S.D.G.N.A.Y.L.H.W.F.L.Q.K.P.G.Q.S.P.R.L.L.I.Y.K.V.S.N.R.F.S.G.V.P.D.R.F.S.G.S
                    # .G.S.G.T.D.F.T.L.K.I.S.R.V.E.A.E.D.V.G.V.Y.Y.C.S.Q.S.T.H.V.P.W.T.F.G.Q.G.T.K.V.E.I.K.R.T.V.A.A.P.S
                    # .V.F.I.F.P.P.S.D.E.Q.L.K.S.G.T.A.S.V.V.C.L.L.N.N.F.Y.P.R.E.A.K.V.Q.W.K.V.D.N.A.L.Q.S.G.N.S.Q.E.S.V
                    # .T.E.Q.D.S.K.D.S.T.Y.S.L.S.S.T.L.T.L.S.K.A.D.Y.E.K.H.K.V.Y.A.C.E.V.T.H.Q.G.L.S.S.P.V.T.K.S.F.N.R.G
                    # .E.C}|PEPTIDE2{E.V.Q.L.V.E.S.G.G.G.L.V.Q.P.G.G.S.L.R.L.S.C.A.A.S.G.F.T.F.S.R.Y.S.M.S.W.V.R.Q.A.P.G
                    # .K.G.L.E.L.V.A.Q.I.N.S.V.G.N.S.T.Y.Y.P.D.T.V.K.G.R.F.T.I.S.R.D.N.A.K.N.T.L.Y.L.Q.M.N.S.L.R.A.E.D.T
                    # .A.V.Y.Y.C.A.S.G.D.Y.W.G.Q.G.T.L.V.T.V.S.S.A.S.T.K.G.P.S.V.F.P.L.A.P.S.S.K.S.T.S.G.G.T.A.A.L.G.C.L
                    # .V.K.D.Y.F.P.E.P.V.T.V.S.W.N.S.G.A.L.T.S.G.V.H.T.F.P.A.V.L.Q.S.S.G.L.Y.S.L.S.S.V.V.T.V.P.S.S.S.L.G
                    # .T.Q.T.Y.I.C.N.V.N.H.K.P.S.N.T.K.V.D.K.K.V.E.P.K.S.C.D.K.T.H.T.C.P.P.C.P.A.P.E.L.L.G.G.P.S.V.F.L.F
                    # .P.P.K.P.K.D.T.L.M.I.S.R.T.P.E.V.T.C.V.V.V.D.V.S.H.E.D.P.E.V.K.F.N.W.Y.V.D.G.V.E.V.H.N.A.K.T.K.P.R
                    # .E.E.Q.Y.N.S.T.Y.R.V.V.S.V.L.T.V.L.H.Q.D.W.L.N.G.K.E.Y.K.C.K.V.S.N.K.A.L.P.A.P.I.E.K.T.I.S.K.A.K.G
                    # .Q.P.R.E.P.Q.V.Y.T.L.P.P.S.R.D.E.L.T.K.N.Q.V.S.L.T.C.L.V.K.G.F.Y.P.S.D.I.A.V.E.W.E.S.N.G.Q.P.E.N.N
                    # .Y.K.T.T.P.P.V.L.D.S.D.G.S.F.F.L.Y.S.K.L.T.V.D.K.S.R.W.Q.Q.G.N.V.F.S.C.S.V.M.H.E.A.L.H.N.H.Y.T.Q.K
                    # .S.L.S.L.S.P.G.K}|PEPTIDE3{E.V.Q.L.V.E.S.G.G.G.L.V.Q.P.G.G.S.L.R.L.S.C.A.A.S.G.F.T.F.S.R.Y.S.M.S.W
                    # .V.R.Q.A.P.G.K.G.L.E.L.V.A.Q.I.N.S.V.G.N.S.T.Y.Y.P.D.T.V.K.G.R.F.T.I.S.R.D.N.A.K.N.T.L.Y.L.Q.M.N.S
                    # .L.R.A.E.D.T.A.V.Y.Y.C.A.S.G.D.Y.W.G.Q.G.T.L.V.T.V.S.S.A.S.T.K.G.P.S.V.F.P.L.A.P.S.S.K.S.T.S.G.G.T
                    # .A.A.L.G.C.L.V.K.D.Y.F.P.E.P.V.T.V.S.W.N.S.G.A.L.T.S.G.V.H.T.F.P.A.V.L.Q.S.S.G.L.Y.S.L.S.S.V.V.T.V
                    # .P.S.S.S.L.G.T.Q.T.Y.I.C.N.V.N.H.K.P.S.N.T.K.V.D.K.K.V.E.P.K.S.C.D.K.T.H.T.C.P.P.C.P.A.P.E.L.L.G.G
                    # .P.S.V.F.L.F.P.P.K.P.K.D.T.L.M.I.S.R.T.P.E.V.T.C.V.V.V.D.V.S.H.E.D.P.E.V.K.F.N.W.Y.V.D.G.V.E.V.H.N
                    # .A.K.T.K.P.R.E.E.Q.Y.N.S.T.Y.R.V.V.S.V.L.T.V.L.H.Q.D.W.L.N.G.K.E.Y.K.C.K.V.S.N.K.A.L.P.A.P.I.E.K.T
                    # .I.S.K.A.K.G.Q.P.R.E.P.Q.V.Y.T.L.P.P.S.R.D.E.L.T.K.N.Q.V.S.L.T.C.L.V.K.G.F.Y.P.S.D.I.A.V.E.W.E.S.N
                    # .G.Q.P.E.N.N.Y.K.T.T.P.P.V.L.D.S.D.G.S.F.F.L.Y.S.K.L.T.V.D.K.S.R.W.Q.Q.G.N.V.F.S.C.S.V.M.H.E.A.L.H
                    # .N.H.Y.T.Q.K.S.L.S.L.S.P.G.K}|PEPTIDE4{D.V.V.M.T.Q.S.P.L.S.L.P.V.T.L.G.Q.P.A.S.I.S.C.R.S.S.Q.S.L.I
                    # .Y.S.D.G.N.A.Y.L.H.W.F.L.Q.K.P.G.Q.S.P.R.L.L.I.Y.K.V.S.N.R.F.S.G.V.P.D.R.F.S.G.S.G.S.G.T.D.F.T.L.K
                    # .I.S.R.V.E.A.E.D.V.G.V.Y.Y.C.S.Q.S.T.H.V.P.W.T.F.G.Q.G.T.K.V.E.I.K.R.T.V.A.A.P.S.V.F.I.F.P.P.S.D.E
                    # .Q.L.K.S.G.T.A.S.V.V.C.L.L.N.N.F.Y.P.R.E.A.K.V.Q.W.K.V.D.N.A.L.Q.S.G.N.S.Q.E.S.V.T.E.Q.D.S.K.D.S.T
                    # .Y.S.L.S.S.T.L.T.L.S.K.A.D.Y.E.K.H.K.V.Y.A.C.E.V.T.H.Q.G.L.S.S.P.V.T.K.S.F.N.R.G.E.C}$PEPTIDE2,PEP
                    # TIDE2,362:R3-420:R3|PEPTIDE3,PEPTIDE3,256:R3-316:R3|PEPTIDE3,PEPTIDE4,215:R3-219:R3|PEPTIDE4,PEPTI
                    # DE4,23:R3-93:R3|PEPTIDE2,PEPTIDE2,256:R3-316:R3|PEPTIDE2,PEPTIDE3,224:R3-224:R3|PEPTIDE2,PEPTIDE1,
                    # 215:R3-219:R3|PEPTIDE2,PEPTIDE3,221:R3-221:R3|PEPTIDE2,PEPTIDE2,22:R3-96:R3|PEPTIDE4,PEPTIDE4,139:
                    # R3-199:R3|PEPTIDE1,PEPTIDE1,23:R3-93:R3|PEPTIDE3,PEPTIDE3,362:R3-420:R3|PEPTIDE2,PEPTIDE2,139:R3-1
                    # 95:R3|PEPTIDE1,PEPTIDE1,139:R3-199:R3|PEPTIDE3,PEPTIDE3,139:R3-195:R3|PEPTIDE3,PEPTIDE3,22:R3-96:R
                    # 3$$$'
                    'molecule_chembl_id': 'TEXT',
                    # EXAMPLES:
                    # 'CHEMBL1743039' , 'CHEMBL1743040' , 'CHEMBL1743044' , 'CHEMBL1743046' , 'CHEMBL1743047' , 'CHEMBL1
                    # 743051' , 'CHEMBL1743052' , 'CHEMBL1743055' , 'CHEMBL1743057' , 'CHEMBL1743058'
                }
            },
            'black_box': 'BOOLEAN',
            # EXAMPLES:
            # 'False' , 'False' , 'True' , 'False' , 'False' , 'False' , 'True' , 'False' , 'False' , 'False'
            'chirality': 'NUMERIC',
            # EXAMPLES:
            # '2' , '1' , '0' , '2' , '2' , '2' , '2' , '1' , '2' , '1'
            'development_phase': 'NUMERIC',
            # EXAMPLES:
            # '4' , '4' , '4' , '4' , '2' , '3' , '4' , '4' , '0' , '4'
            'drug_type': 'NUMERIC',
            # EXAMPLES:
            # '1' , '1' , '1' , '1' , '1' , '7' , '1' , '7' , '1' , '7'
            'drug_warnings': 
            {
                'properties': 
                {
                    'warning_class': 'TEXT',
                    # EXAMPLES:
                    # 'Neurotoxicity' , 'Neurotoxicity' , 'Neurotoxicity' , 'Misuse' , 'Neurotoxicity' , 'Hepatotoxicity
                    # ' , 'Carcinogenicity' , 'Carcinogenicity' , 'Cardiotoxicity' , 'Gastrotoxicity'
                    'warning_country': 'TEXT',
                    # EXAMPLES:
                    # 'United States' , 'United States' , 'United States' , 'Canada; Italy; Argentina' , 'United States'
                    #  , 'Norway' , 'Norway' , 'Norway' , 'United Kingdom' , 'United Kingdom; United States; Germany; Fr
                    # ance'
                    'warning_description': 'TEXT',
                    # EXAMPLES:
                    # 'Hepatotoxicity' , 'Increased risk of dysglycemia' , 'Hepatic necrosis' , 'Self-poisonings' , 'Sel
                    # f-Poisonings' , 'Self-Poisonings' , 'Liver Toxicity and Death' , 'Risk for birth defects' , 'Cardi
                    # ac arrythmias' , 'Neurotoxicity'
                    'warning_id': 'NUMERIC',
                    # EXAMPLES:
                    # '1364' , '944' , '373' , '1350' , '108' , '767' , '2190' , '2425' , '2110' , '1716'
                    'warning_refs': 
                    {
                        'properties': 
                        {
                            'ref_id': 'TEXT',
                            # EXAMPLES:
                            # 'ee1bf431-97fa-4aba-9cc3-0cfcea779ca2' , '4babe1c2-15f2-40af-b326-b256507a921c' , '7049f87
                            # 0-6741-4a67-8033-398c36126a06' , 'eb1cc8d0-4231-41ea-8535-4fd872129713' , '8175c1eb-80af-4
                            # 8f1-813c-c8f0e736d894' , '10.1177/009286150103500134' , 'f84b28ff-aae1-4796-a8f0-e06e14623
                            # 5a2' , 'CFR-2019-title21-vol4/pdf/CFR-2019-title21-vol4-sec216-24.pdf' , '6a85ad01-8144-4d
                            # 9c-e053-2991aa0a4f85' , 'ae951dc4-9031-43bf-943c-cb2366951f23'
                            'ref_type': 'TEXT',
                            # EXAMPLES:
                            # 'FDA' , 'FDA' , 'FDA' , 'FDA' , 'FDA' , 'DOI' , 'FDA' , 'USGPO' , 'FDA' , 'FDA'
                            'ref_url': 'TEXT',
                            # EXAMPLES:
                            # 'https://api.fda.gov/drug/label.json?search=set_id:ee1bf431-97fa-4aba-9cc3-0cfcea779ca2' ,
                            #  'https://api.fda.gov/drug/label.json?search=set_id:4babe1c2-15f2-40af-b326-b256507a921c' 
                            # , 'https://api.fda.gov/drug/label.json?search=set_id:7049f870-6741-4a67-8033-398c36126a06'
                            #  , 'https://api.fda.gov/drug/label.json?search=set_id:eb1cc8d0-4231-41ea-8535-4fd872129713
                            # ' , 'https://api.fda.gov/drug/label.json?search=set_id:8175c1eb-80af-48f1-813c-c8f0e736d89
                            # 4' , 'https://doi.org/10.1177/009286150103500134' , 'https://api.fda.gov/drug/label.json?s
                            # earch=set_id:f84b28ff-aae1-4796-a8f0-e06e146235a2' , 'https://www.govinfo.gov/content/pkg/
                            # CFR-2019-title21-vol4/pdf/CFR-2019-title21-vol4-sec216-24.pdf' , 'https://api.fda.gov/drug
                            # /label.json?search=set_id:6a85ad01-8144-4d9c-e053-2991aa0a4f85' , 'https://api.fda.gov/dru
                            # g/label.json?search=set_id:ae951dc4-9031-43bf-943c-cb2366951f23'
                        }
                    },
                    'warning_type': 'TEXT',
                    # EXAMPLES:
                    # 'Black Box Warning' , 'Black Box Warning' , 'Black Box Warning' , 'Black Box Warning' , 'Black Box
                    #  Warning' , 'Black Box Warning' , 'Withdrawn' , 'Black Box Warning' , 'Withdrawn' , 'Black Box War
                    # ning'
                    'warning_year': 'NUMERIC',
                    # EXAMPLES:
                    # '1997' , '2006' , '1996' , '1980' , '1980' , '1980' , '1986' , '1980' , '1989' , '2005'
                }
            },
            'first_approval': 'NUMERIC',
            # EXAMPLES:
            # '1976' , '1984' , '1990' , '1964' , '1965' , '1986' , '1993' , '1987' , '1986' , '1955'
            'first_in_class': 'BOOLEAN',
            # EXAMPLES:
            # 'False' , 'False' , 'False' , 'False' , 'False' , 'False' , 'False' , 'False' , 'False' , 'False'
            'helm_notation': 'TEXT',
            # EXAMPLES:
            # 'PEPTIDE1{D.I.Q.L.T.Q.S.P.L.S.L.P.V.T.L.G.Q.P.A.S.I.S.C.R.S.S.Q.S.L.V.H.R.N.G.N.T.Y.L.H.W.F.Q.Q.R.P.G.Q.S.
            # P.R.L.L.I.Y.T.V.S.N.R.F.S.G.V.P.D.R.F.S.G.S.G.S.G.T.D.F.T.L.K.I.S.R.V.E.A.E.D.V.G.V.Y.F.C.S.Q.S.S.H.V.P.P.
            # T.F.G.A.G.T.R.L.E.I.K.R.T.V.A.A.P.S.V.F.I.F.P.P.S.D.E.Q.L.K.S.G.T.A.S.V.V.C.L.L.N.N.F.Y.P.R.E.A.K.V.Q.W.K.
            # V.D.N.A.L.Q.S.G.N.S.Q.E.S.V.T.E.Q.D.S.K.D.S.T.Y.S.L.S.S.T.L.T.L.S.K.A.D.Y.E.K.H.K.V.Y.A.C.E.V.T.H.Q.G.L.S.
            # S.P.V.T.K.S.F.N.R.G.E.C}|PEPTIDE2{Q.V.Q.L.Q.Q.S.G.S.E.L.K.K.P.G.A.S.V.K.V.S.C.K.A.S.G.Y.T.F.T.N.Y.G.V.N.W.
            # I.K.Q.A.P.G.Q.G.L.Q.W.M.G.W.I.N.P.N.T.G.E.P.T.F.D.D.D.F.K.G.R.F.A.F.S.L.D.T.S.V.S.T.A.Y.L.Q.I.S.S.L.K.A.D.
            # D.T.A.V.Y.F.C.S.R.S.R.G.K.N.E.A.W.F.A.Y.W.G.Q.G.T.L.V.T.V.S.S.A.S.T.K.G.P.S.V.F.P.L.A.P.S.S.K.S.T.S.G.G.T.
            # A.A.L.G.C.L.V.K.D.Y.F.P.E.P.V.T.V.S.W.N.S.G.A.L.T.S.G.V.H.T.F.P.A.V.L.Q.S.S.G.L.Y.S.L.S.S.V.V.T.V.P.S.S.S.
            # L.G.T.Q.T.Y.I.C.N.V.N.H.K.P.S.N.T.K.V.D.K.R.V.E.P.K.S.C.D.K.T.H.T.C.P.P.C.P.A.P.E.L.L.G.G.P.S.V.F.L.F.P.P.
            # K.P.K.D.T.L.M.I.S.R.T.P.E.V.T.C.V.V.V.D.V.S.H.E.D.P.E.V.K.F.N.W.Y.V.D.G.V.E.V.H.N.A.K.T.K.P.R.E.E.Q.Y.N.S.
            # T.Y.R.V.V.S.V.L.T.V.L.H.Q.D.W.L.N.G.K.E.Y.K.C.K.V.S.N.K.A.L.P.A.P.I.E.K.T.I.S.K.A.K.G.Q.P.R.E.P.Q.V.Y.T.L.
            # P.P.S.R.E.E.M.T.K.N.Q.V.S.L.T.C.L.V.K.G.F.Y.P.S.D.I.A.V.E.W.E.S.N.G.Q.P.E.N.N.Y.K.T.T.P.P.V.L.D.S.D.G.S.F.
            # F.L.Y.S.K.L.T.V.D.K.S.R.W.Q.Q.G.N.V.F.S.C.S.V.M.H.E.A.L.H.N.H.Y.T.Q.K.S.L.S.L.S.P.G.K}|PEPTIDE3{Q.V.Q.L.Q.
            # Q.S.G.S.E.L.K.K.P.G.A.S.V.K.V.S.C.K.A.S.G.Y.T.F.T.N.Y.G.V.N.W.I.K.Q.A.P.G.Q.G.L.Q.W.M.G.W.I.N.P.N.T.G.E.P.
            # T.F.D.D.D.F.K.G.R.F.A.F.S.L.D.T.S.V.S.T.A.Y.L.Q.I.S.S.L.K.A.D.D.T.A.V.Y.F.C.S.R.S.R.G.K.N.E.A.W.F.A.Y.W.G.
            # Q.G.T.L.V.T.V.S.S.A.S.T.K.G.P.S.V.F.P.L.A.P.S.S.K.S.T.S.G.G.T.A.A.L.G.C.L.V.K.D.Y.F.P.E.P.V.T.V.S.W.N.S.G.
            # A.L.T.S.G.V.H.T.F.P.A.V.L.Q.S.S.G.L.Y.S.L.S.S.V.V.T.V.P.S.S.S.L.G.T.Q.T.Y.I.C.N.V.N.H.K.P.S.N.T.K.V.D.K.R.
            # V.E.P.K.S.C.D.K.T.H.T.C.P.P.C.P.A.P.E.L.L.G.G.P.S.V.F.L.F.P.P.K.P.K.D.T.L.M.I.S.R.T.P.E.V.T.C.V.V.V.D.V.S.
            # H.E.D.P.E.V.K.F.N.W.Y.V.D.G.V.E.V.H.N.A.K.T.K.P.R.E.E.Q.Y.N.S.T.Y.R.V.V.S.V.L.T.V.L.H.Q.D.W.L.N.G.K.E.Y.K.
            # C.K.V.S.N.K.A.L.P.A.P.I.E.K.T.I.S.K.A.K.G.Q.P.R.E.P.Q.V.Y.T.L.P.P.S.R.E.E.M.T.K.N.Q.V.S.L.T.C.L.V.K.G.F.Y.
            # P.S.D.I.A.V.E.W.E.S.N.G.Q.P.E.N.N.Y.K.T.T.P.P.V.L.D.S.D.G.S.F.F.L.Y.S.K.L.T.V.D.K.S.R.W.Q.Q.G.N.V.F.S.C.S.
            # V.M.H.E.A.L.H.N.H.Y.T.Q.K.S.L.S.L.S.P.G.K}|PEPTIDE4{D.I.Q.L.T.Q.S.P.L.S.L.P.V.T.L.G.Q.P.A.S.I.S.C.R.S.S.Q.
            # S.L.V.H.R.N.G.N.T.Y.L.H.W.F.Q.Q.R.P.G.Q.S.P.R.L.L.I.Y.T.V.S.N.R.F.S.G.V.P.D.R.F.S.G.S.G.S.G.T.D.F.T.L.K.I.
            # S.R.V.E.A.E.D.V.G.V.Y.F.C.S.Q.S.S.H.V.P.P.T.F.G.A.G.T.R.L.E.I.K.R.T.V.A.A.P.S.V.F.I.F.P.P.S.D.E.Q.L.K.S.G.
            # T.A.S.V.V.C.L.L.N.N.F.Y.P.R.E.A.K.V.Q.W.K.V.D.N.A.L.Q.S.G.N.S.Q.E.S.V.T.E.Q.D.S.K.D.S.T.Y.S.L.S.S.T.L.T.L.
            # S.K.A.D.Y.E.K.H.K.V.Y.A.C.E.V.T.H.Q.G.L.S.S.P.V.T.K.S.F.N.R.G.E.C}$PEPTIDE4,PEPTIDE4,23:R3-93:R3|PEPTIDE2,
            # PEPTIDE3,232:R3-232:R3|PEPTIDE3,PEPTIDE3,22:R3-96:R3|PEPTIDE2,PEPTIDE2,147:R3-203:R3|PEPTIDE2,PEPTIDE2,370
            # :R3-428:R3|PEPTIDE3,PEPTIDE3,147:R3-203:R3|PEPTIDE3,PEPTIDE3,370:R3-428:R3|PEPTIDE1,PEPTIDE1,23:R3-93:R3|P
            # EPTIDE3,PEPTIDE3,264:R3-324:R3|PEPTIDE2,PEPTIDE2,22:R3-96:R3|PEPTIDE2,PEPTIDE2,264:R3-324:R3|PEPTIDE3,PEPT
            # IDE4,223:R3-219:R3|PEPTIDE2,PEPTIDE1,223:R3-219:R3|PEPTIDE4,PEPTIDE4,139:R3-199:R3|PEPTIDE2,PEPTIDE3,229:R
            # 3-229:R3|PEPTIDE1,PEPTIDE1,139:R3-199:R3$$$' , 'PEPTIDE1{D.I.Q.M.T.Q.S.P.S.S.V.S.A.S.V.G.D.R.V.T.I.A.C.R.A
            # .S.Q.N.I.R.N.I.L.N.W.Y.Q.Q.R.P.G.K.A.P.Q.L.L.I.Y.A.A.S.N.L.Q.S.G.V.P.S.R.F.S.G.S.G.S.G.T.D.F.T.L.T.I.N.S.L
            # .Q.P.E.D.F.A.T.Y.Y.C.Q.Q.S.Y.S.M.P.R.T.F.G.G.G.T.K.L.E.I.K.R.T.V.A.A.P.S.V.F.I.F.P.P.S.D.E.Q.L.K.S.G.T.A.S
            # .V.V.C.L.L.N.N.F.Y.P.R.E.A.K.V.Q.W.K.V.D.N.A.L.Q.S.G.N.S.Q.E.S.V.T.E.Q.D.S.K.D.S.T.Y.S.L.S.S.T.L.T.L.S.K.A
            # .D.Y.E.K.H.K.V.Y.A.C.E.V.T.H.Q.G.L.S.S.P.V.T.K.S.F.N.R.G.E.C}|PEPTIDE2{Q.V.Q.L.V.Q.S.G.A.E.V.K.K.P.G.A.S.V
            # .K.V.S.C.K.A.F.G.Y.P.F.T.D.Y.L.L.H.W.V.R.Q.A.P.G.Q.G.L.E.W.V.G.W.L.N.P.Y.S.G.D.T.N.Y.A.Q.K.F.Q.G.R.V.T.M.T
            # .R.D.T.S.I.S.T.A.Y.M.E.L.S.R.L.R.S.D.D.T.A.V.Y.Y.C.T.R.T.T.L.I.S.V.Y.F.D.Y.W.G.Q.G.T.M.V.T.V.S.S.A.S.T.K.G
            # .P.S.V.F.P.L.A.P.S.S.K.S.T.S.G.G.T.A.A.L.G.C.L.V.K.D.Y.F.P.E.P.V.T.V.S.W.N.S.G.A.L.T.S.G.V.H.T.F.P.A.V.L.Q
            # .S.S.G.L.Y.S.L.S.S.V.V.T.V.P.S.S.S.L.G.T.Q.T.Y.I.C.N.V.N.H.K.P.S.N.T.K.V.D.K.K.V.E.P.K.S.C.D.K.T.H.T.C.P.P
            # .C.P.A.P.E.L.L.G.G.P.S.V.F.L.F.P.P.K.P.K.D.T.L.M.I.S.R.T.P.E.V.T.C.V.V.V.D.V.S.H.E.D.P.E.V.K.F.N.W.Y.V.D.G
            # .V.E.V.H.N.A.K.T.K.P.R.E.E.Q.Y.N.S.T.Y.R.V.V.S.V.L.T.V.L.H.Q.D.W.L.N.G.K.E.Y.K.C.K.V.S.N.K.A.L.P.A.P.I.E.K
            # .T.I.S.K.A.K.G.Q.P.R.E.P.Q.V.Y.T.L.P.P.S.R.D.E.L.T.K.N.Q.V.S.L.T.C.L.V.K.G.F.Y.P.S.D.I.A.V.E.W.E.S.N.G.Q.P
            # .E.N.N.Y.K.T.T.P.P.V.L.D.S.D.G.S.F.F.L.Y.S.K.L.T.V.D.K.S.R.W.Q.Q.G.N.V.F.S.C.S.V.M.H.E.A.L.H.N.H.Y.T.Q.K.S
            # .L.S.L.S.P.G.K}|PEPTIDE3{Q.V.Q.L.V.Q.S.G.A.E.V.K.K.P.G.A.S.V.K.V.S.C.K.A.F.G.Y.P.F.T.D.Y.L.L.H.W.V.R.Q.A.P
            # .G.Q.G.L.E.W.V.G.W.L.N.P.Y.S.G.D.T.N.Y.A.Q.K.F.Q.G.R.V.T.M.T.R.D.T.S.I.S.T.A.Y.M.E.L.S.R.L.R.S.D.D.T.A.V.Y
            # .Y.C.T.R.T.T.L.I.S.V.Y.F.D.Y.W.G.Q.G.T.M.V.T.V.S.S.A.S.T.K.G.P.S.V.F.P.L.A.P.S.S.K.S.T.S.G.G.T.A.A.L.G.C.L
            # .V.K.D.Y.F.P.E.P.V.T.V.S.W.N.S.G.A.L.T.S.G.V.H.T.F.P.A.V.L.Q.S.S.G.L.Y.S.L.S.S.V.V.T.V.P.S.S.S.L.G.T.Q.T.Y
            # .I.C.N.V.N.H.K.P.S.N.T.K.V.D.K.K.V.E.P.K.S.C.D.K.T.H.T.C.P.P.C.P.A.P.E.L.L.G.G.P.S.V.F.L.F.P.P.K.P.K.D.T.L
            # .M.I.S.R.T.P.E.V.T.C.V.V.V.D.V.S.H.E.D.P.E.V.K.F.N.W.Y.V.D.G.V.E.V.H.N.A.K.T.K.P.R.E.E.Q.Y.N.S.T.Y.R.V.V.S
            # .V.L.T.V.L.H.Q.D.W.L.N.G.K.E.Y.K.C.K.V.S.N.K.A.L.P.A.P.I.E.K.T.I.S.K.A.K.G.Q.P.R.E.P.Q.V.Y.T.L.P.P.S.R.D.E
            # .L.T.K.N.Q.V.S.L.T.C.L.V.K.G.F.Y.P.S.D.I.A.V.E.W.E.S.N.G.Q.P.E.N.N.Y.K.T.T.P.P.V.L.D.S.D.G.S.F.F.L.Y.S.K.L
            # .T.V.D.K.S.R.W.Q.Q.G.N.V.F.S.C.S.V.M.H.E.A.L.H.N.H.Y.T.Q.K.S.L.S.L.S.P.G.K}|PEPTIDE4{D.I.Q.M.T.Q.S.P.S.S.V
            # .S.A.S.V.G.D.R.V.T.I.A.C.R.A.S.Q.N.I.R.N.I.L.N.W.Y.Q.Q.R.P.G.K.A.P.Q.L.L.I.Y.A.A.S.N.L.Q.S.G.V.P.S.R.F.S.G
            # .S.G.S.G.T.D.F.T.L.T.I.N.S.L.Q.P.E.D.F.A.T.Y.Y.C.Q.Q.S.Y.S.M.P.R.T.F.G.G.G.T.K.L.E.I.K.R.T.V.A.A.P.S.V.F.I
            # .F.P.P.S.D.E.Q.L.K.S.G.T.A.S.V.V.C.L.L.N.N.F.Y.P.R.E.A.K.V.Q.W.K.V.D.N.A.L.Q.S.G.N.S.Q.E.S.V.T.E.Q.D.S.K.D
            # .S.T.Y.S.L.S.S.T.L.T.L.S.K.A.D.Y.E.K.H.K.V.Y.A.C.E.V.T.H.Q.G.L.S.S.P.V.T.K.S.F.N.R.G.E.C}$PEPTIDE3,PEPTIDE
            # 4,222:R3-214:R3|PEPTIDE1,PEPTIDE1,134:R3-194:R3|PEPTIDE2,PEPTIDE3,231:R3-231:R3|PEPTIDE4,PEPTIDE4,23:R3-88
            # :R3|PEPTIDE3,PEPTIDE3,369:R3-427:R3|PEPTIDE2,PEPTIDE2,369:R3-427:R3|PEPTIDE1,PEPTIDE1,23:R3-88:R3|PEPTIDE2
            # ,PEPTIDE2,146:R3-202:R3|PEPTIDE4,PEPTIDE4,134:R3-194:R3|PEPTIDE2,PEPTIDE2,22:R3-96:R3|PEPTIDE3,PEPTIDE3,26
            # 3:R3-323:R3|PEPTIDE3,PEPTIDE3,22:R3-96:R3|PEPTIDE2,PEPTIDE1,222:R3-214:R3|PEPTIDE3,PEPTIDE3,146:R3-202:R3|
            # PEPTIDE2,PEPTIDE3,228:R3-228:R3|PEPTIDE2,PEPTIDE2,263:R3-323:R3$$$' , 'PEPTIDE1{E.I.V.L.T.Q.S.P.A.T.L.S.L.
            # S.P.G.E.R.A.T.L.S.C.R.A.S.Q.S.V.S.R.Y.L.A.W.Y.Q.Q.K.P.G.Q.A.P.R.L.L.I.Y.D.A.S.N.R.A.T.G.I.P.A.R.F.S.G.S.G.
            # S.G.T.D.F.T.L.T.I.S.S.L.E.P.E.D.F.A.V.Y.Y.C.Q.Q.R.S.N.W.P.R.T.F.G.Q.G.T.K.V.E.I.K.R.T.V.A.A.P.S.V.F.I.F.P.
            # P.S.D.E.Q.L.K.S.G.T.A.S.V.V.C.L.L.N.N.F.Y.P.R.E.A.K.V.Q.W.K.V.D.N.A.L.Q.S.G.N.S.Q.E.S.V.T.E.Q.D.S.K.D.S.T.
            # Y.S.L.S.S.T.L.T.L.S.K.A.D.Y.E.K.H.K.V.Y.A.C.E.V.T.H.Q.G.L.S.S.P.V.T.K.S.F.N.R.G.E.C}|PEPTIDE2{E.V.Q.L.V.E.
            # S.G.G.G.L.V.Q.P.G.G.S.L.R.L.S.C.A.A.S.G.F.T.F.S.S.Y.L.M.T.W.V.R.Q.A.P.G.K.G.L.E.W.V.A.N.I.K.Q.D.G.S.E.K.Y.
            # Y.V.D.S.V.K.G.R.F.T.I.S.R.D.N.A.K.N.S.L.N.L.Q.M.N.S.L.R.A.E.D.T.A.V.Y.Y.C.T.R.D.G.Y.S.S.G.R.H.Y.G.M.D.V.W.
            # G.Q.G.T.T.V.I.V.S.S.A.S.T.K.G.P.S.V.F.P.L.A.P.S.S.K.S.T.S.G.G.T.A.A.L.G.C.L.V.K.D.Y.F.P.E.P.V.T.V.S.W.N.S.
            # G.A.L.T.S.G.V.H.T.F.P.A.V.L.Q.S.S.G.L.Y.S.L.S.S.V.V.T.V.P.S.S.S.L.G.T.Q.T.Y.I.C.N.V.N.H.K.P.S.N.T.K.V.D.K.
            # R.V.E.P.K.S.C.D.K.T.H.T.C.P.P.C.P.A.P.E.L.L.G.G.P.S.V.F.L.F.P.P.K.P.K.D.T.L.M.I.S.R.T.P.E.V.T.C.V.V.V.D.V.
            # S.H.E.D.P.E.V.K.F.N.W.Y.V.D.G.V.E.V.H.N.A.K.T.K.P.R.E.E.Q.Y.N.S.T.Y.R.V.V.S.V.L.T.V.L.H.Q.D.W.L.N.G.K.E.Y.
            # K.C.K.V.S.N.K.A.L.P.A.P.I.E.K.T.I.S.K.A.K.G.Q.P.R.E.P.Q.V.Y.T.L.P.P.S.R.E.E.M.T.K.N.Q.V.S.L.T.C.L.V.K.G.F.
            # Y.P.S.D.I.A.V.E.W.E.S.N.G.Q.P.E.N.N.Y.K.T.T.P.P.V.L.D.S.D.G.S.F.F.L.Y.S.K.L.T.V.D.K.S.R.W.Q.Q.G.N.V.F.S.C.
            # S.V.M.H.E.A.L.H.N.H.Y.T.Q.K.S.L.S.L.S.P.G.K}|PEPTIDE3{E.V.Q.L.V.E.S.G.G.G.L.V.Q.P.G.G.S.L.R.L.S.C.A.A.S.G.
            # F.T.F.S.S.Y.L.M.T.W.V.R.Q.A.P.G.K.G.L.E.W.V.A.N.I.K.Q.D.G.S.E.K.Y.Y.V.D.S.V.K.G.R.F.T.I.S.R.D.N.A.K.N.S.L.
            # N.L.Q.M.N.S.L.R.A.E.D.T.A.V.Y.Y.C.T.R.D.G.Y.S.S.G.R.H.Y.G.M.D.V.W.G.Q.G.T.T.V.I.V.S.S.A.S.T.K.G.P.S.V.F.P.
            # L.A.P.S.S.K.S.T.S.G.G.T.A.A.L.G.C.L.V.K.D.Y.F.P.E.P.V.T.V.S.W.N.S.G.A.L.T.S.G.V.H.T.F.P.A.V.L.Q.S.S.G.L.Y.
            # S.L.S.S.V.V.T.V.P.S.S.S.L.G.T.Q.T.Y.I.C.N.V.N.H.K.P.S.N.T.K.V.D.K.R.V.E.P.K.S.C.D.K.T.H.T.C.P.P.C.P.A.P.E.
            # L.L.G.G.P.S.V.F.L.F.P.P.K.P.K.D.T.L.M.I.S.R.T.P.E.V.T.C.V.V.V.D.V.S.H.E.D.P.E.V.K.F.N.W.Y.V.D.G.V.E.V.H.N.
            # A.K.T.K.P.R.E.E.Q.Y.N.S.T.Y.R.V.V.S.V.L.T.V.L.H.Q.D.W.L.N.G.K.E.Y.K.C.K.V.S.N.K.A.L.P.A.P.I.E.K.T.I.S.K.A.
            # K.G.Q.P.R.E.P.Q.V.Y.T.L.P.P.S.R.E.E.M.T.K.N.Q.V.S.L.T.C.L.V.K.G.F.Y.P.S.D.I.A.V.E.W.E.S.N.G.Q.P.E.N.N.Y.K.
            # T.T.P.P.V.L.D.S.D.G.S.F.F.L.Y.S.K.L.T.V.D.K.S.R.W.Q.Q.G.N.V.F.S.C.S.V.M.H.E.A.L.H.N.H.Y.T.Q.K.S.L.S.L.S.P.
            # G.K}|PEPTIDE4{E.I.V.L.T.Q.S.P.A.T.L.S.L.S.P.G.E.R.A.T.L.S.C.R.A.S.Q.S.V.S.R.Y.L.A.W.Y.Q.Q.K.P.G.Q.A.P.R.L.
            # L.I.Y.D.A.S.N.R.A.T.G.I.P.A.R.F.S.G.S.G.S.G.T.D.F.T.L.T.I.S.S.L.E.P.E.D.F.A.V.Y.Y.C.Q.Q.R.S.N.W.P.R.T.F.G.
            # Q.G.T.K.V.E.I.K.R.T.V.A.A.P.S.V.F.I.F.P.P.S.D.E.Q.L.K.S.G.T.A.S.V.V.C.L.L.N.N.F.Y.P.R.E.A.K.V.Q.W.K.V.D.N.
            # A.L.Q.S.G.N.S.Q.E.S.V.T.E.Q.D.S.K.D.S.T.Y.S.L.S.S.T.L.T.L.S.K.A.D.Y.E.K.H.K.V.Y.A.C.E.V.T.H.Q.G.L.S.S.P.V.
            # T.K.S.F.N.R.G.E.C}$PEPTIDE4,PEPTIDE4,23:R3-88:R3|PEPTIDE1,PEPTIDE1,23:R3-88:R3|PEPTIDE3,PEPTIDE3,372:R3-43
            # 0:R3|PEPTIDE4,PEPTIDE4,134:R3-194:R3|PEPTIDE2,PEPTIDE2,22:R3-96:R3|PEPTIDE2,PEPTIDE2,149:R3-205:R3|PEPTIDE
            # 2,PEPTIDE2,266:R3-326:R3|PEPTIDE3,PEPTIDE3,149:R3-205:R3|PEPTIDE2,PEPTIDE2,372:R3-430:R3|PEPTIDE2,PEPTIDE3
            # ,231:R3-231:R3|PEPTIDE2,PEPTIDE1,225:R3-214:R3|PEPTIDE3,PEPTIDE3,266:R3-326:R3|PEPTIDE3,PEPTIDE4,225:R3-21
            # 4:R3|PEPTIDE3,PEPTIDE3,22:R3-96:R3|PEPTIDE1,PEPTIDE1,134:R3-194:R3|PEPTIDE2,PEPTIDE3,234:R3-234:R3$$$' , '
            # PEPTIDE1{E.I.V.M.T.Q.S.P.A.T.L.S.L.S.P.G.E.R.A.T.L.S.C.R.A.S.Q.S.V.S.S.Y.L.A.W.Y.Q.Q.K.P.G.Q.A.P.R.L.L.I.Y
            # .D.A.S.N.R.A.T.G.I.P.A.R.F.S.G.S.G.S.G.T.D.F.T.L.T.I.S.S.L.E.P.E.D.F.A.V.Y.Y.C.H.Q.Y.G.S.T.P.L.T.F.G.G.G.T
            # .K.A.E.I.K.R.T.V.A.A.P.S.V.F.I.F.P.P.S.D.E.Q.L.K.S.G.T.A.S.V.V.C.L.L.N.N.F.Y.P.R.E.A.K.V.Q.W.K.V.D.N.A.L.Q
            # .S.G.N.S.Q.E.S.V.T.E.Q.D.S.K.D.S.T.Y.S.L.S.S.T.L.T.L.S.K.A.D.Y.E.K.H.K.V.Y.A.C.E.V.T.H.Q.G.L.S.S.P.V.T.K.S
            # .F.N.R.G.E.C}|PEPTIDE2{Q.V.Q.L.Q.E.S.G.P.G.L.V.K.P.S.Q.T.L.S.L.T.C.T.V.S.G.G.S.I.S.S.G.D.Y.Y.W.S.W.I.R.Q.P
            # .P.G.K.G.L.E.W.I.G.Y.I.Y.Y.S.G.S.T.D.Y.N.P.S.L.K.S.R.V.T.M.S.V.D.T.S.K.N.Q.F.S.L.K.V.N.S.V.T.A.A.D.T.A.V.Y
            # .Y.C.A.R.V.S.I.F.G.V.G.T.F.D.Y.W.G.Q.G.T.L.V.T.V.S.S.A.S.T.K.G.P.S.V.L.P.L.A.P.S.S.K.S.T.S.G.G.T.A.A.L.G.C
            # .L.V.K.D.Y.F.P.E.P.V.T.V.S.W.N.S.G.A.L.T.S.G.V.H.T.F.P.A.V.L.Q.S.S.G.L.Y.S.L.S.S.V.V.T.V.P.S.S.S.L.G.T.Q.T
            # .Y.I.C.N.V.N.H.K.P.S.N.T.K.V.D.K.R.V.E.P.K.S.C.D.K.T.H.T.C.P.P.C.P.A.P.E.L.L.G.G.P.S.V.F.L.F.P.P.K.P.K.D.T
            # .L.M.I.S.R.T.P.E.V.T.C.V.V.V.D.V.S.H.E.D.P.E.V.K.F.N.W.Y.V.D.G.V.E.V.H.N.A.K.T.K.P.R.E.E.Q.Y.N.S.T.Y.R.V.V
            # .S.V.L.T.V.L.H.Q.D.W.L.N.G.K.E.Y.K.C.K.V.S.N.K.A.L.P.A.P.I.E.K.T.I.S.K.A.K.G.Q.P.R.E.P.Q.V.Y.T.L.P.P.S.R.E
            # .E.M.T.K.N.Q.V.S.L.T.C.L.V.K.G.F.Y.P.S.D.I.A.V.E.W.E.S.N.G.Q.P.E.N.N.Y.K.T.T.P.P.V.L.D.S.D.G.S.F.F.L.Y.S.K
            # .L.T.V.D.K.S.R.W.Q.Q.G.N.V.F.S.C.S.V.M.H.E.A.L.H.N.H.Y.T.Q.K.S.L.S.L.S.P.G.K}|PEPTIDE3{Q.V.Q.L.Q.E.S.G.P.G
            # .L.V.K.P.S.Q.T.L.S.L.T.C.T.V.S.G.G.S.I.S.S.G.D.Y.Y.W.S.W.I.R.Q.P.P.G.K.G.L.E.W.I.G.Y.I.Y.Y.S.G.S.T.D.Y.N.P
            # .S.L.K.S.R.V.T.M.S.V.D.T.S.K.N.Q.F.S.L.K.V.N.S.V.T.A.A.D.T.A.V.Y.Y.C.A.R.V.S.I.F.G.V.G.T.F.D.Y.W.G.Q.G.T.L
            # .V.T.V.S.S.A.S.T.K.G.P.S.V.L.P.L.A.P.S.S.K.S.T.S.G.G.T.A.A.L.G.C.L.V.K.D.Y.F.P.E.P.V.T.V.S.W.N.S.G.A.L.T.S
            # .G.V.H.T.F.P.A.V.L.Q.S.S.G.L.Y.S.L.S.S.V.V.T.V.P.S.S.S.L.G.T.Q.T.Y.I.C.N.V.N.H.K.P.S.N.T.K.V.D.K.R.V.E.P.K
            # .S.C.D.K.T.H.T.C.P.P.C.P.A.P.E.L.L.G.G.P.S.V.F.L.F.P.P.K.P.K.D.T.L.M.I.S.R.T.P.E.V.T.C.V.V.V.D.V.S.H.E.D.P
            # .E.V.K.F.N.W.Y.V.D.G.V.E.V.H.N.A.K.T.K.P.R.E.E.Q.Y.N.S.T.Y.R.V.V.S.V.L.T.V.L.H.Q.D.W.L.N.G.K.E.Y.K.C.K.V.S
            # .N.K.A.L.P.A.P.I.E.K.T.I.S.K.A.K.G.Q.P.R.E.P.Q.V.Y.T.L.P.P.S.R.E.E.M.T.K.N.Q.V.S.L.T.C.L.V.K.G.F.Y.P.S.D.I
            # .A.V.E.W.E.S.N.G.Q.P.E.N.N.Y.K.T.T.P.P.V.L.D.S.D.G.S.F.F.L.Y.S.K.L.T.V.D.K.S.R.W.Q.Q.G.N.V.F.S.C.S.V.M.H.E
            # .A.L.H.N.H.Y.T.Q.K.S.L.S.L.S.P.G.K}|PEPTIDE4{E.I.V.M.T.Q.S.P.A.T.L.S.L.S.P.G.E.R.A.T.L.S.C.R.A.S.Q.S.V.S.S
            # .Y.L.A.W.Y.Q.Q.K.P.G.Q.A.P.R.L.L.I.Y.D.A.S.N.R.A.T.G.I.P.A.R.F.S.G.S.G.S.G.T.D.F.T.L.T.I.S.S.L.E.P.E.D.F.A
            # .V.Y.Y.C.H.Q.Y.G.S.T.P.L.T.F.G.G.G.T.K.A.E.I.K.R.T.V.A.A.P.S.V.F.I.F.P.P.S.D.E.Q.L.K.S.G.T.A.S.V.V.C.L.L.N
            # .N.F.Y.P.R.E.A.K.V.Q.W.K.V.D.N.A.L.Q.S.G.N.S.Q.E.S.V.T.E.Q.D.S.K.D.S.T.Y.S.L.S.S.T.L.T.L.S.K.A.D.Y.E.K.H.K
            # .V.Y.A.C.E.V.T.H.Q.G.L.S.S.P.V.T.K.S.F.N.R.G.E.C}$PEPTIDE3,PEPTIDE4,224:R3-214:R3|PEPTIDE3,PEPTIDE3,22:R3-
            # 97:R3|PEPTIDE3,PEPTIDE3,148:R3-204:R3|PEPTIDE3,PEPTIDE3,265:R3-325:R3|PEPTIDE2,PEPTIDE2,371:R3-429:R3|PEPT
            # IDE1,PEPTIDE1,134:R3-194:R3|PEPTIDE2,PEPTIDE3,233:R3-233:R3|PEPTIDE4,PEPTIDE4,23:R3-88:R3|PEPTIDE2,PEPTIDE
            # 1,224:R3-214:R3|PEPTIDE2,PEPTIDE2,148:R3-204:R3|PEPTIDE2,PEPTIDE2,22:R3-97:R3|PEPTIDE2,PEPTIDE2,265:R3-325
            # :R3|PEPTIDE2,PEPTIDE3,230:R3-230:R3|PEPTIDE4,PEPTIDE4,134:R3-194:R3|PEPTIDE3,PEPTIDE3,371:R3-429:R3|PEPTID
            # E1,PEPTIDE1,23:R3-88:R3$$$' , 'PEPTIDE1{D.I.Q.M.T.Q.T.T.S.S.L.S.A.S.L.G.D.R.V.T.I.S.C.R.A.S.Q.D.I.S.N.Y.L.
            # N.W.Y.Q.Q.K.P.D.G.T.V.K.L.L.I.Y.Y.T.S.R.L.H.S.G.V.P.S.R.F.S.G.S.G.S.G.T.D.Y.S.L.T.I.S.N.L.E.Q.E.D.I.A.T.Y.
            # F.C.Q.Q.G.N.T.L.P.W.T.F.G.G.G.T.K.L.E.I.K.R.A.D.A.A.P.T.V.S.I.F.P.P.S.S.E.Q.L.T.S.G.G.A.S.V.V.C.F.L.N.N.F.
            # Y.P.K.D.I.N.V.K.W.K.I.D.G.S.E.R.Q.N.G.V.L.N.S.W.T.D.Q.D.S.K.D.S.T.Y.S.M.S.S.T.L.T.L.T.K.D.E.Y.E.R.H.N.S.Y.
            # T.C.E.A.T.H.K.T.S.T.S.P.I.V.K.S.F.N.R.N.E.C}|PEPTIDE2{Q.V.Q.L.Q.Q.S.G.A.E.L.V.K.P.G.A.S.V.K.L.S.C.K.A.S.G.
            # Y.T.F.T.S.Y.D.I.N.W.V.R.Q.R.P.E.Q.G.L.E.W.I.G.W.I.F.P.G.D.G.S.T.K.Y.N.E.K.F.K.G.K.A.T.L.T.T.D.K.S.S.S.T.A.
            # Y.M.Q.L.S.R.L.T.S.E.D.S.A.V.Y.F.C.A.R.E.D.Y.Y.D.N.S.Y.Y.F.D.Y.W.G.Q.G.T.T.L.T.V.S.S.A.K.T.T.P.P.S.V.Y.P.L.
            # A.P.G.S.A.A.Q.T.N.S.M.V.T.L.G.C.L.V.K.G.Y.F.P.E.P.V.T.V.T.W.N.S.G.S.L.S.S.G.V.H.T.F.P.A.V.L.Q.S.D.L.Y.T.L.
            # S.S.S.V.T.V.P.S.S.P.R.P.S.E.T.V.T.C.N.V.A.H.P.A.S.S.T.K.V.D.K.K.I.V.P.R.D.C.G.C.K.P.C.I.C.T.V.P.E.V.S.S.V.
            # F.I.F.P.P.K.P.K.D.V.L.T.I.T.L.T.P.K.V.T.C.V.V.V.D.I.S.K.D.D.P.E.V.Q.F.S.W.F.V.D.D.V.E.V.H.T.A.Q.T.Q.P.R.E.
            # E.Q.F.N.S.T.F.R.S.V.S.E.L.P.I.M.H.Q.D.W.L.N.G.K.E.F.K.C.R.V.N.S.A.A.F.P.A.P.I.E.K.T.I.S.K.T.K.G.R.P.K.A.P.
            # Q.V.Y.T.I.P.P.P.K.E.Q.M.A.K.D.K.V.S.L.T.C.M.I.T.D.F.F.P.E.D.I.T.V.E.W.Q.W.N.G.Q.P.A.E.N.Y.K.N.T.Q.P.I.M.N.
            # T.N.G.S.Y.F.V.Y.S.K.L.N.V.Q.K.S.N.W.E.A.G.N.T.F.T.C.S.V.L.H.E.G.L.H.N.H.H.T.E.K.S.L.S.H.S.P.G.K}|PEPTIDE3{
            # Q.V.Q.L.Q.Q.S.G.A.E.L.V.K.P.G.A.S.V.K.L.S.C.K.A.S.G.Y.T.F.T.S.Y.D.I.N.W.V.R.Q.R.P.E.Q.G.L.E.W.I.G.W.I.F.P.
            # G.D.G.S.T.K.Y.N.E.K.F.K.G.K.A.T.L.T.T.D.K.S.S.S.T.A.Y.M.Q.L.S.R.L.T.S.E.D.S.A.V.Y.F.C.A.R.E.D.Y.Y.D.N.S.Y.
            # Y.F.D.Y.W.G.Q.G.T.T.L.T.V.S.S.A.K.T.T.P.P.S.V.Y.P.L.A.P.G.S.A.A.Q.T.N.S.M.V.T.L.G.C.L.V.K.G.Y.F.P.E.P.V.T.
            # V.T.W.N.S.G.S.L.S.S.G.V.H.T.F.P.A.V.L.Q.S.D.L.Y.T.L.S.S.S.V.T.V.P.S.S.P.R.P.S.E.T.V.T.C.N.V.A.H.P.A.S.S.T.
            # K.V.D.K.K.I.V.P.R.D.C.G.C.K.P.C.I.C.T.V.P.E.V.S.S.V.F.I.F.P.P.K.P.K.D.V.L.T.I.T.L.T.P.K.V.T.C.V.V.V.D.I.S.
            # K.D.D.P.E.V.Q.F.S.W.F.V.D.D.V.E.V.H.T.A.Q.T.Q.P.R.E.E.Q.F.N.S.T.F.R.S.V.S.E.L.P.I.M.H.Q.D.W.L.N.G.K.E.F.K.
            # C.R.V.N.S.A.A.F.P.A.P.I.E.K.T.I.S.K.T.K.G.R.P.K.A.P.Q.V.Y.T.I.P.P.P.K.E.Q.M.A.K.D.K.V.S.L.T.C.M.I.T.D.F.F.
            # P.E.D.I.T.V.E.W.Q.W.N.G.Q.P.A.E.N.Y.K.N.T.Q.P.I.M.N.T.N.G.S.Y.F.V.Y.S.K.L.N.V.Q.K.S.N.W.E.A.G.N.T.F.T.C.S.
            # V.L.H.E.G.L.H.N.H.H.T.E.K.S.L.S.H.S.P.G.K}|PEPTIDE4{D.I.Q.M.T.Q.T.T.S.S.L.S.A.S.L.G.D.R.V.T.I.S.C.R.A.S.Q.
            # D.I.S.N.Y.L.N.W.Y.Q.Q.K.P.D.G.T.V.K.L.L.I.Y.Y.T.S.R.L.H.S.G.V.P.S.R.F.S.G.S.G.S.G.T.D.Y.S.L.T.I.S.N.L.E.Q.
            # E.D.I.A.T.Y.F.C.Q.Q.G.N.T.L.P.W.T.F.G.G.G.T.K.L.E.I.K.R.A.D.A.A.P.T.V.S.I.F.P.P.S.S.E.Q.L.T.S.G.G.A.S.V.V.
            # C.F.L.N.N.F.Y.P.K.D.I.N.V.K.W.K.I.D.G.S.E.R.Q.N.G.V.L.N.S.W.T.D.Q.D.S.K.D.S.T.Y.S.M.S.S.T.L.T.L.T.K.D.E.Y.
            # E.R.H.N.S.Y.T.C.E.A.T.H.K.T.S.T.S.P.I.V.K.S.F.N.R.N.E.C}$PEPTIDE2,PEPTIDE3,225:R3-225:R3|PEPTIDE2,PEPTIDE2
            # ,365:R3-423:R3|PEPTIDE3,PEPTIDE3,365:R3-423:R3|PEPTIDE1,PEPTIDE1,23:R3-88:R3|PEPTIDE3,PEPTIDE3,259:R3-319:
            # R3|PEPTIDE2,PEPTIDE1,223:R3-214:R3|PEPTIDE2,PEPTIDE2,148:R3-203:R3|PEPTIDE1,PEPTIDE1,134:R3-194:R3|PEPTIDE
            # 3,PEPTIDE4,223:R3-214:R3|PEPTIDE2,PEPTIDE2,22:R3-96:R3|PEPTIDE4,PEPTIDE4,134:R3-194:R3|PEPTIDE3,PEPTIDE3,2
            # 2:R3-96:R3|PEPTIDE2,PEPTIDE2,259:R3-319:R3|PEPTIDE2,PEPTIDE3,230:R3-230:R3|PEPTIDE3,PEPTIDE3,148:R3-203:R3
            # |PEPTIDE4,PEPTIDE4,23:R3-88:R3|PEPTIDE2,PEPTIDE3,228:R3-228:R3$$$' , 'PEPTIDE1{D.I.Q.M.T.Q.S.P.S.S.V.S.A.S
            # .I.G.D.R.V.T.I.T.C.R.A.S.Q.G.I.D.N.W.L.G.W.Y.Q.Q.K.P.G.K.A.P.K.L.L.I.Y.D.A.S.N.L.D.T.G.V.P.S.R.F.S.G.S.G.S
            # .G.T.Y.F.T.L.T.I.S.S.L.Q.A.E.D.F.A.V.Y.F.C.Q.Q.A.K.A.F.P.P.T.F.G.G.G.T.K.V.D.I.K.G.T.V.A.A.P.S.V.F.I.F.P.P
            # .S.D.E.Q.L.K.S.G.T.A.S.V.V.C.L.L.N.N.F.Y.P.R.E.A.K.V.Q.W.K.V.D.N.A.L.Q.S.G.N.S.Q.E.S.V.T.E.Q.D.S.K.D.S.T.Y
            # .S.L.S.S.T.L.T.L.S.K.A.D.Y.E.K.H.K.V.Y.A.C.E.V.T.H.Q.G.L.S.S.P.V.T.K.S.F.N.R.G.E.C}|PEPTIDE2{E.V.Q.L.V.Q.S
            # .G.G.G.L.V.K.P.G.G.S.L.R.L.S.C.A.A.S.G.F.T.F.S.S.Y.S.M.N.W.V.R.Q.A.P.G.K.G.L.E.W.V.S.S.I.S.S.S.S.S.Y.I.Y.Y
            # .A.D.S.V.K.G.R.F.T.I.S.R.D.N.A.K.N.S.L.Y.L.Q.M.N.S.L.R.A.E.D.T.A.V.Y.Y.C.A.R.V.T.D.A.F.D.I.W.G.Q.G.T.M.V.T
            # .V.S.S.A.S.T.K.G.P.S.V.F.P.L.A.P.S.S.K.S.T.S.G.G.T.A.A.L.G.C.L.V.K.D.Y.F.P.E.P.V.T.V.S.W.N.S.G.A.L.T.S.G.V
            # .H.T.F.P.A.V.L.Q.S.S.G.L.Y.S.L.S.S.V.V.T.V.P.S.S.S.L.G.T.Q.T.Y.I.C.N.V.N.H.K.P.S.N.T.K.V.D.K.K.V.E.P.K.S.C
            # .D.K.T.H.T.C.P.P.C.P.A.P.E.L.L.G.G.P.S.V.F.L.F.P.P.K.P.K.D.T.L.M.I.S.R.T.P.E.V.T.C.V.V.V.D.V.S.H.E.D.P.E.V
            # .K.F.N.W.Y.V.D.G.V.E.V.H.N.A.K.T.K.P.R.E.E.Q.Y.N.S.T.Y.R.V.V.S.V.L.T.V.L.H.Q.D.W.L.N.G.K.E.Y.K.C.K.V.S.N.K
            # .A.L.P.A.P.I.E.K.T.I.S.K.A.K.G.Q.P.R.E.P.Q.V.Y.T.L.P.P.S.R.E.E.M.T.K.N.Q.V.S.L.T.C.L.V.K.G.F.Y.P.S.D.I.A.V
            # .E.W.E.S.N.G.Q.P.E.N.N.Y.K.T.T.P.P.V.L.D.S.D.G.S.F.F.L.Y.S.K.L.T.V.D.K.S.R.W.Q.Q.G.N.V.F.S.C.S.V.M.H.E.A.L
            # .H.N.H.Y.T.Q.K.S.L.S.L.S.P.G.K}|PEPTIDE3{E.V.Q.L.V.Q.S.G.G.G.L.V.K.P.G.G.S.L.R.L.S.C.A.A.S.G.F.T.F.S.S.Y.S
            # .M.N.W.V.R.Q.A.P.G.K.G.L.E.W.V.S.S.I.S.S.S.S.S.Y.I.Y.Y.A.D.S.V.K.G.R.F.T.I.S.R.D.N.A.K.N.S.L.Y.L.Q.M.N.S.L
            # .R.A.E.D.T.A.V.Y.Y.C.A.R.V.T.D.A.F.D.I.W.G.Q.G.T.M.V.T.V.S.S.A.S.T.K.G.P.S.V.F.P.L.A.P.S.S.K.S.T.S.G.G.T.A
            # .A.L.G.C.L.V.K.D.Y.F.P.E.P.V.T.V.S.W.N.S.G.A.L.T.S.G.V.H.T.F.P.A.V.L.Q.S.S.G.L.Y.S.L.S.S.V.V.T.V.P.S.S.S.L
            # .G.T.Q.T.Y.I.C.N.V.N.H.K.P.S.N.T.K.V.D.K.K.V.E.P.K.S.C.D.K.T.H.T.C.P.P.C.P.A.P.E.L.L.G.G.P.S.V.F.L.F.P.P.K
            # .P.K.D.T.L.M.I.S.R.T.P.E.V.T.C.V.V.V.D.V.S.H.E.D.P.E.V.K.F.N.W.Y.V.D.G.V.E.V.H.N.A.K.T.K.P.R.E.E.Q.Y.N.S.T
            # .Y.R.V.V.S.V.L.T.V.L.H.Q.D.W.L.N.G.K.E.Y.K.C.K.V.S.N.K.A.L.P.A.P.I.E.K.T.I.S.K.A.K.G.Q.P.R.E.P.Q.V.Y.T.L.P
            # .P.S.R.E.E.M.T.K.N.Q.V.S.L.T.C.L.V.K.G.F.Y.P.S.D.I.A.V.E.W.E.S.N.G.Q.P.E.N.N.Y.K.T.T.P.P.V.L.D.S.D.G.S.F.F
            # .L.Y.S.K.L.T.V.D.K.S.R.W.Q.Q.G.N.V.F.S.C.S.V.M.H.E.A.L.H.N.H.Y.T.Q.K.S.L.S.L.S.P.G.K}|PEPTIDE4{D.I.Q.M.T.Q
            # .S.P.S.S.V.S.A.S.I.G.D.R.V.T.I.T.C.R.A.S.Q.G.I.D.N.W.L.G.W.Y.Q.Q.K.P.G.K.A.P.K.L.L.I.Y.D.A.S.N.L.D.T.G.V.P
            # .S.R.F.S.G.S.G.S.G.T.Y.F.T.L.T.I.S.S.L.Q.A.E.D.F.A.V.Y.F.C.Q.Q.A.K.A.F.P.P.T.F.G.G.G.T.K.V.D.I.K.G.T.V.A.A
            # .P.S.V.F.I.F.P.P.S.D.E.Q.L.K.S.G.T.A.S.V.V.C.L.L.N.N.F.Y.P.R.E.A.K.V.Q.W.K.V.D.N.A.L.Q.S.G.N.S.Q.E.S.V.T.E
            # .Q.D.S.K.D.S.T.Y.S.L.S.S.T.L.T.L.S.K.A.D.Y.E.K.H.K.V.Y.A.C.E.V.T.H.Q.G.L.S.S.P.V.T.K.S.F.N.R.G.E.C}$PEPTID
            # E3,PEPTIDE4,219:R3-214:R3|PEPTIDE2,PEPTIDE2,143:R3-199:R3|PEPTIDE1,PEPTIDE1,23:R3-88:R3|PEPTIDE3,PEPTIDE3,
            # 366:R3-424:R3|PEPTIDE3,PEPTIDE3,260:R3-320:R3|PEPTIDE2,PEPTIDE3,225:R3-225:R3|PEPTIDE2,PEPTIDE2,366:R3-424
            # :R3|PEPTIDE3,PEPTIDE3,143:R3-199:R3|PEPTIDE4,PEPTIDE4,134:R3-194:R3|PEPTIDE2,PEPTIDE2,260:R3-320:R3|PEPTID
            # E2,PEPTIDE1,219:R3-214:R3|PEPTIDE1,PEPTIDE1,134:R3-194:R3|PEPTIDE2,PEPTIDE2,22:R3-96:R3|PEPTIDE3,PEPTIDE3,
            # 22:R3-96:R3|PEPTIDE2,PEPTIDE3,228:R3-228:R3|PEPTIDE4,PEPTIDE4,23:R3-88:R3$$$' , 'PEPTIDE1{E.I.V.L.T.Q.S.P.
            # G.T.L.S.V.S.P.G.E.R.A.T.L.S.C.R.A.S.Q.S.I.G.S.S.L.H.W.Y.Q.Q.K.P.G.Q.A.P.R.L.L.I.K.Y.A.S.Q.S.L.S.G.I.P.D.R.
            # F.S.G.S.G.S.G.T.D.F.T.L.T.I.S.R.L.E.P.E.D.F.A.V.Y.Y.C.H.Q.S.S.R.L.P.H.T.F.G.Q.G.T.K.V.E.I.K.R.T.V.A.A.P.S.
            # V.F.I.F.P.P.S.D.E.Q.L.K.S.G.T.A.S.V.V.C.L.L.N.N.F.Y.P.R.E.A.K.V.Q.W.K.V.D.N.A.L.Q.S.G.N.S.Q.E.S.V.T.E.Q.D.
            # S.K.D.S.T.Y.S.L.S.S.T.L.T.L.S.K.A.D.Y.E.K.H.K.V.Y.A.C.E.V.T.H.Q.G.L.S.S.P.V.T.K.S.F.N.R.G.E.C}|PEPTIDE2{E.
            # V.Q.L.V.Q.S.G.G.G.L.V.K.P.G.G.S.L.R.L.S.C.A.A.S.G.F.T.F.S.S.F.A.M.H.W.V.R.Q.A.P.G.K.G.L.E.W.I.S.V.I.D.T.R.
            # G.A.T.Y.Y.A.D.S.V.K.G.R.F.T.I.S.R.D.N.A.K.N.S.L.Y.L.Q.M.N.S.L.R.A.E.D.T.A.V.Y.Y.C.A.R.L.G.N.F.Y.Y.G.M.D.V.
            # W.G.Q.G.T.T.V.T.V.S.S.A.S.T.K.G.P.S.V.F.P.L.A.P.S.S.K.S.T.S.G.G.T.A.A.L.G.C.L.V.K.D.Y.F.P.E.P.V.T.V.S.W.N.
            # S.G.A.L.T.S.G.V.H.T.F.P.A.V.L.Q.S.S.G.L.Y.S.L.S.S.V.V.T.V.P.S.S.S.L.G.T.Q.T.Y.I.C.N.V.N.H.K.P.S.N.T.K.V.D.
            # K.K.V.E.P.K.S.C.D.K.T.H.T.C.P.P.C.P.A.P.E.L.L.G.G.P.S.V.F.L.F.P.P.K.P.K.D.T.L.M.I.S.R.T.P.E.V.T.C.V.V.V.D.
            # V.S.H.E.D.P.E.V.K.F.N.W.Y.V.D.G.V.E.V.H.N.A.K.T.K.P.R.E.E.Q.Y.N.S.T.Y.R.V.V.S.V.L.T.V.L.H.Q.D.W.L.N.G.K.E.
            # Y.K.C.K.V.S.N.K.A.L.P.A.P.I.E.K.T.I.S.K.A.K.G.Q.P.R.E.P.Q.V.Y.T.L.P.P.S.R.D.E.L.T.K.N.Q.V.S.L.T.C.L.V.K.G.
            # F.Y.P.S.D.I.A.V.E.W.E.S.N.G.Q.P.E.N.N.Y.K.T.T.P.P.V.L.D.S.D.G.S.F.F.L.Y.S.K.L.T.V.D.K.S.R.W.Q.Q.G.N.V.F.S.
            # C.S.V.M.H.E.A.L.H.N.H.Y.T.Q.K.S.L.S.L.S.P.G.K}|PEPTIDE3{E.V.Q.L.V.Q.S.G.G.G.L.V.K.P.G.G.S.L.R.L.S.C.A.A.S.
            # G.F.T.F.S.S.F.A.M.H.W.V.R.Q.A.P.G.K.G.L.E.W.I.S.V.I.D.T.R.G.A.T.Y.Y.A.D.S.V.K.G.R.F.T.I.S.R.D.N.A.K.N.S.L.
            # Y.L.Q.M.N.S.L.R.A.E.D.T.A.V.Y.Y.C.A.R.L.G.N.F.Y.Y.G.M.D.V.W.G.Q.G.T.T.V.T.V.S.S.A.S.T.K.G.P.S.V.F.P.L.A.P.
            # S.S.K.S.T.S.G.G.T.A.A.L.G.C.L.V.K.D.Y.F.P.E.P.V.T.V.S.W.N.S.G.A.L.T.S.G.V.H.T.F.P.A.V.L.Q.S.S.G.L.Y.S.L.S.
            # S.V.V.T.V.P.S.S.S.L.G.T.Q.T.Y.I.C.N.V.N.H.K.P.S.N.T.K.V.D.K.K.V.E.P.K.S.C.D.K.T.H.T.C.P.P.C.P.A.P.E.L.L.G.
            # G.P.S.V.F.L.F.P.P.K.P.K.D.T.L.M.I.S.R.T.P.E.V.T.C.V.V.V.D.V.S.H.E.D.P.E.V.K.F.N.W.Y.V.D.G.V.E.V.H.N.A.K.T.
            # K.P.R.E.E.Q.Y.N.S.T.Y.R.V.V.S.V.L.T.V.L.H.Q.D.W.L.N.G.K.E.Y.K.C.K.V.S.N.K.A.L.P.A.P.I.E.K.T.I.S.K.A.K.G.Q.
            # P.R.E.P.Q.V.Y.T.L.P.P.S.R.D.E.L.T.K.N.Q.V.S.L.T.C.L.V.K.G.F.Y.P.S.D.I.A.V.E.W.E.S.N.G.Q.P.E.N.N.Y.K.T.T.P.
            # P.V.L.D.S.D.G.S.F.F.L.Y.S.K.L.T.V.D.K.S.R.W.Q.Q.G.N.V.F.S.C.S.V.M.H.E.A.L.H.N.H.Y.T.Q.K.S.L.S.L.S.P.G.K}|P
            # EPTIDE4{E.I.V.L.T.Q.S.P.G.T.L.S.V.S.P.G.E.R.A.T.L.S.C.R.A.S.Q.S.I.G.S.S.L.H.W.Y.Q.Q.K.P.G.Q.A.P.R.L.L.I.K.
            # Y.A.S.Q.S.L.S.G.I.P.D.R.F.S.G.S.G.S.G.T.D.F.T.L.T.I.S.R.L.E.P.E.D.F.A.V.Y.Y.C.H.Q.S.S.R.L.P.H.T.F.G.Q.G.T.
            # K.V.E.I.K.R.T.V.A.A.P.S.V.F.I.F.P.P.S.D.E.Q.L.K.S.G.T.A.S.V.V.C.L.L.N.N.F.Y.P.R.E.A.K.V.Q.W.K.V.D.N.A.L.Q.
            # S.G.N.S.Q.E.S.V.T.E.Q.D.S.K.D.S.T.Y.S.L.S.S.T.L.T.L.S.K.A.D.Y.E.K.H.K.V.Y.A.C.E.V.T.H.Q.G.L.S.S.P.V.T.K.S.
            # F.N.R.G.E.C}$PEPTIDE2,PEPTIDE3,230:R3-230:R3|PEPTIDE3,PEPTIDE3,22:R3-95:R3|PEPTIDE4,PEPTIDE4,23:R3-88:R3|P
            # EPTIDE2,PEPTIDE2,145:R3-201:R3|PEPTIDE1,PEPTIDE1,23:R3-88:R3|PEPTIDE2,PEPTIDE2,368:R3-426:R3|PEPTIDE2,PEPT
            # IDE3,227:R3-227:R3|PEPTIDE3,PEPTIDE3,368:R3-426:R3|PEPTIDE3,PEPTIDE4,221:R3-214:R3|PEPTIDE4,PEPTIDE4,134:R
            # 3-194:R3|PEPTIDE1,PEPTIDE1,134:R3-194:R3|PEPTIDE2,PEPTIDE1,221:R3-214:R3|PEPTIDE2,PEPTIDE2,262:R3-322:R3|P
            # EPTIDE2,PEPTIDE2,22:R3-95:R3|PEPTIDE3,PEPTIDE3,262:R3-322:R3|PEPTIDE3,PEPTIDE3,145:R3-201:R3$$$' , 'PEPTID
            # E1{E.I.V.L.T.Q.S.P.G.T.L.S.L.S.P.G.E.R.A.T.L.S.C.R.A.S.Q.S.V.S.S.T.Y.L.A.W.Y.Q.Q.K.P.G.Q.A.P.R.L.L.I.Y.G.A
            # .S.S.R.A.T.G.I.P.D.R.F.S.G.S.G.S.G.T.D.F.T.L.T.I.S.R.L.E.P.E.D.F.A.V.Y.Y.C.Q.Q.Y.G.S.S.P.R.T.F.G.Q.G.T.K.V
            # .E.I.K.R.T.V.A.A.P.S.V.F.I.F.P.P.S.D.E.Q.L.K.S.G.T.A.S.V.V.C.L.L.N.N.F.Y.P.R.E.A.K.V.Q.W.K.V.D.N.A.L.Q.S.G
            # .N.S.Q.E.S.V.T.E.Q.D.S.K.D.S.T.Y.S.L.S.S.T.L.T.L.S.K.A.D.Y.E.K.H.K.V.Y.A.C.E.V.T.H.Q.G.L.S.S.P.V.T.K.S.F.N
            # .R.G.E.C}|PEPTIDE2{Q.V.Q.L.V.Q.S.G.A.E.V.K.K.P.G.A.S.V.K.V.S.C.K.A.S.G.Y.T.F.T.S.Y.S.I.S.W.V.R.Q.A.P.G.Q.G
            # .L.E.W.M.G.W.I.S.V.Y.N.G.N.T.N.Y.A.Q.K.F.Q.G.R.V.T.M.T.T.D.T.S.T.S.T.A.Y.L.E.L.R.S.L.R.S.D.D.T.A.V.Y.Y.C.A
            # .R.D.P.I.A.A.G.Y.W.G.Q.G.T.L.V.T.V.S.S.A.S.T.K.G.P.S.V.F.P.L.A.P.S.S.K.S.T.S.G.G.T.A.A.L.G.C.L.V.K.D.Y.F.P
            # .E.P.V.T.V.S.W.N.S.G.A.L.T.S.G.V.H.T.F.P.A.V.L.Q.S.S.G.L.Y.S.L.S.S.V.V.T.V.P.S.S.S.L.G.T.Q.T.Y.I.C.N.V.N.H
            # .K.P.S.N.T.K.V.D.K.K.V.E.P.K.S.C.D.K.T.H.T.C.P.P.C.P.A.P.E.L.L.G.G.P.S.V.F.L.F.P.P.K.P.K.D.T.L.M.I.S.R.T.P
            # .E.V.T.C.V.V.V.D.V.S.H.E.D.P.E.V.K.F.N.W.Y.V.D.G.V.E.V.H.N.A.K.T.K.P.R.E.E.Q.Y.N.S.T.Y.R.V.V.S.V.L.T.V.L.H
            # .Q.D.W.L.N.G.K.E.Y.K.C.K.V.S.N.K.A.L.P.A.P.I.E.K.T.I.S.K.A.K.G.Q.P.R.E.P.Q.V.Y.T.L.P.P.S.R.E.E.M.T.K.N.Q.V
            # .S.L.T.C.L.V.K.G.F.Y.P.S.D.I.A.V.E.W.E.S.N.G.Q.P.E.N.N.Y.K.T.T.P.P.V.L.D.S.D.G.S.F.F.L.Y.S.K.L.T.V.D.K.S.R
            # .W.Q.Q.G.N.V.F.S.C.S.V.M.H.E.A.L.H.N.H.Y.T.Q.K.S.L.S.L.S.P.G.K}|PEPTIDE3{Q.V.Q.L.V.Q.S.G.A.E.V.K.K.P.G.A.S
            # .V.K.V.S.C.K.A.S.G.Y.T.F.T.S.Y.S.I.S.W.V.R.Q.A.P.G.Q.G.L.E.W.M.G.W.I.S.V.Y.N.G.N.T.N.Y.A.Q.K.F.Q.G.R.V.T.M
            # .T.T.D.T.S.T.S.T.A.Y.L.E.L.R.S.L.R.S.D.D.T.A.V.Y.Y.C.A.R.D.P.I.A.A.G.Y.W.G.Q.G.T.L.V.T.V.S.S.A.S.T.K.G.P.S
            # .V.F.P.L.A.P.S.S.K.S.T.S.G.G.T.A.A.L.G.C.L.V.K.D.Y.F.P.E.P.V.T.V.S.W.N.S.G.A.L.T.S.G.V.H.T.F.P.A.V.L.Q.S.S
            # .G.L.Y.S.L.S.S.V.V.T.V.P.S.S.S.L.G.T.Q.T.Y.I.C.N.V.N.H.K.P.S.N.T.K.V.D.K.K.V.E.P.K.S.C.D.K.T.H.T.C.P.P.C.P
            # .A.P.E.L.L.G.G.P.S.V.F.L.F.P.P.K.P.K.D.T.L.M.I.S.R.T.P.E.V.T.C.V.V.V.D.V.S.H.E.D.P.E.V.K.F.N.W.Y.V.D.G.V.E
            # .V.H.N.A.K.T.K.P.R.E.E.Q.Y.N.S.T.Y.R.V.V.S.V.L.T.V.L.H.Q.D.W.L.N.G.K.E.Y.K.C.K.V.S.N.K.A.L.P.A.P.I.E.K.T.I
            # .S.K.A.K.G.Q.P.R.E.P.Q.V.Y.T.L.P.P.S.R.E.E.M.T.K.N.Q.V.S.L.T.C.L.V.K.G.F.Y.P.S.D.I.A.V.E.W.E.S.N.G.Q.P.E.N
            # .N.Y.K.T.T.P.P.V.L.D.S.D.G.S.F.F.L.Y.S.K.L.T.V.D.K.S.R.W.Q.Q.G.N.V.F.S.C.S.V.M.H.E.A.L.H.N.H.Y.T.Q.K.S.L.S
            # .L.S.P.G.K}|PEPTIDE4{E.I.V.L.T.Q.S.P.G.T.L.S.L.S.P.G.E.R.A.T.L.S.C.R.A.S.Q.S.V.S.S.T.Y.L.A.W.Y.Q.Q.K.P.G.Q
            # .A.P.R.L.L.I.Y.G.A.S.S.R.A.T.G.I.P.D.R.F.S.G.S.G.S.G.T.D.F.T.L.T.I.S.R.L.E.P.E.D.F.A.V.Y.Y.C.Q.Q.Y.G.S.S.P
            # .R.T.F.G.Q.G.T.K.V.E.I.K.R.T.V.A.A.P.S.V.F.I.F.P.P.S.D.E.Q.L.K.S.G.T.A.S.V.V.C.L.L.N.N.F.Y.P.R.E.A.K.V.Q.W
            # .K.V.D.N.A.L.Q.S.G.N.S.Q.E.S.V.T.E.Q.D.S.K.D.S.T.Y.S.L.S.S.T.L.T.L.S.K.A.D.Y.E.K.H.K.V.Y.A.C.E.V.T.H.Q.G.L
            # .S.S.P.V.T.K.S.F.N.R.G.E.C}$PEPTIDE2,PEPTIDE2,143:R3-199:R3|PEPTIDE2,PEPTIDE1,219:R3-215:R3|PEPTIDE3,PEPTI
            # DE4,219:R3-215:R3|PEPTIDE3,PEPTIDE3,260:R3-320:R3|PEPTIDE2,PEPTIDE2,22:R3-96:R3|PEPTIDE3,PEPTIDE3,366:R3-4
            # 24:R3|PEPTIDE4,PEPTIDE4,135:R3-195:R3|PEPTIDE1,PEPTIDE1,23:R3-89:R3|PEPTIDE2,PEPTIDE2,260:R3-320:R3|PEPTID
            # E2,PEPTIDE3,225:R3-225:R3|PEPTIDE1,PEPTIDE1,135:R3-195:R3|PEPTIDE2,PEPTIDE2,366:R3-424:R3|PEPTIDE3,PEPTIDE
            # 3,143:R3-199:R3|PEPTIDE4,PEPTIDE4,23:R3-89:R3|PEPTIDE3,PEPTIDE3,22:R3-96:R3|PEPTIDE2,PEPTIDE3,228:R3-228:R
            # 3$$$' , 'PEPTIDE1{E.I.V.L.T.Q.S.P.A.T.L.S.L.S.P.G.E.R.A.T.L.S.C.S.A.S.I.S.V.S.Y.M.Y.W.Y.Q.Q.K.P.G.Q.A.P.R.
            # L.L.I.Y.D.M.S.N.L.A.S.G.I.P.A.R.F.S.G.S.G.S.G.T.D.F.T.L.T.I.S.S.L.E.P.E.D.F.A.V.Y.Y.C.M.Q.W.S.G.Y.P.Y.T.F.
            # G.G.G.T.K.V.E.I.K.R.T.V.A.A.P.S.V.F.I.F.P.P.S.D.E.Q.L.K.S.G.T.A.S.V.V.C.L.L.N.N.F.Y.P.R.E.A.K.V.Q.W.K.V.D.
            # N.A.L.Q.S.G.N.S.Q.E.S.V.T.E.Q.D.S.K.D.S.T.Y.S.L.S.S.T.L.T.L.S.K.A.D.Y.E.K.H.K.V.Y.A.C.E.V.T.H.Q.G.L.S.S.P.
            # V.T.K.S.F.N.R.G.E.C}|PEPTIDE2{E.V.Q.L.V.E.S.G.G.G.L.V.Q.P.G.G.S.L.R.L.S.C.A.A.S.G.F.T.F.S.P.F.A.M.S.W.V.R.
            # Q.A.P.G.K.G.L.E.W.V.A.K.I.S.P.G.G.S.W.T.Y.Y.S.D.T.V.T.G.R.F.T.I.S.R.D.N.A.K.N.S.L.Y.L.Q.M.N.S.L.R.A.E.D.T.
            # A.V.Y.Y.C.A.R.Q.L.W.G.Y.Y.A.L.D.I.W.G.Q.G.T.T.V.T.V.S.S.A.S.T.K.G.P.S.V.F.P.L.A.P.S.S.K.S.T.S.G.G.T.A.A.L.
            # G.C.L.V.K.D.Y.F.P.E.P.V.T.V.S.W.N.S.G.A.L.T.S.G.V.H.T.F.P.A.V.L.Q.S.S.G.L.Y.S.L.S.S.V.V.T.V.P.S.S.S.L.G.T.
            # Q.T.Y.I.C.N.V.N.H.K.P.S.N.T.K.V.D.K.K.V.E.P.K.S.C.D.K.T.H.T.C.P.P.C.P.A.P.E.L.L.G.G.P.S.V.F.L.F.P.P.K.P.K.
            # D.T.L.M.I.S.R.T.P.E.V.T.C.V.V.V.D.V.S.H.E.D.P.E.V.K.F.N.W.Y.V.D.G.V.E.V.H.N.A.K.T.K.P.R.E.E.Q.Y.N.S.T.Y.R.
            # V.V.S.V.L.T.V.L.H.Q.D.W.L.N.G.K.E.Y.K.C.K.V.S.N.K.A.L.P.A.P.I.E.K.T.I.S.K.A.K.G.Q.P.R.E.P.Q.V.Y.T.L.P.P.S.
            # R.D.E.L.T.K.N.Q.V.S.L.T.C.L.V.K.G.F.Y.P.S.D.I.A.V.E.W.E.S.N.G.Q.P.E.N.N.Y.K.T.T.P.P.V.L.D.S.D.G.S.F.F.L.Y.
            # S.K.L.T.V.D.K.S.R.W.Q.Q.G.N.V.F.S.C.S.V.M.H.E.A.L.H.N.H.Y.T.Q.K.S.L.S.L.S.P.G.K}|PEPTIDE3{E.V.Q.L.V.E.S.G.
            # G.G.L.V.Q.P.G.G.S.L.R.L.S.C.A.A.S.G.F.T.F.S.P.F.A.M.S.W.V.R.Q.A.P.G.K.G.L.E.W.V.A.K.I.S.P.G.G.S.W.T.Y.Y.S.
            # D.T.V.T.G.R.F.T.I.S.R.D.N.A.K.N.S.L.Y.L.Q.M.N.S.L.R.A.E.D.T.A.V.Y.Y.C.A.R.Q.L.W.G.Y.Y.A.L.D.I.W.G.Q.G.T.T.
            # V.T.V.S.S.A.S.T.K.G.P.S.V.F.P.L.A.P.S.S.K.S.T.S.G.G.T.A.A.L.G.C.L.V.K.D.Y.F.P.E.P.V.T.V.S.W.N.S.G.A.L.T.S.
            # G.V.H.T.F.P.A.V.L.Q.S.S.G.L.Y.S.L.S.S.V.V.T.V.P.S.S.S.L.G.T.Q.T.Y.I.C.N.V.N.H.K.P.S.N.T.K.V.D.K.K.V.E.P.K.
            # S.C.D.K.T.H.T.C.P.P.C.P.A.P.E.L.L.G.G.P.S.V.F.L.F.P.P.K.P.K.D.T.L.M.I.S.R.T.P.E.V.T.C.V.V.V.D.V.S.H.E.D.P.
            # E.V.K.F.N.W.Y.V.D.G.V.E.V.H.N.A.K.T.K.P.R.E.E.Q.Y.N.S.T.Y.R.V.V.S.V.L.T.V.L.H.Q.D.W.L.N.G.K.E.Y.K.C.K.V.S.
            # N.K.A.L.P.A.P.I.E.K.T.I.S.K.A.K.G.Q.P.R.E.P.Q.V.Y.T.L.P.P.S.R.D.E.L.T.K.N.Q.V.S.L.T.C.L.V.K.G.F.Y.P.S.D.I.
            # A.V.E.W.E.S.N.G.Q.P.E.N.N.Y.K.T.T.P.P.V.L.D.S.D.G.S.F.F.L.Y.S.K.L.T.V.D.K.S.R.W.Q.Q.G.N.V.F.S.C.S.V.M.H.E.
            # A.L.H.N.H.Y.T.Q.K.S.L.S.L.S.P.G.K}|PEPTIDE4{E.I.V.L.T.Q.S.P.A.T.L.S.L.S.P.G.E.R.A.T.L.S.C.S.A.S.I.S.V.S.Y.
            # M.Y.W.Y.Q.Q.K.P.G.Q.A.P.R.L.L.I.Y.D.M.S.N.L.A.S.G.I.P.A.R.F.S.G.S.G.S.G.T.D.F.T.L.T.I.S.S.L.E.P.E.D.F.A.V.
            # Y.Y.C.M.Q.W.S.G.Y.P.Y.T.F.G.G.G.T.K.V.E.I.K.R.T.V.A.A.P.S.V.F.I.F.P.P.S.D.E.Q.L.K.S.G.T.A.S.V.V.C.L.L.N.N.
            # F.Y.P.R.E.A.K.V.Q.W.K.V.D.N.A.L.Q.S.G.N.S.Q.E.S.V.T.E.Q.D.S.K.D.S.T.Y.S.L.S.S.T.L.T.L.S.K.A.D.Y.E.K.H.K.V.
            # Y.A.C.E.V.T.H.Q.G.L.S.S.P.V.T.K.S.F.N.R.G.E.C}$PEPTIDE1,PEPTIDE1,23:R3-87:R3|PEPTIDE3,PEPTIDE4,222:R3-213:
            # R3|PEPTIDE2,PEPTIDE2,22:R3-96:R3|PEPTIDE1,PEPTIDE1,133:R3-193:R3|PEPTIDE4,PEPTIDE4,133:R3-193:R3|PEPTIDE2,
            # PEPTIDE2,146:R3-202:R3|PEPTIDE3,PEPTIDE3,369:R3-427:R3|PEPTIDE2,PEPTIDE1,222:R3-213:R3|PEPTIDE3,PEPTIDE3,1
            # 46:R3-202:R3|PEPTIDE3,PEPTIDE3,22:R3-96:R3|PEPTIDE3,PEPTIDE3,263:R3-323:R3|PEPTIDE2,PEPTIDE2,263:R3-323:R3
            # |PEPTIDE2,PEPTIDE3,228:R3-228:R3|PEPTIDE4,PEPTIDE4,23:R3-87:R3|PEPTIDE2,PEPTIDE2,369:R3-427:R3|PEPTIDE2,PE
            # PTIDE3,231:R3-231:R3$$$' , 'PEPTIDE1{D.V.V.M.T.Q.S.P.L.S.L.P.V.T.L.G.Q.P.A.S.I.S.C.R.S.S.Q.S.L.I.Y.S.D.G.N
            # .A.Y.L.H.W.F.L.Q.K.P.G.Q.S.P.R.L.L.I.Y.K.V.S.N.R.F.S.G.V.P.D.R.F.S.G.S.G.S.G.T.D.F.T.L.K.I.S.R.V.E.A.E.D.V
            # .G.V.Y.Y.C.S.Q.S.T.H.V.P.W.T.F.G.Q.G.T.K.V.E.I.K.R.T.V.A.A.P.S.V.F.I.F.P.P.S.D.E.Q.L.K.S.G.T.A.S.V.V.C.L.L
            # .N.N.F.Y.P.R.E.A.K.V.Q.W.K.V.D.N.A.L.Q.S.G.N.S.Q.E.S.V.T.E.Q.D.S.K.D.S.T.Y.S.L.S.S.T.L.T.L.S.K.A.D.Y.E.K.H
            # .K.V.Y.A.C.E.V.T.H.Q.G.L.S.S.P.V.T.K.S.F.N.R.G.E.C}|PEPTIDE2{E.V.Q.L.V.E.S.G.G.G.L.V.Q.P.G.G.S.L.R.L.S.C.A
            # .A.S.G.F.T.F.S.R.Y.S.M.S.W.V.R.Q.A.P.G.K.G.L.E.L.V.A.Q.I.N.S.V.G.N.S.T.Y.Y.P.D.T.V.K.G.R.F.T.I.S.R.D.N.A.K
            # .N.T.L.Y.L.Q.M.N.S.L.R.A.E.D.T.A.V.Y.Y.C.A.S.G.D.Y.W.G.Q.G.T.L.V.T.V.S.S.A.S.T.K.G.P.S.V.F.P.L.A.P.S.S.K.S
            # .T.S.G.G.T.A.A.L.G.C.L.V.K.D.Y.F.P.E.P.V.T.V.S.W.N.S.G.A.L.T.S.G.V.H.T.F.P.A.V.L.Q.S.S.G.L.Y.S.L.S.S.V.V.T
            # .V.P.S.S.S.L.G.T.Q.T.Y.I.C.N.V.N.H.K.P.S.N.T.K.V.D.K.K.V.E.P.K.S.C.D.K.T.H.T.C.P.P.C.P.A.P.E.L.L.G.G.P.S.V
            # .F.L.F.P.P.K.P.K.D.T.L.M.I.S.R.T.P.E.V.T.C.V.V.V.D.V.S.H.E.D.P.E.V.K.F.N.W.Y.V.D.G.V.E.V.H.N.A.K.T.K.P.R.E
            # .E.Q.Y.N.S.T.Y.R.V.V.S.V.L.T.V.L.H.Q.D.W.L.N.G.K.E.Y.K.C.K.V.S.N.K.A.L.P.A.P.I.E.K.T.I.S.K.A.K.G.Q.P.R.E.P
            # .Q.V.Y.T.L.P.P.S.R.D.E.L.T.K.N.Q.V.S.L.T.C.L.V.K.G.F.Y.P.S.D.I.A.V.E.W.E.S.N.G.Q.P.E.N.N.Y.K.T.T.P.P.V.L.D
            # .S.D.G.S.F.F.L.Y.S.K.L.T.V.D.K.S.R.W.Q.Q.G.N.V.F.S.C.S.V.M.H.E.A.L.H.N.H.Y.T.Q.K.S.L.S.L.S.P.G.K}|PEPTIDE3
            # {E.V.Q.L.V.E.S.G.G.G.L.V.Q.P.G.G.S.L.R.L.S.C.A.A.S.G.F.T.F.S.R.Y.S.M.S.W.V.R.Q.A.P.G.K.G.L.E.L.V.A.Q.I.N.S
            # .V.G.N.S.T.Y.Y.P.D.T.V.K.G.R.F.T.I.S.R.D.N.A.K.N.T.L.Y.L.Q.M.N.S.L.R.A.E.D.T.A.V.Y.Y.C.A.S.G.D.Y.W.G.Q.G.T
            # .L.V.T.V.S.S.A.S.T.K.G.P.S.V.F.P.L.A.P.S.S.K.S.T.S.G.G.T.A.A.L.G.C.L.V.K.D.Y.F.P.E.P.V.T.V.S.W.N.S.G.A.L.T
            # .S.G.V.H.T.F.P.A.V.L.Q.S.S.G.L.Y.S.L.S.S.V.V.T.V.P.S.S.S.L.G.T.Q.T.Y.I.C.N.V.N.H.K.P.S.N.T.K.V.D.K.K.V.E.P
            # .K.S.C.D.K.T.H.T.C.P.P.C.P.A.P.E.L.L.G.G.P.S.V.F.L.F.P.P.K.P.K.D.T.L.M.I.S.R.T.P.E.V.T.C.V.V.V.D.V.S.H.E.D
            # .P.E.V.K.F.N.W.Y.V.D.G.V.E.V.H.N.A.K.T.K.P.R.E.E.Q.Y.N.S.T.Y.R.V.V.S.V.L.T.V.L.H.Q.D.W.L.N.G.K.E.Y.K.C.K.V
            # .S.N.K.A.L.P.A.P.I.E.K.T.I.S.K.A.K.G.Q.P.R.E.P.Q.V.Y.T.L.P.P.S.R.D.E.L.T.K.N.Q.V.S.L.T.C.L.V.K.G.F.Y.P.S.D
            # .I.A.V.E.W.E.S.N.G.Q.P.E.N.N.Y.K.T.T.P.P.V.L.D.S.D.G.S.F.F.L.Y.S.K.L.T.V.D.K.S.R.W.Q.Q.G.N.V.F.S.C.S.V.M.H
            # .E.A.L.H.N.H.Y.T.Q.K.S.L.S.L.S.P.G.K}|PEPTIDE4{D.V.V.M.T.Q.S.P.L.S.L.P.V.T.L.G.Q.P.A.S.I.S.C.R.S.S.Q.S.L.I
            # .Y.S.D.G.N.A.Y.L.H.W.F.L.Q.K.P.G.Q.S.P.R.L.L.I.Y.K.V.S.N.R.F.S.G.V.P.D.R.F.S.G.S.G.S.G.T.D.F.T.L.K.I.S.R.V
            # .E.A.E.D.V.G.V.Y.Y.C.S.Q.S.T.H.V.P.W.T.F.G.Q.G.T.K.V.E.I.K.R.T.V.A.A.P.S.V.F.I.F.P.P.S.D.E.Q.L.K.S.G.T.A.S
            # .V.V.C.L.L.N.N.F.Y.P.R.E.A.K.V.Q.W.K.V.D.N.A.L.Q.S.G.N.S.Q.E.S.V.T.E.Q.D.S.K.D.S.T.Y.S.L.S.S.T.L.T.L.S.K.A
            # .D.Y.E.K.H.K.V.Y.A.C.E.V.T.H.Q.G.L.S.S.P.V.T.K.S.F.N.R.G.E.C}$PEPTIDE2,PEPTIDE2,362:R3-420:R3|PEPTIDE3,PEP
            # TIDE3,256:R3-316:R3|PEPTIDE3,PEPTIDE4,215:R3-219:R3|PEPTIDE4,PEPTIDE4,23:R3-93:R3|PEPTIDE2,PEPTIDE2,256:R3
            # -316:R3|PEPTIDE2,PEPTIDE3,224:R3-224:R3|PEPTIDE2,PEPTIDE1,215:R3-219:R3|PEPTIDE2,PEPTIDE3,221:R3-221:R3|PE
            # PTIDE2,PEPTIDE2,22:R3-96:R3|PEPTIDE4,PEPTIDE4,139:R3-199:R3|PEPTIDE1,PEPTIDE1,23:R3-93:R3|PEPTIDE3,PEPTIDE
            # 3,362:R3-420:R3|PEPTIDE2,PEPTIDE2,139:R3-195:R3|PEPTIDE1,PEPTIDE1,139:R3-199:R3|PEPTIDE3,PEPTIDE3,139:R3-1
            # 95:R3|PEPTIDE3,PEPTIDE3,22:R3-96:R3$$$'
            'indication_class': 'TEXT',
            # EXAMPLES:
            # 'Antihypertensive' , 'Smoking Cessation Adjunct' , 'Antibacterial' , 'Antibacterial' , 'Anti-Inflammatory'
            #  , 'Inhibitor (beta-lactamase); Synergist (penicillin/cephalosporin),Synergist (penicillin/cephalosporin);
            #  Inhibitor (beta-lactamase)' , 'Anti-Infective (DNA gyrase inhibitor)' , 'Inhibitor (beta-lactamase)' , 'A
            # ntibacterial' , 'Antibacterial'
            'molecule_chembl_id': 'TEXT',
            # EXAMPLES:
            # 'CHEMBL2' , 'CHEMBL3' , 'CHEMBL4' , 'CHEMBL5' , 'CHEMBL6246' , 'CHEMBL204021' , 'CHEMBL6' , 'CHEMBL403' , 
            # 'CHEMBL6259' , 'CHEMBL404'
            'molecule_properties': 
            {
                'properties': 
                {
                    'alogp': 'NUMERIC',
                    # EXAMPLES:
                    # '1.78' , '1.85' , '1.54' , '1.42' , '1.31' , '7.22' , '3.93' , '-0.79' , '2.72' , '-1.52'
                    'aromatic_rings': 'NUMERIC',
                    # EXAMPLES:
                    # '3' , '1' , '2' , '2' , '4' , '4' , '3' , '0' , '3' , '1'
                    'cx_logd': 'NUMERIC',
                    # EXAMPLES:
                    # '1.43' , '-0.04' , '-0.47' , '-0.45' , '-0.53' , '6.34' , '0.26' , '-4.35' , '1.44' , '-4.89'
                    'cx_logp': 'NUMERIC',
                    # EXAMPLES:
                    # '1.65' , '1.16' , '0.51' , '0.79' , '2.32' , '7.31' , '3.53' , '-0.89' , '2.23' , '-1.40'
                    'cx_most_apka': 'NUMERIC',
                    # EXAMPLES:
                    # '5.29' , '4.37' , '5.54' , '3.79' , '3.09' , '5.48' , '2.86' , '5.32' , '5.46' , '5.62'
                    'cx_most_bpka': 'NUMERIC',
                    # EXAMPLES:
                    # '7.24' , '8.58' , '6.16' , '6.06' , '8.31' , '6.42' , '0.75' , '5.99' , '10.33' , '6.45'
                    'full_molformula': 'TEXT',
                    # EXAMPLES:
                    # 'C19H21N5O4' , 'C10H14N2' , 'C18H20FN3O4' , 'C12H12N2O3' , 'C14H6O8' , 'C36H38F4N4O2S' , 'C19H16Cl
                    # NO4' , 'C8H11NO5S' , 'C21H19F2N3O3' , 'C10H12N4O5S'
                    'full_mwt': 'NUMERIC',
                    # EXAMPLES:
                    # '383.41' , '162.24' , '361.37' , '232.24' , '302.19' , '666.79' , '357.79' , '233.25' , '399.40' ,
                    #  '300.30'
                    'hba': 'NUMERIC',
                    # EXAMPLES:
                    # '8' , '2' , '6' , '4' , '8' , '6' , '4' , '4' , '5' , '7'
                    'hba_lipinski': 'NUMERIC',
                    # EXAMPLES:
                    # '9' , '2' , '7' , '5' , '8' , '6' , '5' , '6' , '6' , '9'
                    'hbd': 'NUMERIC',
                    # EXAMPLES:
                    # '1' , '0' , '1' , '1' , '4' , '0' , '1' , '1' , '1' , '1'
                    'hbd_lipinski': 'NUMERIC',
                    # EXAMPLES:
                    # '2' , '0' , '1' , '1' , '4' , '0' , '1' , '1' , '1' , '1'
                    'heavy_atoms': 'NUMERIC',
                    # EXAMPLES:
                    # '28' , '12' , '26' , '17' , '22' , '47' , '25' , '15' , '29' , '20'
                    'molecular_species': 'TEXT',
                    # EXAMPLES:
                    # 'NEUTRAL' , 'BASE' , 'ACID' , 'ACID' , 'ACID' , 'NEUTRAL' , 'ACID' , 'ACID' , 'ACID' , 'ACID'
                    'mw_freebase': 'NUMERIC',
                    # EXAMPLES:
                    # '383.41' , '162.24' , '361.37' , '232.24' , '302.19' , '666.79' , '357.79' , '233.25' , '399.40' ,
                    #  '300.30'
                    'mw_monoisotopic': 'NUMERIC',
                    # EXAMPLES:
                    # '383.1594' , '162.1157' , '361.1438' , '232.0848' , '302.0063' , '666.2652' , '357.0768' , '233.03
                    # 58' , '399.1394' , '300.0528'
                    'num_lipinski_ro5_violations': 'NUMERIC',
                    # EXAMPLES:
                    # '0' , '0' , '0' , '0' , '0' , '2' , '0' , '0' , '0' , '0'
                    'num_ro5_violations': 'NUMERIC',
                    # EXAMPLES:
                    # '0' , '0' , '0' , '0' , '0' , '2' , '0' , '0' , '0' , '0'
                    'psa': 'NUMERIC',
                    # EXAMPLES:
                    # '106.95' , '16.13' , '75.01' , '72.19' , '141.34' , '58.44' , '68.53' , '91.75' , '65.78' , '122.4
                    # 6'
                    'qed_weighted': 'NUMERIC',
                    # EXAMPLES:
                    # '0.73' , '0.63' , '0.87' , '0.85' , '0.22' , '0.09' , '0.77' , '0.60' , '0.73' , '0.67'
                    'ro3_pass': 'TEXT',
                    # EXAMPLES:
                    # 'N' , 'Y' , 'N' , 'N' , 'N' , 'N' , 'N' , 'N' , 'N' , 'N'
                    'rtb': 'NUMERIC',
                    # EXAMPLES:
                    # '4' , '1' , '2' , '2' , '0' , '13' , '4' , '1' , '3' , '3'
                }
            },
            'molecule_structures': 
            {
                'properties': 
                {
                    'canonical_smiles': 'TEXT',
                    # EXAMPLES:
                    # 'COc1cc2nc(N3CCN(C(=O)c4ccco4)CC3)nc(N)c2cc1OC' , 'CN1CCC[C@H]1c1cccnc1' , 'CC1COc2c(N3CCN(C)CC3)c
                    # (F)cc3c(=O)c(C(=O)O)cn1c23' , 'CCn1cc(C(=O)O)c(=O)c2ccc(C)nc21' , 'O=c1oc2c(O)c(O)cc3c(=O)oc4c(O)c
                    # (O)cc1c4c23' , 'CCN(CC)CCN(Cc1ccc(-c2ccc(C(F)(F)F)cc2)cc1)C(=O)Cn1c(SCc2ccc(F)cc2)nc(=O)c2c1CCC2' 
                    # , 'COc1ccc2c(c1)c(CC(=O)O)c(C)n2C(=O)c1ccc(Cl)cc1' , 'CC1(C)[C@H](C(=O)O)N2C(=O)C[C@H]2S1(=O)=O' ,
                    #  'CN1CCN(c2cc3c(cc2F)c(=O)c(C(=O)O)cn3-c2ccc(F)cc2)CC1' , 'C[C@]1(Cn2ccnn2)[C@H](C(=O)O)N2C(=O)C[C
                    # @H]2S1(=O)=O'
                    'standard_inchi': 'TEXT',
                    # EXAMPLES:
                    # 'InChI=1S/C19H21N5O4/c1-26-15-10-12-13(11-16(15)27-2)21-19(22-17(12)20)24-7-5-23(6-8-24)18(25)14-4
                    # -3-9-28-14/h3-4,9-11H,5-8H2,1-2H3,(H2,20,21,22)' , 'InChI=1S/C10H14N2/c1-12-7-3-5-10(12)9-4-2-6-11
                    # -8-9/h2,4,6,8,10H,3,5,7H2,1H3/t10-/m0/s1' , 'InChI=1S/C18H20FN3O4/c1-10-9-26-17-14-11(16(23)12(18(
                    # 24)25)8-22(10)14)7-13(19)15(17)21-5-3-20(2)4-6-21/h7-8,10H,3-6,9H2,1-2H3,(H,24,25)' , 'InChI=1S/C1
                    # 2H12N2O3/c1-3-14-6-9(12(16)17)10(15)8-5-4-7(2)13-11(8)14/h4-6H,3H2,1-2H3,(H,16,17)' , 'InChI=1S/C1
                    # 4H6O8/c15-5-1-3-7-8-4(14(20)22-11(7)9(5)17)2-6(16)10(18)12(8)21-13(3)19/h1-2,15-18H' , 'InChI=1S/C
                    # 36H38F4N4O2S/c1-3-42(4-2)20-21-43(22-25-8-12-27(13-9-25)28-14-16-29(17-15-28)36(38,39)40)33(45)23-
                    # 44-32-7-5-6-31(32)34(46)41-35(44)47-24-26-10-18-30(37)19-11-26/h8-19H,3-7,20-24H2,1-2H3' , 'InChI=
                    # 1S/C19H16ClNO4/c1-11-15(10-18(22)23)16-9-14(25-2)7-8-17(16)21(11)19(24)12-3-5-13(20)6-4-12/h3-9H,1
                    # 0H2,1-2H3,(H,22,23)' , 'InChI=1S/C8H11NO5S/c1-8(2)6(7(11)12)9-4(10)3-5(9)15(8,13)14/h5-6H,3H2,1-2H
                    # 3,(H,11,12)/t5-,6+/m1/s1' , 'InChI=1S/C21H19F2N3O3/c1-24-6-8-25(9-7-24)19-11-18-15(10-17(19)23)20(
                    # 27)16(21(28)29)12-26(18)14-4-2-13(22)3-5-14/h2-5,10-12H,6-9H2,1H3,(H,28,29)' , 'InChI=1S/C10H12N4O
                    # 5S/c1-10(5-13-3-2-11-12-13)8(9(16)17)14-6(15)4-7(14)20(10,18)19/h2-3,7-8H,4-5H2,1H3,(H,16,17)/t7-,
                    # 8+,10+/m1/s1'
                    'standard_inchi_key': 'TEXT',
                    # EXAMPLES:
                    # 'IENZQIKPVFGBNW-UHFFFAOYSA-N' , 'SNICXCGAKADSCV-JTQLQIEISA-N' , 'GSDSWSVVBLHKDQ-UHFFFAOYSA-N' , 'M
                    # HWLWQUZZRMNGJ-UHFFFAOYSA-N' , 'AFSDNFLWKVMVRB-UHFFFAOYSA-N' , 'WDPFJWLDPVQCAJ-UHFFFAOYSA-N' , 'CGI
                    # GDMFJXJATDK-UHFFFAOYSA-N' , 'FKENQMMABCRJMK-RITPCOANSA-N' , 'NOCJXYPHIIZEHN-UHFFFAOYSA-N' , 'LPQZK
                    # KCYTLCDGQ-WEDXCCLWSA-N'
                }
            },
            'molecule_synonyms': 
            {
                'properties': 
                {
                    'molecule_synonym': 'TEXT',
                    # EXAMPLES:
                    # 'CP-12299' , 'Habitrol' , 'DL-8280' , 'Mictral' , 'Benzoaric acid' , 'Darapladib' , 'Artracin' , '
                    # CP-45899' , 'Difloxacin' , 'CL 298,741'
                    'syn_type': 'TEXT',
                    # EXAMPLES:
                    # 'RESEARCH_CODE' , 'TRADE_NAME' , 'RESEARCH_CODE' , 'TRADE_NAME' , 'OTHER' , 'INN' , 'TRADE_NAME' ,
                    #  'RESEARCH_CODE' , 'INN' , 'RESEARCH_CODE'
                    'synonyms': 'TEXT',
                    # EXAMPLES:
                    # 'CP-12299' , 'HABITROL' , 'DL-8280' , 'MICTRAL' , 'BENZOARIC ACID' , 'DARAPLADIB' , 'ARTRACIN' , '
                    # CP-45899' , 'DIFLOXACIN' , 'CL 298,741'
                }
            },
            'ob_patent': 'NUMERIC',
            # EXAMPLES:
            # '8323683' , '8734847' , '6900184' , '6284804' , '6384020' , '6465463' , '8895546' , '9504655' , '7994214' 
            # , '6923984'
            'oral': 'BOOLEAN',
            # EXAMPLES:
            # 'True' , 'True' , 'True' , 'True' , 'False' , 'False' , 'True' , 'False' , 'False' , 'False'
            'parenteral': 'BOOLEAN',
            # EXAMPLES:
            # 'False' , 'False' , 'True' , 'False' , 'False' , 'False' , 'True' , 'True' , 'False' , 'True'
            'prodrug': 'BOOLEAN',
            # EXAMPLES:
            # 'False' , 'False' , 'False' , 'False' , 'False' , 'False' , 'False' , 'False' , 'False' , 'False'
            'research_codes': 'TEXT',
            # EXAMPLES:
            # 'NSC-292810' , 'NSC-97238' , 'DL-8280' , 'NSC-82174' , 'NSC-656272' , 'SB-480848' , 'NSC-77541' , 'CP-45,8
            # 99-99' , 'ABBOTT-56619' , 'CL-298741'
            'rule_of_five': 'BOOLEAN',
            # EXAMPLES:
            # 'True' , 'True' , 'True' , 'True' , 'True' , 'False' , 'True' , 'True' , 'True' , 'True'
            'sc_patent': 'TEXT',
            # EXAMPLES:
            # 'US-8323683-B2' , 'US-8734847-B2' , 'US-6900184-B2' , 'US-6284804-B1' , 'US-6384020-B1' , 'US-6465463-B1' 
            # , 'US-8895546-B2' , 'US-9504655-B2' , 'US-7994214-B2' , 'US-6923984-B1'
            'synonyms': 'TEXT',
            # EXAMPLES:
            # 'Prazosin hydrochloride (FDA, JAN, MI, USAN, USP)' , 'Nicotine bitartrate (MI, USAN)' , 'Ofloxacin (BAN, F
            # DA, INN, JAN, MI, USAN, USP)' , 'Nalidixate sodium (USAN)' , 'Ellagic acid (DCF, INN, MI)' , 'Darapladib (
            # INN, JAN, MI, USAN)' , 'Indometacin sodium (JAN)' , 'Sulbactam sodium (FDA, JAN, USAN, USP)' , 'Difloxacin
            #  (INN)' , 'Tazobactam sodium (FDA, USAN)'
            'topical': 'BOOLEAN',
            # EXAMPLES:
            # 'False' , 'True' , 'True' , 'False' , 'False' , 'False' , 'True' , 'False' , 'False' , 'False'
            'usan_stem': 'TEXT',
            # EXAMPLES:
            # '-azosin' , '-oxacin' , 'nal-' , '-pladib' , '-bactam' , '-oxacin' , '-bactam' , '-oxacin' , '-oxacin' , '
            # -oxacin'
            'usan_stem_definition': 'TEXT',
            # EXAMPLES:
            # 'antihypertensives (prazosin type)' , 'antibacterials (quinolone derivatives)' , 'narcotic agonists/antago
            # nists (normorphine type)' , 'phospholipase A2 inhibitors' , 'beta-lactamase inhibitors' , 'antibacterials 
            # (quinolone derivatives)' , 'beta-lactamase inhibitors' , 'antibacterials (quinolone derivatives)' , 'antib
            # acterials (quinolone derivatives)' , 'antibacterials (quinolone derivatives)'
            'usan_stem_substem': 'TEXT',
            # EXAMPLES:
            # '-azosin(-azosin)' , '-oxacin(-oxacin)' , 'nal-(nal-)' , '-pladib(-pladib)' , '-bactam(-bactam)' , '-oxaci
            # n(-oxacin)' , '-bactam(-bactam)' , '-oxacin(-oxacin)' , '-oxacin(-oxacin)' , '-oxacin(-oxacin)'
            'usan_year': 'NUMERIC',
            # EXAMPLES:
            # '1968' , '1985' , '1984' , '1962' , '2005' , '1963' , '1980' , '1986' , '1989' , '1987'
            'withdrawn_class': 'TEXT',
            # EXAMPLES:
            # 'Hepatotoxicity' , 'Hepatotoxicity' , 'Gastrotoxicity' , 'Hepatotoxicity' , 'Misuse' , 'Misuse' , 'Misuse'
            #  , 'Misuse' , 'Hepatotoxicity' , 'Teratogenicity'
            'withdrawn_country': 'TEXT',
            # EXAMPLES:
            # 'United States' , 'United States' , 'European Union; United States' , 'United States' , 'Canada; Italy; Ar
            # gentina' , 'United States' , 'Norway' , 'France; Norway' , 'Norway' , 'Norway'
            'withdrawn_reason': 'TEXT',
            # EXAMPLES:
            # 'Hepatotoxicity' , 'Hepatotoxicity' , 'Increased risk of dysglycemia' , 'Hepatic necrosis' , 'Self-poisoni
            # ngs' , 'Self-poisoning' , 'Self-Poisonings' , 'Self-Poisonings' , 'Liver Toxicity and Death' , 'Risk for b
            # irth defects'
            'withdrawn_year': 'NUMERIC',
            # EXAMPLES:
            # '1997' , '1999' , '2006' , '1996' , '1980' , '1980' , '1980' , '1980' , '1986' , '1980'
        }
    }
