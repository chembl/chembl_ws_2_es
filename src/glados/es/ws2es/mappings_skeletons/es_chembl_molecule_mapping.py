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
                    'atc_classifications': 
                    {
                        'properties': 
                        {
                            'level1': 'TEXT',
                            # EXAMPLES:
                            # 'P' , 'L' , 'M' , 'M' , 'N' , 'G' , 'A' , 'C' , 'A' , 'L'
                            'level1_description': 'TEXT',
                            # EXAMPLES:
                            # 'P - ANTIPARASITIC PRODUCTS, INSECTICIDES AND REPELLENTS' , 'L - ANTINEOPLASTIC AND IMMUNO
                            # MODULATING AGENTS' , 'M - MUSCULO-SKELETAL SYSTEM' , 'M - MUSCULO-SKELETAL SYSTEM' , 'N - 
                            # NERVOUS SYSTEM' , 'G - GENITO URINARY SYSTEM AND SEX HORMONES' , 'A - ALIMENTARY TRACT AND
                            #  METABOLISM' , 'C - CARDIOVASCULAR SYSTEM' , 'A - ALIMENTARY TRACT AND METABOLISM' , 'L - 
                            # ANTINEOPLASTIC AND IMMUNOMODULATING AGENTS'
                            'level2': 'TEXT',
                            # EXAMPLES:
                            # 'P03' , 'L03' , 'M01' , 'M02' , 'N05' , 'G04' , 'A16' , 'C10' , 'A11' , 'L01'
                            'level2_description': 'TEXT',
                            # EXAMPLES:
                            # 'P03 - ECTOPARASITICIDES, INCL. SCABICIDES, INSECTICIDES AND REPELLENTS' , 'L03 - IMMUNOST
                            # IMULANTS' , 'M01 - ANTIINFLAMMATORY AND ANTIRHEUMATIC PRODUCTS' , 'M02 - TOPICAL PRODUCTS 
                            # FOR JOINT AND MUSCULAR PAIN' , 'N05 - PSYCHOLEPTICS' , 'G04 - UROLOGICALS' , 'A16 - OTHER 
                            # ALIMENTARY TRACT AND METABOLISM PRODUCTS' , 'C10 - LIPID MODIFYING AGENTS' , 'A11 - VITAMI
                            # NS' , 'L01 - ANTINEOPLASTIC AGENTS'
                            'level3': 'TEXT',
                            # EXAMPLES:
                            # 'P03B' , 'L03A' , 'M01A' , 'M02A' , 'N05C' , 'G04B' , 'A16A' , 'C10A' , 'A11H' , 'L01X'
                            'level3_description': 'TEXT',
                            # EXAMPLES:
                            # 'P03B - INSECTICIDES AND REPELLENTS' , 'L03A - IMMUNOSTIMULANTS' , 'M01A - ANTIINFLAMMATOR
                            # Y AND ANTIRHEUMATIC PRODUCTS, NON-STEROIDS' , 'M02A - TOPICAL PRODUCTS FOR JOINT AND MUSCU
                            # LAR PAIN' , 'N05C - HYPNOTICS AND SEDATIVES' , 'G04B - UROLOGICALS' , 'A16A - OTHER ALIMEN
                            # TARY TRACT AND METABOLISM PRODUCTS' , 'C10A - LIPID MODIFYING AGENTS, PLAIN' , 'A11H - OTH
                            # ER PLAIN VITAMIN PREPARATIONS' , 'L01X - OTHER ANTINEOPLASTIC AGENTS'
                            'level4': 'TEXT',
                            # EXAMPLES:
                            # 'P03BA' , 'L03AX' , 'M01AE' , 'M02AA' , 'N05CM' , 'G04BE' , 'A16AA' , 'C10AB' , 'A11HA' , 
                            # 'L01XE'
                            'level4_description': 'TEXT',
                            # EXAMPLES:
                            # 'P03BA - Pyrethrines' , 'L03AX - Other immunostimulants' , 'M01AE - Propionic acid derivat
                            # ives' , 'M02AA - Antiinflammatory preparations, non-steroids for topical use' , 'N05CM - O
                            # ther hypnotics and sedatives' , 'G04BE - Drugs used in erectile dysfunction' , 'A16AA - Am
                            # ino acids and derivatives' , 'C10AB - Fibrates' , 'A11HA - Other plain vitamin preparation
                            # s' , 'L01XE - Protein kinase inhibitors'
                            'level5': 'TEXT',
                            # EXAMPLES:
                            # 'P03BA03' , 'L03AX18' , 'M01AE10' , 'M02AA05' , 'N05CM18' , 'G04BE08' , 'A16AA04' , 'C10AB
                            # 02' , 'A11HA05' , 'L01XE01'
                            'who_name': 'TEXT',
                            # EXAMPLES:
                            # 'decamethrin' , 'cridanimod' , 'indoprofen' , 'benzydamine' , 'dexmedetomidine' , 'tadalaf
                            # il' , 'mercaptamine' , 'bezafibrate' , 'biotin' , 'imatinib'
                        }
                    },
                    'compound_generated': 
                    {
                        'properties': 
                        {
                            'availability_type_label': 'TEXT',
                            # EXAMPLES:
                            # 'Unknown' , 'Unknown' , 'Unknown' , 'Unknown' , 'Unknown' , 'Unknown' , 'Unknown' , 'Unkno
                            # wn' , 'Unknown' , 'Unknown'
                            'chirality_label': 'TEXT',
                            # EXAMPLES:
                            # 'Unknown' , 'Unknown' , 'Unknown' , 'Unknown' , 'Unknown' , 'Unknown' , 'Unknown' , 'Unkno
                            # wn' , 'Unknown' , 'Unknown'
                            'image_file': 'TEXT',
                            # EXAMPLES:
                            # 'unknown.svg' , 'unknown.svg' , 'metalContaining.svg' , 'unknown.svg' , 'metalContaining.s
                            # vg' , 'metalContaining.svg' , 'metalContaining.svg' , 'metalContaining.svg' , 'metalContai
                            # ning.svg' , 'metalContaining.svg'
                        }
                    },
                    'compound_records': 
                    {
                        'properties': 
                        {
                            'compound_key': 'TEXT',
                            # EXAMPLES:
                            # 'SID24787119' , 'SID49733282' , 'SID24841359' , 'SID22406147' , 'SID3715914' , 'SID4973307
                            # 8' , 'SID24834653' , 'SID49667584' , 'SID24818566' , 'SID26663220'
                            'compound_name': 'TEXT',
                            # EXAMPLES:
                            # 'SID24787119' , 'SID49733282' , 'SID24841359' , 'SID22406147' , 'SID3715914' , 'SID4973307
                            # 8' , 'SID24834653' , 'SID49667584' , 'SID24818566' , 'SID26663220'
                            'src_description': 'TEXT',
                            # EXAMPLES:
                            # 'PubChem BioAssays' , 'PubChem BioAssays' , 'PubChem BioAssays' , 'PubChem BioAssays' , 'P
                            # ubChem BioAssays' , 'PubChem BioAssays' , 'PubChem BioAssays' , 'PubChem BioAssays' , 'Pub
                            # Chem BioAssays' , 'PubChem BioAssays'
                            'src_id': 'NUMERIC',
                            # EXAMPLES:
                            # '7' , '7' , '7' , '7' , '7' , '7' , '7' , '7' , '7' , '7'
                            'src_short_name': 'TEXT',
                            # EXAMPLES:
                            # 'PUBCHEM_BIOASSAY' , 'PUBCHEM_BIOASSAY' , 'PUBCHEM_BIOASSAY' , 'PUBCHEM_BIOASSAY' , 'PUBCH
                            # EM_BIOASSAY' , 'PUBCHEM_BIOASSAY' , 'PUBCHEM_BIOASSAY' , 'PUBCHEM_BIOASSAY' , 'PUBCHEM_BIO
                            # ASSAY' , 'PUBCHEM_BIOASSAY'
                        }
                    },
                    'compound_structural_alerts': 
                    {
                        'properties': 
                        {
                            'alert_count': 'NUMERIC',
                            # EXAMPLES:
                            # '3' , '11' , '4' , '2' , '1' , '1' , '6' , '4' , '2' , '7'
                            'alerts': 
                            {
                                'properties': 
                                {
                                    'alert': 
                                    {
                                        'properties': 
                                        {
                                            'alert_id': 'NUMERIC',
                                            # EXAMPLES:
                                            # '63' , '1078' , '1030' , '1064' , '1064' , '1043' , '139' , '62' , '1064' 
                                            # , '1025'
                                            'alert_name': 'TEXT',
                                            # EXAMPLES:
                                            # 'Aliphatic long chain' , 'Oxalyl' , 'Ester' , 'Hetero_hetero' , 'Hetero_he
                                            # tero' , 'Dye 25' , 'quaternary nitrogen' , 'aldehyde' , 'Hetero_hetero' , 
                                            # 'Azo'
                                            'alert_set': 
                                            {
                                                'properties': 
                                                {
                                                    'priority': 'NUMERIC',
                                                    # EXAMPLES:
                                                    # '4' , '3' , '3' , '3' , '3' , '3' , '4' , '4' , '3' , '3'
                                                    'set_name': 'TEXT',
                                                    # EXAMPLES:
                                                    # 'Dundee' , 'MLSMR' , 'MLSMR' , 'MLSMR' , 'MLSMR' , 'MLSMR' , 'Dund
                                                    # ee' , 'Dundee' , 'MLSMR' , 'MLSMR'
                                                }
                                            },
                                            'smarts': 'TEXT',
                                            # EXAMPLES:
                                            # '[R0;D2][R0;D2][R0;D2][R0;D2]' , 'O=C-&!@C=O' , '[#6]-C(=O)O-[#6]' , '*[N,
                                            # S,O]-&!@[N,S,O][#6]' , '*[N,S,O]-&!@[N,S,O][#6]' , 'acC=&!@Cca' , '[s,S,c,
                                            # C,n,N,o,O]~[n+,N+](~[s,S,c,C,n,N,o,O])(~[s,S,c,C,n,N,o,O])~[s,S,c,C,n,N,o,
                                            # O]' , '[CH1](=O)' , '*[N,S,O]-&!@[N,S,O][#6]' , 'N=N'
                                        }
                                    },
                                    'cpd_str_alert_id': 'NUMERIC',
                                    # EXAMPLES:
                                    # '45922557' , '48929736' , '47761792' , '48658371' , '48658374' , '48382261' , '492
                                    # 12493' , '45815279' , '48658376' , '47436261'
                                    'molecule_chembl_id': 'TEXT',
                                    # EXAMPLES:
                                    # 'CHEMBL1584351' , 'CHEMBL1584363' , 'CHEMBL1584365' , 'CHEMBL1584367' , 'CHEMBL158
                                    # 4374' , 'CHEMBL1584379' , 'CHEMBL1584381' , 'CHEMBL1584384' , 'CHEMBL1584388' , 'C
                                    # HEMBL1584392'
                                }
                            }
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
                                    'applicants': 'TEXT',
                                    # EXAMPLES:
                                    # 'Actavis Inc' , 'Sun Pharmaceutical Industries Ltd' , 'Horizon Pharma Usa Inc' , '
                                    # Hospira Inc' , 'Shilpa Medicare Ltd' , 'Mylan Pharmaceuticals Inc' , 'Mylan Pharma
                                    # ceuticals Inc' , 'Mylan Pharmaceuticals Inc' , 'Otsuka Pharmaceutical Co Ltd' , 'H
                                    # offmann La Roche Inc'
                                    'atc_classification': 
                                    {
                                        'properties': 
                                        {
                                            'code': 'TEXT',
                                            # EXAMPLES:
                                            # 'P03BA03' , 'L03AX18' , 'M01AE10' , 'G02CC03' , 'N05CM18' , 'G04BE08' , 'S
                                            # 01XA21' , 'C10AB02' , 'A11HA05' , 'L01XE01'
                                            'description': 'TEXT',
                                            # EXAMPLES:
                                            # 'ANTIPARASITIC PRODUCTS, INSECTICIDES AND REPELLENTS: ECTOPARASITICIDES, I
                                            # NCL. SCABICIDES, INSECTICIDES AND REPELLENTS: INSECTICIDES AND REPELLENTS:
                                            #  Pyrethrines' , 'ANTINEOPLASTIC AND IMMUNOMODULATING AGENTS: IMMUNOSTIMULA
                                            # NTS: IMMUNOSTIMULANTS: Other immunostimulants' , 'MUSCULO-SKELETAL SYSTEM:
                                            #  ANTIINFLAMMATORY AND ANTIRHEUMATIC PRODUCTS: ANTIINFLAMMATORY AND ANTIRHE
                                            # UMATIC PRODUCTS, NON-STEROIDS: Propionic acid derivatives' , 'GENITO URINA
                                            # RY SYSTEM AND SEX HORMONES: OTHER GYNECOLOGICALS: OTHER GYNECOLOGICALS: An
                                            # tiinflammatory products for vaginal administratio' , 'NERVOUS SYSTEM: PSYC
                                            # HOLEPTICS: HYPNOTICS AND SEDATIVES: Other hypnotics and sedatives' , 'GENI
                                            # TO URINARY SYSTEM AND SEX HORMONES: UROLOGICALS: UROLOGICALS: Drugs used i
                                            # n erectile dysfunction' , 'SENSORY ORGANS: OPHTHALMOLOGICALS: OTHER OPHTHA
                                            # LMOLOGICALS: Other ophthalmological' , 'CARDIOVASCULAR SYSTEM: LIPID MODIF
                                            # YING AGENTS: LIPID MODIFYING AGENTS, PLAIN: Fibrates' , 'ALIMENTARY TRACT 
                                            # AND METABOLISM: VITAMINS: OTHER PLAIN VITAMIN PREPARATIONS: Other plain vi
                                            # tamin preparations' , 'ANTINEOPLASTIC AND IMMUNOMODULATING AGENTS: ANTINEO
                                            # PLASTIC AGENTS: OTHER ANTINEOPLASTIC AGENTS: Protein kinase inhibitors'
                                        }
                                    },
                                    'availability_type': 'NUMERIC',
                                    # EXAMPLES:
                                    # '-2' , '-2' , '-2' , '-1' , '1' , '1' , '-1' , '1' , '-1' , '1'
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
                                                    # '19353' , '10166' , '10182' , '6359' , '6335' , '6553' , '6320' , 
                                                    # '6375' , '6393' , '6377'
                                                    'component_type': 'TEXT',
                                                    # EXAMPLES:
                                                    # 'PROTEIN' , 'PROTEIN' , 'PROTEIN' , 'PROTEIN' , 'PROTEIN' , 'PROTE
                                                    # IN' , 'PROTEIN' , 'PROTEIN' , 'PROTEIN' , 'PROTEIN'
                                                    'description': 'TEXT',
                                                    # EXAMPLES:
                                                    # 'RELABOTULINUMTOXINA Sequence' , 'UTOMILUMAB Heavy Chain' , 'TAMTU
                                                    # VETMAB Heavy Chain' , 'Blinatumumab single chain variable fragment
                                                    #  fusion protein (bite)' , 'Brentuximab vedotin heavy chain' , 'Bro
                                                    # dalumab heavy chain' , 'Cantuzumab ravtansine heavy chain' , 'Cixu
                                                    # tumumab heavy chain' , 'Conatumumab heavy chain' , 'Dalotuzumab he
                                                    # avy chain'
                                                    'organism': 'TEXT',
                                                    # EXAMPLES:
                                                    # 'Homo sapiens' , 'Homo sapiens' , 'Homo sapiens' , 'Homo sapiens' 
                                                    # , 'Homo sapiens' , 'Homo sapiens' , 'Homo sapiens' , 'Homo sapiens
                                                    # ' , 'Homo sapiens' , 'Homo sapiens'
                                                    'sequence': 'TEXT',
                                                    # EXAMPLES:
                                                    # 'PFVNKQFNYKDPVNGVDIAYIKIPNAGQMQPVKAFKIHNKIWVIPERDTFTNPEEGDLNPPPEAK
                                                    # QVPVSYYDSTYLSTDNEKDNYLKGVTKLFERIYSTDLGRMLLTSIVRGIPFWGGSTIDTELKVIDT
                                                    # NCINVIQPDGSYRSEELNLVIIGPSADIIQFECKSFGHEVLNLTRNGYGSTQYIRFSPDFTFGFEE
                                                    # SLEVDTNPLLGAGKFATDPAVTLAHELIHAGHRLYGIAINPNRVFKVNTNAYYEMSGLEVSFEELR
                                                    # TFGGHDAKFIDSLQENEFRLYYYNKFKDIASTLNKAKSIVGTTASLQYMKNVFKEKYLLSEDTSGK
                                                    # FSVDKLKFDKLYKMLTEIYTEDNFVKFFKVLNRKTYLNFDKAVFKINIVPKVNYTIYDGFNLRNTN
                                                    # LAANFNGQNTEINNMNFTKLKNFTGLFEFYKLLCVRGIITSKTKSLDKGYNKALNDLCIKVNNWDL
                                                    # FFSPSEDNFTNDLNKGEEITSDTNIEAAEENISLDLIQQYYLTFNFDNEPENISIENLSSDIIGQL
                                                    # ELMPNIERFPNGKKYELDKYTMFHYLRAQEFEHGKSRIALTNSVNEALLNPSRVYTFFSSDYVKKV
                                                    # NKATEAAMFLGWVEQLVYDFTDETSEVSTTDKIADITIIIPYIGPALNIGNMLYKDDFVGALIFSG
                                                    # AVILLEFIPEIAIPVLGTFALVSYIANKVLTVQTIDNALSKRNEKWDEVYKYIVTNWLAKVNTQID
                                                    # LIRKKMKEALENQAEATKAIINYQYNQYTEEEKNNINFNIDDLSSKLNESINKAMININKFLNQCS
                                                    # VSYLMNSMIPYGVKRLEDFDASLKDALLKYIYDNRGTLIGQVDRLKDKVNNTLSTDIPFQLSKYVD
                                                    # NQRLLSTFTEYIKNIINTSILNLRYESNHLIDLSRYASKINIGSKVNFDPIDKNQIQLFNLESSKI
                                                    # EVILKNAIVYNSMYENFSTSFWIRIPKYFNSISLNNEYTIINCMENNSGWKVSLNYGEIIWTLQDT
                                                    # QEIKQRVVFKYSQMINISDYINRWIFVTITNNRLNNSKIYINGRLIDQKPISNLGNIHASNNIMFK
                                                    # LDGCRDTHRYIWIKYFNLFDKELNEKEIKDLYDNQSNSGILKDFWGDYLQYDKPYYMLNLYDPNKY
                                                    # VDVNNVGIRGYMYLKGPRGSVMTTNIYLNSSLYRGTKFIIKKYASGNKDNIVRNNDRVYINVVVKN
                                                    # KEYRLATNASQAGVEKILSALEIPDVGNLSQVVVMKSKNDQGITNKCKMNLQDNNGNDIGFIGFHQ
                                                    # FNNIAKLVASNWYNRQIERSSRTLGCSWEFIPVDDGWGERPL' , 'EVQLVQSGAEVKKPGESLR
                                                    # ISCKGSGYSFSTYWISWVRQMPGKGLEWMGKIYPGDSYTNYSPSFQGQVTISADKSISTAYLQWSS
                                                    # LKASDTAMYYCARGYGIFDYWGQGTLVTVSSASTKGPSVFPLAPCSRSTSESTAALGCLVKDYFPE
                                                    # PVTVSWNSGALTSGVHTFPAVLQSSGLYSLSSVVTVPSSNFGTQTYTCNVDHKPSNTKVDKTVERK
                                                    # CCVECPPCPAPPVAGPSVFLFPPKPKDTLMISRTPEVTCVVVDVSHEDPEVQFNWYVDGVEVHNAK
                                                    # TKPREEQFNSTFRVVSVLTVVHQDWLNGKEYKCKVSNKGLPAPIEKTISKTKGQPREPQVYTLPPS
                                                    # REEMTKNQVSLTCLVKGFYPSDIAVEWESNGQPENNYKTTPPMLDSDGSFFLYSKLTVDKSRWQQG
                                                    # NVFSCSVMHEALHNHYTQKSLSLSPG' , 'EVKLLESGGGLVQPGGSMRLSCAGSGFTFTDFYMN
                                                    # WIRQPAGKAPEWLGFIRDKAKGYTTEYNPSVKGRFTISRDNTQNMLYLQMNTLRAEDTATYYCARE
                                                    # GHTAAPFDYWGQGTLVTVSSASTTAPSVFPLAPSCGSTSGSTVALACLVSGYFPEPVTVSWNSGSL
                                                    # TSGVHTFPSVLQSSGLYSLSSMVTVPSSRWPSETFTCNVAHPASKTKVDKPVPKRENGRVPRPPDC
                                                    # PKCPAPEMLGGPSVFIFPPKPKDTLLIARTPEVTCVVVDLDPEDPEVQISWFVDGKQMQTAKTQPR
                                                    # EEQFNGTYRVVSVLPIGHQDWLKGKQFTCKVNNKALPSPIERTISKARGQAHQPSVYVLPPSREEL
                                                    # SKNTVSLTCLIKDFFPPDIDVEWQSNGQQEPESKYRTTPPQLDEDGSYFLYSKLSVDKSRWQRGDT
                                                    # FICAVMHEALHNHYTQKSLSHSPGK' , 'DIQLTQSPASLAVSLGQRATISCKASQSVDYDGDSY
                                                    # LNWYQQIPGQPPKLLIYDASNLVSGIPPRFSGSGSGTDFTLNIHPVEKVDAATYHCQQSTEDPWTF
                                                    # GGGTKLEIKGGGGSGGGGSGGGGSQVQLQQSGAELVRPGSSVKISCKASGYAFSSYWMNWVKQRPG
                                                    # QGLEWIGQIWPGDGDTNYNGKFKGKATLTADESSSTAYMQLSSLASEDSAVYFCARRETTTVGRYY
                                                    # YAMDYWGQGTTVTVSSGGGGSDIKLQQSGAELARPGASVKMSCKTSGYTFTRYTMHWVKQRPGQGL
                                                    # EWIGYINPSRGYTNYNQKFKDKATLTTDKSSSTAYMQLSSLTSEDSAVYYCARYYDDHYCLDYWGQ
                                                    # GTTLTVSSVEGGSGGSGGSGGSGGVDDIQLTQSPAIMSASPGEKVTMTCRASSSVSYMNWYQQKSG
                                                    # TSPKRWIYDTSKVASGVPYRFSGSGSGTSYSLTISSMEAEDAATYYCQQWSSNPLTFGAGTKLELK
                                                    # HHHHHH' , 'QIQLQQSGPEVVKPGASVKISCKASGYTFTDYYITWVKQKPGQGLEWIGWIYPGS
                                                    # GNTKYNEKFKGKATLTVDTSSSTAFMQLSSLTSEDTAVYFCANYGNYWFAYWGQGTQVTVSAASTK
                                                    # GPSVFPLAPSSKSTSGGTAALGCLVKDYFPEPVTVSWNSGALTSGVHTFPAVLQSSGLYSLSSVVT
                                                    # VPSSSLGTQTYICNVNHKPSNTKVDKKVEPKSCDKTHTCPPCPAPELLGGPSVFLFPPKPKDTLMI
                                                    # SRTPEVTCVVVDVSHEDPEVKFNWYVDGVEVHNAKTKPREEQYNSTYRVVSVLTVLHQDWLNGKEY
                                                    # KCKVSNKALPAPIEKTISKAKGQPREPQVYTLPPSRDELTKNQVSLTCLVKGFYPSDIAVEWESNG
                                                    # QPENNYKTTPPVLDSDGSFFLYSKLTVDKSRWQQGNVFSCSVMHEALHNHYTQKSLSLSPG' , '
                                                    # QVQLVQSGAEVKKPGASVKVSCKASGYTFTRYGISWVRQAPGQGLEWMGWISTYSGNTNYAQKLQG
                                                    # RVTMTTDTSTSTAYMELRSLRSDDTAVYYCARRQLYFDYWGQGTLVTVSSASTKGPSVFPLAPCSR
                                                    # STSESTAALGCLVKDYFPEPVTVSWNSGALTSGVHTFPAVLQSSGLYSLSSVVTVPSSNFGTQTYT
                                                    # CNVDHKPSNTKVDKTVERKCCVECPPCPAPPVAGPSVFLFPPKPKDTLMISRTPEVTCVVVDVSHE
                                                    # DPEVQFNWYVDGVEVHNAKTKPREEQFNSTFRVVSVLTVVHQDWLNGKEYKCKVSNKGLPAPIEKT
                                                    # ISKTKGQPREPQVYTLPPSREEMTKNQVSLTCLVKGFYPSDIAVEWESNGQPENNYKTTPPMLDSD
                                                    # GSFFLYSKLTVDKSRWQQGNVFSCSVMHEALHNHYTQKSLSLSPGK' , 'QVQLVQSGAEVKKPG
                                                    # ETVKISCKASDYTFTYYGMNWVKQAPGQGLKWMGWIDTTTGEPTYAQKFQGRIAFSLETSASTAYL
                                                    # QIKSLKSEDTATYFCARRGPYNWYFDVWGQGTTVTVSSASTKGPSVFPLAPSSKSTSGGTAALGCL
                                                    # VKDYFPEPVTVSWNSGALTSGVHTFPAVLQSSGLYSLSSVVTVPSSSLGTQTYICNVNHKPSNTKV
                                                    # DKKVEPKSCDKTHTCPPCPAPELLGGPSVFLFPPKPKDTLMISRTPEVTCVVVDVSHEDPEVKFNW
                                                    # YVDGVEVHNAKTKPREEQYNSTYRVVSVLTVLHQDWLNGKEYKCKVSNKALPAPIEKTISKAKGQP
                                                    # REPQVYTLPPSRDELTKNQVSLTCLVKGFYPSDIAVEWESNGQPENNYKTTPPVLDSDGSFFLYSK
                                                    # LTVDKSRWQQGNVFSCSVMHEALHNHYTQKSLSLSPGK' , 'EVQLVQSGAEVKKPGSSVKVSCK
                                                    # ASGGTFSSYAISWVRQAPGQGLEWMGGIIPIFGTANYAQKFQGRVTITADKSTSTAYMELSSLRSE
                                                    # DTAVYYCARAPLRFLEWSTQDHYYYYYMDVWGKGTTVTVSSASTKGPSVFPLAPSSKSTSGGTAAL
                                                    # GCLVKDYFPEPVTVSWNSGALTSGVHTFPAVLQSSGLYSLSSVVTVPSSSLGTQTYICNVNHKPSN
                                                    # TKVDKKVEPKSCDKTHTCPPCPAPELLGGPSVFLFPPKPKDTLMISRTPEVTCVVVDVSHEDPEVK
                                                    # FNWYVDGVEVHNAKTKPREEQYNSTYRVVSVLTVLHQDWLNGKEYKCKVSNKALPAPIEKTISKAK
                                                    # GQPREPQVYTLPPSREEMTKNQVSLTCLVKGFYPSDIAVEWESNGQPENNYKTTPPVLDSDGSFFL
                                                    # YSKLTVDKSRWQQGNVFSCSVMHEALHNHYTQKSLSLSPGK' , 'QVQLQESGPGLVKPSQTLSL
                                                    # TCTVSGGSISSGDYFWSWIRQLPGKGLEWIGHIHNSGTTYYNPSLKSRVTISVDTSKKQFSLRLSS
                                                    # VTAADTAVYYCARDRGGDYYYGMDVWGQGTTVTVSSASTKGPSVFPLAPSSKSTSGGTAALGCLVK
                                                    # DYFPEPVTVSWNSGALTSGVHTFPAVLQSSGLYSLSSVVTVPSSSLGTQTYICNVNHKPSNTKVDK
                                                    # RVEPKSCDKTHTCPPCPAPELLGGPSVFLFPPKPKDTLMISRTPEVTCVVVDVSHEDPEVKFNWYV
                                                    # DGVEVHNAKTKPREEQYNSTYRVVSVLTVLHQDWLNGKEYKCKVSNKALPAPIEKTISKAKGQPRE
                                                    # PQVYTLPPSREEMTKNQVSLTCLVKGFYPSDIAVEWESNGQPENNYKTTPPVLDSDGSFFLYSKLT
                                                    # VDKSRWQQGNVFSCSVMHEALHNHYTQKSLSLSPGK' , 'QVQLQQSGPGLVKPSQTLSLTCTVS
                                                    # GWSISGGWLWNWIRQPPGKGLQWIGWISWDGTNNWKPSLKDRVTISVDTSKNQFSLKLSSVTAADT
                                                    # AVWWCARWGRVFFDWWGQGTLVTVSSASTKGPSVFPLAPSSKSTSGGTAALGCLVKDYFPEPVTVS
                                                    # WNSGALTSGVHTFPAVLQSSGLYSLSSVVTVPSSSLGTQTYICNVNHKPSNTKVDKRVEPKSCDKT
                                                    # HTCPPCPAPELLGGPSVFLFPPKPKDTLMISRTPEVTCVVVDVSHEDPEVKFNWYVDGVEVHNAKT
                                                    # KPREEQYNSTYRVVSVLTVLHQDWLNGKEYKCKVSNKALPAPIEKTISKAKGQPREPQVYTLPPSR
                                                    # EEMTKNQVSLTCLVKGFYPSDIAVEWESNGQPENNYKTTPPVLDSDGSFFLYSKLTVDKSRWQQGN
                                                    # VFSCSVMHEALHNHYTQKSLSLSPGK'
                                                    'tax_id': 'NUMERIC',
                                                    # EXAMPLES:
                                                    # '9606' , '9606' , '9606' , '9606' , '9606' , '9606' , '9606' , '96
                                                    # 06' , '9606' , '9606'
                                                }
                                            },
                                            'description': 'TEXT',
                                            # EXAMPLES:
                                            # 'TEPROTIDE' , 'Hu3F4 (mab)' , 'ONCOLYSIN B (Immunotoxin mab)' , 'Minretumo
                                            # mab (mouse mab)' , 'Vapaliximab (chimeric mab)' , 'huPAM4 (mab)' , 'cA2 (m
                                            # ab)' , 'ICM3 (humanized mab)' , 'ImmuRAIT-LL2 (mouse mab)' , '14G2a (mouse
                                            #  mab)'
                                            'helm_notation': 'TEXT',
                                            # EXAMPLES:
                                            # 'PEPTIDE1{[Glp].W.P.R.P.Q.I.P.P}$$$$' , 'PEPTIDE1{S.S.E.L.T.Q.D.P.A.V.S.V.
                                            # A.L.G.Q.T.V.R.I.T.C.Q.G.D.S.L.R.S.Y.Y.A.T.W.Y.Q.Q.K.P.G.Q.A.P.I.L.V.I.Y.G.
                                            # E.N.K.R.P.S.G.I.P.D.R.F.S.G.S.S.S.G.N.T.A.S.L.T.I.T.G.A.Q.A.E.D.E.A.D.Y.Y.
                                            # C.K.S.R.D.G.S.G.Q.H.L.V.F.G.G.G.T.K.L.T.V.L.G.Q.P.K.A.A.P.S.V.T.L.F.P.P.S.
                                            # S.E.E.L.Q.A.N.K.A.T.L.V.C.L.I.S.D.F.Y.P.G.A.V.T.V.A.W.K.A.D.S.S.P.V.K.A.G.
                                            # V.E.T.T.T.P.S.K.Q.S.N.N.K.Y.A.A.S.S.Y.L.S.L.T.P.E.Q.W.K.S.H.R.S.Y.S.C.Q.V.
                                            # T.H.E.G.S.T.V.E.K.T.V.A.P.A.E.C.S}|PEPTIDE2{E.V.Q.L.V.Q.S.G.A.E.V.K.K.P.G.
                                            # S.S.V.K.V.S.C.K.A.S.G.G.T.F.S.S.Y.A.I.S.W.V.R.Q.A.P.G.Q.G.L.E.W.M.G.G.I.I.
                                            # P.I.F.G.T.A.N.Y.A.Q.K.F.Q.G.R.V.T.I.T.A.D.K.S.T.S.T.A.Y.M.E.L.S.S.L.R.S.E.
                                            # D.T.A.V.Y.Y.C.A.R.A.P.L.R.F.L.E.W.S.T.Q.D.H.Y.Y.Y.Y.Y.M.D.V.W.G.K.G.T.T.V.
                                            # T.V.S.S.A.S.T.K.G.P.S.V.F.P.L.A.P.S.S.K.S.T.S.G.G.T.A.A.L.G.C.L.V.K.D.Y.F.
                                            # P.E.P.V.T.V.S.W.N.S.G.A.L.T.S.G.V.H.T.F.P.A.V.L.Q.S.S.G.L.Y.S.L.S.S.V.V.T.
                                            # V.P.S.S.S.L.G.T.Q.T.Y.I.C.N.V.N.H.K.P.S.N.T.K.V.D.K.K.V.E.P.K.S.C.D.K.T.H.
                                            # T.C.P.P.C.P.A.P.E.L.L.G.G.P.S.V.F.L.F.P.P.K.P.K.D.T.L.M.I.S.R.T.P.E.V.T.C.
                                            # V.V.V.D.V.S.H.E.D.P.E.V.K.F.N.W.Y.V.D.G.V.E.V.H.N.A.K.T.K.P.R.E.E.Q.Y.N.S.
                                            # T.Y.R.V.V.S.V.L.T.V.L.H.Q.D.W.L.N.G.K.E.Y.K.C.K.V.S.N.K.A.L.P.A.P.I.E.K.T.
                                            # I.S.K.A.K.G.Q.P.R.E.P.Q.V.Y.T.L.P.P.S.R.E.E.M.T.K.N.Q.V.S.L.T.C.L.V.K.G.F.
                                            # Y.P.S.D.I.A.V.E.W.E.S.N.G.Q.P.E.N.N.Y.K.T.T.P.P.V.L.D.S.D.G.S.F.F.L.Y.S.K.
                                            # L.T.V.D.K.S.R.W.Q.Q.G.N.V.F.S.C.S.V.M.H.E.A.L.H.N.H.Y.T.Q.K.S.L.S.L.S.P.G.
                                            # K}|PEPTIDE3{E.V.Q.L.V.Q.S.G.A.E.V.K.K.P.G.S.S.V.K.V.S.C.K.A.S.G.G.T.F.S.S.
                                            # Y.A.I.S.W.V.R.Q.A.P.G.Q.G.L.E.W.M.G.G.I.I.P.I.F.G.T.A.N.Y.A.Q.K.F.Q.G.R.V.
                                            # T.I.T.A.D.K.S.T.S.T.A.Y.M.E.L.S.S.L.R.S.E.D.T.A.V.Y.Y.C.A.R.A.P.L.R.F.L.E.
                                            # W.S.T.Q.D.H.Y.Y.Y.Y.Y.M.D.V.W.G.K.G.T.T.V.T.V.S.S.A.S.T.K.G.P.S.V.F.P.L.A.
                                            # P.S.S.K.S.T.S.G.G.T.A.A.L.G.C.L.V.K.D.Y.F.P.E.P.V.T.V.S.W.N.S.G.A.L.T.S.G.
                                            # V.H.T.F.P.A.V.L.Q.S.S.G.L.Y.S.L.S.S.V.V.T.V.P.S.S.S.L.G.T.Q.T.Y.I.C.N.V.N.
                                            # H.K.P.S.N.T.K.V.D.K.K.V.E.P.K.S.C.D.K.T.H.T.C.P.P.C.P.A.P.E.L.L.G.G.P.S.V.
                                            # F.L.F.P.P.K.P.K.D.T.L.M.I.S.R.T.P.E.V.T.C.V.V.V.D.V.S.H.E.D.P.E.V.K.F.N.W.
                                            # Y.V.D.G.V.E.V.H.N.A.K.T.K.P.R.E.E.Q.Y.N.S.T.Y.R.V.V.S.V.L.T.V.L.H.Q.D.W.L.
                                            # N.G.K.E.Y.K.C.K.V.S.N.K.A.L.P.A.P.I.E.K.T.I.S.K.A.K.G.Q.P.R.E.P.Q.V.Y.T.L.
                                            # P.P.S.R.E.E.M.T.K.N.Q.V.S.L.T.C.L.V.K.G.F.Y.P.S.D.I.A.V.E.W.E.S.N.G.Q.P.E.
                                            # N.N.Y.K.T.T.P.P.V.L.D.S.D.G.S.F.F.L.Y.S.K.L.T.V.D.K.S.R.W.Q.Q.G.N.V.F.S.C.
                                            # S.V.M.H.E.A.L.H.N.H.Y.T.Q.K.S.L.S.L.S.P.G.K}|PEPTIDE4{S.S.E.L.T.Q.D.P.A.V.
                                            # S.V.A.L.G.Q.T.V.R.I.T.C.Q.G.D.S.L.R.S.Y.Y.A.T.W.Y.Q.Q.K.P.G.Q.A.P.I.L.V.I.
                                            # Y.G.E.N.K.R.P.S.G.I.P.D.R.F.S.G.S.S.S.G.N.T.A.S.L.T.I.T.G.A.Q.A.E.D.E.A.D.
                                            # Y.Y.C.K.S.R.D.G.S.G.Q.H.L.V.F.G.G.G.T.K.L.T.V.L.G.Q.P.K.A.A.P.S.V.T.L.F.P.
                                            # P.S.S.E.E.L.Q.A.N.K.A.T.L.V.C.L.I.S.D.F.Y.P.G.A.V.T.V.A.W.K.A.D.S.S.P.V.K.
                                            # A.G.V.E.T.T.T.P.S.K.Q.S.N.N.K.Y.A.A.S.S.Y.L.S.L.T.P.E.Q.W.K.S.H.R.S.Y.S.C.
                                            # Q.V.T.H.E.G.S.T.V.E.K.T.V.A.P.A.E.C.S}$PEPTIDE2,PEPTIDE1,233:R3-213:R3|PEP
                                            # TIDE3,PEPTIDE3,157:R3-213:R3|PEPTIDE2,PEPTIDE2,380:R3-438:R3|PEPTIDE2,PEPT
                                            # IDE3,239:R3-239:R3|PEPTIDE3,PEPTIDE3,22:R3-96:R3|PEPTIDE4,PEPTIDE4,136:R3-
                                            # 195:R3|PEPTIDE2,PEPTIDE3,242:R3-242:R3|PEPTIDE3,PEPTIDE3,380:R3-438:R3|PEP
                                            # TIDE2,PEPTIDE2,22:R3-96:R3|PEPTIDE1,PEPTIDE1,136:R3-195:R3|PEPTIDE3,PEPTID
                                            # E4,233:R3-213:R3|PEPTIDE2,PEPTIDE2,157:R3-213:R3|PEPTIDE3,PEPTIDE3,274:R3-
                                            # 334:R3|PEPTIDE1,PEPTIDE1,22:R3-87:R3|PEPTIDE2,PEPTIDE2,274:R3-334:R3|PEPTI
                                            # DE4,PEPTIDE4,22:R3-87:R3$$$' , 'PEPTIDE1{E.I.V.L.T.Q.S.P.G.T.L.S.L.S.P.G.E
                                            # .R.A.T.L.S.C.R.A.S.Q.G.I.S.R.S.Y.L.A.W.Y.Q.Q.K.P.G.Q.A.P.S.L.L.I.Y.G.A.S.S
                                            # .R.A.T.G.I.P.D.R.F.S.G.S.G.S.G.T.D.F.T.L.T.I.S.R.L.E.P.E.D.F.A.V.Y.Y.C.Q.Q
                                            # .F.G.S.S.P.W.T.F.G.Q.G.T.K.V.E.I.K.R.T.V.A.A.P.S.V.F.I.F.P.P.S.D.E.Q.L.K.S
                                            # .G.T.A.S.V.V.C.L.L.N.N.F.Y.P.R.E.A.K.V.Q.W.K.V.D.N.A.L.Q.S.G.N.S.Q.E.S.V.T
                                            # .E.Q.D.S.K.D.S.T.Y.S.L.S.S.T.L.T.L.S.K.A.D.Y.E.K.H.K.V.Y.A.C.E.V.T.H.Q.G.L
                                            # .S.S.P.V.T.K.S.F.N.R.G.E.C}|PEPTIDE2{Q.V.Q.L.Q.E.S.G.P.G.L.V.K.P.S.Q.T.L.S
                                            # .L.T.C.T.V.S.G.G.S.I.S.S.G.D.Y.F.W.S.W.I.R.Q.L.P.G.K.G.L.E.W.I.G.H.I.H.N.S
                                            # .G.T.T.Y.Y.N.P.S.L.K.S.R.V.T.I.S.V.D.T.S.K.K.Q.F.S.L.R.L.S.S.V.T.A.A.D.T.A
                                            # .V.Y.Y.C.A.R.D.R.G.G.D.Y.Y.Y.G.M.D.V.W.G.Q.G.T.T.V.T.V.S.S.A.S.T.K.G.P.S.V
                                            # .F.P.L.A.P.S.S.K.S.T.S.G.G.T.A.A.L.G.C.L.V.K.D.Y.F.P.E.P.V.T.V.S.W.N.S.G.A
                                            # .L.T.S.G.V.H.T.F.P.A.V.L.Q.S.S.G.L.Y.S.L.S.S.V.V.T.V.P.S.S.S.L.G.T.Q.T.Y.I
                                            # .C.N.V.N.H.K.P.S.N.T.K.V.D.K.R.V.E.P.K.S.C.D.K.T.H.T.C.P.P.C.P.A.P.E.L.L.G
                                            # .G.P.S.V.F.L.F.P.P.K.P.K.D.T.L.M.I.S.R.T.P.E.V.T.C.V.V.V.D.V.S.H.E.D.P.E.V
                                            # .K.F.N.W.Y.V.D.G.V.E.V.H.N.A.K.T.K.P.R.E.E.Q.Y.N.S.T.Y.R.V.V.S.V.L.T.V.L.H
                                            # .Q.D.W.L.N.G.K.E.Y.K.C.K.V.S.N.K.A.L.P.A.P.I.E.K.T.I.S.K.A.K.G.Q.P.R.E.P.Q
                                            # .V.Y.T.L.P.P.S.R.E.E.M.T.K.N.Q.V.S.L.T.C.L.V.K.G.F.Y.P.S.D.I.A.V.E.W.E.S.N
                                            # .G.Q.P.E.N.N.Y.K.T.T.P.P.V.L.D.S.D.G.S.F.F.L.Y.S.K.L.T.V.D.K.S.R.W.Q.Q.G.N
                                            # .V.F.S.C.S.V.M.H.E.A.L.H.N.H.Y.T.Q.K.S.L.S.L.S.P.G.K}|PEPTIDE3{Q.V.Q.L.Q.E
                                            # .S.G.P.G.L.V.K.P.S.Q.T.L.S.L.T.C.T.V.S.G.G.S.I.S.S.G.D.Y.F.W.S.W.I.R.Q.L.P
                                            # .G.K.G.L.E.W.I.G.H.I.H.N.S.G.T.T.Y.Y.N.P.S.L.K.S.R.V.T.I.S.V.D.T.S.K.K.Q.F
                                            # .S.L.R.L.S.S.V.T.A.A.D.T.A.V.Y.Y.C.A.R.D.R.G.G.D.Y.Y.Y.G.M.D.V.W.G.Q.G.T.T
                                            # .V.T.V.S.S.A.S.T.K.G.P.S.V.F.P.L.A.P.S.S.K.S.T.S.G.G.T.A.A.L.G.C.L.V.K.D.Y
                                            # .F.P.E.P.V.T.V.S.W.N.S.G.A.L.T.S.G.V.H.T.F.P.A.V.L.Q.S.S.G.L.Y.S.L.S.S.V.V
                                            # .T.V.P.S.S.S.L.G.T.Q.T.Y.I.C.N.V.N.H.K.P.S.N.T.K.V.D.K.R.V.E.P.K.S.C.D.K.T
                                            # .H.T.C.P.P.C.P.A.P.E.L.L.G.G.P.S.V.F.L.F.P.P.K.P.K.D.T.L.M.I.S.R.T.P.E.V.T
                                            # .C.V.V.V.D.V.S.H.E.D.P.E.V.K.F.N.W.Y.V.D.G.V.E.V.H.N.A.K.T.K.P.R.E.E.Q.Y.N
                                            # .S.T.Y.R.V.V.S.V.L.T.V.L.H.Q.D.W.L.N.G.K.E.Y.K.C.K.V.S.N.K.A.L.P.A.P.I.E.K
                                            # .T.I.S.K.A.K.G.Q.P.R.E.P.Q.V.Y.T.L.P.P.S.R.E.E.M.T.K.N.Q.V.S.L.T.C.L.V.K.G
                                            # .F.Y.P.S.D.I.A.V.E.W.E.S.N.G.Q.P.E.N.N.Y.K.T.T.P.P.V.L.D.S.D.G.S.F.F.L.Y.S
                                            # .K.L.T.V.D.K.S.R.W.Q.Q.G.N.V.F.S.C.S.V.M.H.E.A.L.H.N.H.Y.T.Q.K.S.L.S.L.S.P
                                            # .G.K}|PEPTIDE4{E.I.V.L.T.Q.S.P.G.T.L.S.L.S.P.G.E.R.A.T.L.S.C.R.A.S.Q.G.I.S
                                            # .R.S.Y.L.A.W.Y.Q.Q.K.P.G.Q.A.P.S.L.L.I.Y.G.A.S.S.R.A.T.G.I.P.D.R.F.S.G.S.G
                                            # .S.G.T.D.F.T.L.T.I.S.R.L.E.P.E.D.F.A.V.Y.Y.C.Q.Q.F.G.S.S.P.W.T.F.G.Q.G.T.K
                                            # .V.E.I.K.R.T.V.A.A.P.S.V.F.I.F.P.P.S.D.E.Q.L.K.S.G.T.A.S.V.V.C.L.L.N.N.F.Y
                                            # .P.R.E.A.K.V.Q.W.K.V.D.N.A.L.Q.S.G.N.S.Q.E.S.V.T.E.Q.D.S.K.D.S.T.Y.S.L.S.S
                                            # .T.L.T.L.S.K.A.D.Y.E.K.H.K.V.Y.A.C.E.V.T.H.Q.G.L.S.S.P.V.T.K.S.F.N.R.G.E.C
                                            # }$PEPTIDE3,PEPTIDE3,266:R3-326:R3|PEPTIDE1,PEPTIDE1,23:R3-89:R3|PEPTIDE1,P
                                            # EPTIDE1,135:R3-195:R3|PEPTIDE2,PEPTIDE3,231:R3-231:R3|PEPTIDE4,PEPTIDE4,23
                                            # :R3-89:R3|PEPTIDE2,PEPTIDE3,234:R3-234:R3|PEPTIDE2,PEPTIDE2,372:R3-430:R3|
                                            # PEPTIDE2,PEPTIDE1,225:R3-215:R3|PEPTIDE4,PEPTIDE4,135:R3-195:R3|PEPTIDE3,P
                                            # EPTIDE4,225:R3-215:R3|PEPTIDE3,PEPTIDE3,22:R3-97:R3|PEPTIDE2,PEPTIDE2,266:
                                            # R3-326:R3|PEPTIDE2,PEPTIDE2,149:R3-205:R3|PEPTIDE3,PEPTIDE3,149:R3-205:R3|
                                            # PEPTIDE3,PEPTIDE3,372:R3-430:R3|PEPTIDE2,PEPTIDE2,22:R3-97:R3$$$' , 'PEPTI
                                            # DE1{D.I.V.M.T.Q.S.P.L.S.L.P.V.T.P.G.Q.P.A.S.I.S.C.R.S.S.Q.S.I.V.H.S.N.G.N.
                                            # T.W.L.Q.W.W.L.Q.K.P.G.Q.S.P.Q.L.L.I.W.K.V.S.N.R.L.W.G.V.P.D.R.F.S.G.S.G.S.
                                            # G.T.D.F.T.L.K.I.S.R.V.Q.A.Q.D.V.G.V.W.W.C.F.Q.G.S.H.V.P.W.T.F.G.Q.G.T.K.V.
                                            # Q.I.K.R.T.V.A.A.P.S.V.F.I.F.P.P.S.D.E.Q.L.K.S.G.T.A.S.V.V.C.L.L.N.N.F.Y.P.
                                            # R.E.A.K.V.Q.W.K.V.D.N.A.L.Q.S.G.N.S.Q.E.S.V.T.E.Q.D.S.K.D.S.T.Y.S.L.S.S.T.
                                            # L.T.L.S.K.A.D.Y.E.K.H.K.V.Y.A.C.E.V.T.H.Q.G.L.S.S.P.V.T.K.S.F.N.R.G.E.C}|P
                                            # EPTIDE2{Q.V.Q.L.Q.Q.S.G.P.G.L.V.K.P.S.Q.T.L.S.L.T.C.T.V.S.G.W.S.I.S.G.G.W.
                                            # L.W.N.W.I.R.Q.P.P.G.K.G.L.Q.W.I.G.W.I.S.W.D.G.T.N.N.W.K.P.S.L.K.D.R.V.T.I.
                                            # S.V.D.T.S.K.N.Q.F.S.L.K.L.S.S.V.T.A.A.D.T.A.V.W.W.C.A.R.W.G.R.V.F.F.D.W.W.
                                            # G.Q.G.T.L.V.T.V.S.S.A.S.T.K.G.P.S.V.F.P.L.A.P.S.S.K.S.T.S.G.G.T.A.A.L.G.C.
                                            # L.V.K.D.Y.F.P.E.P.V.T.V.S.W.N.S.G.A.L.T.S.G.V.H.T.F.P.A.V.L.Q.S.S.G.L.Y.S.
                                            # L.S.S.V.V.T.V.P.S.S.S.L.G.T.Q.T.Y.I.C.N.V.N.H.K.P.S.N.T.K.V.D.K.R.V.E.P.K.
                                            # S.C.D.K.T.H.T.C.P.P.C.P.A.P.E.L.L.G.G.P.S.V.F.L.F.P.P.K.P.K.D.T.L.M.I.S.R.
                                            # T.P.E.V.T.C.V.V.V.D.V.S.H.E.D.P.E.V.K.F.N.W.Y.V.D.G.V.E.V.H.N.A.K.T.K.P.R.
                                            # E.E.Q.Y.N.S.T.Y.R.V.V.S.V.L.T.V.L.H.Q.D.W.L.N.G.K.E.Y.K.C.K.V.S.N.K.A.L.P.
                                            # A.P.I.E.K.T.I.S.K.A.K.G.Q.P.R.E.P.Q.V.Y.T.L.P.P.S.R.E.E.M.T.K.N.Q.V.S.L.T.
                                            # C.L.V.K.G.F.Y.P.S.D.I.A.V.E.W.E.S.N.G.Q.P.E.N.N.Y.K.T.T.P.P.V.L.D.S.D.G.S.
                                            # F.F.L.Y.S.K.L.T.V.D.K.S.R.W.Q.Q.G.N.V.F.S.C.S.V.M.H.E.A.L.H.N.H.Y.T.Q.K.S.
                                            # L.S.L.S.P.G.K}|PEPTIDE3{Q.V.Q.L.Q.Q.S.G.P.G.L.V.K.P.S.Q.T.L.S.L.T.C.T.V.S.
                                            # G.W.S.I.S.G.G.W.L.W.N.W.I.R.Q.P.P.G.K.G.L.Q.W.I.G.W.I.S.W.D.G.T.N.N.W.K.P.
                                            # S.L.K.D.R.V.T.I.S.V.D.T.S.K.N.Q.F.S.L.K.L.S.S.V.T.A.A.D.T.A.V.W.W.C.A.R.W.
                                            # G.R.V.F.F.D.W.W.G.Q.G.T.L.V.T.V.S.S.A.S.T.K.G.P.S.V.F.P.L.A.P.S.S.K.S.T.S.
                                            # G.G.T.A.A.L.G.C.L.V.K.D.Y.F.P.E.P.V.T.V.S.W.N.S.G.A.L.T.S.G.V.H.T.F.P.A.V.
                                            # L.Q.S.S.G.L.Y.S.L.S.S.V.V.T.V.P.S.S.S.L.G.T.Q.T.Y.I.C.N.V.N.H.K.P.S.N.T.K.
                                            # V.D.K.R.V.E.P.K.S.C.D.K.T.H.T.C.P.P.C.P.A.P.E.L.L.G.G.P.S.V.F.L.F.P.P.K.P.
                                            # K.D.T.L.M.I.S.R.T.P.E.V.T.C.V.V.V.D.V.S.H.E.D.P.E.V.K.F.N.W.Y.V.D.G.V.E.V.
                                            # H.N.A.K.T.K.P.R.E.E.Q.Y.N.S.T.Y.R.V.V.S.V.L.T.V.L.H.Q.D.W.L.N.G.K.E.Y.K.C.
                                            # K.V.S.N.K.A.L.P.A.P.I.E.K.T.I.S.K.A.K.G.Q.P.R.E.P.Q.V.Y.T.L.P.P.S.R.E.E.M.
                                            # T.K.N.Q.V.S.L.T.C.L.V.K.G.F.Y.P.S.D.I.A.V.E.W.E.S.N.G.Q.P.E.N.N.Y.K.T.T.P.
                                            # P.V.L.D.S.D.G.S.F.F.L.Y.S.K.L.T.V.D.K.S.R.W.Q.Q.G.N.V.F.S.C.S.V.M.H.E.A.L.
                                            # H.N.H.Y.T.Q.K.S.L.S.L.S.P.G.K}|PEPTIDE4{D.I.V.M.T.Q.S.P.L.S.L.P.V.T.P.G.Q.
                                            # P.A.S.I.S.C.R.S.S.Q.S.I.V.H.S.N.G.N.T.W.L.Q.W.W.L.Q.K.P.G.Q.S.P.Q.L.L.I.W.
                                            # K.V.S.N.R.L.W.G.V.P.D.R.F.S.G.S.G.S.G.T.D.F.T.L.K.I.S.R.V.Q.A.Q.D.V.G.V.W.
                                            # W.C.F.Q.G.S.H.V.P.W.T.F.G.Q.G.T.K.V.Q.I.K.R.T.V.A.A.P.S.V.F.I.F.P.P.S.D.E.
                                            # Q.L.K.S.G.T.A.S.V.V.C.L.L.N.N.F.Y.P.R.E.A.K.V.Q.W.K.V.D.N.A.L.Q.S.G.N.S.Q.
                                            # E.S.V.T.E.Q.D.S.K.D.S.T.Y.S.L.S.S.T.L.T.L.S.K.A.D.Y.E.K.H.K.V.Y.A.C.E.V.T.
                                            # H.Q.G.L.S.S.P.V.T.K.S.F.N.R.G.E.C}$PEPTIDE4,PEPTIDE4,139:R3-199:R3|PEPTIDE
                                            # 2,PEPTIDE1,220:R3-219:R3|PEPTIDE3,PEPTIDE3,367:R3-425:R3|PEPTIDE2,PEPTIDE3
                                            # ,226:R3-226:R3|PEPTIDE1,PEPTIDE1,23:R3-93:R3|PEPTIDE3,PEPTIDE4,220:R3-219:
                                            # R3|PEPTIDE1,PEPTIDE1,139:R3-199:R3|PEPTIDE4,PEPTIDE4,23:R3-93:R3|PEPTIDE2,
                                            # PEPTIDE2,367:R3-425:R3|PEPTIDE2,PEPTIDE2,144:R3-200:R3|PEPTIDE2,PEPTIDE2,2
                                            # 2:R3-96:R3|PEPTIDE2,PEPTIDE2,261:R3-321:R3|PEPTIDE3,PEPTIDE3,22:R3-96:R3|P
                                            # EPTIDE2,PEPTIDE3,229:R3-229:R3|PEPTIDE3,PEPTIDE3,261:R3-321:R3|PEPTIDE3,PE
                                            # PTIDE3,144:R3-200:R3$$$' , 'PEPTIDE1{D.I.V.L.T.Q.S.P.A.T.L.S.L.S.P.G.E.R.A
                                            # .T.L.S.C.R.A.S.Q.S.V.S.S.S.Y.L.A.W.Y.Q.Q.K.P.G.Q.A.P.R.L.L.I.Y.G.A.S.S.R.A
                                            # .T.G.V.P.A.R.F.S.G.S.G.S.G.T.D.F.T.L.T.I.S.S.L.E.P.E.D.F.A.T.Y.Y.C.L.Q.I.Y
                                            # .N.M.P.I.T.F.G.Q.G.T.K.V.E.I.K.R.T.V.A.A.P.S.V.F.I.F.P.P.S.D.E.Q.L.K.S.G.T
                                            # .A.S.V.V.C.L.L.N.N.F.Y.P.R.E.A.K.V.Q.W.K.V.D.N.A.L.Q.S.G.N.S.Q.E.S.V.T.E.Q
                                            # .D.S.K.D.S.T.Y.S.L.S.S.T.L.T.L.S.K.A.D.Y.E.K.H.K.V.Y.A.C.E.V.T.H.Q.G.L.S.S
                                            # .P.V.T.K.S.F.N.R.G.E.C}|PEPTIDE2{Q.V.E.L.V.E.S.G.G.G.L.V.Q.P.G.G.S.L.R.L.S
                                            # .C.A.A.S.G.F.T.F.S.S.Y.A.M.S.W.V.R.Q.A.P.G.K.G.L.E.W.V.S.A.I.N.A.S.G.T.R.T
                                            # .Y.Y.A.D.S.V.K.G.R.F.T.I.S.R.D.N.S.K.N.T.L.Y.L.Q.M.N.S.L.R.A.E.D.T.A.V.Y.Y
                                            # .C.A.R.G.K.G.N.T.H.K.P.Y.G.Y.V.R.Y.F.D.V.W.G.Q.G.T.L.V.T.V.S.S.A.S.T.K.G.P
                                            # .S.V.F.P.L.A.P.S.S.K.S.T.S.G.G.T.A.A.L.G.C.L.V.K.D.Y.F.P.E.P.V.T.V.S.W.N.S
                                            # .G.A.L.T.S.G.V.H.T.F.P.A.V.L.Q.S.S.G.L.Y.S.L.S.S.V.V.T.V.P.S.S.S.L.G.T.Q.T
                                            # .Y.I.C.N.V.N.H.K.P.S.N.T.K.V.D.K.K.V.E.P.K.S.C.D.K.T.H.T.C.P.P.C.P.A.P.E.L
                                            # .L.G.G.P.S.V.F.L.F.P.P.K.P.K.D.T.L.M.I.S.R.T.P.E.V.T.C.V.V.V.D.V.S.H.E.D.P
                                            # .E.V.K.F.N.W.Y.V.D.G.V.E.V.H.N.A.K.T.K.P.R.E.E.Q.Y.N.S.T.Y.R.V.V.S.V.L.T.V
                                            # .L.H.Q.D.W.L.N.G.K.E.Y.K.C.K.V.S.N.K.A.L.P.A.P.I.E.K.T.I.S.K.A.K.G.Q.P.R.E
                                            # .P.Q.V.Y.T.L.P.P.S.R.D.E.L.T.K.N.Q.V.S.L.T.C.L.V.K.G.F.Y.P.S.D.I.A.V.E.W.E
                                            # .S.N.G.Q.P.E.N.N.Y.K.T.T.P.P.V.L.D.S.D.G.S.F.F.L.Y.S.K.L.T.V.D.K.S.R.W.Q.Q
                                            # .G.N.V.F.S.C.S.V.M.H.E.A.L.H.N.H.Y.T.Q.K.S.L.S.L.S.P.G.K}|PEPTIDE3{Q.V.E.L
                                            # .V.E.S.G.G.G.L.V.Q.P.G.G.S.L.R.L.S.C.A.A.S.G.F.T.F.S.S.Y.A.M.S.W.V.R.Q.A.P
                                            # .G.K.G.L.E.W.V.S.A.I.N.A.S.G.T.R.T.Y.Y.A.D.S.V.K.G.R.F.T.I.S.R.D.N.S.K.N.T
                                            # .L.Y.L.Q.M.N.S.L.R.A.E.D.T.A.V.Y.Y.C.A.R.G.K.G.N.T.H.K.P.Y.G.Y.V.R.Y.F.D.V
                                            # .W.G.Q.G.T.L.V.T.V.S.S.A.S.T.K.G.P.S.V.F.P.L.A.P.S.S.K.S.T.S.G.G.T.A.A.L.G
                                            # .C.L.V.K.D.Y.F.P.E.P.V.T.V.S.W.N.S.G.A.L.T.S.G.V.H.T.F.P.A.V.L.Q.S.S.G.L.Y
                                            # .S.L.S.S.V.V.T.V.P.S.S.S.L.G.T.Q.T.Y.I.C.N.V.N.H.K.P.S.N.T.K.V.D.K.K.V.E.P
                                            # .K.S.C.D.K.T.H.T.C.P.P.C.P.A.P.E.L.L.G.G.P.S.V.F.L.F.P.P.K.P.K.D.T.L.M.I.S
                                            # .R.T.P.E.V.T.C.V.V.V.D.V.S.H.E.D.P.E.V.K.F.N.W.Y.V.D.G.V.E.V.H.N.A.K.T.K.P
                                            # .R.E.E.Q.Y.N.S.T.Y.R.V.V.S.V.L.T.V.L.H.Q.D.W.L.N.G.K.E.Y.K.C.K.V.S.N.K.A.L
                                            # .P.A.P.I.E.K.T.I.S.K.A.K.G.Q.P.R.E.P.Q.V.Y.T.L.P.P.S.R.D.E.L.T.K.N.Q.V.S.L
                                            # .T.C.L.V.K.G.F.Y.P.S.D.I.A.V.E.W.E.S.N.G.Q.P.E.N.N.Y.K.T.T.P.P.V.L.D.S.D.G
                                            # .S.F.F.L.Y.S.K.L.T.V.D.K.S.R.W.Q.Q.G.N.V.F.S.C.S.V.M.H.E.A.L.H.N.H.Y.T.Q.K
                                            # .S.L.S.L.S.P.G.K}|PEPTIDE4{D.I.V.L.T.Q.S.P.A.T.L.S.L.S.P.G.E.R.A.T.L.S.C.R
                                            # .A.S.Q.S.V.S.S.S.Y.L.A.W.Y.Q.Q.K.P.G.Q.A.P.R.L.L.I.Y.G.A.S.S.R.A.T.G.V.P.A
                                            # .R.F.S.G.S.G.S.G.T.D.F.T.L.T.I.S.S.L.E.P.E.D.F.A.T.Y.Y.C.L.Q.I.Y.N.M.P.I.T
                                            # .F.G.Q.G.T.K.V.E.I.K.R.T.V.A.A.P.S.V.F.I.F.P.P.S.D.E.Q.L.K.S.G.T.A.S.V.V.C
                                            # .L.L.N.N.F.Y.P.R.E.A.K.V.Q.W.K.V.D.N.A.L.Q.S.G.N.S.Q.E.S.V.T.E.Q.D.S.K.D.S
                                            # .T.Y.S.L.S.S.T.L.T.L.S.K.A.D.Y.E.K.H.K.V.Y.A.C.E.V.T.H.Q.G.L.S.S.P.V.T.K.S
                                            # .F.N.R.G.E.C}$PEPTIDE3,PEPTIDE4,229:R3-215:R3|PEPTIDE2,PEPTIDE2,270:R3-330
                                            # :R3|PEPTIDE4,PEPTIDE4,135:R3-195:R3|PEPTIDE3,PEPTIDE3,22:R3-96:R3|PEPTIDE3
                                            # ,PEPTIDE3,376:R3-434:R3|PEPTIDE1,PEPTIDE1,135:R3-195:R3|PEPTIDE3,PEPTIDE3,
                                            # 153:R3-209:R3|PEPTIDE2,PEPTIDE2,22:R3-96:R3|PEPTIDE2,PEPTIDE3,238:R3-238:R
                                            # 3|PEPTIDE2,PEPTIDE3,235:R3-235:R3|PEPTIDE1,PEPTIDE1,23:R3-89:R3|PEPTIDE4,P
                                            # EPTIDE4,23:R3-89:R3|PEPTIDE2,PEPTIDE2,376:R3-434:R3|PEPTIDE3,PEPTIDE3,270:
                                            # R3-330:R3|PEPTIDE2,PEPTIDE1,229:R3-215:R3|PEPTIDE2,PEPTIDE2,153:R3-209:R3$
                                            # $$' , 'PEPTIDE1{D.I.V.M.T.Q.S.Q.R.F.M.S.T.T.V.G.D.R.V.S.I.T.C.K.A.S.Q.N.V.
                                            # V.S.A.V.A.W.Y.Q.Q.K.P.G.Q.S.P.K.L.L.I.Y.S.A.S.N.R.Y.T.G.V.P.D.R.F.T.G.S.G.
                                            # S.G.T.D.F.T.L.T.I.S.N.M.Q.S.E.D.L.A.D.F.F.C.Q.Q.Y.S.N.Y.P.W.T.F.G.G.G.T.K.
                                            # L.E.I.K.R.T.V.A.A.P.S.V.F.I.F.P.P.S.D.E.Q.L.K.S.G.T.A.S.V.V.C.L.L.N.N.F.Y.
                                            # P.R.E.A.K.V.Q.W.K.V.D.N.A.L.Q.S.G.N.S.Q.E.S.V.T.E.Q.D.S.K.D.S.T.Y.S.L.S.S.
                                            # T.L.T.L.S.K.A.D.Y.E.K.H.K.V.Y.A.C.E.V.T.H.Q.G.L.S.S.P.V.T.K.S.F.N.R.G.E.C}
                                            # |PEPTIDE2{D.V.K.L.V.E.S.G.G.G.L.V.K.L.G.G.S.L.K.L.S.C.A.A.S.G.F.T.F.S.N.Y.
                                            # Y.M.S.W.V.R.Q.T.P.E.K.R.L.E.L.V.A.A.I.N.S.D.G.G.I.T.Y.Y.L.D.T.V.K.G.R.F.T.
                                            # I.S.R.D.N.A.K.N.T.L.Y.L.Q.M.S.S.L.K.S.E.D.T.A.L.F.Y.C.A.R.H.R.S.G.Y.F.S.M.
                                            # D.Y.W.G.Q.G.T.S.V.T.V.S.S.A.S.T.K.G.P.S.V.F.P.L.A.P.S.S.K.S.T.S.G.G.T.A.A.
                                            # L.G.C.L.V.K.D.Y.F.P.E.P.V.T.V.S.W.N.S.G.A.L.T.S.G.V.H.T.F.P.A.V.L.Q.S.S.G.
                                            # L.Y.S.L.S.S.V.V.T.V.P.S.S.S.L.G.T.Q.T.Y.I.C.N.V.N.H.K.P.S.N.T.K.V.D.K.K.V.
                                            # E.P.K.S.C.D.K.T.H.T.C.P.P.C.P.A.P.E.L.L.G.G.P.S.V.F.L.F.P.P.K.P.K.D.T.L.M.
                                            # I.S.R.T.P.E.V.T.C.V.V.V.D.V.S.H.E.D.P.E.V.K.F.N.W.Y.V.D.G.V.E.V.H.N.A.K.T.
                                            # K.P.R.E.E.Q.Y.N.S.T.Y.R.V.V.S.V.L.T.V.L.H.Q.D.W.L.N.G.K.E.Y.K.C.K.V.S.N.K.
                                            # A.L.P.A.P.I.E.K.T.I.S.K.A.K.G.Q.P.R.E.P.Q.V.Y.T.L.P.P.S.R.D.E.L.T.K.N.Q.V.
                                            # S.L.T.C.L.V.K.G.F.Y.P.S.D.I.A.V.E.W.E.S.N.G.Q.P.E.N.N.Y.K.T.T.P.P.V.L.D.S.
                                            # D.G.S.F.F.L.Y.S.K.L.T.V.D.K.S.R.W.Q.Q.G.N.V.F.S.C.S.V.M.H.E.A.L.H.N.H.Y.T.
                                            # Q.K.S.L.S.L.S.P.G.K}|PEPTIDE3{D.V.K.L.V.E.S.G.G.G.L.V.K.L.G.G.S.L.K.L.S.C.
                                            # A.A.S.G.F.T.F.S.N.Y.Y.M.S.W.V.R.Q.T.P.E.K.R.L.E.L.V.A.A.I.N.S.D.G.G.I.T.Y.
                                            # Y.L.D.T.V.K.G.R.F.T.I.S.R.D.N.A.K.N.T.L.Y.L.Q.M.S.S.L.K.S.E.D.T.A.L.F.Y.C.
                                            # A.R.H.R.S.G.Y.F.S.M.D.Y.W.G.Q.G.T.S.V.T.V.S.S.A.S.T.K.G.P.S.V.F.P.L.A.P.S.
                                            # S.K.S.T.S.G.G.T.A.A.L.G.C.L.V.K.D.Y.F.P.E.P.V.T.V.S.W.N.S.G.A.L.T.S.G.V.H.
                                            # T.F.P.A.V.L.Q.S.S.G.L.Y.S.L.S.S.V.V.T.V.P.S.S.S.L.G.T.Q.T.Y.I.C.N.V.N.H.K.
                                            # P.S.N.T.K.V.D.K.K.V.E.P.K.S.C.D.K.T.H.T.C.P.P.C.P.A.P.E.L.L.G.G.P.S.V.F.L.
                                            # F.P.P.K.P.K.D.T.L.M.I.S.R.T.P.E.V.T.C.V.V.V.D.V.S.H.E.D.P.E.V.K.F.N.W.Y.V.
                                            # D.G.V.E.V.H.N.A.K.T.K.P.R.E.E.Q.Y.N.S.T.Y.R.V.V.S.V.L.T.V.L.H.Q.D.W.L.N.G.
                                            # K.E.Y.K.C.K.V.S.N.K.A.L.P.A.P.I.E.K.T.I.S.K.A.K.G.Q.P.R.E.P.Q.V.Y.T.L.P.P.
                                            # S.R.D.E.L.T.K.N.Q.V.S.L.T.C.L.V.K.G.F.Y.P.S.D.I.A.V.E.W.E.S.N.G.Q.P.E.N.N.
                                            # Y.K.T.T.P.P.V.L.D.S.D.G.S.F.F.L.Y.S.K.L.T.V.D.K.S.R.W.Q.Q.G.N.V.F.S.C.S.V.
                                            # M.H.E.A.L.H.N.H.Y.T.Q.K.S.L.S.L.S.P.G.K}|PEPTIDE4{D.I.V.M.T.Q.S.Q.R.F.M.S.
                                            # T.T.V.G.D.R.V.S.I.T.C.K.A.S.Q.N.V.V.S.A.V.A.W.Y.Q.Q.K.P.G.Q.S.P.K.L.L.I.Y.
                                            # S.A.S.N.R.Y.T.G.V.P.D.R.F.T.G.S.G.S.G.T.D.F.T.L.T.I.S.N.M.Q.S.E.D.L.A.D.F.
                                            # F.C.Q.Q.Y.S.N.Y.P.W.T.F.G.G.G.T.K.L.E.I.K.R.T.V.A.A.P.S.V.F.I.F.P.P.S.D.E.
                                            # Q.L.K.S.G.T.A.S.V.V.C.L.L.N.N.F.Y.P.R.E.A.K.V.Q.W.K.V.D.N.A.L.Q.S.G.N.S.Q.
                                            # E.S.V.T.E.Q.D.S.K.D.S.T.Y.S.L.S.S.T.L.T.L.S.K.A.D.Y.E.K.H.K.V.Y.A.C.E.V.T.
                                            # H.Q.G.L.S.S.P.V.T.K.S.F.N.R.G.E.C}$PEPTIDE3,PEPTIDE4,222:R3-214:R3|PEPTIDE
                                            # 4,PEPTIDE4,134:R3-194:R3|PEPTIDE1,PEPTIDE1,134:R3-194:R3|PEPTIDE3,PEPTIDE3
                                            # ,22:R3-96:R3|PEPTIDE2,PEPTIDE2,146:R3-202:R3|PEPTIDE2,PEPTIDE1,222:R3-214:
                                            # R3|PEPTIDE2,PEPTIDE2,369:R3-427:R3|PEPTIDE3,PEPTIDE3,263:R3-323:R3|PEPTIDE
                                            # 2,PEPTIDE2,263:R3-323:R3|PEPTIDE4,PEPTIDE4,23:R3-88:R3|PEPTIDE1,PEPTIDE1,2
                                            # 3:R3-88:R3|PEPTIDE2,PEPTIDE3,231:R3-231:R3|PEPTIDE3,PEPTIDE3,369:R3-427:R3
                                            # |PEPTIDE2,PEPTIDE2,22:R3-96:R3|PEPTIDE3,PEPTIDE3,146:R3-202:R3|PEPTIDE2,PE
                                            # PTIDE3,228:R3-228:R3$$$' , 'PEPTIDE1{D.I.Q.M.T.Q.S.P.S.S.L.S.A.S.V.G.D.R.V
                                            # .T.I.T.C.K.A.S.R.D.I.R.S.Y.L.T.W.Y.Q.Q.K.P.G.K.A.P.K.T.L.I.Y.Y.A.T.S.L.A.D
                                            # .G.V.P.S.R.F.S.G.S.G.S.G.Q.D.Y.S.L.T.I.S.S.L.E.S.D.D.T.A.T.Y.Y.C.L.Q.H.G.E
                                            # .S.P.F.T.L.G.S.G.T.K.L.E.I.K.R.T.V.A.A.P.S.V.F.I.F.P.P.S.D.E.Q.L.K.S.G.T.A
                                            # .S.V.V.C.L.L.N.N.F.Y.P.R.E.A.K.V.Q.W.K.V.D.N.A.L.Q.S.G.N.S.Q.E.S.V.T.E.Q.D
                                            # .S.K.D.S.T.Y.S.L.S.S.T.L.T.L.S.K.A.D.Y.E.K.H.K.V.Y.A.C.E.V.T.H.Q.G.L.S.S.P
                                            # .V.T.K.S.F.N.R.G.E.C}|PEPTIDE2{E.V.Q.L.V.E.S.G.G.G.L.V.K.P.G.G.S.L.K.L.S.C
                                            # .A.A.S.G.F.K.F.S.R.Y.A.M.S.W.V.R.Q.A.P.G.K.R.L.E.W.V.A.T.I.S.S.G.G.S.Y.I.Y
                                            # .Y.P.D.S.V.K.G.R.F.T.I.S.R.D.N.V.K.N.T.L.Y.L.Q.M.S.S.L.R.S.E.D.T.A.M.Y.Y.C
                                            # .A.R.R.D.Y.D.L.D.Y.F.D.S.W.G.Q.G.T.L.V.T.V.S.S.A.S.T.K.G.P.S.V.F.P.L.A.P.S
                                            # .S.K.S.T.S.G.G.T.A.A.L.G.C.L.V.K.D.Y.F.P.E.P.V.T.V.S.W.N.S.G.A.L.T.S.G.V.H
                                            # .T.F.P.A.V.L.Q.S.S.G.L.Y.S.L.S.S.V.V.T.V.P.S.S.S.L.G.T.Q.T.Y.I.C.N.V.N.H.K
                                            # .P.S.N.T.K.V.D.K.K.V.E.P.K.S.C.D.K.T.H.T.C.P.P.C.P.A.P.E.L.L.G.G.P.S.V.F.L
                                            # .F.P.P.K.P.K.D.T.L.M.I.S.R.T.P.E.V.T.C.V.V.V.D.V.S.H.E.D.P.E.V.K.F.N.W.Y.V
                                            # .D.G.V.E.V.H.N.A.K.T.K.P.R.E.E.Q.Y.N.S.T.Y.R.V.V.S.V.L.T.V.L.H.Q.D.W.L.N.G
                                            # .K.E.Y.K.C.K.V.S.N.K.A.L.P.A.P.I.E.K.T.I.S.K.A.K.G.Q.P.R.E.P.Q.V.Y.T.L.P.P
                                            # .S.R.D.E.L.T.K.N.Q.V.S.L.T.C.L.V.K.G.F.Y.P.S.D.I.A.V.E.W.E.S.N.G.Q.P.E.N.N
                                            # .Y.K.T.T.P.P.V.L.D.S.D.G.S.F.F.L.Y.S.K.L.T.V.D.K.S.R.W.Q.Q.G.N.V.F.S.C.S.V
                                            # .M.H.E.A.L.H.N.H.Y.T.Q.K.S.L.S.L.S.P.G.K}|PEPTIDE3{E.V.Q.L.V.E.S.G.G.G.L.V
                                            # .K.P.G.G.S.L.K.L.S.C.A.A.S.G.F.K.F.S.R.Y.A.M.S.W.V.R.Q.A.P.G.K.R.L.E.W.V.A
                                            # .T.I.S.S.G.G.S.Y.I.Y.Y.P.D.S.V.K.G.R.F.T.I.S.R.D.N.V.K.N.T.L.Y.L.Q.M.S.S.L
                                            # .R.S.E.D.T.A.M.Y.Y.C.A.R.R.D.Y.D.L.D.Y.F.D.S.W.G.Q.G.T.L.V.T.V.S.S.A.S.T.K
                                            # .G.P.S.V.F.P.L.A.P.S.S.K.S.T.S.G.G.T.A.A.L.G.C.L.V.K.D.Y.F.P.E.P.V.T.V.S.W
                                            # .N.S.G.A.L.T.S.G.V.H.T.F.P.A.V.L.Q.S.S.G.L.Y.S.L.S.S.V.V.T.V.P.S.S.S.L.G.T
                                            # .Q.T.Y.I.C.N.V.N.H.K.P.S.N.T.K.V.D.K.K.V.E.P.K.S.C.D.K.T.H.T.C.P.P.C.P.A.P
                                            # .E.L.L.G.G.P.S.V.F.L.F.P.P.K.P.K.D.T.L.M.I.S.R.T.P.E.V.T.C.V.V.V.D.V.S.H.E
                                            # .D.P.E.V.K.F.N.W.Y.V.D.G.V.E.V.H.N.A.K.T.K.P.R.E.E.Q.Y.N.S.T.Y.R.V.V.S.V.L
                                            # .T.V.L.H.Q.D.W.L.N.G.K.E.Y.K.C.K.V.S.N.K.A.L.P.A.P.I.E.K.T.I.S.K.A.K.G.Q.P
                                            # .R.E.P.Q.V.Y.T.L.P.P.S.R.D.E.L.T.K.N.Q.V.S.L.T.C.L.V.K.G.F.Y.P.S.D.I.A.V.E
                                            # .W.E.S.N.G.Q.P.E.N.N.Y.K.T.T.P.P.V.L.D.S.D.G.S.F.F.L.Y.S.K.L.T.V.D.K.S.R.W
                                            # .Q.Q.G.N.V.F.S.C.S.V.M.H.E.A.L.H.N.H.Y.T.Q.K.S.L.S.L.S.P.G.K}|PEPTIDE4{D.I
                                            # .Q.M.T.Q.S.P.S.S.L.S.A.S.V.G.D.R.V.T.I.T.C.K.A.S.R.D.I.R.S.Y.L.T.W.Y.Q.Q.K
                                            # .P.G.K.A.P.K.T.L.I.Y.Y.A.T.S.L.A.D.G.V.P.S.R.F.S.G.S.G.S.G.Q.D.Y.S.L.T.I.S
                                            # .S.L.E.S.D.D.T.A.T.Y.Y.C.L.Q.H.G.E.S.P.F.T.L.G.S.G.T.K.L.E.I.K.R.T.V.A.A.P
                                            # .S.V.F.I.F.P.P.S.D.E.Q.L.K.S.G.T.A.S.V.V.C.L.L.N.N.F.Y.P.R.E.A.K.V.Q.W.K.V
                                            # .D.N.A.L.Q.S.G.N.S.Q.E.S.V.T.E.Q.D.S.K.D.S.T.Y.S.L.S.S.T.L.T.L.S.K.A.D.Y.E
                                            # .K.H.K.V.Y.A.C.E.V.T.H.Q.G.L.S.S.P.V.T.K.S.F.N.R.G.E.C}$PEPTIDE1,PEPTIDE1,
                                            # 23:R3-88:R3|PEPTIDE3,PEPTIDE4,222:R3-214:R3|PEPTIDE3,PEPTIDE3,22:R3-96:R3|
                                            # PEPTIDE2,PEPTIDE2,263:R3-323:R3|PEPTIDE4,PEPTIDE4,134:R3-194:R3|PEPTIDE2,P
                                            # EPTIDE1,222:R3-214:R3|PEPTIDE3,PEPTIDE3,263:R3-323:R3|PEPTIDE2,PEPTIDE2,14
                                            # 6:R3-202:R3|PEPTIDE2,PEPTIDE2,369:R3-427:R3|PEPTIDE3,PEPTIDE3,146:R3-202:R
                                            # 3|PEPTIDE3,PEPTIDE3,369:R3-427:R3|PEPTIDE1,PEPTIDE1,134:R3-194:R3|PEPTIDE2
                                            # ,PEPTIDE2,22:R3-96:R3|PEPTIDE2,PEPTIDE3,228:R3-228:R3|PEPTIDE2,PEPTIDE3,23
                                            # 1:R3-231:R3|PEPTIDE4,PEPTIDE4,23:R3-88:R3$$$' , 'PEPTIDE1{S.S.E.L.T.Q.D.P.
                                            # A.V.S.V.A.L.G.Q.T.V.R.I.T.C.Q.G.D.S.L.R.S.Y.Y.A.S.W.Y.Q.Q.K.P.G.Q.A.P.V.L.
                                            # V.I.Y.G.K.N.N.R.P.S.G.I.P.D.R.F.S.G.S.S.S.G.N.T.A.S.L.T.I.T.G.A.Q.A.E.D.E.
                                            # A.D.Y.Y.C.N.S.R.D.S.S.G.N.H.V.V.F.G.G.G.T.K.L.T.V.L.G.Q.P.K.A.A.P.S.V.T.L.
                                            # F.P.P.S.S.E.E.L.Q.A.N.K.A.T.L.V.C.L.I.S.D.F.Y.P.G.A.V.T.V.A.W.K.A.D.S.S.P.
                                            # V.K.A.G.V.E.T.T.T.P.S.K.Q.S.N.N.K.Y.A.A.S.S.Y.L.S.L.T.P.E.Q.W.K.S.H.R.S.Y.
                                            # S.C.Q.V.T.H.E.G.S.T.V.E.K.T.V.A.P.T.E.C.S}|PEPTIDE2{E.V.Q.L.V.Q.S.G.G.G.V.
                                            # E.R.P.G.G.S.L.R.L.S.C.A.A.S.G.F.T.F.D.D.Y.G.M.S.W.V.R.Q.A.P.G.K.G.L.E.W.V.
                                            # S.G.I.N.W.N.G.G.S.T.G.Y.A.D.S.V.K.G.R.V.T.I.S.R.D.N.A.K.N.S.L.Y.L.Q.M.N.S.
                                            # L.R.A.E.D.T.A.V.Y.Y.C.A.K.I.L.G.A.G.R.G.W.Y.F.D.L.W.G.K.G.T.T.V.T.V.S.S.A.
                                            # S.T.K.G.P.S.V.F.P.L.A.P.S.S.K.S.T.S.G.G.T.A.A.L.G.C.L.V.K.D.Y.F.P.E.P.V.T.
                                            # V.S.W.N.S.G.A.L.T.S.G.V.H.T.F.P.A.V.L.Q.S.S.G.L.Y.S.L.S.S.V.V.T.V.P.S.S.S.
                                            # L.G.T.Q.T.Y.I.C.N.V.N.H.K.P.S.N.T.K.V.D.K.R.V.E.P.K.S.C.D.K.T.H.T.C.P.P.C.
                                            # P.A.P.E.L.L.G.G.P.S.V.F.L.F.P.P.K.P.K.D.T.L.M.I.S.R.T.P.E.V.T.C.V.V.V.D.V.
                                            # S.H.E.D.P.E.V.K.F.N.W.Y.V.D.G.V.E.V.H.N.A.K.T.K.P.R.E.E.Q.Y.N.S.T.Y.R.V.V.
                                            # S.V.L.T.V.L.H.Q.D.W.L.N.G.K.E.Y.K.C.K.V.S.N.K.A.L.P.A.P.I.E.K.T.I.S.K.A.K.
                                            # G.Q.P.R.E.P.Q.V.Y.T.L.P.P.S.R.E.E.M.T.K.N.Q.V.S.L.T.C.L.V.K.G.F.Y.P.S.D.I.
                                            # A.V.E.W.E.S.N.G.Q.P.E.N.N.Y.K.T.T.P.P.V.L.D.S.D.G.S.F.F.L.Y.S.K.L.T.V.D.K.
                                            # S.R.W.Q.Q.G.N.V.F.S.C.S.V.M.H.E.A.L.H.N.H.Y.T.Q.K.S.L.S.L.S.P.G.K}|PEPTIDE
                                            # 3{E.V.Q.L.V.Q.S.G.G.G.V.E.R.P.G.G.S.L.R.L.S.C.A.A.S.G.F.T.F.D.D.Y.G.M.S.W.
                                            # V.R.Q.A.P.G.K.G.L.E.W.V.S.G.I.N.W.N.G.G.S.T.G.Y.A.D.S.V.K.G.R.V.T.I.S.R.D.
                                            # N.A.K.N.S.L.Y.L.Q.M.N.S.L.R.A.E.D.T.A.V.Y.Y.C.A.K.I.L.G.A.G.R.G.W.Y.F.D.L.
                                            # W.G.K.G.T.T.V.T.V.S.S.A.S.T.K.G.P.S.V.F.P.L.A.P.S.S.K.S.T.S.G.G.T.A.A.L.G.
                                            # C.L.V.K.D.Y.F.P.E.P.V.T.V.S.W.N.S.G.A.L.T.S.G.V.H.T.F.P.A.V.L.Q.S.S.G.L.Y.
                                            # S.L.S.S.V.V.T.V.P.S.S.S.L.G.T.Q.T.Y.I.C.N.V.N.H.K.P.S.N.T.K.V.D.K.R.V.E.P.
                                            # K.S.C.D.K.T.H.T.C.P.P.C.P.A.P.E.L.L.G.G.P.S.V.F.L.F.P.P.K.P.K.D.T.L.M.I.S.
                                            # R.T.P.E.V.T.C.V.V.V.D.V.S.H.E.D.P.E.V.K.F.N.W.Y.V.D.G.V.E.V.H.N.A.K.T.K.P.
                                            # R.E.E.Q.Y.N.S.T.Y.R.V.V.S.V.L.T.V.L.H.Q.D.W.L.N.G.K.E.Y.K.C.K.V.S.N.K.A.L.
                                            # P.A.P.I.E.K.T.I.S.K.A.K.G.Q.P.R.E.P.Q.V.Y.T.L.P.P.S.R.E.E.M.T.K.N.Q.V.S.L.
                                            # T.C.L.V.K.G.F.Y.P.S.D.I.A.V.E.W.E.S.N.G.Q.P.E.N.N.Y.K.T.T.P.P.V.L.D.S.D.G.
                                            # S.F.F.L.Y.S.K.L.T.V.D.K.S.R.W.Q.Q.G.N.V.F.S.C.S.V.M.H.E.A.L.H.N.H.Y.T.Q.K.
                                            # S.L.S.L.S.P.G.K}|PEPTIDE4{S.S.E.L.T.Q.D.P.A.V.S.V.A.L.G.Q.T.V.R.I.T.C.Q.G.
                                            # D.S.L.R.S.Y.Y.A.S.W.Y.Q.Q.K.P.G.Q.A.P.V.L.V.I.Y.G.K.N.N.R.P.S.G.I.P.D.R.F.
                                            # S.G.S.S.S.G.N.T.A.S.L.T.I.T.G.A.Q.A.E.D.E.A.D.Y.Y.C.N.S.R.D.S.S.G.N.H.V.V.
                                            # F.G.G.G.T.K.L.T.V.L.G.Q.P.K.A.A.P.S.V.T.L.F.P.P.S.S.E.E.L.Q.A.N.K.A.T.L.V.
                                            # C.L.I.S.D.F.Y.P.G.A.V.T.V.A.W.K.A.D.S.S.P.V.K.A.G.V.E.T.T.T.P.S.K.Q.S.N.N.
                                            # K.Y.A.A.S.S.Y.L.S.L.T.P.E.Q.W.K.S.H.R.S.Y.S.C.Q.V.T.H.E.G.S.T.V.E.K.T.V.A.
                                            # P.T.E.C.S}$PEPTIDE4,PEPTIDE4,22:R3-87:R3|PEPTIDE3,PEPTIDE3,148:R3-204:R3|P
                                            # EPTIDE2,PEPTIDE3,230:R3-230:R3|PEPTIDE2,PEPTIDE2,148:R3-204:R3|PEPTIDE4,PE
                                            # PTIDE4,136:R3-195:R3|PEPTIDE3,PEPTIDE4,224:R3-213:R3|PEPTIDE2,PEPTIDE2,22:
                                            # R3-96:R3|PEPTIDE1,PEPTIDE1,22:R3-87:R3|PEPTIDE3,PEPTIDE3,265:R3-325:R3|PEP
                                            # TIDE2,PEPTIDE1,224:R3-213:R3|PEPTIDE3,PEPTIDE3,22:R3-96:R3|PEPTIDE2,PEPTID
                                            # E2,371:R3-429:R3|PEPTIDE1,PEPTIDE1,136:R3-195:R3|PEPTIDE2,PEPTIDE2,265:R3-
                                            # 325:R3|PEPTIDE3,PEPTIDE3,371:R3-429:R3|PEPTIDE2,PEPTIDE3,233:R3-233:R3$$$'
                                            #  , 'PEPTIDE1{D.V.L.M.T.Q.S.P.L.S.L.P.V.T.P.G.E.P.A.S.I.S.C.R.S.S.R.N.I.V.H
                                            # .I.N.G.D.T.Y.L.E.W.Y.L.Q.K.P.G.Q.S.P.Q.L.L.I.Y.K.V.S.N.R.F.S.G.V.P.D.R.F.S
                                            # .G.S.G.S.G.T.D.F.T.L.K.I.S.R.V.E.A.E.D.V.G.V.Y.Y.C.F.Q.G.S.L.L.P.W.T.F.G.Q
                                            # .G.T.K.V.E.I.K.R.T.V.A.A.P.S.V.F.I.F.P.P.S.D.E.Q.L.K.S.G.T.A.S.V.V.C.L.L.N
                                            # .N.F.Y.P.R.E.A.K.V.Q.W.K.V.D.N.A.L.Q.S.G.N.S.Q.E.S.V.T.E.Q.D.S.K.D.S.T.Y.S
                                            # .L.S.S.T.L.T.L.S.K.A.D.Y.E.K.H.K.V.Y.A.C.E.V.T.H.Q.G.L.S.S.P.V.T.K.S.F.N.R
                                            # .G.E.C}|PEPTIDE2{E.V.Q.L.V.E.S.G.G.D.L.V.Q.P.G.R.S.L.R.L.S.C.A.A.S.G.F.I.F
                                            # .S.N.Y.G.M.S.W.V.R.Q.A.P.G.K.G.L.E.W.V.A.T.I.S.S.A.S.T.Y.S.Y.Y.P.D.S.V.K.G
                                            # .R.F.T.I.S.R.D.N.A.K.N.S.L.Y.L.Q.M.N.S.L.R.V.E.D.T.A.L.Y.Y.C.G.R.H.S.D.G.N
                                            # .F.A.F.G.Y.W.G.Q.G.T.L.V.T.V.S.S.A.S.T.K.G.P.S.V.F.P.L.A.P.S.S.K.S.T.S.G.G
                                            # .T.A.A.L.G.C.L.V.K.D.Y.F.P.E.P.V.T.V.S.W.N.S.G.A.L.T.S.G.V.H.T.F.P.A.V.L.Q
                                            # .S.S.G.L.Y.S.L.S.S.V.V.T.V.P.S.S.S.L.G.T.Q.T.Y.I.C.N.V.N.H.K.P.S.N.T.K.V.D
                                            # .K.K.V.E.P.K.S.C.D.K.T.H.T.C.P.P.C.P.A.P.E.L.L.G.G.P.S.V.F.L.F.P.P.K.P.K.D
                                            # .T.L.M.I.S.R.T.P.E.V.T.C.V.V.V.D.V.S.H.E.D.P.E.V.K.F.N.W.Y.V.D.G.V.E.V.H.N
                                            # .A.K.T.K.P.R.E.E.Q.Y.N.S.T.Y.R.V.V.S.V.L.T.V.L.H.Q.D.W.L.N.G.K.E.Y.K.C.K.V
                                            # .S.N.K.A.L.P.A.P.I.E.K.T.I.S.K.A.K.G.Q.P.R.E.P.Q.V.Y.T.L.P.P.S.R.D.E.L.T.K
                                            # .N.Q.V.S.L.T.C.L.V.K.G.F.Y.P.S.D.I.A.V.E.W.E.S.N.G.Q.P.E.N.N.Y.K.T.T.P.P.V
                                            # .L.D.S.D.G.S.F.F.L.Y.S.K.L.T.V.D.K.S.R.W.Q.Q.G.N.V.F.S.C.S.V.M.H.E.A.L.H.N
                                            # .H.Y.T.Q.K.S.L.S.L.S.P.G.K}|PEPTIDE3{E.V.Q.L.V.E.S.G.G.D.L.V.Q.P.G.R.S.L.R
                                            # .L.S.C.A.A.S.G.F.I.F.S.N.Y.G.M.S.W.V.R.Q.A.P.G.K.G.L.E.W.V.A.T.I.S.S.A.S.T
                                            # .Y.S.Y.Y.P.D.S.V.K.G.R.F.T.I.S.R.D.N.A.K.N.S.L.Y.L.Q.M.N.S.L.R.V.E.D.T.A.L
                                            # .Y.Y.C.G.R.H.S.D.G.N.F.A.F.G.Y.W.G.Q.G.T.L.V.T.V.S.S.A.S.T.K.G.P.S.V.F.P.L
                                            # .A.P.S.S.K.S.T.S.G.G.T.A.A.L.G.C.L.V.K.D.Y.F.P.E.P.V.T.V.S.W.N.S.G.A.L.T.S
                                            # .G.V.H.T.F.P.A.V.L.Q.S.S.G.L.Y.S.L.S.S.V.V.T.V.P.S.S.S.L.G.T.Q.T.Y.I.C.N.V
                                            # .N.H.K.P.S.N.T.K.V.D.K.K.V.E.P.K.S.C.D.K.T.H.T.C.P.P.C.P.A.P.E.L.L.G.G.P.S
                                            # .V.F.L.F.P.P.K.P.K.D.T.L.M.I.S.R.T.P.E.V.T.C.V.V.V.D.V.S.H.E.D.P.E.V.K.F.N
                                            # .W.Y.V.D.G.V.E.V.H.N.A.K.T.K.P.R.E.E.Q.Y.N.S.T.Y.R.V.V.S.V.L.T.V.L.H.Q.D.W
                                            # .L.N.G.K.E.Y.K.C.K.V.S.N.K.A.L.P.A.P.I.E.K.T.I.S.K.A.K.G.Q.P.R.E.P.Q.V.Y.T
                                            # .L.P.P.S.R.D.E.L.T.K.N.Q.V.S.L.T.C.L.V.K.G.F.Y.P.S.D.I.A.V.E.W.E.S.N.G.Q.P
                                            # .E.N.N.Y.K.T.T.P.P.V.L.D.S.D.G.S.F.F.L.Y.S.K.L.T.V.D.K.S.R.W.Q.Q.G.N.V.F.S
                                            # .C.S.V.M.H.E.A.L.H.N.H.Y.T.Q.K.S.L.S.L.S.P.G.K}|PEPTIDE4{D.V.L.M.T.Q.S.P.L
                                            # .S.L.P.V.T.P.G.E.P.A.S.I.S.C.R.S.S.R.N.I.V.H.I.N.G.D.T.Y.L.E.W.Y.L.Q.K.P.G
                                            # .Q.S.P.Q.L.L.I.Y.K.V.S.N.R.F.S.G.V.P.D.R.F.S.G.S.G.S.G.T.D.F.T.L.K.I.S.R.V
                                            # .E.A.E.D.V.G.V.Y.Y.C.F.Q.G.S.L.L.P.W.T.F.G.Q.G.T.K.V.E.I.K.R.T.V.A.A.P.S.V
                                            # .F.I.F.P.P.S.D.E.Q.L.K.S.G.T.A.S.V.V.C.L.L.N.N.F.Y.P.R.E.A.K.V.Q.W.K.V.D.N
                                            # .A.L.Q.S.G.N.S.Q.E.S.V.T.E.Q.D.S.K.D.S.T.Y.S.L.S.S.T.L.T.L.S.K.A.D.Y.E.K.H
                                            # .K.V.Y.A.C.E.V.T.H.Q.G.L.S.S.P.V.T.K.S.F.N.R.G.E.C}$PEPTIDE2,PEPTIDE2,146:
                                            # R3-202:R3|PEPTIDE3,PEPTIDE3,263:R3-323:R3|PEPTIDE2,PEPTIDE2,263:R3-323:R3|
                                            # PEPTIDE3,PEPTIDE3,22:R3-96:R3|PEPTIDE2,PEPTIDE3,231:R3-231:R3|PEPTIDE2,PEP
                                            # TIDE1,222:R3-219:R3|PEPTIDE4,PEPTIDE4,23:R3-93:R3|PEPTIDE2,PEPTIDE2,22:R3-
                                            # 96:R3|PEPTIDE4,PEPTIDE4,139:R3-199:R3|PEPTIDE1,PEPTIDE1,139:R3-199:R3|PEPT
                                            # IDE3,PEPTIDE3,146:R3-202:R3|PEPTIDE3,PEPTIDE4,222:R3-219:R3|PEPTIDE2,PEPTI
                                            # DE2,369:R3-427:R3|PEPTIDE3,PEPTIDE3,369:R3-427:R3|PEPTIDE1,PEPTIDE1,23:R3-
                                            # 93:R3|PEPTIDE2,PEPTIDE3,228:R3-228:R3$$$' , 'PEPTIDE1{D.I.Q.M.T.Q.S.P.S.S.
                                            # V.S.A.S.V.G.D.R.V.T.I.A.C.R.A.S.Q.N.I.R.N.I.L.N.W.Y.Q.Q.R.P.G.K.A.P.Q.L.L.
                                            # I.Y.A.A.S.N.L.Q.S.G.V.P.S.R.F.S.G.S.G.S.G.T.D.F.T.L.T.I.N.S.L.Q.P.E.D.F.A.
                                            # T.Y.Y.C.Q.Q.S.Y.S.M.P.R.T.F.G.G.G.T.K.L.E.I.K.R.T.V.A.A.P.S.V.F.I.F.P.P.S.
                                            # D.E.Q.L.K.S.G.T.A.S.V.V.C.L.L.N.N.F.Y.P.R.E.A.K.V.Q.W.K.V.D.N.A.L.Q.S.G.N.
                                            # S.Q.E.S.V.T.E.Q.D.S.K.D.S.T.Y.S.L.S.S.T.L.T.L.S.K.A.D.Y.E.K.H.K.V.Y.A.C.E.
                                            # V.T.H.Q.G.L.S.S.P.V.T.K.S.F.N.R.G.E.C}|PEPTIDE2{Q.V.Q.L.V.Q.S.G.A.E.V.K.K.
                                            # P.G.A.S.V.K.V.S.C.K.A.F.G.Y.P.F.T.D.Y.L.L.H.W.V.R.Q.A.P.G.Q.G.L.E.W.V.G.W.
                                            # L.N.P.Y.S.G.D.T.N.Y.A.Q.K.F.Q.G.R.V.T.M.T.R.D.T.S.I.S.T.A.Y.M.E.L.S.R.L.R.
                                            # S.D.D.T.A.V.Y.Y.C.T.R.T.T.L.I.S.V.Y.F.D.Y.W.G.Q.G.T.M.V.T.V.S.S.A.S.T.K.G.
                                            # P.S.V.F.P.L.A.P.S.S.K.S.T.S.G.G.T.A.A.L.G.C.L.V.K.D.Y.F.P.E.P.V.T.V.S.W.N.
                                            # S.G.A.L.T.S.G.V.H.T.F.P.A.V.L.Q.S.S.G.L.Y.S.L.S.S.V.V.T.V.P.S.S.S.L.G.T.Q.
                                            # T.Y.I.C.N.V.N.H.K.P.S.N.T.K.V.D.K.K.V.E.P.K.S.C.D.K.T.H.T.C.P.P.C.P.A.P.E.
                                            # L.L.G.G.P.S.V.F.L.F.P.P.K.P.K.D.T.L.M.I.S.R.T.P.E.V.T.C.V.V.V.D.V.S.H.E.D.
                                            # P.E.V.K.F.N.W.Y.V.D.G.V.E.V.H.N.A.K.T.K.P.R.E.E.Q.Y.N.S.T.Y.R.V.V.S.V.L.T.
                                            # V.L.H.Q.D.W.L.N.G.K.E.Y.K.C.K.V.S.N.K.A.L.P.A.P.I.E.K.T.I.S.K.A.K.G.Q.P.R.
                                            # E.P.Q.V.Y.T.L.P.P.S.R.D.E.L.T.K.N.Q.V.S.L.T.C.L.V.K.G.F.Y.P.S.D.I.A.V.E.W.
                                            # E.S.N.G.Q.P.E.N.N.Y.K.T.T.P.P.V.L.D.S.D.G.S.F.F.L.Y.S.K.L.T.V.D.K.S.R.W.Q.
                                            # Q.G.N.V.F.S.C.S.V.M.H.E.A.L.H.N.H.Y.T.Q.K.S.L.S.L.S.P.G.K}|PEPTIDE3{Q.V.Q.
                                            # L.V.Q.S.G.A.E.V.K.K.P.G.A.S.V.K.V.S.C.K.A.F.G.Y.P.F.T.D.Y.L.L.H.W.V.R.Q.A.
                                            # P.G.Q.G.L.E.W.V.G.W.L.N.P.Y.S.G.D.T.N.Y.A.Q.K.F.Q.G.R.V.T.M.T.R.D.T.S.I.S.
                                            # T.A.Y.M.E.L.S.R.L.R.S.D.D.T.A.V.Y.Y.C.T.R.T.T.L.I.S.V.Y.F.D.Y.W.G.Q.G.T.M.
                                            # V.T.V.S.S.A.S.T.K.G.P.S.V.F.P.L.A.P.S.S.K.S.T.S.G.G.T.A.A.L.G.C.L.V.K.D.Y.
                                            # F.P.E.P.V.T.V.S.W.N.S.G.A.L.T.S.G.V.H.T.F.P.A.V.L.Q.S.S.G.L.Y.S.L.S.S.V.V.
                                            # T.V.P.S.S.S.L.G.T.Q.T.Y.I.C.N.V.N.H.K.P.S.N.T.K.V.D.K.K.V.E.P.K.S.C.D.K.T.
                                            # H.T.C.P.P.C.P.A.P.E.L.L.G.G.P.S.V.F.L.F.P.P.K.P.K.D.T.L.M.I.S.R.T.P.E.V.T.
                                            # C.V.V.V.D.V.S.H.E.D.P.E.V.K.F.N.W.Y.V.D.G.V.E.V.H.N.A.K.T.K.P.R.E.E.Q.Y.N.
                                            # S.T.Y.R.V.V.S.V.L.T.V.L.H.Q.D.W.L.N.G.K.E.Y.K.C.K.V.S.N.K.A.L.P.A.P.I.E.K.
                                            # T.I.S.K.A.K.G.Q.P.R.E.P.Q.V.Y.T.L.P.P.S.R.D.E.L.T.K.N.Q.V.S.L.T.C.L.V.K.G.
                                            # F.Y.P.S.D.I.A.V.E.W.E.S.N.G.Q.P.E.N.N.Y.K.T.T.P.P.V.L.D.S.D.G.S.F.F.L.Y.S.
                                            # K.L.T.V.D.K.S.R.W.Q.Q.G.N.V.F.S.C.S.V.M.H.E.A.L.H.N.H.Y.T.Q.K.S.L.S.L.S.P.
                                            # G.K}|PEPTIDE4{D.I.Q.M.T.Q.S.P.S.S.V.S.A.S.V.G.D.R.V.T.I.A.C.R.A.S.Q.N.I.R.
                                            # N.I.L.N.W.Y.Q.Q.R.P.G.K.A.P.Q.L.L.I.Y.A.A.S.N.L.Q.S.G.V.P.S.R.F.S.G.S.G.S.
                                            # G.T.D.F.T.L.T.I.N.S.L.Q.P.E.D.F.A.T.Y.Y.C.Q.Q.S.Y.S.M.P.R.T.F.G.G.G.T.K.L.
                                            # E.I.K.R.T.V.A.A.P.S.V.F.I.F.P.P.S.D.E.Q.L.K.S.G.T.A.S.V.V.C.L.L.N.N.F.Y.P.
                                            # R.E.A.K.V.Q.W.K.V.D.N.A.L.Q.S.G.N.S.Q.E.S.V.T.E.Q.D.S.K.D.S.T.Y.S.L.S.S.T.
                                            # L.T.L.S.K.A.D.Y.E.K.H.K.V.Y.A.C.E.V.T.H.Q.G.L.S.S.P.V.T.K.S.F.N.R.G.E.C}$P
                                            # EPTIDE3,PEPTIDE4,222:R3-214:R3|PEPTIDE1,PEPTIDE1,134:R3-194:R3|PEPTIDE2,PE
                                            # PTIDE3,231:R3-231:R3|PEPTIDE4,PEPTIDE4,23:R3-88:R3|PEPTIDE3,PEPTIDE3,369:R
                                            # 3-427:R3|PEPTIDE2,PEPTIDE2,369:R3-427:R3|PEPTIDE1,PEPTIDE1,23:R3-88:R3|PEP
                                            # TIDE2,PEPTIDE2,146:R3-202:R3|PEPTIDE4,PEPTIDE4,134:R3-194:R3|PEPTIDE2,PEPT
                                            # IDE2,22:R3-96:R3|PEPTIDE3,PEPTIDE3,263:R3-323:R3|PEPTIDE3,PEPTIDE3,22:R3-9
                                            # 6:R3|PEPTIDE2,PEPTIDE1,222:R3-214:R3|PEPTIDE3,PEPTIDE3,146:R3-202:R3|PEPTI
                                            # DE2,PEPTIDE3,228:R3-228:R3|PEPTIDE2,PEPTIDE2,263:R3-323:R3$$$'
                                            'molecule_chembl_id': 'TEXT',
                                            # EXAMPLES:
                                            # 'CHEMBL408983' , 'CHEMBL4594317' , 'CHEMBL2109419' , 'CHEMBL2109308' , 'CH
                                            # EMBL2108796' , 'CHEMBL2108827' , 'CHEMBL2109365' , 'CHEMBL2109588' , 'CHEM
                                            # BL2109481' , 'CHEMBL2109508'
                                        }
                                    },
                                    'black_box': 'BOOLEAN',
                                    # EXAMPLES:
                                    # 'False' , 'False' , 'False' , 'False' , 'False' , 'False' , 'False' , 'False' , 'F
                                    # alse' , 'False'
                                    'chirality': 'NUMERIC',
                                    # EXAMPLES:
                                    # '1' , '1' , '2' , '2' , '2' , '2' , '0' , '1' , '2' , '2'
                                    'development_phase': 'NUMERIC',
                                    # EXAMPLES:
                                    # '0' , '0' , '0' , '2' , '4' , '4' , '4' , '2' , '4' , '0'
                                    'drug_type': 'NUMERIC',
                                    # EXAMPLES:
                                    # '1' , '7' , '1' , '1' , '1' , '1' , '1' , '7' , '1' , '1'
                                    'drug_warnings': 
                                    {
                                        'properties': 
                                        {
                                            'warning_class': 'TEXT',
                                            # EXAMPLES:
                                            # 'Carcinogenicity' , 'Hematological toxicity' , 'Carcinogenicity' , 'Hemato
                                            # logical toxicity' , 'Respiratory toxicity' , 'Cardiotoxicity' , 'Neurotoxi
                                            # city' , 'Respiratory toxicity' , 'Hepatotoxicity' , 'Dermatological toxici
                                            # ty'
                                            'warning_country': 'TEXT',
                                            # EXAMPLES:
                                            # 'United Kingdom' , 'France' , 'United Kingdom; Spain; Germany' , 'United S
                                            # tates' , 'Spain; Germany; France' , 'Germany' , 'United Kingdom; Germany; 
                                            # Italy; Ireland; Netherlands; European Union' , 'European Union; Germany; F
                                            # rance' , 'European Union' , 'Spain; Germany; France'
                                            'warning_description': 'TEXT',
                                            # EXAMPLES:
                                            # 'Cutaneous Reactions; Animal Carcinogenicity' , 'Agranulocytosis' , 'Anima
                                            # l Carcinogenicity (rodent); Gastrointestinal Toxicity' , 'Stevens Johnson 
                                            # Syndrome; Toxic Epidermal Necrolysis' , 'Dermatologic, Hematologic and Hep
                                            # atic Reactions' , 'Arrhythmias and Sudden Cardiac Death (Arrhythmias and S
                                            # udden)' , 'Polyneuropathy' , 'Cardiac valvulopathy; Pulmonary arterial hyp
                                            # ertension' , 'Hepatotoxicity' , 'Hepatotoxicity'
                                            'warning_id': 'NUMERIC',
                                            # EXAMPLES:
                                            # '2107' , '2118' , '2116' , '2561' , '1686' , '1049' , '1404' , '783' , '22
                                            # 98' , '2278'
                                            'warning_refs': 
                                            {
                                                'properties': 
                                                {
                                                    'ref_id': 'TEXT',
                                                    # EXAMPLES:
                                                    # '7628177' , '10.1177/009286150103500134' , '10.1177/00928615010350
                                                    # 0134' , 'b5b17cde-a94c-4105-871c-54e7d2bd47e8' , '5fa97bf5-28a2-48
                                                    # f1-8955-f56012d296be' , 'b0a5ded2-8ee2-49ca-a86c-2b28ae40f60c' , '
                                                    # 86b915c9-9c00-46c2-8dd9-3e15a6b42323' , '67f66894-addc-4e92-855a-c
                                                    # 9ae03a5c2c5' , 'CFR-2019-title21-vol4/pdf/CFR-2019-title21-vol4-se
                                                    # c216-24.pdf' , '0df6fd1e-7d9c-4a38-848c-1e562e211c91'
                                                    'ref_type': 'TEXT',
                                                    # EXAMPLES:
                                                    # 'PubMed' , 'DOI' , 'DOI' , 'FDA' , 'FDA' , 'FDA' , 'FDA' , 'FDA' ,
                                                    #  'USGPO' , 'FDA'
                                                    'ref_url': 'TEXT',
                                                    # EXAMPLES:
                                                    # 'http://europepmc.org/abstract/MED/7628177' , 'https://doi.org/10.
                                                    # 1177/009286150103500134' , 'https://doi.org/10.1177/00928615010350
                                                    # 0134' , 'https://api.fda.gov/drug/label.json?search=set_id:b5b17cd
                                                    # e-a94c-4105-871c-54e7d2bd47e8' , 'https://api.fda.gov/drug/label.j
                                                    # son?search=set_id:5fa97bf5-28a2-48f1-8955-f56012d296be' , 'https:/
                                                    # /api.fda.gov/drug/label.json?search=set_id:b0a5ded2-8ee2-49ca-a86c
                                                    # -2b28ae40f60c' , 'https://api.fda.gov/drug/label.json?search=set_i
                                                    # d:86b915c9-9c00-46c2-8dd9-3e15a6b42323' , 'https://api.fda.gov/dru
                                                    # g/label.json?search=set_id:67f66894-addc-4e92-855a-c9ae03a5c2c5' ,
                                                    #  'https://www.govinfo.gov/content/pkg/CFR-2019-title21-vol4/pdf/CF
                                                    # R-2019-title21-vol4-sec216-24.pdf' , 'https://api.fda.gov/drug/lab
                                                    # el.json?search=set_id:0df6fd1e-7d9c-4a38-848c-1e562e211c91'
                                                }
                                            },
                                            'warning_type': 'TEXT',
                                            # EXAMPLES:
                                            # 'Withdrawn' , 'Withdrawn' , 'Withdrawn' , 'Black Box Warning' , 'Black Box
                                            #  Warning' , 'Black Box Warning' , 'Black Box Warning' , 'Black Box Warning
                                            # ' , 'Black Box Warning' , 'Withdrawn'
                                            'warning_year': 'NUMERIC',
                                            # EXAMPLES:
                                            # '1984' , '1985' , '1983' , '1983' , '1988' , '1998' , '1987' , '2009' , '1
                                            # 985' , '1971'
                                        }
                                    },
                                    'first_approval': 'NUMERIC',
                                    # EXAMPLES:
                                    # '1978' , '1979' , '1999' , '2003' , '1994' , '1985' , '2001' , '1997' , '1977' , '
                                    # 1977'
                                    'first_in_class': 'BOOLEAN',
                                    # EXAMPLES:
                                    # 'False' , 'False' , 'False' , 'False' , 'False' , 'False' , 'False' , 'False' , 'F
                                    # alse' , 'False'
                                    'helm_notation': 'TEXT',
                                    # EXAMPLES:
                                    # 'PEPTIDE1{[Glp].W.P.R.P.Q.I.P.P}$$$$' , 'PEPTIDE1{S.S.E.L.T.Q.D.P.A.V.S.V.A.L.G.Q.
                                    # T.V.R.I.T.C.Q.G.D.S.L.R.S.Y.Y.A.T.W.Y.Q.Q.K.P.G.Q.A.P.I.L.V.I.Y.G.E.N.K.R.P.S.G.I.
                                    # P.D.R.F.S.G.S.S.S.G.N.T.A.S.L.T.I.T.G.A.Q.A.E.D.E.A.D.Y.Y.C.K.S.R.D.G.S.G.Q.H.L.V.
                                    # F.G.G.G.T.K.L.T.V.L.G.Q.P.K.A.A.P.S.V.T.L.F.P.P.S.S.E.E.L.Q.A.N.K.A.T.L.V.C.L.I.S.
                                    # D.F.Y.P.G.A.V.T.V.A.W.K.A.D.S.S.P.V.K.A.G.V.E.T.T.T.P.S.K.Q.S.N.N.K.Y.A.A.S.S.Y.L.
                                    # S.L.T.P.E.Q.W.K.S.H.R.S.Y.S.C.Q.V.T.H.E.G.S.T.V.E.K.T.V.A.P.A.E.C.S}|PEPTIDE2{E.V.
                                    # Q.L.V.Q.S.G.A.E.V.K.K.P.G.S.S.V.K.V.S.C.K.A.S.G.G.T.F.S.S.Y.A.I.S.W.V.R.Q.A.P.G.Q.
                                    # G.L.E.W.M.G.G.I.I.P.I.F.G.T.A.N.Y.A.Q.K.F.Q.G.R.V.T.I.T.A.D.K.S.T.S.T.A.Y.M.E.L.S.
                                    # S.L.R.S.E.D.T.A.V.Y.Y.C.A.R.A.P.L.R.F.L.E.W.S.T.Q.D.H.Y.Y.Y.Y.Y.M.D.V.W.G.K.G.T.T.
                                    # V.T.V.S.S.A.S.T.K.G.P.S.V.F.P.L.A.P.S.S.K.S.T.S.G.G.T.A.A.L.G.C.L.V.K.D.Y.F.P.E.P.
                                    # V.T.V.S.W.N.S.G.A.L.T.S.G.V.H.T.F.P.A.V.L.Q.S.S.G.L.Y.S.L.S.S.V.V.T.V.P.S.S.S.L.G.
                                    # T.Q.T.Y.I.C.N.V.N.H.K.P.S.N.T.K.V.D.K.K.V.E.P.K.S.C.D.K.T.H.T.C.P.P.C.P.A.P.E.L.L.
                                    # G.G.P.S.V.F.L.F.P.P.K.P.K.D.T.L.M.I.S.R.T.P.E.V.T.C.V.V.V.D.V.S.H.E.D.P.E.V.K.F.N.
                                    # W.Y.V.D.G.V.E.V.H.N.A.K.T.K.P.R.E.E.Q.Y.N.S.T.Y.R.V.V.S.V.L.T.V.L.H.Q.D.W.L.N.G.K.
                                    # E.Y.K.C.K.V.S.N.K.A.L.P.A.P.I.E.K.T.I.S.K.A.K.G.Q.P.R.E.P.Q.V.Y.T.L.P.P.S.R.E.E.M.
                                    # T.K.N.Q.V.S.L.T.C.L.V.K.G.F.Y.P.S.D.I.A.V.E.W.E.S.N.G.Q.P.E.N.N.Y.K.T.T.P.P.V.L.D.
                                    # S.D.G.S.F.F.L.Y.S.K.L.T.V.D.K.S.R.W.Q.Q.G.N.V.F.S.C.S.V.M.H.E.A.L.H.N.H.Y.T.Q.K.S.
                                    # L.S.L.S.P.G.K}|PEPTIDE3{E.V.Q.L.V.Q.S.G.A.E.V.K.K.P.G.S.S.V.K.V.S.C.K.A.S.G.G.T.F.
                                    # S.S.Y.A.I.S.W.V.R.Q.A.P.G.Q.G.L.E.W.M.G.G.I.I.P.I.F.G.T.A.N.Y.A.Q.K.F.Q.G.R.V.T.I.
                                    # T.A.D.K.S.T.S.T.A.Y.M.E.L.S.S.L.R.S.E.D.T.A.V.Y.Y.C.A.R.A.P.L.R.F.L.E.W.S.T.Q.D.H.
                                    # Y.Y.Y.Y.Y.M.D.V.W.G.K.G.T.T.V.T.V.S.S.A.S.T.K.G.P.S.V.F.P.L.A.P.S.S.K.S.T.S.G.G.T.
                                    # A.A.L.G.C.L.V.K.D.Y.F.P.E.P.V.T.V.S.W.N.S.G.A.L.T.S.G.V.H.T.F.P.A.V.L.Q.S.S.G.L.Y.
                                    # S.L.S.S.V.V.T.V.P.S.S.S.L.G.T.Q.T.Y.I.C.N.V.N.H.K.P.S.N.T.K.V.D.K.K.V.E.P.K.S.C.D.
                                    # K.T.H.T.C.P.P.C.P.A.P.E.L.L.G.G.P.S.V.F.L.F.P.P.K.P.K.D.T.L.M.I.S.R.T.P.E.V.T.C.V.
                                    # V.V.D.V.S.H.E.D.P.E.V.K.F.N.W.Y.V.D.G.V.E.V.H.N.A.K.T.K.P.R.E.E.Q.Y.N.S.T.Y.R.V.V.
                                    # S.V.L.T.V.L.H.Q.D.W.L.N.G.K.E.Y.K.C.K.V.S.N.K.A.L.P.A.P.I.E.K.T.I.S.K.A.K.G.Q.P.R.
                                    # E.P.Q.V.Y.T.L.P.P.S.R.E.E.M.T.K.N.Q.V.S.L.T.C.L.V.K.G.F.Y.P.S.D.I.A.V.E.W.E.S.N.G.
                                    # Q.P.E.N.N.Y.K.T.T.P.P.V.L.D.S.D.G.S.F.F.L.Y.S.K.L.T.V.D.K.S.R.W.Q.Q.G.N.V.F.S.C.S.
                                    # V.M.H.E.A.L.H.N.H.Y.T.Q.K.S.L.S.L.S.P.G.K}|PEPTIDE4{S.S.E.L.T.Q.D.P.A.V.S.V.A.L.G.
                                    # Q.T.V.R.I.T.C.Q.G.D.S.L.R.S.Y.Y.A.T.W.Y.Q.Q.K.P.G.Q.A.P.I.L.V.I.Y.G.E.N.K.R.P.S.G.
                                    # I.P.D.R.F.S.G.S.S.S.G.N.T.A.S.L.T.I.T.G.A.Q.A.E.D.E.A.D.Y.Y.C.K.S.R.D.G.S.G.Q.H.L.
                                    # V.F.G.G.G.T.K.L.T.V.L.G.Q.P.K.A.A.P.S.V.T.L.F.P.P.S.S.E.E.L.Q.A.N.K.A.T.L.V.C.L.I.
                                    # S.D.F.Y.P.G.A.V.T.V.A.W.K.A.D.S.S.P.V.K.A.G.V.E.T.T.T.P.S.K.Q.S.N.N.K.Y.A.A.S.S.Y.
                                    # L.S.L.T.P.E.Q.W.K.S.H.R.S.Y.S.C.Q.V.T.H.E.G.S.T.V.E.K.T.V.A.P.A.E.C.S}$PEPTIDE2,PE
                                    # PTIDE1,233:R3-213:R3|PEPTIDE3,PEPTIDE3,157:R3-213:R3|PEPTIDE2,PEPTIDE2,380:R3-438:
                                    # R3|PEPTIDE2,PEPTIDE3,239:R3-239:R3|PEPTIDE3,PEPTIDE3,22:R3-96:R3|PEPTIDE4,PEPTIDE4
                                    # ,136:R3-195:R3|PEPTIDE2,PEPTIDE3,242:R3-242:R3|PEPTIDE3,PEPTIDE3,380:R3-438:R3|PEP
                                    # TIDE2,PEPTIDE2,22:R3-96:R3|PEPTIDE1,PEPTIDE1,136:R3-195:R3|PEPTIDE3,PEPTIDE4,233:R
                                    # 3-213:R3|PEPTIDE2,PEPTIDE2,157:R3-213:R3|PEPTIDE3,PEPTIDE3,274:R3-334:R3|PEPTIDE1,
                                    # PEPTIDE1,22:R3-87:R3|PEPTIDE2,PEPTIDE2,274:R3-334:R3|PEPTIDE4,PEPTIDE4,22:R3-87:R3
                                    # $$$' , 'PEPTIDE1{E.I.V.L.T.Q.S.P.G.T.L.S.L.S.P.G.E.R.A.T.L.S.C.R.A.S.Q.G.I.S.R.S.Y
                                    # .L.A.W.Y.Q.Q.K.P.G.Q.A.P.S.L.L.I.Y.G.A.S.S.R.A.T.G.I.P.D.R.F.S.G.S.G.S.G.T.D.F.T.L
                                    # .T.I.S.R.L.E.P.E.D.F.A.V.Y.Y.C.Q.Q.F.G.S.S.P.W.T.F.G.Q.G.T.K.V.E.I.K.R.T.V.A.A.P.S
                                    # .V.F.I.F.P.P.S.D.E.Q.L.K.S.G.T.A.S.V.V.C.L.L.N.N.F.Y.P.R.E.A.K.V.Q.W.K.V.D.N.A.L.Q
                                    # .S.G.N.S.Q.E.S.V.T.E.Q.D.S.K.D.S.T.Y.S.L.S.S.T.L.T.L.S.K.A.D.Y.E.K.H.K.V.Y.A.C.E.V
                                    # .T.H.Q.G.L.S.S.P.V.T.K.S.F.N.R.G.E.C}|PEPTIDE2{Q.V.Q.L.Q.E.S.G.P.G.L.V.K.P.S.Q.T.L
                                    # .S.L.T.C.T.V.S.G.G.S.I.S.S.G.D.Y.F.W.S.W.I.R.Q.L.P.G.K.G.L.E.W.I.G.H.I.H.N.S.G.T.T
                                    # .Y.Y.N.P.S.L.K.S.R.V.T.I.S.V.D.T.S.K.K.Q.F.S.L.R.L.S.S.V.T.A.A.D.T.A.V.Y.Y.C.A.R.D
                                    # .R.G.G.D.Y.Y.Y.G.M.D.V.W.G.Q.G.T.T.V.T.V.S.S.A.S.T.K.G.P.S.V.F.P.L.A.P.S.S.K.S.T.S
                                    # .G.G.T.A.A.L.G.C.L.V.K.D.Y.F.P.E.P.V.T.V.S.W.N.S.G.A.L.T.S.G.V.H.T.F.P.A.V.L.Q.S.S
                                    # .G.L.Y.S.L.S.S.V.V.T.V.P.S.S.S.L.G.T.Q.T.Y.I.C.N.V.N.H.K.P.S.N.T.K.V.D.K.R.V.E.P.K
                                    # .S.C.D.K.T.H.T.C.P.P.C.P.A.P.E.L.L.G.G.P.S.V.F.L.F.P.P.K.P.K.D.T.L.M.I.S.R.T.P.E.V
                                    # .T.C.V.V.V.D.V.S.H.E.D.P.E.V.K.F.N.W.Y.V.D.G.V.E.V.H.N.A.K.T.K.P.R.E.E.Q.Y.N.S.T.Y
                                    # .R.V.V.S.V.L.T.V.L.H.Q.D.W.L.N.G.K.E.Y.K.C.K.V.S.N.K.A.L.P.A.P.I.E.K.T.I.S.K.A.K.G
                                    # .Q.P.R.E.P.Q.V.Y.T.L.P.P.S.R.E.E.M.T.K.N.Q.V.S.L.T.C.L.V.K.G.F.Y.P.S.D.I.A.V.E.W.E
                                    # .S.N.G.Q.P.E.N.N.Y.K.T.T.P.P.V.L.D.S.D.G.S.F.F.L.Y.S.K.L.T.V.D.K.S.R.W.Q.Q.G.N.V.F
                                    # .S.C.S.V.M.H.E.A.L.H.N.H.Y.T.Q.K.S.L.S.L.S.P.G.K}|PEPTIDE3{Q.V.Q.L.Q.E.S.G.P.G.L.V
                                    # .K.P.S.Q.T.L.S.L.T.C.T.V.S.G.G.S.I.S.S.G.D.Y.F.W.S.W.I.R.Q.L.P.G.K.G.L.E.W.I.G.H.I
                                    # .H.N.S.G.T.T.Y.Y.N.P.S.L.K.S.R.V.T.I.S.V.D.T.S.K.K.Q.F.S.L.R.L.S.S.V.T.A.A.D.T.A.V
                                    # .Y.Y.C.A.R.D.R.G.G.D.Y.Y.Y.G.M.D.V.W.G.Q.G.T.T.V.T.V.S.S.A.S.T.K.G.P.S.V.F.P.L.A.P
                                    # .S.S.K.S.T.S.G.G.T.A.A.L.G.C.L.V.K.D.Y.F.P.E.P.V.T.V.S.W.N.S.G.A.L.T.S.G.V.H.T.F.P
                                    # .A.V.L.Q.S.S.G.L.Y.S.L.S.S.V.V.T.V.P.S.S.S.L.G.T.Q.T.Y.I.C.N.V.N.H.K.P.S.N.T.K.V.D
                                    # .K.R.V.E.P.K.S.C.D.K.T.H.T.C.P.P.C.P.A.P.E.L.L.G.G.P.S.V.F.L.F.P.P.K.P.K.D.T.L.M.I
                                    # .S.R.T.P.E.V.T.C.V.V.V.D.V.S.H.E.D.P.E.V.K.F.N.W.Y.V.D.G.V.E.V.H.N.A.K.T.K.P.R.E.E
                                    # .Q.Y.N.S.T.Y.R.V.V.S.V.L.T.V.L.H.Q.D.W.L.N.G.K.E.Y.K.C.K.V.S.N.K.A.L.P.A.P.I.E.K.T
                                    # .I.S.K.A.K.G.Q.P.R.E.P.Q.V.Y.T.L.P.P.S.R.E.E.M.T.K.N.Q.V.S.L.T.C.L.V.K.G.F.Y.P.S.D
                                    # .I.A.V.E.W.E.S.N.G.Q.P.E.N.N.Y.K.T.T.P.P.V.L.D.S.D.G.S.F.F.L.Y.S.K.L.T.V.D.K.S.R.W
                                    # .Q.Q.G.N.V.F.S.C.S.V.M.H.E.A.L.H.N.H.Y.T.Q.K.S.L.S.L.S.P.G.K}|PEPTIDE4{E.I.V.L.T.Q
                                    # .S.P.G.T.L.S.L.S.P.G.E.R.A.T.L.S.C.R.A.S.Q.G.I.S.R.S.Y.L.A.W.Y.Q.Q.K.P.G.Q.A.P.S.L
                                    # .L.I.Y.G.A.S.S.R.A.T.G.I.P.D.R.F.S.G.S.G.S.G.T.D.F.T.L.T.I.S.R.L.E.P.E.D.F.A.V.Y.Y
                                    # .C.Q.Q.F.G.S.S.P.W.T.F.G.Q.G.T.K.V.E.I.K.R.T.V.A.A.P.S.V.F.I.F.P.P.S.D.E.Q.L.K.S.G
                                    # .T.A.S.V.V.C.L.L.N.N.F.Y.P.R.E.A.K.V.Q.W.K.V.D.N.A.L.Q.S.G.N.S.Q.E.S.V.T.E.Q.D.S.K
                                    # .D.S.T.Y.S.L.S.S.T.L.T.L.S.K.A.D.Y.E.K.H.K.V.Y.A.C.E.V.T.H.Q.G.L.S.S.P.V.T.K.S.F.N
                                    # .R.G.E.C}$PEPTIDE3,PEPTIDE3,266:R3-326:R3|PEPTIDE1,PEPTIDE1,23:R3-89:R3|PEPTIDE1,P
                                    # EPTIDE1,135:R3-195:R3|PEPTIDE2,PEPTIDE3,231:R3-231:R3|PEPTIDE4,PEPTIDE4,23:R3-89:R
                                    # 3|PEPTIDE2,PEPTIDE3,234:R3-234:R3|PEPTIDE2,PEPTIDE2,372:R3-430:R3|PEPTIDE2,PEPTIDE
                                    # 1,225:R3-215:R3|PEPTIDE4,PEPTIDE4,135:R3-195:R3|PEPTIDE3,PEPTIDE4,225:R3-215:R3|PE
                                    # PTIDE3,PEPTIDE3,22:R3-97:R3|PEPTIDE2,PEPTIDE2,266:R3-326:R3|PEPTIDE2,PEPTIDE2,149:
                                    # R3-205:R3|PEPTIDE3,PEPTIDE3,149:R3-205:R3|PEPTIDE3,PEPTIDE3,372:R3-430:R3|PEPTIDE2
                                    # ,PEPTIDE2,22:R3-97:R3$$$' , 'PEPTIDE1{D.I.V.M.T.Q.S.P.L.S.L.P.V.T.P.G.Q.P.A.S.I.S.
                                    # C.R.S.S.Q.S.I.V.H.S.N.G.N.T.W.L.Q.W.W.L.Q.K.P.G.Q.S.P.Q.L.L.I.W.K.V.S.N.R.L.W.G.V.
                                    # P.D.R.F.S.G.S.G.S.G.T.D.F.T.L.K.I.S.R.V.Q.A.Q.D.V.G.V.W.W.C.F.Q.G.S.H.V.P.W.T.F.G.
                                    # Q.G.T.K.V.Q.I.K.R.T.V.A.A.P.S.V.F.I.F.P.P.S.D.E.Q.L.K.S.G.T.A.S.V.V.C.L.L.N.N.F.Y.
                                    # P.R.E.A.K.V.Q.W.K.V.D.N.A.L.Q.S.G.N.S.Q.E.S.V.T.E.Q.D.S.K.D.S.T.Y.S.L.S.S.T.L.T.L.
                                    # S.K.A.D.Y.E.K.H.K.V.Y.A.C.E.V.T.H.Q.G.L.S.S.P.V.T.K.S.F.N.R.G.E.C}|PEPTIDE2{Q.V.Q.
                                    # L.Q.Q.S.G.P.G.L.V.K.P.S.Q.T.L.S.L.T.C.T.V.S.G.W.S.I.S.G.G.W.L.W.N.W.I.R.Q.P.P.G.K.
                                    # G.L.Q.W.I.G.W.I.S.W.D.G.T.N.N.W.K.P.S.L.K.D.R.V.T.I.S.V.D.T.S.K.N.Q.F.S.L.K.L.S.S.
                                    # V.T.A.A.D.T.A.V.W.W.C.A.R.W.G.R.V.F.F.D.W.W.G.Q.G.T.L.V.T.V.S.S.A.S.T.K.G.P.S.V.F.
                                    # P.L.A.P.S.S.K.S.T.S.G.G.T.A.A.L.G.C.L.V.K.D.Y.F.P.E.P.V.T.V.S.W.N.S.G.A.L.T.S.G.V.
                                    # H.T.F.P.A.V.L.Q.S.S.G.L.Y.S.L.S.S.V.V.T.V.P.S.S.S.L.G.T.Q.T.Y.I.C.N.V.N.H.K.P.S.N.
                                    # T.K.V.D.K.R.V.E.P.K.S.C.D.K.T.H.T.C.P.P.C.P.A.P.E.L.L.G.G.P.S.V.F.L.F.P.P.K.P.K.D.
                                    # T.L.M.I.S.R.T.P.E.V.T.C.V.V.V.D.V.S.H.E.D.P.E.V.K.F.N.W.Y.V.D.G.V.E.V.H.N.A.K.T.K.
                                    # P.R.E.E.Q.Y.N.S.T.Y.R.V.V.S.V.L.T.V.L.H.Q.D.W.L.N.G.K.E.Y.K.C.K.V.S.N.K.A.L.P.A.P.
                                    # I.E.K.T.I.S.K.A.K.G.Q.P.R.E.P.Q.V.Y.T.L.P.P.S.R.E.E.M.T.K.N.Q.V.S.L.T.C.L.V.K.G.F.
                                    # Y.P.S.D.I.A.V.E.W.E.S.N.G.Q.P.E.N.N.Y.K.T.T.P.P.V.L.D.S.D.G.S.F.F.L.Y.S.K.L.T.V.D.
                                    # K.S.R.W.Q.Q.G.N.V.F.S.C.S.V.M.H.E.A.L.H.N.H.Y.T.Q.K.S.L.S.L.S.P.G.K}|PEPTIDE3{Q.V.
                                    # Q.L.Q.Q.S.G.P.G.L.V.K.P.S.Q.T.L.S.L.T.C.T.V.S.G.W.S.I.S.G.G.W.L.W.N.W.I.R.Q.P.P.G.
                                    # K.G.L.Q.W.I.G.W.I.S.W.D.G.T.N.N.W.K.P.S.L.K.D.R.V.T.I.S.V.D.T.S.K.N.Q.F.S.L.K.L.S.
                                    # S.V.T.A.A.D.T.A.V.W.W.C.A.R.W.G.R.V.F.F.D.W.W.G.Q.G.T.L.V.T.V.S.S.A.S.T.K.G.P.S.V.
                                    # F.P.L.A.P.S.S.K.S.T.S.G.G.T.A.A.L.G.C.L.V.K.D.Y.F.P.E.P.V.T.V.S.W.N.S.G.A.L.T.S.G.
                                    # V.H.T.F.P.A.V.L.Q.S.S.G.L.Y.S.L.S.S.V.V.T.V.P.S.S.S.L.G.T.Q.T.Y.I.C.N.V.N.H.K.P.S.
                                    # N.T.K.V.D.K.R.V.E.P.K.S.C.D.K.T.H.T.C.P.P.C.P.A.P.E.L.L.G.G.P.S.V.F.L.F.P.P.K.P.K.
                                    # D.T.L.M.I.S.R.T.P.E.V.T.C.V.V.V.D.V.S.H.E.D.P.E.V.K.F.N.W.Y.V.D.G.V.E.V.H.N.A.K.T.
                                    # K.P.R.E.E.Q.Y.N.S.T.Y.R.V.V.S.V.L.T.V.L.H.Q.D.W.L.N.G.K.E.Y.K.C.K.V.S.N.K.A.L.P.A.
                                    # P.I.E.K.T.I.S.K.A.K.G.Q.P.R.E.P.Q.V.Y.T.L.P.P.S.R.E.E.M.T.K.N.Q.V.S.L.T.C.L.V.K.G.
                                    # F.Y.P.S.D.I.A.V.E.W.E.S.N.G.Q.P.E.N.N.Y.K.T.T.P.P.V.L.D.S.D.G.S.F.F.L.Y.S.K.L.T.V.
                                    # D.K.S.R.W.Q.Q.G.N.V.F.S.C.S.V.M.H.E.A.L.H.N.H.Y.T.Q.K.S.L.S.L.S.P.G.K}|PEPTIDE4{D.
                                    # I.V.M.T.Q.S.P.L.S.L.P.V.T.P.G.Q.P.A.S.I.S.C.R.S.S.Q.S.I.V.H.S.N.G.N.T.W.L.Q.W.W.L.
                                    # Q.K.P.G.Q.S.P.Q.L.L.I.W.K.V.S.N.R.L.W.G.V.P.D.R.F.S.G.S.G.S.G.T.D.F.T.L.K.I.S.R.V.
                                    # Q.A.Q.D.V.G.V.W.W.C.F.Q.G.S.H.V.P.W.T.F.G.Q.G.T.K.V.Q.I.K.R.T.V.A.A.P.S.V.F.I.F.P.
                                    # P.S.D.E.Q.L.K.S.G.T.A.S.V.V.C.L.L.N.N.F.Y.P.R.E.A.K.V.Q.W.K.V.D.N.A.L.Q.S.G.N.S.Q.
                                    # E.S.V.T.E.Q.D.S.K.D.S.T.Y.S.L.S.S.T.L.T.L.S.K.A.D.Y.E.K.H.K.V.Y.A.C.E.V.T.H.Q.G.L.
                                    # S.S.P.V.T.K.S.F.N.R.G.E.C}$PEPTIDE4,PEPTIDE4,139:R3-199:R3|PEPTIDE2,PEPTIDE1,220:R
                                    # 3-219:R3|PEPTIDE3,PEPTIDE3,367:R3-425:R3|PEPTIDE2,PEPTIDE3,226:R3-226:R3|PEPTIDE1,
                                    # PEPTIDE1,23:R3-93:R3|PEPTIDE3,PEPTIDE4,220:R3-219:R3|PEPTIDE1,PEPTIDE1,139:R3-199:
                                    # R3|PEPTIDE4,PEPTIDE4,23:R3-93:R3|PEPTIDE2,PEPTIDE2,367:R3-425:R3|PEPTIDE2,PEPTIDE2
                                    # ,144:R3-200:R3|PEPTIDE2,PEPTIDE2,22:R3-96:R3|PEPTIDE2,PEPTIDE2,261:R3-321:R3|PEPTI
                                    # DE3,PEPTIDE3,22:R3-96:R3|PEPTIDE2,PEPTIDE3,229:R3-229:R3|PEPTIDE3,PEPTIDE3,261:R3-
                                    # 321:R3|PEPTIDE3,PEPTIDE3,144:R3-200:R3$$$' , 'PEPTIDE1{D.I.V.L.T.Q.S.P.A.T.L.S.L.S
                                    # .P.G.E.R.A.T.L.S.C.R.A.S.Q.S.V.S.S.S.Y.L.A.W.Y.Q.Q.K.P.G.Q.A.P.R.L.L.I.Y.G.A.S.S.R
                                    # .A.T.G.V.P.A.R.F.S.G.S.G.S.G.T.D.F.T.L.T.I.S.S.L.E.P.E.D.F.A.T.Y.Y.C.L.Q.I.Y.N.M.P
                                    # .I.T.F.G.Q.G.T.K.V.E.I.K.R.T.V.A.A.P.S.V.F.I.F.P.P.S.D.E.Q.L.K.S.G.T.A.S.V.V.C.L.L
                                    # .N.N.F.Y.P.R.E.A.K.V.Q.W.K.V.D.N.A.L.Q.S.G.N.S.Q.E.S.V.T.E.Q.D.S.K.D.S.T.Y.S.L.S.S
                                    # .T.L.T.L.S.K.A.D.Y.E.K.H.K.V.Y.A.C.E.V.T.H.Q.G.L.S.S.P.V.T.K.S.F.N.R.G.E.C}|PEPTID
                                    # E2{Q.V.E.L.V.E.S.G.G.G.L.V.Q.P.G.G.S.L.R.L.S.C.A.A.S.G.F.T.F.S.S.Y.A.M.S.W.V.R.Q.A
                                    # .P.G.K.G.L.E.W.V.S.A.I.N.A.S.G.T.R.T.Y.Y.A.D.S.V.K.G.R.F.T.I.S.R.D.N.S.K.N.T.L.Y.L
                                    # .Q.M.N.S.L.R.A.E.D.T.A.V.Y.Y.C.A.R.G.K.G.N.T.H.K.P.Y.G.Y.V.R.Y.F.D.V.W.G.Q.G.T.L.V
                                    # .T.V.S.S.A.S.T.K.G.P.S.V.F.P.L.A.P.S.S.K.S.T.S.G.G.T.A.A.L.G.C.L.V.K.D.Y.F.P.E.P.V
                                    # .T.V.S.W.N.S.G.A.L.T.S.G.V.H.T.F.P.A.V.L.Q.S.S.G.L.Y.S.L.S.S.V.V.T.V.P.S.S.S.L.G.T
                                    # .Q.T.Y.I.C.N.V.N.H.K.P.S.N.T.K.V.D.K.K.V.E.P.K.S.C.D.K.T.H.T.C.P.P.C.P.A.P.E.L.L.G
                                    # .G.P.S.V.F.L.F.P.P.K.P.K.D.T.L.M.I.S.R.T.P.E.V.T.C.V.V.V.D.V.S.H.E.D.P.E.V.K.F.N.W
                                    # .Y.V.D.G.V.E.V.H.N.A.K.T.K.P.R.E.E.Q.Y.N.S.T.Y.R.V.V.S.V.L.T.V.L.H.Q.D.W.L.N.G.K.E
                                    # .Y.K.C.K.V.S.N.K.A.L.P.A.P.I.E.K.T.I.S.K.A.K.G.Q.P.R.E.P.Q.V.Y.T.L.P.P.S.R.D.E.L.T
                                    # .K.N.Q.V.S.L.T.C.L.V.K.G.F.Y.P.S.D.I.A.V.E.W.E.S.N.G.Q.P.E.N.N.Y.K.T.T.P.P.V.L.D.S
                                    # .D.G.S.F.F.L.Y.S.K.L.T.V.D.K.S.R.W.Q.Q.G.N.V.F.S.C.S.V.M.H.E.A.L.H.N.H.Y.T.Q.K.S.L
                                    # .S.L.S.P.G.K}|PEPTIDE3{Q.V.E.L.V.E.S.G.G.G.L.V.Q.P.G.G.S.L.R.L.S.C.A.A.S.G.F.T.F.S
                                    # .S.Y.A.M.S.W.V.R.Q.A.P.G.K.G.L.E.W.V.S.A.I.N.A.S.G.T.R.T.Y.Y.A.D.S.V.K.G.R.F.T.I.S
                                    # .R.D.N.S.K.N.T.L.Y.L.Q.M.N.S.L.R.A.E.D.T.A.V.Y.Y.C.A.R.G.K.G.N.T.H.K.P.Y.G.Y.V.R.Y
                                    # .F.D.V.W.G.Q.G.T.L.V.T.V.S.S.A.S.T.K.G.P.S.V.F.P.L.A.P.S.S.K.S.T.S.G.G.T.A.A.L.G.C
                                    # .L.V.K.D.Y.F.P.E.P.V.T.V.S.W.N.S.G.A.L.T.S.G.V.H.T.F.P.A.V.L.Q.S.S.G.L.Y.S.L.S.S.V
                                    # .V.T.V.P.S.S.S.L.G.T.Q.T.Y.I.C.N.V.N.H.K.P.S.N.T.K.V.D.K.K.V.E.P.K.S.C.D.K.T.H.T.C
                                    # .P.P.C.P.A.P.E.L.L.G.G.P.S.V.F.L.F.P.P.K.P.K.D.T.L.M.I.S.R.T.P.E.V.T.C.V.V.V.D.V.S
                                    # .H.E.D.P.E.V.K.F.N.W.Y.V.D.G.V.E.V.H.N.A.K.T.K.P.R.E.E.Q.Y.N.S.T.Y.R.V.V.S.V.L.T.V
                                    # .L.H.Q.D.W.L.N.G.K.E.Y.K.C.K.V.S.N.K.A.L.P.A.P.I.E.K.T.I.S.K.A.K.G.Q.P.R.E.P.Q.V.Y
                                    # .T.L.P.P.S.R.D.E.L.T.K.N.Q.V.S.L.T.C.L.V.K.G.F.Y.P.S.D.I.A.V.E.W.E.S.N.G.Q.P.E.N.N
                                    # .Y.K.T.T.P.P.V.L.D.S.D.G.S.F.F.L.Y.S.K.L.T.V.D.K.S.R.W.Q.Q.G.N.V.F.S.C.S.V.M.H.E.A
                                    # .L.H.N.H.Y.T.Q.K.S.L.S.L.S.P.G.K}|PEPTIDE4{D.I.V.L.T.Q.S.P.A.T.L.S.L.S.P.G.E.R.A.T
                                    # .L.S.C.R.A.S.Q.S.V.S.S.S.Y.L.A.W.Y.Q.Q.K.P.G.Q.A.P.R.L.L.I.Y.G.A.S.S.R.A.T.G.V.P.A
                                    # .R.F.S.G.S.G.S.G.T.D.F.T.L.T.I.S.S.L.E.P.E.D.F.A.T.Y.Y.C.L.Q.I.Y.N.M.P.I.T.F.G.Q.G
                                    # .T.K.V.E.I.K.R.T.V.A.A.P.S.V.F.I.F.P.P.S.D.E.Q.L.K.S.G.T.A.S.V.V.C.L.L.N.N.F.Y.P.R
                                    # .E.A.K.V.Q.W.K.V.D.N.A.L.Q.S.G.N.S.Q.E.S.V.T.E.Q.D.S.K.D.S.T.Y.S.L.S.S.T.L.T.L.S.K
                                    # .A.D.Y.E.K.H.K.V.Y.A.C.E.V.T.H.Q.G.L.S.S.P.V.T.K.S.F.N.R.G.E.C}$PEPTIDE3,PEPTIDE4,
                                    # 229:R3-215:R3|PEPTIDE2,PEPTIDE2,270:R3-330:R3|PEPTIDE4,PEPTIDE4,135:R3-195:R3|PEPT
                                    # IDE3,PEPTIDE3,22:R3-96:R3|PEPTIDE3,PEPTIDE3,376:R3-434:R3|PEPTIDE1,PEPTIDE1,135:R3
                                    # -195:R3|PEPTIDE3,PEPTIDE3,153:R3-209:R3|PEPTIDE2,PEPTIDE2,22:R3-96:R3|PEPTIDE2,PEP
                                    # TIDE3,238:R3-238:R3|PEPTIDE2,PEPTIDE3,235:R3-235:R3|PEPTIDE1,PEPTIDE1,23:R3-89:R3|
                                    # PEPTIDE4,PEPTIDE4,23:R3-89:R3|PEPTIDE2,PEPTIDE2,376:R3-434:R3|PEPTIDE3,PEPTIDE3,27
                                    # 0:R3-330:R3|PEPTIDE2,PEPTIDE1,229:R3-215:R3|PEPTIDE2,PEPTIDE2,153:R3-209:R3$$$' , 
                                    # 'PEPTIDE1{D.I.V.M.T.Q.S.Q.R.F.M.S.T.T.V.G.D.R.V.S.I.T.C.K.A.S.Q.N.V.V.S.A.V.A.W.Y.
                                    # Q.Q.K.P.G.Q.S.P.K.L.L.I.Y.S.A.S.N.R.Y.T.G.V.P.D.R.F.T.G.S.G.S.G.T.D.F.T.L.T.I.S.N.
                                    # M.Q.S.E.D.L.A.D.F.F.C.Q.Q.Y.S.N.Y.P.W.T.F.G.G.G.T.K.L.E.I.K.R.T.V.A.A.P.S.V.F.I.F.
                                    # P.P.S.D.E.Q.L.K.S.G.T.A.S.V.V.C.L.L.N.N.F.Y.P.R.E.A.K.V.Q.W.K.V.D.N.A.L.Q.S.G.N.S.
                                    # Q.E.S.V.T.E.Q.D.S.K.D.S.T.Y.S.L.S.S.T.L.T.L.S.K.A.D.Y.E.K.H.K.V.Y.A.C.E.V.T.H.Q.G.
                                    # L.S.S.P.V.T.K.S.F.N.R.G.E.C}|PEPTIDE2{D.V.K.L.V.E.S.G.G.G.L.V.K.L.G.G.S.L.K.L.S.C.
                                    # A.A.S.G.F.T.F.S.N.Y.Y.M.S.W.V.R.Q.T.P.E.K.R.L.E.L.V.A.A.I.N.S.D.G.G.I.T.Y.Y.L.D.T.
                                    # V.K.G.R.F.T.I.S.R.D.N.A.K.N.T.L.Y.L.Q.M.S.S.L.K.S.E.D.T.A.L.F.Y.C.A.R.H.R.S.G.Y.F.
                                    # S.M.D.Y.W.G.Q.G.T.S.V.T.V.S.S.A.S.T.K.G.P.S.V.F.P.L.A.P.S.S.K.S.T.S.G.G.T.A.A.L.G.
                                    # C.L.V.K.D.Y.F.P.E.P.V.T.V.S.W.N.S.G.A.L.T.S.G.V.H.T.F.P.A.V.L.Q.S.S.G.L.Y.S.L.S.S.
                                    # V.V.T.V.P.S.S.S.L.G.T.Q.T.Y.I.C.N.V.N.H.K.P.S.N.T.K.V.D.K.K.V.E.P.K.S.C.D.K.T.H.T.
                                    # C.P.P.C.P.A.P.E.L.L.G.G.P.S.V.F.L.F.P.P.K.P.K.D.T.L.M.I.S.R.T.P.E.V.T.C.V.V.V.D.V.
                                    # S.H.E.D.P.E.V.K.F.N.W.Y.V.D.G.V.E.V.H.N.A.K.T.K.P.R.E.E.Q.Y.N.S.T.Y.R.V.V.S.V.L.T.
                                    # V.L.H.Q.D.W.L.N.G.K.E.Y.K.C.K.V.S.N.K.A.L.P.A.P.I.E.K.T.I.S.K.A.K.G.Q.P.R.E.P.Q.V.
                                    # Y.T.L.P.P.S.R.D.E.L.T.K.N.Q.V.S.L.T.C.L.V.K.G.F.Y.P.S.D.I.A.V.E.W.E.S.N.G.Q.P.E.N.
                                    # N.Y.K.T.T.P.P.V.L.D.S.D.G.S.F.F.L.Y.S.K.L.T.V.D.K.S.R.W.Q.Q.G.N.V.F.S.C.S.V.M.H.E.
                                    # A.L.H.N.H.Y.T.Q.K.S.L.S.L.S.P.G.K}|PEPTIDE3{D.V.K.L.V.E.S.G.G.G.L.V.K.L.G.G.S.L.K.
                                    # L.S.C.A.A.S.G.F.T.F.S.N.Y.Y.M.S.W.V.R.Q.T.P.E.K.R.L.E.L.V.A.A.I.N.S.D.G.G.I.T.Y.Y.
                                    # L.D.T.V.K.G.R.F.T.I.S.R.D.N.A.K.N.T.L.Y.L.Q.M.S.S.L.K.S.E.D.T.A.L.F.Y.C.A.R.H.R.S.
                                    # G.Y.F.S.M.D.Y.W.G.Q.G.T.S.V.T.V.S.S.A.S.T.K.G.P.S.V.F.P.L.A.P.S.S.K.S.T.S.G.G.T.A.
                                    # A.L.G.C.L.V.K.D.Y.F.P.E.P.V.T.V.S.W.N.S.G.A.L.T.S.G.V.H.T.F.P.A.V.L.Q.S.S.G.L.Y.S.
                                    # L.S.S.V.V.T.V.P.S.S.S.L.G.T.Q.T.Y.I.C.N.V.N.H.K.P.S.N.T.K.V.D.K.K.V.E.P.K.S.C.D.K.
                                    # T.H.T.C.P.P.C.P.A.P.E.L.L.G.G.P.S.V.F.L.F.P.P.K.P.K.D.T.L.M.I.S.R.T.P.E.V.T.C.V.V.
                                    # V.D.V.S.H.E.D.P.E.V.K.F.N.W.Y.V.D.G.V.E.V.H.N.A.K.T.K.P.R.E.E.Q.Y.N.S.T.Y.R.V.V.S.
                                    # V.L.T.V.L.H.Q.D.W.L.N.G.K.E.Y.K.C.K.V.S.N.K.A.L.P.A.P.I.E.K.T.I.S.K.A.K.G.Q.P.R.E.
                                    # P.Q.V.Y.T.L.P.P.S.R.D.E.L.T.K.N.Q.V.S.L.T.C.L.V.K.G.F.Y.P.S.D.I.A.V.E.W.E.S.N.G.Q.
                                    # P.E.N.N.Y.K.T.T.P.P.V.L.D.S.D.G.S.F.F.L.Y.S.K.L.T.V.D.K.S.R.W.Q.Q.G.N.V.F.S.C.S.V.
                                    # M.H.E.A.L.H.N.H.Y.T.Q.K.S.L.S.L.S.P.G.K}|PEPTIDE4{D.I.V.M.T.Q.S.Q.R.F.M.S.T.T.V.G.
                                    # D.R.V.S.I.T.C.K.A.S.Q.N.V.V.S.A.V.A.W.Y.Q.Q.K.P.G.Q.S.P.K.L.L.I.Y.S.A.S.N.R.Y.T.G.
                                    # V.P.D.R.F.T.G.S.G.S.G.T.D.F.T.L.T.I.S.N.M.Q.S.E.D.L.A.D.F.F.C.Q.Q.Y.S.N.Y.P.W.T.F.
                                    # G.G.G.T.K.L.E.I.K.R.T.V.A.A.P.S.V.F.I.F.P.P.S.D.E.Q.L.K.S.G.T.A.S.V.V.C.L.L.N.N.F.
                                    # Y.P.R.E.A.K.V.Q.W.K.V.D.N.A.L.Q.S.G.N.S.Q.E.S.V.T.E.Q.D.S.K.D.S.T.Y.S.L.S.S.T.L.T.
                                    # L.S.K.A.D.Y.E.K.H.K.V.Y.A.C.E.V.T.H.Q.G.L.S.S.P.V.T.K.S.F.N.R.G.E.C}$PEPTIDE3,PEPT
                                    # IDE4,222:R3-214:R3|PEPTIDE4,PEPTIDE4,134:R3-194:R3|PEPTIDE1,PEPTIDE1,134:R3-194:R3
                                    # |PEPTIDE3,PEPTIDE3,22:R3-96:R3|PEPTIDE2,PEPTIDE2,146:R3-202:R3|PEPTIDE2,PEPTIDE1,2
                                    # 22:R3-214:R3|PEPTIDE2,PEPTIDE2,369:R3-427:R3|PEPTIDE3,PEPTIDE3,263:R3-323:R3|PEPTI
                                    # DE2,PEPTIDE2,263:R3-323:R3|PEPTIDE4,PEPTIDE4,23:R3-88:R3|PEPTIDE1,PEPTIDE1,23:R3-8
                                    # 8:R3|PEPTIDE2,PEPTIDE3,231:R3-231:R3|PEPTIDE3,PEPTIDE3,369:R3-427:R3|PEPTIDE2,PEPT
                                    # IDE2,22:R3-96:R3|PEPTIDE3,PEPTIDE3,146:R3-202:R3|PEPTIDE2,PEPTIDE3,228:R3-228:R3$$
                                    # $' , 'PEPTIDE1{D.I.Q.M.T.Q.S.P.S.S.L.S.A.S.V.G.D.R.V.T.I.T.C.K.A.S.R.D.I.R.S.Y.L.T
                                    # .W.Y.Q.Q.K.P.G.K.A.P.K.T.L.I.Y.Y.A.T.S.L.A.D.G.V.P.S.R.F.S.G.S.G.S.G.Q.D.Y.S.L.T.I
                                    # .S.S.L.E.S.D.D.T.A.T.Y.Y.C.L.Q.H.G.E.S.P.F.T.L.G.S.G.T.K.L.E.I.K.R.T.V.A.A.P.S.V.F
                                    # .I.F.P.P.S.D.E.Q.L.K.S.G.T.A.S.V.V.C.L.L.N.N.F.Y.P.R.E.A.K.V.Q.W.K.V.D.N.A.L.Q.S.G
                                    # .N.S.Q.E.S.V.T.E.Q.D.S.K.D.S.T.Y.S.L.S.S.T.L.T.L.S.K.A.D.Y.E.K.H.K.V.Y.A.C.E.V.T.H
                                    # .Q.G.L.S.S.P.V.T.K.S.F.N.R.G.E.C}|PEPTIDE2{E.V.Q.L.V.E.S.G.G.G.L.V.K.P.G.G.S.L.K.L
                                    # .S.C.A.A.S.G.F.K.F.S.R.Y.A.M.S.W.V.R.Q.A.P.G.K.R.L.E.W.V.A.T.I.S.S.G.G.S.Y.I.Y.Y.P
                                    # .D.S.V.K.G.R.F.T.I.S.R.D.N.V.K.N.T.L.Y.L.Q.M.S.S.L.R.S.E.D.T.A.M.Y.Y.C.A.R.R.D.Y.D
                                    # .L.D.Y.F.D.S.W.G.Q.G.T.L.V.T.V.S.S.A.S.T.K.G.P.S.V.F.P.L.A.P.S.S.K.S.T.S.G.G.T.A.A
                                    # .L.G.C.L.V.K.D.Y.F.P.E.P.V.T.V.S.W.N.S.G.A.L.T.S.G.V.H.T.F.P.A.V.L.Q.S.S.G.L.Y.S.L
                                    # .S.S.V.V.T.V.P.S.S.S.L.G.T.Q.T.Y.I.C.N.V.N.H.K.P.S.N.T.K.V.D.K.K.V.E.P.K.S.C.D.K.T
                                    # .H.T.C.P.P.C.P.A.P.E.L.L.G.G.P.S.V.F.L.F.P.P.K.P.K.D.T.L.M.I.S.R.T.P.E.V.T.C.V.V.V
                                    # .D.V.S.H.E.D.P.E.V.K.F.N.W.Y.V.D.G.V.E.V.H.N.A.K.T.K.P.R.E.E.Q.Y.N.S.T.Y.R.V.V.S.V
                                    # .L.T.V.L.H.Q.D.W.L.N.G.K.E.Y.K.C.K.V.S.N.K.A.L.P.A.P.I.E.K.T.I.S.K.A.K.G.Q.P.R.E.P
                                    # .Q.V.Y.T.L.P.P.S.R.D.E.L.T.K.N.Q.V.S.L.T.C.L.V.K.G.F.Y.P.S.D.I.A.V.E.W.E.S.N.G.Q.P
                                    # .E.N.N.Y.K.T.T.P.P.V.L.D.S.D.G.S.F.F.L.Y.S.K.L.T.V.D.K.S.R.W.Q.Q.G.N.V.F.S.C.S.V.M
                                    # .H.E.A.L.H.N.H.Y.T.Q.K.S.L.S.L.S.P.G.K}|PEPTIDE3{E.V.Q.L.V.E.S.G.G.G.L.V.K.P.G.G.S
                                    # .L.K.L.S.C.A.A.S.G.F.K.F.S.R.Y.A.M.S.W.V.R.Q.A.P.G.K.R.L.E.W.V.A.T.I.S.S.G.G.S.Y.I
                                    # .Y.Y.P.D.S.V.K.G.R.F.T.I.S.R.D.N.V.K.N.T.L.Y.L.Q.M.S.S.L.R.S.E.D.T.A.M.Y.Y.C.A.R.R
                                    # .D.Y.D.L.D.Y.F.D.S.W.G.Q.G.T.L.V.T.V.S.S.A.S.T.K.G.P.S.V.F.P.L.A.P.S.S.K.S.T.S.G.G
                                    # .T.A.A.L.G.C.L.V.K.D.Y.F.P.E.P.V.T.V.S.W.N.S.G.A.L.T.S.G.V.H.T.F.P.A.V.L.Q.S.S.G.L
                                    # .Y.S.L.S.S.V.V.T.V.P.S.S.S.L.G.T.Q.T.Y.I.C.N.V.N.H.K.P.S.N.T.K.V.D.K.K.V.E.P.K.S.C
                                    # .D.K.T.H.T.C.P.P.C.P.A.P.E.L.L.G.G.P.S.V.F.L.F.P.P.K.P.K.D.T.L.M.I.S.R.T.P.E.V.T.C
                                    # .V.V.V.D.V.S.H.E.D.P.E.V.K.F.N.W.Y.V.D.G.V.E.V.H.N.A.K.T.K.P.R.E.E.Q.Y.N.S.T.Y.R.V
                                    # .V.S.V.L.T.V.L.H.Q.D.W.L.N.G.K.E.Y.K.C.K.V.S.N.K.A.L.P.A.P.I.E.K.T.I.S.K.A.K.G.Q.P
                                    # .R.E.P.Q.V.Y.T.L.P.P.S.R.D.E.L.T.K.N.Q.V.S.L.T.C.L.V.K.G.F.Y.P.S.D.I.A.V.E.W.E.S.N
                                    # .G.Q.P.E.N.N.Y.K.T.T.P.P.V.L.D.S.D.G.S.F.F.L.Y.S.K.L.T.V.D.K.S.R.W.Q.Q.G.N.V.F.S.C
                                    # .S.V.M.H.E.A.L.H.N.H.Y.T.Q.K.S.L.S.L.S.P.G.K}|PEPTIDE4{D.I.Q.M.T.Q.S.P.S.S.L.S.A.S
                                    # .V.G.D.R.V.T.I.T.C.K.A.S.R.D.I.R.S.Y.L.T.W.Y.Q.Q.K.P.G.K.A.P.K.T.L.I.Y.Y.A.T.S.L.A
                                    # .D.G.V.P.S.R.F.S.G.S.G.S.G.Q.D.Y.S.L.T.I.S.S.L.E.S.D.D.T.A.T.Y.Y.C.L.Q.H.G.E.S.P.F
                                    # .T.L.G.S.G.T.K.L.E.I.K.R.T.V.A.A.P.S.V.F.I.F.P.P.S.D.E.Q.L.K.S.G.T.A.S.V.V.C.L.L.N
                                    # .N.F.Y.P.R.E.A.K.V.Q.W.K.V.D.N.A.L.Q.S.G.N.S.Q.E.S.V.T.E.Q.D.S.K.D.S.T.Y.S.L.S.S.T
                                    # .L.T.L.S.K.A.D.Y.E.K.H.K.V.Y.A.C.E.V.T.H.Q.G.L.S.S.P.V.T.K.S.F.N.R.G.E.C}$PEPTIDE1
                                    # ,PEPTIDE1,23:R3-88:R3|PEPTIDE3,PEPTIDE4,222:R3-214:R3|PEPTIDE3,PEPTIDE3,22:R3-96:R
                                    # 3|PEPTIDE2,PEPTIDE2,263:R3-323:R3|PEPTIDE4,PEPTIDE4,134:R3-194:R3|PEPTIDE2,PEPTIDE
                                    # 1,222:R3-214:R3|PEPTIDE3,PEPTIDE3,263:R3-323:R3|PEPTIDE2,PEPTIDE2,146:R3-202:R3|PE
                                    # PTIDE2,PEPTIDE2,369:R3-427:R3|PEPTIDE3,PEPTIDE3,146:R3-202:R3|PEPTIDE3,PEPTIDE3,36
                                    # 9:R3-427:R3|PEPTIDE1,PEPTIDE1,134:R3-194:R3|PEPTIDE2,PEPTIDE2,22:R3-96:R3|PEPTIDE2
                                    # ,PEPTIDE3,228:R3-228:R3|PEPTIDE2,PEPTIDE3,231:R3-231:R3|PEPTIDE4,PEPTIDE4,23:R3-88
                                    # :R3$$$' , 'PEPTIDE1{S.S.E.L.T.Q.D.P.A.V.S.V.A.L.G.Q.T.V.R.I.T.C.Q.G.D.S.L.R.S.Y.Y.
                                    # A.S.W.Y.Q.Q.K.P.G.Q.A.P.V.L.V.I.Y.G.K.N.N.R.P.S.G.I.P.D.R.F.S.G.S.S.S.G.N.T.A.S.L.
                                    # T.I.T.G.A.Q.A.E.D.E.A.D.Y.Y.C.N.S.R.D.S.S.G.N.H.V.V.F.G.G.G.T.K.L.T.V.L.G.Q.P.K.A.
                                    # A.P.S.V.T.L.F.P.P.S.S.E.E.L.Q.A.N.K.A.T.L.V.C.L.I.S.D.F.Y.P.G.A.V.T.V.A.W.K.A.D.S.
                                    # S.P.V.K.A.G.V.E.T.T.T.P.S.K.Q.S.N.N.K.Y.A.A.S.S.Y.L.S.L.T.P.E.Q.W.K.S.H.R.S.Y.S.C.
                                    # Q.V.T.H.E.G.S.T.V.E.K.T.V.A.P.T.E.C.S}|PEPTIDE2{E.V.Q.L.V.Q.S.G.G.G.V.E.R.P.G.G.S.
                                    # L.R.L.S.C.A.A.S.G.F.T.F.D.D.Y.G.M.S.W.V.R.Q.A.P.G.K.G.L.E.W.V.S.G.I.N.W.N.G.G.S.T.
                                    # G.Y.A.D.S.V.K.G.R.V.T.I.S.R.D.N.A.K.N.S.L.Y.L.Q.M.N.S.L.R.A.E.D.T.A.V.Y.Y.C.A.K.I.
                                    # L.G.A.G.R.G.W.Y.F.D.L.W.G.K.G.T.T.V.T.V.S.S.A.S.T.K.G.P.S.V.F.P.L.A.P.S.S.K.S.T.S.
                                    # G.G.T.A.A.L.G.C.L.V.K.D.Y.F.P.E.P.V.T.V.S.W.N.S.G.A.L.T.S.G.V.H.T.F.P.A.V.L.Q.S.S.
                                    # G.L.Y.S.L.S.S.V.V.T.V.P.S.S.S.L.G.T.Q.T.Y.I.C.N.V.N.H.K.P.S.N.T.K.V.D.K.R.V.E.P.K.
                                    # S.C.D.K.T.H.T.C.P.P.C.P.A.P.E.L.L.G.G.P.S.V.F.L.F.P.P.K.P.K.D.T.L.M.I.S.R.T.P.E.V.
                                    # T.C.V.V.V.D.V.S.H.E.D.P.E.V.K.F.N.W.Y.V.D.G.V.E.V.H.N.A.K.T.K.P.R.E.E.Q.Y.N.S.T.Y.
                                    # R.V.V.S.V.L.T.V.L.H.Q.D.W.L.N.G.K.E.Y.K.C.K.V.S.N.K.A.L.P.A.P.I.E.K.T.I.S.K.A.K.G.
                                    # Q.P.R.E.P.Q.V.Y.T.L.P.P.S.R.E.E.M.T.K.N.Q.V.S.L.T.C.L.V.K.G.F.Y.P.S.D.I.A.V.E.W.E.
                                    # S.N.G.Q.P.E.N.N.Y.K.T.T.P.P.V.L.D.S.D.G.S.F.F.L.Y.S.K.L.T.V.D.K.S.R.W.Q.Q.G.N.V.F.
                                    # S.C.S.V.M.H.E.A.L.H.N.H.Y.T.Q.K.S.L.S.L.S.P.G.K}|PEPTIDE3{E.V.Q.L.V.Q.S.G.G.G.V.E.
                                    # R.P.G.G.S.L.R.L.S.C.A.A.S.G.F.T.F.D.D.Y.G.M.S.W.V.R.Q.A.P.G.K.G.L.E.W.V.S.G.I.N.W.
                                    # N.G.G.S.T.G.Y.A.D.S.V.K.G.R.V.T.I.S.R.D.N.A.K.N.S.L.Y.L.Q.M.N.S.L.R.A.E.D.T.A.V.Y.
                                    # Y.C.A.K.I.L.G.A.G.R.G.W.Y.F.D.L.W.G.K.G.T.T.V.T.V.S.S.A.S.T.K.G.P.S.V.F.P.L.A.P.S.
                                    # S.K.S.T.S.G.G.T.A.A.L.G.C.L.V.K.D.Y.F.P.E.P.V.T.V.S.W.N.S.G.A.L.T.S.G.V.H.T.F.P.A.
                                    # V.L.Q.S.S.G.L.Y.S.L.S.S.V.V.T.V.P.S.S.S.L.G.T.Q.T.Y.I.C.N.V.N.H.K.P.S.N.T.K.V.D.K.
                                    # R.V.E.P.K.S.C.D.K.T.H.T.C.P.P.C.P.A.P.E.L.L.G.G.P.S.V.F.L.F.P.P.K.P.K.D.T.L.M.I.S.
                                    # R.T.P.E.V.T.C.V.V.V.D.V.S.H.E.D.P.E.V.K.F.N.W.Y.V.D.G.V.E.V.H.N.A.K.T.K.P.R.E.E.Q.
                                    # Y.N.S.T.Y.R.V.V.S.V.L.T.V.L.H.Q.D.W.L.N.G.K.E.Y.K.C.K.V.S.N.K.A.L.P.A.P.I.E.K.T.I.
                                    # S.K.A.K.G.Q.P.R.E.P.Q.V.Y.T.L.P.P.S.R.E.E.M.T.K.N.Q.V.S.L.T.C.L.V.K.G.F.Y.P.S.D.I.
                                    # A.V.E.W.E.S.N.G.Q.P.E.N.N.Y.K.T.T.P.P.V.L.D.S.D.G.S.F.F.L.Y.S.K.L.T.V.D.K.S.R.W.Q.
                                    # Q.G.N.V.F.S.C.S.V.M.H.E.A.L.H.N.H.Y.T.Q.K.S.L.S.L.S.P.G.K}|PEPTIDE4{S.S.E.L.T.Q.D.
                                    # P.A.V.S.V.A.L.G.Q.T.V.R.I.T.C.Q.G.D.S.L.R.S.Y.Y.A.S.W.Y.Q.Q.K.P.G.Q.A.P.V.L.V.I.Y.
                                    # G.K.N.N.R.P.S.G.I.P.D.R.F.S.G.S.S.S.G.N.T.A.S.L.T.I.T.G.A.Q.A.E.D.E.A.D.Y.Y.C.N.S.
                                    # R.D.S.S.G.N.H.V.V.F.G.G.G.T.K.L.T.V.L.G.Q.P.K.A.A.P.S.V.T.L.F.P.P.S.S.E.E.L.Q.A.N.
                                    # K.A.T.L.V.C.L.I.S.D.F.Y.P.G.A.V.T.V.A.W.K.A.D.S.S.P.V.K.A.G.V.E.T.T.T.P.S.K.Q.S.N.
                                    # N.K.Y.A.A.S.S.Y.L.S.L.T.P.E.Q.W.K.S.H.R.S.Y.S.C.Q.V.T.H.E.G.S.T.V.E.K.T.V.A.P.T.E.
                                    # C.S}$PEPTIDE4,PEPTIDE4,22:R3-87:R3|PEPTIDE3,PEPTIDE3,148:R3-204:R3|PEPTIDE2,PEPTID
                                    # E3,230:R3-230:R3|PEPTIDE2,PEPTIDE2,148:R3-204:R3|PEPTIDE4,PEPTIDE4,136:R3-195:R3|P
                                    # EPTIDE3,PEPTIDE4,224:R3-213:R3|PEPTIDE2,PEPTIDE2,22:R3-96:R3|PEPTIDE1,PEPTIDE1,22:
                                    # R3-87:R3|PEPTIDE3,PEPTIDE3,265:R3-325:R3|PEPTIDE2,PEPTIDE1,224:R3-213:R3|PEPTIDE3,
                                    # PEPTIDE3,22:R3-96:R3|PEPTIDE2,PEPTIDE2,371:R3-429:R3|PEPTIDE1,PEPTIDE1,136:R3-195:
                                    # R3|PEPTIDE2,PEPTIDE2,265:R3-325:R3|PEPTIDE3,PEPTIDE3,371:R3-429:R3|PEPTIDE2,PEPTID
                                    # E3,233:R3-233:R3$$$' , 'PEPTIDE1{D.V.L.M.T.Q.S.P.L.S.L.P.V.T.P.G.E.P.A.S.I.S.C.R.S
                                    # .S.R.N.I.V.H.I.N.G.D.T.Y.L.E.W.Y.L.Q.K.P.G.Q.S.P.Q.L.L.I.Y.K.V.S.N.R.F.S.G.V.P.D.R
                                    # .F.S.G.S.G.S.G.T.D.F.T.L.K.I.S.R.V.E.A.E.D.V.G.V.Y.Y.C.F.Q.G.S.L.L.P.W.T.F.G.Q.G.T
                                    # .K.V.E.I.K.R.T.V.A.A.P.S.V.F.I.F.P.P.S.D.E.Q.L.K.S.G.T.A.S.V.V.C.L.L.N.N.F.Y.P.R.E
                                    # .A.K.V.Q.W.K.V.D.N.A.L.Q.S.G.N.S.Q.E.S.V.T.E.Q.D.S.K.D.S.T.Y.S.L.S.S.T.L.T.L.S.K.A
                                    # .D.Y.E.K.H.K.V.Y.A.C.E.V.T.H.Q.G.L.S.S.P.V.T.K.S.F.N.R.G.E.C}|PEPTIDE2{E.V.Q.L.V.E
                                    # .S.G.G.D.L.V.Q.P.G.R.S.L.R.L.S.C.A.A.S.G.F.I.F.S.N.Y.G.M.S.W.V.R.Q.A.P.G.K.G.L.E.W
                                    # .V.A.T.I.S.S.A.S.T.Y.S.Y.Y.P.D.S.V.K.G.R.F.T.I.S.R.D.N.A.K.N.S.L.Y.L.Q.M.N.S.L.R.V
                                    # .E.D.T.A.L.Y.Y.C.G.R.H.S.D.G.N.F.A.F.G.Y.W.G.Q.G.T.L.V.T.V.S.S.A.S.T.K.G.P.S.V.F.P
                                    # .L.A.P.S.S.K.S.T.S.G.G.T.A.A.L.G.C.L.V.K.D.Y.F.P.E.P.V.T.V.S.W.N.S.G.A.L.T.S.G.V.H
                                    # .T.F.P.A.V.L.Q.S.S.G.L.Y.S.L.S.S.V.V.T.V.P.S.S.S.L.G.T.Q.T.Y.I.C.N.V.N.H.K.P.S.N.T
                                    # .K.V.D.K.K.V.E.P.K.S.C.D.K.T.H.T.C.P.P.C.P.A.P.E.L.L.G.G.P.S.V.F.L.F.P.P.K.P.K.D.T
                                    # .L.M.I.S.R.T.P.E.V.T.C.V.V.V.D.V.S.H.E.D.P.E.V.K.F.N.W.Y.V.D.G.V.E.V.H.N.A.K.T.K.P
                                    # .R.E.E.Q.Y.N.S.T.Y.R.V.V.S.V.L.T.V.L.H.Q.D.W.L.N.G.K.E.Y.K.C.K.V.S.N.K.A.L.P.A.P.I
                                    # .E.K.T.I.S.K.A.K.G.Q.P.R.E.P.Q.V.Y.T.L.P.P.S.R.D.E.L.T.K.N.Q.V.S.L.T.C.L.V.K.G.F.Y
                                    # .P.S.D.I.A.V.E.W.E.S.N.G.Q.P.E.N.N.Y.K.T.T.P.P.V.L.D.S.D.G.S.F.F.L.Y.S.K.L.T.V.D.K
                                    # .S.R.W.Q.Q.G.N.V.F.S.C.S.V.M.H.E.A.L.H.N.H.Y.T.Q.K.S.L.S.L.S.P.G.K}|PEPTIDE3{E.V.Q
                                    # .L.V.E.S.G.G.D.L.V.Q.P.G.R.S.L.R.L.S.C.A.A.S.G.F.I.F.S.N.Y.G.M.S.W.V.R.Q.A.P.G.K.G
                                    # .L.E.W.V.A.T.I.S.S.A.S.T.Y.S.Y.Y.P.D.S.V.K.G.R.F.T.I.S.R.D.N.A.K.N.S.L.Y.L.Q.M.N.S
                                    # .L.R.V.E.D.T.A.L.Y.Y.C.G.R.H.S.D.G.N.F.A.F.G.Y.W.G.Q.G.T.L.V.T.V.S.S.A.S.T.K.G.P.S
                                    # .V.F.P.L.A.P.S.S.K.S.T.S.G.G.T.A.A.L.G.C.L.V.K.D.Y.F.P.E.P.V.T.V.S.W.N.S.G.A.L.T.S
                                    # .G.V.H.T.F.P.A.V.L.Q.S.S.G.L.Y.S.L.S.S.V.V.T.V.P.S.S.S.L.G.T.Q.T.Y.I.C.N.V.N.H.K.P
                                    # .S.N.T.K.V.D.K.K.V.E.P.K.S.C.D.K.T.H.T.C.P.P.C.P.A.P.E.L.L.G.G.P.S.V.F.L.F.P.P.K.P
                                    # .K.D.T.L.M.I.S.R.T.P.E.V.T.C.V.V.V.D.V.S.H.E.D.P.E.V.K.F.N.W.Y.V.D.G.V.E.V.H.N.A.K
                                    # .T.K.P.R.E.E.Q.Y.N.S.T.Y.R.V.V.S.V.L.T.V.L.H.Q.D.W.L.N.G.K.E.Y.K.C.K.V.S.N.K.A.L.P
                                    # .A.P.I.E.K.T.I.S.K.A.K.G.Q.P.R.E.P.Q.V.Y.T.L.P.P.S.R.D.E.L.T.K.N.Q.V.S.L.T.C.L.V.K
                                    # .G.F.Y.P.S.D.I.A.V.E.W.E.S.N.G.Q.P.E.N.N.Y.K.T.T.P.P.V.L.D.S.D.G.S.F.F.L.Y.S.K.L.T
                                    # .V.D.K.S.R.W.Q.Q.G.N.V.F.S.C.S.V.M.H.E.A.L.H.N.H.Y.T.Q.K.S.L.S.L.S.P.G.K}|PEPTIDE4
                                    # {D.V.L.M.T.Q.S.P.L.S.L.P.V.T.P.G.E.P.A.S.I.S.C.R.S.S.R.N.I.V.H.I.N.G.D.T.Y.L.E.W.Y
                                    # .L.Q.K.P.G.Q.S.P.Q.L.L.I.Y.K.V.S.N.R.F.S.G.V.P.D.R.F.S.G.S.G.S.G.T.D.F.T.L.K.I.S.R
                                    # .V.E.A.E.D.V.G.V.Y.Y.C.F.Q.G.S.L.L.P.W.T.F.G.Q.G.T.K.V.E.I.K.R.T.V.A.A.P.S.V.F.I.F
                                    # .P.P.S.D.E.Q.L.K.S.G.T.A.S.V.V.C.L.L.N.N.F.Y.P.R.E.A.K.V.Q.W.K.V.D.N.A.L.Q.S.G.N.S
                                    # .Q.E.S.V.T.E.Q.D.S.K.D.S.T.Y.S.L.S.S.T.L.T.L.S.K.A.D.Y.E.K.H.K.V.Y.A.C.E.V.T.H.Q.G
                                    # .L.S.S.P.V.T.K.S.F.N.R.G.E.C}$PEPTIDE2,PEPTIDE2,146:R3-202:R3|PEPTIDE3,PEPTIDE3,26
                                    # 3:R3-323:R3|PEPTIDE2,PEPTIDE2,263:R3-323:R3|PEPTIDE3,PEPTIDE3,22:R3-96:R3|PEPTIDE2
                                    # ,PEPTIDE3,231:R3-231:R3|PEPTIDE2,PEPTIDE1,222:R3-219:R3|PEPTIDE4,PEPTIDE4,23:R3-93
                                    # :R3|PEPTIDE2,PEPTIDE2,22:R3-96:R3|PEPTIDE4,PEPTIDE4,139:R3-199:R3|PEPTIDE1,PEPTIDE
                                    # 1,139:R3-199:R3|PEPTIDE3,PEPTIDE3,146:R3-202:R3|PEPTIDE3,PEPTIDE4,222:R3-219:R3|PE
                                    # PTIDE2,PEPTIDE2,369:R3-427:R3|PEPTIDE3,PEPTIDE3,369:R3-427:R3|PEPTIDE1,PEPTIDE1,23
                                    # :R3-93:R3|PEPTIDE2,PEPTIDE3,228:R3-228:R3$$$' , 'PEPTIDE1{D.I.Q.M.T.Q.S.P.S.S.V.S.
                                    # A.S.V.G.D.R.V.T.I.A.C.R.A.S.Q.N.I.R.N.I.L.N.W.Y.Q.Q.R.P.G.K.A.P.Q.L.L.I.Y.A.A.S.N.
                                    # L.Q.S.G.V.P.S.R.F.S.G.S.G.S.G.T.D.F.T.L.T.I.N.S.L.Q.P.E.D.F.A.T.Y.Y.C.Q.Q.S.Y.S.M.
                                    # P.R.T.F.G.G.G.T.K.L.E.I.K.R.T.V.A.A.P.S.V.F.I.F.P.P.S.D.E.Q.L.K.S.G.T.A.S.V.V.C.L.
                                    # L.N.N.F.Y.P.R.E.A.K.V.Q.W.K.V.D.N.A.L.Q.S.G.N.S.Q.E.S.V.T.E.Q.D.S.K.D.S.T.Y.S.L.S.
                                    # S.T.L.T.L.S.K.A.D.Y.E.K.H.K.V.Y.A.C.E.V.T.H.Q.G.L.S.S.P.V.T.K.S.F.N.R.G.E.C}|PEPTI
                                    # DE2{Q.V.Q.L.V.Q.S.G.A.E.V.K.K.P.G.A.S.V.K.V.S.C.K.A.F.G.Y.P.F.T.D.Y.L.L.H.W.V.R.Q.
                                    # A.P.G.Q.G.L.E.W.V.G.W.L.N.P.Y.S.G.D.T.N.Y.A.Q.K.F.Q.G.R.V.T.M.T.R.D.T.S.I.S.T.A.Y.
                                    # M.E.L.S.R.L.R.S.D.D.T.A.V.Y.Y.C.T.R.T.T.L.I.S.V.Y.F.D.Y.W.G.Q.G.T.M.V.T.V.S.S.A.S.
                                    # T.K.G.P.S.V.F.P.L.A.P.S.S.K.S.T.S.G.G.T.A.A.L.G.C.L.V.K.D.Y.F.P.E.P.V.T.V.S.W.N.S.
                                    # G.A.L.T.S.G.V.H.T.F.P.A.V.L.Q.S.S.G.L.Y.S.L.S.S.V.V.T.V.P.S.S.S.L.G.T.Q.T.Y.I.C.N.
                                    # V.N.H.K.P.S.N.T.K.V.D.K.K.V.E.P.K.S.C.D.K.T.H.T.C.P.P.C.P.A.P.E.L.L.G.G.P.S.V.F.L.
                                    # F.P.P.K.P.K.D.T.L.M.I.S.R.T.P.E.V.T.C.V.V.V.D.V.S.H.E.D.P.E.V.K.F.N.W.Y.V.D.G.V.E.
                                    # V.H.N.A.K.T.K.P.R.E.E.Q.Y.N.S.T.Y.R.V.V.S.V.L.T.V.L.H.Q.D.W.L.N.G.K.E.Y.K.C.K.V.S.
                                    # N.K.A.L.P.A.P.I.E.K.T.I.S.K.A.K.G.Q.P.R.E.P.Q.V.Y.T.L.P.P.S.R.D.E.L.T.K.N.Q.V.S.L.
                                    # T.C.L.V.K.G.F.Y.P.S.D.I.A.V.E.W.E.S.N.G.Q.P.E.N.N.Y.K.T.T.P.P.V.L.D.S.D.G.S.F.F.L.
                                    # Y.S.K.L.T.V.D.K.S.R.W.Q.Q.G.N.V.F.S.C.S.V.M.H.E.A.L.H.N.H.Y.T.Q.K.S.L.S.L.S.P.G.K}
                                    # |PEPTIDE3{Q.V.Q.L.V.Q.S.G.A.E.V.K.K.P.G.A.S.V.K.V.S.C.K.A.F.G.Y.P.F.T.D.Y.L.L.H.W.
                                    # V.R.Q.A.P.G.Q.G.L.E.W.V.G.W.L.N.P.Y.S.G.D.T.N.Y.A.Q.K.F.Q.G.R.V.T.M.T.R.D.T.S.I.S.
                                    # T.A.Y.M.E.L.S.R.L.R.S.D.D.T.A.V.Y.Y.C.T.R.T.T.L.I.S.V.Y.F.D.Y.W.G.Q.G.T.M.V.T.V.S.
                                    # S.A.S.T.K.G.P.S.V.F.P.L.A.P.S.S.K.S.T.S.G.G.T.A.A.L.G.C.L.V.K.D.Y.F.P.E.P.V.T.V.S.
                                    # W.N.S.G.A.L.T.S.G.V.H.T.F.P.A.V.L.Q.S.S.G.L.Y.S.L.S.S.V.V.T.V.P.S.S.S.L.G.T.Q.T.Y.
                                    # I.C.N.V.N.H.K.P.S.N.T.K.V.D.K.K.V.E.P.K.S.C.D.K.T.H.T.C.P.P.C.P.A.P.E.L.L.G.G.P.S.
                                    # V.F.L.F.P.P.K.P.K.D.T.L.M.I.S.R.T.P.E.V.T.C.V.V.V.D.V.S.H.E.D.P.E.V.K.F.N.W.Y.V.D.
                                    # G.V.E.V.H.N.A.K.T.K.P.R.E.E.Q.Y.N.S.T.Y.R.V.V.S.V.L.T.V.L.H.Q.D.W.L.N.G.K.E.Y.K.C.
                                    # K.V.S.N.K.A.L.P.A.P.I.E.K.T.I.S.K.A.K.G.Q.P.R.E.P.Q.V.Y.T.L.P.P.S.R.D.E.L.T.K.N.Q.
                                    # V.S.L.T.C.L.V.K.G.F.Y.P.S.D.I.A.V.E.W.E.S.N.G.Q.P.E.N.N.Y.K.T.T.P.P.V.L.D.S.D.G.S.
                                    # F.F.L.Y.S.K.L.T.V.D.K.S.R.W.Q.Q.G.N.V.F.S.C.S.V.M.H.E.A.L.H.N.H.Y.T.Q.K.S.L.S.L.S.
                                    # P.G.K}|PEPTIDE4{D.I.Q.M.T.Q.S.P.S.S.V.S.A.S.V.G.D.R.V.T.I.A.C.R.A.S.Q.N.I.R.N.I.L.
                                    # N.W.Y.Q.Q.R.P.G.K.A.P.Q.L.L.I.Y.A.A.S.N.L.Q.S.G.V.P.S.R.F.S.G.S.G.S.G.T.D.F.T.L.T.
                                    # I.N.S.L.Q.P.E.D.F.A.T.Y.Y.C.Q.Q.S.Y.S.M.P.R.T.F.G.G.G.T.K.L.E.I.K.R.T.V.A.A.P.S.V.
                                    # F.I.F.P.P.S.D.E.Q.L.K.S.G.T.A.S.V.V.C.L.L.N.N.F.Y.P.R.E.A.K.V.Q.W.K.V.D.N.A.L.Q.S.
                                    # G.N.S.Q.E.S.V.T.E.Q.D.S.K.D.S.T.Y.S.L.S.S.T.L.T.L.S.K.A.D.Y.E.K.H.K.V.Y.A.C.E.V.T.
                                    # H.Q.G.L.S.S.P.V.T.K.S.F.N.R.G.E.C}$PEPTIDE3,PEPTIDE4,222:R3-214:R3|PEPTIDE1,PEPTID
                                    # E1,134:R3-194:R3|PEPTIDE2,PEPTIDE3,231:R3-231:R3|PEPTIDE4,PEPTIDE4,23:R3-88:R3|PEP
                                    # TIDE3,PEPTIDE3,369:R3-427:R3|PEPTIDE2,PEPTIDE2,369:R3-427:R3|PEPTIDE1,PEPTIDE1,23:
                                    # R3-88:R3|PEPTIDE2,PEPTIDE2,146:R3-202:R3|PEPTIDE4,PEPTIDE4,134:R3-194:R3|PEPTIDE2,
                                    # PEPTIDE2,22:R3-96:R3|PEPTIDE3,PEPTIDE3,263:R3-323:R3|PEPTIDE3,PEPTIDE3,22:R3-96:R3
                                    # |PEPTIDE2,PEPTIDE1,222:R3-214:R3|PEPTIDE3,PEPTIDE3,146:R3-202:R3|PEPTIDE2,PEPTIDE3
                                    # ,228:R3-228:R3|PEPTIDE2,PEPTIDE2,263:R3-323:R3$$$'
                                    'indication_class': 'TEXT',
                                    # EXAMPLES:
                                    # 'Regulator (calcium)' , 'Anti-Inflammatory' , 'Analgesic; Anti-Inflammatory' , 'An
                                    # ti-Inflammatory; Antipyretic; Analgesic' , 'Antineoplastic' , 'Tranquilizer' , 'An
                                    # ti-Urolithic (cystine calculi)' , 'Antihyperlipoproteinemic' , 'Vitamin' , 'Antihy
                                    # pertensive (beta-blocker, ophthalmic)'
                                    'molecule_chembl_id': 'TEXT',
                                    # EXAMPLES:
                                    # 'CHEMBL1593566' , 'CHEMBL1590076' , 'CHEMBL1518149' , 'CHEMBL1569545' , 'CHEMBL156
                                    # 77' , 'CHEMBL276520' , 'CHEMBL15870' , 'CHEMBL38700' , 'CHEMBL12610' , 'CHEMBL2432
                                    # 9'
                                    'molecule_properties': 
                                    {
                                        'properties': 
                                        {
                                            'alogp': 'NUMERIC',
                                            # EXAMPLES:
                                            # '6.49' , '5.70' , '4.02' , '2.24' , '4.41' , '3.10' , '3.04' , '-0.59' , '
                                            # 3.42' , '0.87'
                                            'aromatic_rings': 'NUMERIC',
                                            # EXAMPLES:
                                            # '2' , '0' , '3' , '3' , '2' , '2' , '2' , '1' , '3' , '3'
                                            'cx_logd': 'NUMERIC',
                                            # EXAMPLES:
                                            # '5.74' , '4.58' , '3.70' , '-0.71' , '0.96' , '0.29' , '-0.43' , '-0.81' ,
                                            #  '1.81' , '-1.91'
                                            'cx_logp': 'NUMERIC',
                                            # EXAMPLES:
                                            # '5.74' , '4.58' , '4.76' , '2.60' , '4.32' , '3.07' , '2.86' , '-0.81' , '
                                            # 3.66' , '0.34'
                                            'cx_most_apka': 'NUMERIC',
                                            # EXAMPLES:
                                            # '10.65' , '13.85' , '3.68' , '3.55' , '3.74' , '9.10' , '13.50' , '4.16' ,
                                            #  '9.42' , '3.83'
                                            'cx_most_bpka': 'NUMERIC',
                                            # EXAMPLES:
                                            # '8.42' , '10.36' , '9.26' , '9.63' , '6.83' , '6.54' , '10.40' , '9.67' , 
                                            # '7.84' , '10.31'
                                            'full_molformula': 'TEXT',
                                            # EXAMPLES:
                                            # 'C22H19Br2NO3' , 'C27H44O3' , 'C22H26N2O2' , 'C15H11NO3' , 'C14H10Cl2O3' ,
                                            #  'C15H20N2' , 'C17H15NO3' , 'C9H10FN3O3' , 'C19H23N3O' , 'C21H25N5O4'
                                            'full_mwt': 'NUMERIC',
                                            # EXAMPLES:
                                            # '505.21' , '416.65' , '350.46' , '253.26' , '297.14' , '228.34' , '281.31'
                                            #  , '227.19' , '309.41' , '411.46'
                                            'hba': 'NUMERIC',
                                            # EXAMPLES:
                                            # '4' , '3' , '4' , '3' , '2' , '1' , '2' , '6' , '4' , '9'
                                            'hba_lipinski': 'NUMERIC',
                                            # EXAMPLES:
                                            # '4' , '3' , '4' , '4' , '3' , '2' , '4' , '6' , '4' , '9'
                                            'hbd': 'NUMERIC',
                                            # EXAMPLES:
                                            # '0' , '3' , '0' , '1' , '1' , '2' , '1' , '2' , '0' , '6'
                                            'hbd_lipinski': 'NUMERIC',
                                            # EXAMPLES:
                                            # '0' , '3' , '0' , '1' , '1' , '2' , '1' , '3' , '0' , '6'
                                            'heavy_atoms': 'NUMERIC',
                                            # EXAMPLES:
                                            # '28' , '30' , '26' , '19' , '19' , '17' , '21' , '16' , '23' , '30'
                                            'molecular_species': 'TEXT',
                                            # EXAMPLES:
                                            # 'NEUTRAL' , 'NEUTRAL' , 'NEUTRAL' , 'ACID' , 'ACID' , 'BASE' , 'ACID' , 'N
                                            # EUTRAL' , 'BASE' , 'BASE'
                                            'mw_freebase': 'NUMERIC',
                                            # EXAMPLES:
                                            # '505.21' , '416.65' , '350.46' , '253.26' , '297.14' , '228.34' , '281.31'
                                            #  , '227.19' , '309.41' , '411.46'
                                            'mw_monoisotopic': 'NUMERIC',
                                            # EXAMPLES:
                                            # '502.9732' , '416.3290' , '350.1994' , '253.0739' , '296.0007' , '228.1626
                                            # ' , '281.1052' , '227.0706' , '309.1841' , '411.1907'
                                            'num_lipinski_ro5_violations': 'NUMERIC',
                                            # EXAMPLES:
                                            # '2' , '1' , '0' , '0' , '0' , '0' , '0' , '0' , '0' , '1'
                                            'num_ro5_violations': 'NUMERIC',
                                            # EXAMPLES:
                                            # '2' , '1' , '0' , '0' , '0' , '0' , '0' , '0' , '0' , '1'
                                            'psa': 'NUMERIC',
                                            # EXAMPLES:
                                            # '59.32' , '60.69' , '34.47' , '59.30' , '46.53' , '27.82' , '57.61' , '90.
                                            # 37' , '30.29' , '131.67'
                                            'qed_weighted': 'NUMERIC',
                                            # EXAMPLES:
                                            # '0.42' , '0.52' , '0.63' , '0.71' , '0.91' , '0.83' , '0.94' , '0.66' , '0
                                            # .63' , '0.18'
                                            'ro3_pass': 'TEXT',
                                            # EXAMPLES:
                                            # 'N' , 'N' , 'N' , 'Y' , 'N' , 'N' , 'N' , 'N' , 'N' , 'N'
                                            'rtb': 'NUMERIC',
                                            # EXAMPLES:
                                            # '6' , '6' , '6' , '2' , '4' , '3' , '3' , '2' , '7' , '9'
                                        }
                                    },
                                    'molecule_structures': 
                                    {
                                        'properties': 
                                        {
                                            'canonical_smiles': 'TEXT',
                                            # EXAMPLES:
                                            # 'CC1(C)[C@@H](C=C(Br)Br)[C@H]1C(=O)O[C@H](C#N)c1cccc(Oc2ccccc2)c1' , 'C=C1
                                            # CC[C@H](O)C/C1=C/C=C1\CCC[C@@]2(C)[C@H]1CC[C@@H]2[C@H](C)CC[C@@H](O)C(C)(C
                                            # )O' , 'Cc1c(C)n(Cc2ccccc2)c2ccc(C(=O)OCCN(C)C)cc12' , 'O=C(O)Cn1c2ccccc2c(
                                            # =O)c2ccccc21' , 'O=C(O)Cc1ccccc1Oc1ccc(Cl)cc1Cl' , 'c1ccc2c(CCC3CCNCC3)c[n
                                            # H]c2c1' , 'CC(C(=O)O)c1ccc(N2Cc3ccccc3C2=O)cc1' , 'Nc1nc(=O)n([C@@H]2C=C[C
                                            # @H](CO)O2)cc1F' , 'CN(C)CCCOc1nn(Cc2ccccc2)c2ccccc12' , 'CNCCNc1ccc2c3c(nn
                                            # 2CCNCCO)-c2c(O)ccc(O)c2C(=O)c13'
                                            'standard_inchi': 'TEXT',
                                            # EXAMPLES:
                                            # 'InChI=1S/C22H19Br2NO3/c1-22(2)17(12-19(23)24)20(22)21(26)28-18(13-25)14-7
                                            # -6-10-16(11-14)27-15-8-4-3-5-9-15/h3-12,17-18,20H,1-2H3/t17-,18+,20-/m0/s1
                                            # ' , 'InChI=1S/C27H44O3/c1-18-8-12-22(28)17-21(18)11-10-20-7-6-16-27(5)23(1
                                            # 3-14-24(20)27)19(2)9-15-25(29)26(3,4)30/h10-11,19,22-25,28-30H,1,6-9,12-17
                                            # H2,2-5H3/b20-10+,21-11-/t19-,22+,23-,24+,25-,27-/m1/s1' , 'InChI=1S/C22H26
                                            # N2O2/c1-16-17(2)24(15-18-8-6-5-7-9-18)21-11-10-19(14-20(16)21)22(25)26-13-
                                            # 12-23(3)4/h5-11,14H,12-13,15H2,1-4H3' , 'InChI=1S/C15H11NO3/c17-14(18)9-16
                                            # -12-7-3-1-5-10(12)15(19)11-6-2-4-8-13(11)16/h1-8H,9H2,(H,17,18)' , 'InChI=
                                            # 1S/C14H10Cl2O3/c15-10-5-6-13(11(16)8-10)19-12-4-2-1-3-9(12)7-14(17)18/h1-6
                                            # ,8H,7H2,(H,17,18)' , 'InChI=1S/C15H20N2/c1-2-4-15-14(3-1)13(11-17-15)6-5-1
                                            # 2-7-9-16-10-8-12/h1-4,11-12,16-17H,5-10H2' , 'InChI=1S/C17H15NO3/c1-11(17(
                                            # 20)21)12-6-8-14(9-7-12)18-10-13-4-2-3-5-15(13)16(18)19/h2-9,11H,10H2,1H3,(
                                            # H,20,21)' , 'InChI=1S/C9H10FN3O3/c10-6-3-13(9(15)12-8(6)11)7-2-1-5(4-14)16
                                            # -7/h1-3,5,7,14H,4H2,(H2,11,12,15)/t5-,7+/m1/s1' , 'InChI=1S/C19H23N3O/c1-2
                                            # 1(2)13-8-14-23-19-17-11-6-7-12-18(17)22(20-19)15-16-9-4-3-5-10-16/h3-7,9-1
                                            # 2H,8,13-15H2,1-2H3' , 'InChI=1S/C21H25N5O4/c1-22-6-7-24-12-2-3-13-17-16(12
                                            # )21(30)19-15(29)5-4-14(28)18(19)20(17)25-26(13)10-8-23-9-11-27/h2-5,22-24,
                                            # 27-29H,6-11H2,1H3'
                                            'standard_inchi_key': 'TEXT',
                                            # EXAMPLES:
                                            # 'OWZREIFADZCYQD-NSHGMRRFSA-N' , 'FCKJYANJHNLEEP-XRWYNYHCSA-N' , 'YKWQHMLRA
                                            # PIWDP-UHFFFAOYSA-N' , 'UOMKBIIXHQIERR-UHFFFAOYSA-N' , 'IDKAXRLETRCXKS-UHFF
                                            # FAOYSA-N' , 'SADQVAVFGNTEOD-UHFFFAOYSA-N' , 'RJMIEHBSYVWVIN-UHFFFAOYSA-N' 
                                            # , 'HSBKFSPNDWWPSL-VDTYLAMSSA-N' , 'CNBGNNVCVSKAQZ-UHFFFAOYSA-N' , 'XASBSYH
                                            # EEHVCSJ-UHFFFAOYSA-N'
                                        }
                                    },
                                    'molecule_synonyms': 
                                    {
                                        'properties': 
                                        {
                                            'molecule_synonym': 'TEXT',
                                            # EXAMPLES:
                                            # 'Decamethrin' , '24, 25-dihydroxycholecalciferol' , 'Indocate' , 'Cridanim
                                            # od' , 'Fenclofenac' , 'Indalpine' , 'Indoprofen' , 'ACH-126443' , 'Benzyda
                                            # mine' , 'Teloxantrone'
                                            'syn_type': 'TEXT',
                                            # EXAMPLES:
                                            # 'INN' , 'OTHER' , 'INN' , 'ATC' , 'OTHER' , 'OTHER' , 'ATC' , 'RESEARCH_CO
                                            # DE' , 'ATC' , 'INN'
                                            'synonyms': 'TEXT',
                                            # EXAMPLES:
                                            # 'Decamethrin' , '24, 25-DIHYDROXYCHOLECALCIFEROL' , 'INDOCATE' , 'CRIDANIM
                                            # OD' , 'Fenclofenac' , 'Indalpine' , 'INDOPROFEN' , 'ACH-126443' , 'BENZYDA
                                            # MINE' , 'TELOXANTRONE'
                                        }
                                    },
                                    'ob_patent': 'NUMERIC',
                                    # EXAMPLES:
                                    # '8242158' , '6943166' , '8026284' , '6958335' , '7695734' , '7387793' , '6562873' 
                                    # , '6315720' , '6545040' , '6488962'
                                    'oral': 'BOOLEAN',
                                    # EXAMPLES:
                                    # 'False' , 'False' , 'False' , 'False' , 'False' , 'False' , 'False' , 'False' , 'F
                                    # alse' , 'False'
                                    'parenteral': 'BOOLEAN',
                                    # EXAMPLES:
                                    # 'False' , 'False' , 'False' , 'False' , 'False' , 'False' , 'False' , 'False' , 'F
                                    # alse' , 'False'
                                    'prodrug': 'BOOLEAN',
                                    # EXAMPLES:
                                    # 'False' , 'False' , 'False' , 'False' , 'False' , 'False' , 'False' , 'False' , 'F
                                    # alse' , 'False'
                                    'research_codes': 'TEXT',
                                    # EXAMPLES:
                                    # 'R 67408' , 'LM-5008' , 'K 4277' , 'ACH-126443' , 'AF-864' , 'DUP 937' , 'MPV-1440
                                    # ' , 'IC-351' , 'NSC-647528' , 'BM 15.075'
                                    'rule_of_five': 'BOOLEAN',
                                    # EXAMPLES:
                                    # 'False' , 'False' , 'True' , 'True' , 'True' , 'True' , 'True' , 'True' , 'True' ,
                                    #  'False'
                                    'sc_patent': 'TEXT',
                                    # EXAMPLES:
                                    # 'US-8242158-B1' , 'US-6943166-B1' , 'US-8026284-B2' , 'US-6958335-B2' , 'US-769573
                                    # 4-B2' , 'US-7387793-B2' , 'US-6562873-B2' , 'US-6315720-B1' , 'US-6545040-B1' , 'U
                                    # S-6488962-B1'
                                    'synonyms': 'TEXT',
                                    # EXAMPLES:
                                    # 'Deltamethrin (BAN)' , 'Secalciferol (BAN, INN, USAN)' , 'Indocate (INN)' , 'Crida
                                    # nimod (INN)' , 'Fenclofenac (BAN, INN, USAN)' , 'Indalpine (BAN, INN, MI)' , 'Indo
                                    # profen (BAN, INN, USAN)' , 'Elvucitabine (INN, USAN)' , 'Benzydamine hydrochloride
                                    #  (JAN, MI, USAN)' , 'Teloxantrone (INN)'
                                    'topical': 'BOOLEAN',
                                    # EXAMPLES:
                                    # 'False' , 'False' , 'False' , 'False' , 'False' , 'False' , 'False' , 'False' , 'F
                                    # alse' , 'False'
                                    'usan_stem': 'TEXT',
                                    # EXAMPLES:
                                    # '-calci-' , '-imod' , '-ac' , '-pine' , '-profen' , '-citabine' , '-antrone' , '-a
                                    # fil' , '-ac' , '-fibrate'
                                    'usan_stem_definition': 'TEXT',
                                    # EXAMPLES:
                                    # 'vitamin D analogues' , 'immunomodulators' , 'anti-inflammatory agents (acetic aci
                                    # d derivatives)' , 'tricyclic compounds' , 'anti-inflammatory/analgesic agents (ibu
                                    # profen type)' , 'nucleoside antiviral or antineoplastic agents, cytarabine or azar
                                    # abine derivatives' , 'antineoplastics, anthraquinone derivatives' , 'PDE5 inhibito
                                    # rs' , 'anti-inflammatory agents (acetic acid derivatives)' , 'antihyperlipidemics 
                                    # (clofibrate type)'
                                    'usan_stem_substem': 'TEXT',
                                    # EXAMPLES:
                                    # '-calci-(-calci-)' , '-imod(-imod)' , '-ac(-ac)' , '-pine(-pine)' , '-profen(-prof
                                    # en)' , '-citabine(-citabine)' , '-antrone(-antrone)' , '-afil(-afil)' , '-ac(-ac)'
                                    #  , '-fibrate(-fibrate)'
                                    'usan_year': 'NUMERIC',
                                    # EXAMPLES:
                                    # '1989' , '1978' , '1976' , '2003' , '1965' , '1992' , '1989' , '2001' , '1990' , '
                                    # 1978'
                                    'withdrawn_class': 'TEXT',
                                    # EXAMPLES:
                                    # 'Carcinogenicity; Dermatological toxicity' , 'Hematological toxicity' , 'Carcinoge
                                    # nicity; Gastrotoxicity' , 'Cardiotoxicity' , 'Dermatological toxicity' , 'Dermatol
                                    # ogical toxicity; Hematological toxicity; Hepatotoxicity' , 'Cardiotoxicity' , 'Neu
                                    # rotoxicity' , 'Cardiotoxicity; Respiratory toxicity' , 'Hepatotoxicity'
                                    'withdrawn_country': 'TEXT',
                                    # EXAMPLES:
                                    # 'United Kingdom' , 'France' , 'United Kingdom; Spain; Germany' , 'United States; U
                                    # nited Kingdom; United States; Germany' , 'United States' , 'United States' , 'Spai
                                    # n; Germany; France' , 'Germany' , 'United Kingdom; Germany; Italy; Ireland; Nether
                                    # lands; European Union' , 'European Union; Germany; France'
                                    'withdrawn_reason': 'TEXT',
                                    # EXAMPLES:
                                    # 'Cutaneous Reactions; Animal Carcinogenicity' , 'Agranulocytosis' , 'Animal Carcin
                                    # ogenicity (rodent); Gastrointestinal Toxicity' , 'Cardiac repolarization; QTc inte
                                    # rval prolongation' , 'Stevens Johnson Syndrome; Toxic Epidermal Necrolysis' , 'Der
                                    # matologic, Hematologic and Hepatic Reactions' , 'Arrhythmias and Sudden Cardiac De
                                    # ath (Arrhythmias and Sudden)' , 'Polyneuropathy' , 'Cardiac valvulopathy; Pulmonar
                                    # y arterial hypertension' , 'Hepatotoxicity'
                                    'withdrawn_year': 'NUMERIC',
                                    # EXAMPLES:
                                    # '1984' , '1985' , '1983' , '1999' , '1983' , '1988' , '1998' , '1987' , '2009' , '
                                    # 1985'
                                }
                            },
                            'is_drug': 'BOOLEAN',
                            # EXAMPLES:
                            # 'True' , 'True' , 'True' , 'True' , 'True' , 'True' , 'True' , 'True' , 'True' , 'True'
                        }
                    },
                    'drug_indications': 
                    {
                        'properties': 
                        {
                            '_metadata': 
                            {
                                'properties': 
                                {
                                    'all_molecule_chembl_ids': 'TEXT',
                                    # EXAMPLES:
                                    # 'CHEMBL1593566' , 'CHEMBL1567328' , 'CHEMBL1569545' , 'CHEMBL15870' , 'CHEMBL38700
                                    # ' , 'CHEMBL12610' , 'CHEMBL778' , 'CHEMBL779' , 'CHEMBL602' , 'CHEMBL264374'
                                }
                            },
                            'drugind_id': 'NUMERIC',
                            # EXAMPLES:
                            # '118494' , '57206' , '120667' , '41845' , '63116' , '112170' , '48970' , '49400' , '54804'
                            #  , '55132'
                            'efo_id': 'TEXT',
                            # EXAMPLES:
                            # 'EFO:0001067' , 'EFO:0003948' , 'MONDO:0011962' , 'EFO:0005755' , 'EFO:0000180' , 'EFO:000
                            # 9688' , 'EFO:0004273' , 'EFO:0001073' , 'HP:0001397' , 'Orphanet:79211'
                            'efo_term': 'TEXT',
                            # EXAMPLES:
                            # 'parasitic infection' , 'gastroesophageal reflux disease' , 'endometrial cancer' , 'rheuma
                            # tic disease' , 'HIV-1 infection' , 'stomatitis' , 'scoliosis' , 'obesity' , 'Hepatic steat
                            # osis' , 'Combined hyperlipidemia'
                            'indication_refs': 
                            {
                                'properties': 
                                {
                                    'ref_id': 'TEXT',
                                    # EXAMPLES:
                                    # 'P03BA03' , 'NCT00857597' , 'NCT03077698' , 'M01AE10' , 'NCT00380159' , 'NCT000514
                                    # 41' , 'NCT00671931' , 'NCT02819440' , 'NCT00799578' , 'NCT02548832'
                                    'ref_type': 'TEXT',
                                    # EXAMPLES:
                                    # 'ATC' , 'ClinicalTrials' , 'ClinicalTrials' , 'ATC' , 'ClinicalTrials' , 'Clinical
                                    # Trials' , 'ClinicalTrials' , 'ClinicalTrials' , 'ClinicalTrials' , 'ClinicalTrials
                                    # '
                                    'ref_url': 'TEXT',
                                    # EXAMPLES:
                                    # 'http://www.whocc.no/atc_ddd_index/?code=P03BA03' , 'https://clinicaltrials.gov/se
                                    # arch?id=%22NCT00857597%22' , 'https://clinicaltrials.gov/search?id=%22NCT03077698%
                                    # 22' , 'http://www.whocc.no/atc_ddd_index/?code=M01AE10' , 'https://clinicaltrials.
                                    # gov/search?id=%22NCT00380159%22' , 'https://clinicaltrials.gov/search?id=%22NCT000
                                    # 51441%22' , 'https://clinicaltrials.gov/search?id=%22NCT00671931%22' , 'https://cl
                                    # inicaltrials.gov/search?id=%22NCT02819440%22' , 'https://clinicaltrials.gov/search
                                    # ?id=%22NCT00799578%22' , 'https://clinicaltrials.gov/search?id=%22NCT02548832%22'
                                }
                            },
                            'max_phase_for_ind': 'NUMERIC',
                            # EXAMPLES:
                            # '0' , '3' , '2' , '4' , '2' , '3' , '1' , '2' , '1' , '2'
                            'mesh_heading': 'TEXT',
                            # EXAMPLES:
                            # 'Ectoparasitic Infestations' , 'Gastroesophageal Reflux' , 'Endometrial Neoplasms' , 'Rheu
                            # matic Diseases' , 'HIV Infections' , 'Stomatitis' , 'Scoliosis' , 'Obesity' , 'Fatty Liver
                            # ' , 'Hyperlipidemia, Familial Combined'
                            'mesh_id': 'TEXT',
                            # EXAMPLES:
                            # 'D004478' , 'D005764' , 'D016889' , 'D012216' , 'D015658' , 'D013280' , 'D012600' , 'D0097
                            # 65' , 'D005234' , 'D006950'
                            'molecule_chembl_id': 'TEXT',
                            # EXAMPLES:
                            # 'CHEMBL1593566' , 'CHEMBL1567328' , 'CHEMBL1569545' , 'CHEMBL15870' , 'CHEMBL38700' , 'CHE
                            # MBL12610' , 'CHEMBL778' , 'CHEMBL779' , 'CHEMBL602' , 'CHEMBL264374'
                            'parent_molecule_chembl_id': 'TEXT',
                            # EXAMPLES:
                            # 'CHEMBL1593566' , 'CHEMBL1503' , 'CHEMBL1569545' , 'CHEMBL15870' , 'CHEMBL38700' , 'CHEMBL
                            # 12610' , 'CHEMBL778' , 'CHEMBL779' , 'CHEMBL602' , 'CHEMBL264374'
                        }
                    },
                    'es_completion': 'TEXT',
                    # EXAMPLES:
                    # '{'input': 'InChI=1S/C14H12N2O4S2/c17-14(11-5-3-9-21-11)20-8-7-15-13-10-4-1-2-6-12(10)22(18,19)16-
                    # 13/h1-6,9H,7-8H2,(H,15,16)', 'weight': 30}' , '{'input': 'Cc1ccc(N2CC(C(=O)N3CCOCC3)CC2=O)cc1C', '
                    # weight': 30}' , '{'input': 'PSAKHUYUMWVJHU-PTNGSMBKSA-N', 'weight': 30}' , '{'input': 'InChI=1S/C1
                    # 7H19ClN4O7S/c1-20(30(27,28)11-6-4-10(18)5-7-11)8-13(24)29-9-12(23)14-15(19)21(2)17(26)22(3)16(14)2
                    # 5/h4-7H,8-9,19H2,1-3H3', 'weight': 30}' , '{'input': 'QKMFWQIPIYXGII-UHFFFAOYSA-N', 'weight': 30}'
                    #  , '{'input': 'InChI=1S/C19H24N4O/c1-3-15-7-4-5-9-17(15)22-18(24)16-8-6-12-23(13-16)19-20-11-10-14
                    # (2)21-19/h4-5,7,9-11,16H,3,6,8,12-13H2,1-2H3,(H,22,24)', 'weight': 30}' , '{'input': 'Cc1ccc(S(=O)
                    # (=O)N(C)c2ccc3ccccc3c2)cc1', 'weight': 30}' , '{'input': 'InChI=1S/C16H11ClN2O/c17-13-7-3-1-5-11(1
                    # 3)9-10-15-18-14-8-4-2-6-12(14)16(20)19-15/h1-10H,(H,18,19,20)/b10-9+', 'weight': 30}' , '{'input':
                    #  'CHEMBL1625293', 'weight': 5}' , '{'input': 'C#CCOC(=O)C[N+](C)(C)CC=C.[Cl-]', 'weight': 30}'
                    'hierarchy': 
                    {
                        'properties': 
                        {
                            'all_family': 
                            {
                                'properties': 
                                {
                                    'chembl_id': 'TEXT',
                                    # EXAMPLES:
                                    # 'CHEMBL1584351' , 'CHEMBL1584358' , 'CHEMBL1584363' , 'CHEMBL1584365' , 'CHEMBL158
                                    # 4367' , 'CHEMBL1584370' , 'CHEMBL1584374' , 'CHEMBL1584379' , 'CHEMBL1625293' , 'C
                                    # HEMBL1625294'
                                    'inchi': 'TEXT',
                                    # EXAMPLES:
                                    # 'InChI=1S/C14H12N2O4S2/c17-14(11-5-3-9-21-11)20-8-7-15-13-10-4-1-2-6-12(10)22(18,1
                                    # 9)16-13/h1-6,9H,7-8H2,(H,15,16)' , 'InChI=1S/C17H22N2O3/c1-12-3-4-15(9-13(12)2)19-
                                    # 11-14(10-16(19)20)17(21)18-5-7-22-8-6-18/h3-4,9,14H,5-8,10-11H2,1-2H3' , 'InChI=1S
                                    # /C19H12N2O5/c22-18(19(23)24)15(11-12-5-8-14(9-6-12)21(25)26)17-10-7-13-3-1-2-4-16(
                                    # 13)20-17/h1-11H,(H,23,24)/b15-11-' , 'InChI=1S/C17H19ClN4O7S/c1-20(30(27,28)11-6-4
                                    # -10(18)5-7-11)8-13(24)29-9-12(23)14-15(19)21(2)17(26)22(3)16(14)25/h4-7H,8-9,19H2,
                                    # 1-3H3' , 'InChI=1S/C23H28N4O4S2/c1-4-26(5-2)33(29,30)17-12-13-19-18(14-17)25-23(32
                                    # -15-22(28)24-16-10-11-16)27(19)20-8-6-7-9-21(20)31-3/h6-9,12-14,16H,4-5,10-11,15H2
                                    # ,1-3H3,(H,24,28)' , 'InChI=1S/C19H24N4O/c1-3-15-7-4-5-9-17(15)22-18(24)16-8-6-12-2
                                    # 3(13-16)19-20-11-10-14(2)21-19/h4-5,7,9-11,16H,3,6,8,12-13H2,1-2H3,(H,22,24)' , 'I
                                    # nChI=1S/C18H17NO2S/c1-14-7-11-18(12-8-14)22(20,21)19(2)17-10-9-15-5-3-4-6-16(15)13
                                    # -17/h3-13H,1-2H3' , 'InChI=1S/C16H11ClN2O/c17-13-7-3-1-5-11(13)9-10-15-18-14-8-4-2
                                    # -6-12(14)16(20)19-15/h1-10H,(H,18,19,20)/b10-9+' , 'InChI=1S/C15H16N4O2/c1-8-11(14
                                    # (20)18-16-8)13(10-6-4-3-5-7-10)12-9(2)17-19-15(12)21/h3-7,11-13H,1-2H3,(H,18,20)(H
                                    # ,19,21)' , 'InChI=1S/C10H16NO2/c1-5-7-11(3,4)9-10(12)13-8-6-2/h2,5H,1,7-9H2,3-4H3/
                                    # q+1'
                                    'inchi_connectivity_layer': 'TEXT',
                                    # EXAMPLES:
                                    # 'QTNRRYNCUTVURP' , 'LUNLRCJOOSYTLZ' , 'PSAKHUYUMWVJHU' , 'OATSQMAOFAXJRE' , 'QKMFW
                                    # QIPIYXGII' , 'MBSXNOVOZXJLHZ' , 'ZTVNQCYDGPRVLJ' , 'GVTQWTBKPKRCFL' , 'KOLCFQXKOSC
                                    # DED' , 'PQZKGVNVNJYDFT'
                                    'inchi_key': 'TEXT',
                                    # EXAMPLES:
                                    # 'QTNRRYNCUTVURP-UHFFFAOYSA-N' , 'LUNLRCJOOSYTLZ-UHFFFAOYSA-N' , 'PSAKHUYUMWVJHU-PT
                                    # NGSMBKSA-N' , 'OATSQMAOFAXJRE-UHFFFAOYSA-N' , 'QKMFWQIPIYXGII-UHFFFAOYSA-N' , 'MBS
                                    # XNOVOZXJLHZ-UHFFFAOYSA-N' , 'ZTVNQCYDGPRVLJ-UHFFFAOYSA-N' , 'GVTQWTBKPKRCFL-MDZDMX
                                    # LPSA-N' , 'KOLCFQXKOSCDED-UHFFFAOYSA-N' , 'PQZKGVNVNJYDFT-UHFFFAOYSA-N'
                                }
                            },
                            'children': 
                            {
                                'properties': 
                                {
                                    'chembl_id': 'TEXT',
                                    # EXAMPLES:
                                    # 'CHEMBL2135280' , 'CHEMBL1600245' , 'CHEMBL2361429' , 'CHEMBL2005724' , 'CHEMBL196
                                    # 8801' , 'CHEMBL1301928' , 'CHEMBL1565749' , 'CHEMBL1334535' , 'CHEMBL2005461' , 'C
                                    # HEMBL3086833'
                                    'sources': 
                                    {
                                        'properties': 
                                        {
                                            'src_description': 'TEXT',
                                            # EXAMPLES:
                                            # 'PubChem BioAssays' , 'PubChem BioAssays' , 'SARS-CoV-2 Screening Data' , 
                                            # 'PubChem BioAssays' , 'PubChem BioAssays' , 'PubChem BioAssays' , 'PubChem
                                            #  BioAssays' , 'CO-ADD antimicrobial screening data' , 'PubChem BioAssays' 
                                            # , 'Scientific Literature'
                                            'src_id': 'NUMERIC',
                                            # EXAMPLES:
                                            # '7' , '7' , '52' , '7' , '7' , '7' , '7' , '40' , '7' , '1'
                                            'src_short_name': 'TEXT',
                                            # EXAMPLES:
                                            # 'PUBCHEM_BIOASSAY' , 'PUBCHEM_BIOASSAY' , 'SARS_COV_2' , 'PUBCHEM_BIOASSAY
                                            # ' , 'PUBCHEM_BIOASSAY' , 'PUBCHEM_BIOASSAY' , 'PUBCHEM_BIOASSAY' , 'COADD'
                                            #  , 'PUBCHEM_BIOASSAY' , 'LITERATURE'
                                        }
                                    },
                                    'synonyms': 
                                    {
                                        'properties': 
                                        {
                                            'molecule_synonym': 'TEXT',
                                            # EXAMPLES:
                                            # 'AF-864' , 'DUP 937' , '2-Phenyl-Thiazolidine (Radiolabeled At Position1[3
                                            # 5S])' , 'Dexmedetomidine hydrochloride' , 'N-Methyldopamine HCl' , 'CI-914
                                            # 8' , 'Adaprolol maleate' , 'Gleevec' , 'Mirapex' , 'Sodium Meso-2,3-Dimerc
                                            # aptosuccinate'
                                            'syn_type': 'TEXT',
                                            # EXAMPLES:
                                            # 'RESEARCH_CODE' , 'RESEARCH_CODE' , 'OTHER' , 'FDA' , 'OTHER' , 'RESEARCH_
                                            # CODE' , 'OTHER' , 'OTHER' , 'TRADE_NAME' , 'OTHER'
                                            'synonyms': 'TEXT',
                                            # EXAMPLES:
                                            # 'AF-864' , 'DUP 937' , '2-Phenyl-Thiazolidine (Radiolabeled At Position1[3
                                            # 5S])' , 'DEXMEDETOMIDINE HYDROCHLORIDE' , 'N-Methyldopamine Hydrochloride'
                                            #  , 'CI-9148' , 'ADAPROLOL MALEATE' , 'Gleevec' , 'Mirapex' , 'Sodium Meso-
                                            # 2,3-Dimercaptosuccinate'
                                        }
                                    }
                                }
                            },
                            'family_inchi_connectivity_layer': 'TEXT',
                            # EXAMPLES:
                            # 'QTNRRYNCUTVURP' , 'LUNLRCJOOSYTLZ' , 'PSAKHUYUMWVJHU' , 'OATSQMAOFAXJRE' , 'QKMFWQIPIYXGI
                            # I' , 'MBSXNOVOZXJLHZ' , 'ZTVNQCYDGPRVLJ' , 'GVTQWTBKPKRCFL' , 'KOLCFQXKOSCDED' , 'PQZKGVNV
                            # NJYDFT'
                            'is_approved_drug': 'BOOLEAN',
                            # EXAMPLES:
                            # 'False' , 'False' , 'False' , 'False' , 'False' , 'False' , 'False' , 'False' , 'False' , 
                            # 'False'
                            'is_usan': 'BOOLEAN',
                            # EXAMPLES:
                            # 'False' , 'False' , 'False' , 'False' , 'False' , 'False' , 'False' , 'False' , 'False' , 
                            # 'False'
                            'parent': 
                            {
                                'properties': 
                                {
                                    'chembl_id': 'TEXT',
                                    # EXAMPLES:
                                    # 'CHEMBL1625293' , 'CHEMBL1625294' , 'CHEMBL1625365' , 'CHEMBL1624347' , 'CHEMBL162
                                    # 4476' , 'CHEMBL1624497' , 'CHEMBL1624498' , 'CHEMBL1624521' , 'CHEMBL1624522' , 'C
                                    # HEMBL1624464'
                                    'sources': 
                                    {
                                        'properties': 
                                        {
                                            'src_description': 'TEXT',
                                            # EXAMPLES:
                                            # 'Scientific Literature' , 'Scientific Literature' , 'Scientific Literature
                                            # ' , 'Scientific Literature' , 'PubChem BioAssays' , 'CO-ADD antimicrobial 
                                            # screening data' , 'PubChem BioAssays' , 'Scientific Literature' , 'St Jude
                                            #  Leishmania Screening' , 'CO-ADD antimicrobial screening data'
                                            'src_id': 'NUMERIC',
                                            # EXAMPLES:
                                            # '1' , '1' , '1' , '1' , '7' , '40' , '7' , '1' , '32' , '40'
                                            'src_short_name': 'TEXT',
                                            # EXAMPLES:
                                            # 'LITERATURE' , 'LITERATURE' , 'LITERATURE' , 'LITERATURE' , 'PUBCHEM_BIOAS
                                            # SAY' , 'COADD' , 'PUBCHEM_BIOASSAY' , 'LITERATURE' , 'ST_JUDE_LEISH' , 'CO
                                            # ADD'
                                        }
                                    },
                                    'synonyms': 
                                    {
                                        'properties': 
                                        {
                                            'molecule_synonym': 'TEXT',
                                            # EXAMPLES:
                                            # 'Levopropoxyphene' , '(+/-)-Noscapine' , 'Benzamidine' , 'MMV080034' , 'An
                                            # tra' , 'GNF-Pf-298' , 'DNDI1417780' , 'Bucladesine' , 'Mecysteine' , 'Thia
                                            # zole'
                                            'syn_type': 'TEXT',
                                            # EXAMPLES:
                                            # 'BAN' , 'OTHER' , 'OTHER' , 'RESEARCH_CODE' , 'TRADE_NAME' , 'RESEARCH_COD
                                            # E' , 'OTHER' , 'ATC' , 'BAN' , 'OTHER'
                                            'synonyms': 'TEXT',
                                            # EXAMPLES:
                                            # 'LEVOPROPOXYPHENE' , '(+/-)-Noscapine' , 'Benzamidine' , 'MMV080034' , 'An
                                            # tra' , 'GNF-Pf-298' , 'DNDI1417780' , 'BUCLADESINE' , 'MECYSTEINE' , 'Thia
                                            # zole'
                                        }
                                    }
                                }
                            }
                        }
                    },
                    'related_activities': 
                    {
                        'properties': 
                        {
                            'count': 'NUMERIC',
                            # EXAMPLES:
                            # '7' , '3' , '26' , '5' , '12' , '5' , '15' , '26' , '13' , '3'
                        }
                    },
                    'related_assays': 
                    {
                        'properties': 
                        {
                            'all_chembl_ids': 'TEXT',
                            # EXAMPLES:
                            # 'CHEMBL1614459 CHEMBL1794580 CHEMBL3562077 CHEMBL1614257 CHEMBL2114810 CHEMBL1614458 CHEMB
                            # L1614234' , 'CHEMBL1794584 CHEMBL1614315 CHEMBL2114861' , 'CHEMBL1794345 CHEMBL1613838 CHE
                            # MBL1794352 CHEMBL1614531 CHEMBL1614421 CHEMBL1613836 CHEMBL1614458 CHEMBL1738312 CHEMBL173
                            # 7991 CHEMBL1794580 CHEMBL3562077 CHEMBL3215046 CHEMBL2114843 CHEMBL1614257 CHEMBL1613842 C
                            # HEMBL1738442 CHEMBL1738184 CHEMBL1613829 CHEMBL3215106 CHEMBL1794585 CHEMBL1614146 CHEMBL1
                            # 614174 CHEMBL1738588 CHEMBL1614263 CHEMBL2114810 CHEMBL1794359' , 'CHEMBL1614087 CHEMBL161
                            # 4174 CHEMBL1614250 CHEMBL2114788 CHEMBL1794375' , 'CHEMBL1794345 CHEMBL1738442 CHEMBL16137
                            # 69 CHEMBL1614459 CHEMBL1613918 CHEMBL1614052 CHEMBL1794580 CHEMBL1614211 CHEMBL1614530 CHE
                            # MBL1738500 CHEMBL2114775 CHEMBL1738588' , 'CHEMBL2354282 CHEMBL1963966 CHEMBL1614459 CHEMB
                            # L1614530 CHEMBL1794580' , 'CHEMBL1614249 CHEMBL1738442 CHEMBL1737991 CHEMBL2354221 CHEMBL1
                            # 613918 CHEMBL1613818 CHEMBL1794580 CHEMBL1614052 CHEMBL2114913 CHEMBL1738588 CHEMBL1614280
                            #  CHEMBL2354254 CHEMBL1794401 CHEMBL2114788 CHEMBL1738312' , 'CHEMBL1794345 CHEMBL1613838 C
                            # HEMBL1613836 CHEMBL1738578 CHEMBL1614128 CHEMBL1963863 CHEMBL1614530 CHEMBL2354254 CHEMBL2
                            # 354221 CHEMBL1614342 CHEMBL1794512 CHEMBL2114807 CHEMBL1738184 CHEMBL1738132 CHEMBL1738495
                            #  CHEMBL1794585 CHEMBL1614079 CHEMBL1614146 CHEMBL1738317 CHEMBL1738502 CHEMBL1614304 CHEMB
                            # L1794483 CHEMBL1738588 CHEMBL1738414 CHEMBL1794352 CHEMBL2114780' , 'CHEMBL1738442 CHEMBL1
                            # 794349 CHEMBL1737902 CHEMBL1794580 CHEMBL1614166 CHEMBL1614421 CHEMBL1614103 CHEMBL1614174
                            #  CHEMBL1794324 CHEMBL1794426 CHEMBL1614031 CHEMBL1614458 CHEMBL1614076' , 'CHEMBL1794580 C
                            # HEMBL1738442 CHEMBL1614530'
                            'count': 'NUMERIC',
                            # EXAMPLES:
                            # '7' , '3' , '26' , '5' , '12' , '5' , '15' , '26' , '13' , '3'
                        }
                    },
                    'related_cell_lines': 
                    {
                        'properties': 
                        {
                            'all_chembl_ids': 'TEXT',
                            # EXAMPLES:
                            # '' , '' , '' , '' , '' , '' , '' , 'CHEMBL3307758' , '' , ''
                            'count': 'NUMERIC',
                            # EXAMPLES:
                            # '0' , '0' , '0' , '0' , '0' , '0' , '0' , '1' , '0' , '0'
                        }
                    },
                    'related_documents': 
                    {
                        'properties': 
                        {
                            'all_chembl_ids': 'TEXT',
                            # EXAMPLES:
                            # 'CHEMBL1201862' , 'CHEMBL1201862' , 'CHEMBL1201862' , 'CHEMBL1201862' , 'CHEMBL1201862' , 
                            # 'CHEMBL1201862' , 'CHEMBL1201862' , 'CHEMBL1201862' , 'CHEMBL1201862' , 'CHEMBL1201862'
                            'count': 'NUMERIC',
                            # EXAMPLES:
                            # '1' , '1' , '1' , '1' , '1' , '1' , '1' , '1' , '1' , '1'
                        }
                    },
                    'related_targets': 
                    {
                        'properties': 
                        {
                            'all_chembl_ids': 'TEXT',
                            # EXAMPLES:
                            # 'CHEMBL364 CHEMBL612545 CHEMBL1293238 CHEMBL2093861 CHEMBL3577 CHEMBL4377' , 'CHEMBL129327
                            # 5 CHEMBL612545 CHEMBL1293258' , 'CHEMBL364 CHEMBL1741220 CHEMBL1293278 CHEMBL3577 CHEMBL20
                            # 29198 CHEMBL4377 CHEMBL1075094 CHEMBL5567 CHEMBL2093861 CHEMBL1293232 CHEMBL612545 CHEMBL1
                            # 293248 CHEMBL2288 CHEMBL1615322 CHEMBL1293294 CHEMBL6032 CHEMBL1793 CHEMBL1293224 CHEMBL38
                            # 85594 CHEMBL1741209 CHEMBL5896 CHEMBL1293236' , 'CHEMBL1293248 CHEMBL1293231 CHEMBL612545 
                            # CHEMBL1784 CHEMBL1293224' , 'CHEMBL364 CHEMBL2026 CHEMBL5619 CHEMBL612545 CHEMBL6032 CHEMB
                            # L1741209 CHEMBL5514 CHEMBL3563 CHEMBL5313 CHEMBL5162' , 'CHEMBL6152 CHEMBL612545 CHEMBL202
                            # 6 CHEMBL364 CHEMBL2007626' , 'CHEMBL1075138 CHEMBL364 CHEMBL1293254 CHEMBL1741220 CHEMBL60
                            # 32 CHEMBL2179 CHEMBL1784 CHEMBL1741209 CHEMBL5514 CHEMBL5896 CHEMBL1287622 CHEMBL5162 CHEM
                            # BL2146305 CHEMBL1741193' , 'CHEMBL364 CHEMBL1741217 CHEMBL1293278 CHEMBL1741207 CHEMBL1075
                            # 094 CHEMBL1075138 CHEMBL2026 CHEMBL1293277 CHEMBL2334 CHEMBL5567 CHEMBL5990 CHEMBL4096 CHE
                            # MBL612545 CHEMBL2288 CHEMBL1615322 CHEMBL1293294 CHEMBL2097170 CHEMBL1741213 CHEMBL1741215
                            #  CHEMBL1741209 CHEMBL2392 CHEMBL5391' , 'CHEMBL364 CHEMBL1293248 CHEMBL612545 CHEMBL129331
                            # 7 CHEMBL1293224 CHEMBL6032 CHEMBL3577 CHEMBL1741192 CHEMBL1741171 CHEMBL2608' , 'CHEMBL603
                            # 2 CHEMBL2026 CHEMBL364'
                            'count': 'NUMERIC',
                            # EXAMPLES:
                            # '6' , '3' , '22' , '5' , '10' , '5' , '14' , '22' , '10' , '3'
                        }
                    },
                    'related_tissues': 
                    {
                        'properties': 
                        {
                            'all_chembl_ids': 'TEXT',
                            # EXAMPLES:
                            # '' , '' , '' , '' , '' , '' , '' , '' , '' , ''
                            'count': 'NUMERIC',
                            # EXAMPLES:
                            # '0' , '0' , '0' , '0' , '0' , '0' , '0' , '0' , '0' , '0'
                        }
                    },
                    'unichem': 
                    {
                        'properties': 
                        {
                        }
                    }
                }
            },
            'atc_classifications': 'TEXT',
            # EXAMPLES:
            # 'P03BA03' , 'L03AX18' , 'M01AE10' , 'M02AA05' , 'N05CM18' , 'G04BE08' , 'A16AA04' , 'C10AB02' , 'A11HA05' 
            # , 'L01XE01'
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
                            # '19353' , '10166' , '10182' , '6359' , '6335' , '6553' , '6320' , '6375' , '6393' , '6377'
                            'component_type': 'TEXT',
                            # EXAMPLES:
                            # 'PROTEIN' , 'PROTEIN' , 'PROTEIN' , 'PROTEIN' , 'PROTEIN' , 'PROTEIN' , 'PROTEIN' , 'PROTE
                            # IN' , 'PROTEIN' , 'PROTEIN'
                            'description': 'TEXT',
                            # EXAMPLES:
                            # 'RELABOTULINUMTOXINA Sequence' , 'UTOMILUMAB Heavy Chain' , 'TAMTUVETMAB Heavy Chain' , 'B
                            # linatumumab single chain variable fragment fusion protein (bite)' , 'Brentuximab vedotin h
                            # eavy chain' , 'Brodalumab heavy chain' , 'Cantuzumab ravtansine heavy chain' , 'Cixutumuma
                            # b heavy chain' , 'Conatumumab heavy chain' , 'Dalotuzumab heavy chain'
                            'organism': 'TEXT',
                            # EXAMPLES:
                            # 'Homo sapiens' , 'Homo sapiens' , 'Homo sapiens' , 'Homo sapiens' , 'Homo sapiens' , 'Homo
                            #  sapiens' , 'Homo sapiens' , 'Homo sapiens' , 'Homo sapiens' , 'Homo sapiens'
                            'sequence': 'TEXT',
                            # EXAMPLES:
                            # 'PFVNKQFNYKDPVNGVDIAYIKIPNAGQMQPVKAFKIHNKIWVIPERDTFTNPEEGDLNPPPEAKQVPVSYYDSTYLSTDNEKDNYLKG
                            # VTKLFERIYSTDLGRMLLTSIVRGIPFWGGSTIDTELKVIDTNCINVIQPDGSYRSEELNLVIIGPSADIIQFECKSFGHEVLNLTRNGY
                            # GSTQYIRFSPDFTFGFEESLEVDTNPLLGAGKFATDPAVTLAHELIHAGHRLYGIAINPNRVFKVNTNAYYEMSGLEVSFEELRTFGGHD
                            # AKFIDSLQENEFRLYYYNKFKDIASTLNKAKSIVGTTASLQYMKNVFKEKYLLSEDTSGKFSVDKLKFDKLYKMLTEIYTEDNFVKFFKV
                            # LNRKTYLNFDKAVFKINIVPKVNYTIYDGFNLRNTNLAANFNGQNTEINNMNFTKLKNFTGLFEFYKLLCVRGIITSKTKSLDKGYNKAL
                            # NDLCIKVNNWDLFFSPSEDNFTNDLNKGEEITSDTNIEAAEENISLDLIQQYYLTFNFDNEPENISIENLSSDIIGQLELMPNIERFPNG
                            # KKYELDKYTMFHYLRAQEFEHGKSRIALTNSVNEALLNPSRVYTFFSSDYVKKVNKATEAAMFLGWVEQLVYDFTDETSEVSTTDKIADI
                            # TIIIPYIGPALNIGNMLYKDDFVGALIFSGAVILLEFIPEIAIPVLGTFALVSYIANKVLTVQTIDNALSKRNEKWDEVYKYIVTNWLAK
                            # VNTQIDLIRKKMKEALENQAEATKAIINYQYNQYTEEEKNNINFNIDDLSSKLNESINKAMININKFLNQCSVSYLMNSMIPYGVKRLED
                            # FDASLKDALLKYIYDNRGTLIGQVDRLKDKVNNTLSTDIPFQLSKYVDNQRLLSTFTEYIKNIINTSILNLRYESNHLIDLSRYASKINI
                            # GSKVNFDPIDKNQIQLFNLESSKIEVILKNAIVYNSMYENFSTSFWIRIPKYFNSISLNNEYTIINCMENNSGWKVSLNYGEIIWTLQDT
                            # QEIKQRVVFKYSQMINISDYINRWIFVTITNNRLNNSKIYINGRLIDQKPISNLGNIHASNNIMFKLDGCRDTHRYIWIKYFNLFDKELN
                            # EKEIKDLYDNQSNSGILKDFWGDYLQYDKPYYMLNLYDPNKYVDVNNVGIRGYMYLKGPRGSVMTTNIYLNSSLYRGTKFIIKKYASGNK
                            # DNIVRNNDRVYINVVVKNKEYRLATNASQAGVEKILSALEIPDVGNLSQVVVMKSKNDQGITNKCKMNLQDNNGNDIGFIGFHQFNNIAK
                            # LVASNWYNRQIERSSRTLGCSWEFIPVDDGWGERPL' , 'EVQLVQSGAEVKKPGESLRISCKGSGYSFSTYWISWVRQMPGKGLEWMG
                            # KIYPGDSYTNYSPSFQGQVTISADKSISTAYLQWSSLKASDTAMYYCARGYGIFDYWGQGTLVTVSSASTKGPSVFPLAPCSRSTSESTA
                            # ALGCLVKDYFPEPVTVSWNSGALTSGVHTFPAVLQSSGLYSLSSVVTVPSSNFGTQTYTCNVDHKPSNTKVDKTVERKCCVECPPCPAPP
                            # VAGPSVFLFPPKPKDTLMISRTPEVTCVVVDVSHEDPEVQFNWYVDGVEVHNAKTKPREEQFNSTFRVVSVLTVVHQDWLNGKEYKCKVS
                            # NKGLPAPIEKTISKTKGQPREPQVYTLPPSREEMTKNQVSLTCLVKGFYPSDIAVEWESNGQPENNYKTTPPMLDSDGSFFLYSKLTVDK
                            # SRWQQGNVFSCSVMHEALHNHYTQKSLSLSPG' , 'EVKLLESGGGLVQPGGSMRLSCAGSGFTFTDFYMNWIRQPAGKAPEWLGFIRD
                            # KAKGYTTEYNPSVKGRFTISRDNTQNMLYLQMNTLRAEDTATYYCAREGHTAAPFDYWGQGTLVTVSSASTTAPSVFPLAPSCGSTSGST
                            # VALACLVSGYFPEPVTVSWNSGSLTSGVHTFPSVLQSSGLYSLSSMVTVPSSRWPSETFTCNVAHPASKTKVDKPVPKRENGRVPRPPDC
                            # PKCPAPEMLGGPSVFIFPPKPKDTLLIARTPEVTCVVVDLDPEDPEVQISWFVDGKQMQTAKTQPREEQFNGTYRVVSVLPIGHQDWLKG
                            # KQFTCKVNNKALPSPIERTISKARGQAHQPSVYVLPPSREELSKNTVSLTCLIKDFFPPDIDVEWQSNGQQEPESKYRTTPPQLDEDGSY
                            # FLYSKLSVDKSRWQRGDTFICAVMHEALHNHYTQKSLSHSPGK' , 'DIQLTQSPASLAVSLGQRATISCKASQSVDYDGDSYLNWYQQ
                            # IPGQPPKLLIYDASNLVSGIPPRFSGSGSGTDFTLNIHPVEKVDAATYHCQQSTEDPWTFGGGTKLEIKGGGGSGGGGSGGGGSQVQLQQ
                            # SGAELVRPGSSVKISCKASGYAFSSYWMNWVKQRPGQGLEWIGQIWPGDGDTNYNGKFKGKATLTADESSSTAYMQLSSLASEDSAVYFC
                            # ARRETTTVGRYYYAMDYWGQGTTVTVSSGGGGSDIKLQQSGAELARPGASVKMSCKTSGYTFTRYTMHWVKQRPGQGLEWIGYINPSRGY
                            # TNYNQKFKDKATLTTDKSSSTAYMQLSSLTSEDSAVYYCARYYDDHYCLDYWGQGTTLTVSSVEGGSGGSGGSGGSGGVDDIQLTQSPAI
                            # MSASPGEKVTMTCRASSSVSYMNWYQQKSGTSPKRWIYDTSKVASGVPYRFSGSGSGTSYSLTISSMEAEDAATYYCQQWSSNPLTFGAG
                            # TKLELKHHHHHH' , 'QIQLQQSGPEVVKPGASVKISCKASGYTFTDYYITWVKQKPGQGLEWIGWIYPGSGNTKYNEKFKGKATLTVD
                            # TSSSTAFMQLSSLTSEDTAVYFCANYGNYWFAYWGQGTQVTVSAASTKGPSVFPLAPSSKSTSGGTAALGCLVKDYFPEPVTVSWNSGAL
                            # TSGVHTFPAVLQSSGLYSLSSVVTVPSSSLGTQTYICNVNHKPSNTKVDKKVEPKSCDKTHTCPPCPAPELLGGPSVFLFPPKPKDTLMI
                            # SRTPEVTCVVVDVSHEDPEVKFNWYVDGVEVHNAKTKPREEQYNSTYRVVSVLTVLHQDWLNGKEYKCKVSNKALPAPIEKTISKAKGQP
                            # REPQVYTLPPSRDELTKNQVSLTCLVKGFYPSDIAVEWESNGQPENNYKTTPPVLDSDGSFFLYSKLTVDKSRWQQGNVFSCSVMHEALH
                            # NHYTQKSLSLSPG' , 'QVQLVQSGAEVKKPGASVKVSCKASGYTFTRYGISWVRQAPGQGLEWMGWISTYSGNTNYAQKLQGRVTMTT
                            # DTSTSTAYMELRSLRSDDTAVYYCARRQLYFDYWGQGTLVTVSSASTKGPSVFPLAPCSRSTSESTAALGCLVKDYFPEPVTVSWNSGAL
                            # TSGVHTFPAVLQSSGLYSLSSVVTVPSSNFGTQTYTCNVDHKPSNTKVDKTVERKCCVECPPCPAPPVAGPSVFLFPPKPKDTLMISRTP
                            # EVTCVVVDVSHEDPEVQFNWYVDGVEVHNAKTKPREEQFNSTFRVVSVLTVVHQDWLNGKEYKCKVSNKGLPAPIEKTISKTKGQPREPQ
                            # VYTLPPSREEMTKNQVSLTCLVKGFYPSDIAVEWESNGQPENNYKTTPPMLDSDGSFFLYSKLTVDKSRWQQGNVFSCSVMHEALHNHYT
                            # QKSLSLSPGK' , 'QVQLVQSGAEVKKPGETVKISCKASDYTFTYYGMNWVKQAPGQGLKWMGWIDTTTGEPTYAQKFQGRIAFSLETS
                            # ASTAYLQIKSLKSEDTATYFCARRGPYNWYFDVWGQGTTVTVSSASTKGPSVFPLAPSSKSTSGGTAALGCLVKDYFPEPVTVSWNSGAL
                            # TSGVHTFPAVLQSSGLYSLSSVVTVPSSSLGTQTYICNVNHKPSNTKVDKKVEPKSCDKTHTCPPCPAPELLGGPSVFLFPPKPKDTLMI
                            # SRTPEVTCVVVDVSHEDPEVKFNWYVDGVEVHNAKTKPREEQYNSTYRVVSVLTVLHQDWLNGKEYKCKVSNKALPAPIEKTISKAKGQP
                            # REPQVYTLPPSRDELTKNQVSLTCLVKGFYPSDIAVEWESNGQPENNYKTTPPVLDSDGSFFLYSKLTVDKSRWQQGNVFSCSVMHEALH
                            # NHYTQKSLSLSPGK' , 'EVQLVQSGAEVKKPGSSVKVSCKASGGTFSSYAISWVRQAPGQGLEWMGGIIPIFGTANYAQKFQGRVTIT
                            # ADKSTSTAYMELSSLRSEDTAVYYCARAPLRFLEWSTQDHYYYYYMDVWGKGTTVTVSSASTKGPSVFPLAPSSKSTSGGTAALGCLVKD
                            # YFPEPVTVSWNSGALTSGVHTFPAVLQSSGLYSLSSVVTVPSSSLGTQTYICNVNHKPSNTKVDKKVEPKSCDKTHTCPPCPAPELLGGP
                            # SVFLFPPKPKDTLMISRTPEVTCVVVDVSHEDPEVKFNWYVDGVEVHNAKTKPREEQYNSTYRVVSVLTVLHQDWLNGKEYKCKVSNKAL
                            # PAPIEKTISKAKGQPREPQVYTLPPSREEMTKNQVSLTCLVKGFYPSDIAVEWESNGQPENNYKTTPPVLDSDGSFFLYSKLTVDKSRWQ
                            # QGNVFSCSVMHEALHNHYTQKSLSLSPGK' , 'QVQLQESGPGLVKPSQTLSLTCTVSGGSISSGDYFWSWIRQLPGKGLEWIGHIHNS
                            # GTTYYNPSLKSRVTISVDTSKKQFSLRLSSVTAADTAVYYCARDRGGDYYYGMDVWGQGTTVTVSSASTKGPSVFPLAPSSKSTSGGTAA
                            # LGCLVKDYFPEPVTVSWNSGALTSGVHTFPAVLQSSGLYSLSSVVTVPSSSLGTQTYICNVNHKPSNTKVDKRVEPKSCDKTHTCPPCPA
                            # PELLGGPSVFLFPPKPKDTLMISRTPEVTCVVVDVSHEDPEVKFNWYVDGVEVHNAKTKPREEQYNSTYRVVSVLTVLHQDWLNGKEYKC
                            # KVSNKALPAPIEKTISKAKGQPREPQVYTLPPSREEMTKNQVSLTCLVKGFYPSDIAVEWESNGQPENNYKTTPPVLDSDGSFFLYSKLT
                            # VDKSRWQQGNVFSCSVMHEALHNHYTQKSLSLSPGK' , 'QVQLQQSGPGLVKPSQTLSLTCTVSGWSISGGWLWNWIRQPPGKGLQWI
                            # GWISWDGTNNWKPSLKDRVTISVDTSKNQFSLKLSSVTAADTAVWWCARWGRVFFDWWGQGTLVTVSSASTKGPSVFPLAPSSKSTSGGT
                            # AALGCLVKDYFPEPVTVSWNSGALTSGVHTFPAVLQSSGLYSLSSVVTVPSSSLGTQTYICNVNHKPSNTKVDKRVEPKSCDKTHTCPPC
                            # PAPELLGGPSVFLFPPKPKDTLMISRTPEVTCVVVDVSHEDPEVKFNWYVDGVEVHNAKTKPREEQYNSTYRVVSVLTVLHQDWLNGKEY
                            # KCKVSNKALPAPIEKTISKAKGQPREPQVYTLPPSREEMTKNQVSLTCLVKGFYPSDIAVEWESNGQPENNYKTTPPVLDSDGSFFLYSK
                            # LTVDKSRWQQGNVFSCSVMHEALHNHYTQKSLSLSPGK'
                            'tax_id': 'NUMERIC',
                            # EXAMPLES:
                            # '9606' , '9606' , '9606' , '9606' , '9606' , '9606' , '9606' , '9606' , '9606' , '9606'
                        }
                    },
                    'description': 'TEXT',
                    # EXAMPLES:
                    # 'DERMORPHIN' , 'PROCTOLIN' , 'NPY[TYR32,LEU34]' , 'YADAIFTNSYRKVLG CYCLO (ELSK) RKLLQDIMSR' , 'MYG
                    # GF' , 'GIGILTVIL' , 'TEPROTIDE' , 'EFEGATRAN SULFATE' , 'NEUROTENSIN' , 'Hu3F4 (mab)'
                    'helm_notation': 'TEXT',
                    # EXAMPLES:
                    # 'PEPTIDE1{A.S.N.E.N.M.E.T.M}$$$$' , 'PEPTIDE1{Y.[dA].F.G.Y.P.S.[am]}$$$$' , 'PEPTIDE1{E.G.Q.[X127]
                    # .E.G.I.[dP]}$$$$' , 'PEPTIDE1{A.L.Q.G.R.L.Q.R.L.L.Q.A.S.G.N.H.A.A.G.I.L.T.M}$$$$' , 'PEPTIDE1{[Glp
                    # ].P.L.P.[X2722].L.H.G.A.G.N.H.A.A.G.I.L.T.L}$$$$' , 'PEPTIDE1{[ac].F.C.S.D.Y.S.C.Y.L.[am]}$PEPTIDE
                    # 1,PEPTIDE1,8:R3-3:R3$$$' , 'PEPTIDE1{[ac].F.C.S.D.Y.S.C.Y.L.[am]}$$$$' , 'PEPTIDE1{C.Q.F.F.G.L.C.[
                    # am]}$$$$' , 'PEPTIDE1{C.F.[dF].G.[dL].[dC].[am]}$PEPTIDE1,PEPTIDE1,6:R3-1:R3$$$' , 'PEPTIDE1{R.[dW
                    # ].[dF].[lalloI].[dF].H.K.K.H.[am]}$$$$'
                    'molecule_chembl_id': 'TEXT',
                    # EXAMPLES:
                    # 'CHEMBL1554014' , 'CHEMBL278789' , 'CHEMBL26573' , 'CHEMBL429374' , 'CHEMBL411934' , 'CHEMBL412578
                    # ' , 'CHEMBL216417' , 'CHEMBL35773' , 'CHEMBL288132' , 'CHEMBL438205'
                }
            },
            'black_box_warning': 'NUMERIC',
            # EXAMPLES:
            # '0' , '0' , '0' , '0' , '0' , '0' , '0' , '0' , '0' , '0'
            'chebi_par_id': 'NUMERIC',
            # EXAMPLES:
            # '4388' , '89992' , '34498' , '38885' , '82534' , '16076' , '59328' , '3580' , '28818' , '75126'
            'chirality': 'NUMERIC',
            # EXAMPLES:
            # '-1' , '-1' , '-1' , '-1' , '-1' , '-1' , '-1' , '-1' , '-1' , '-1'
            'cross_references': 
            {
                'properties': 
                {
                    'xref_id': 'NUMERIC',
                    # EXAMPLES:
                    # '24787119' , '49733282' , '24841359' , '22406147' , '24839932' , '49733078' , '24834653' , '496675
                    # 84' , '24818566' , '26663220'
                    'xref_name': 'TEXT',
                    # EXAMPLES:
                    # 'SID: 24787119' , 'SID: 49733282' , 'SID: 24841359' , 'SID: 22406147' , 'SID: 24839932' , 'SID: 49
                    # 733078' , 'SID: 24834653' , 'SID: 49667584' , 'SID: 24818566' , 'SID: 26663220'
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
            # '1962' , '2003' , '1978' , '1979' , '1999' , '2003' , '1994' , '1985' , '2001' , '1997'
            'first_in_class': 'NUMERIC',
            # EXAMPLES:
            # '-1' , '-1' , '-1' , '-1' , '-1' , '-1' , '-1' , '-1' , '-1' , '-1'
            'helm_notation': 'TEXT',
            # EXAMPLES:
            # 'PEPTIDE1{A.S.N.E.N.M.E.T.M}$$$$' , 'PEPTIDE1{Y.[dA].F.G.Y.P.S.[am]}$$$$' , 'PEPTIDE1{E.G.Q.[X127].E.G.I.[
            # dP]}$$$$' , 'PEPTIDE1{A.L.Q.G.R.L.Q.R.L.L.Q.A.S.G.N.H.A.A.G.I.L.T.M}$$$$' , 'PEPTIDE1{[Glp].P.L.P.[X2722].
            # L.H.G.A.G.N.H.A.A.G.I.L.T.L}$$$$' , 'PEPTIDE1{[ac].F.C.S.D.Y.S.C.Y.L.[am]}$PEPTIDE1,PEPTIDE1,8:R3-3:R3$$$'
            #  , 'PEPTIDE1{[ac].F.C.S.D.Y.S.C.Y.L.[am]}$$$$' , 'PEPTIDE1{C.Q.F.F.G.L.C.[am]}$$$$' , 'PEPTIDE1{C.F.[dF].G
            # .[dL].[dC].[am]}$PEPTIDE1,PEPTIDE1,6:R3-1:R3$$$' , 'PEPTIDE1{R.[dW].[dF].[lalloI].[dF].H.K.K.H.[am]}$$$$'
            'indication_class': 'TEXT',
            # EXAMPLES:
            # 'Antitussive' , 'Antihistaminic' , 'Regulator (calcium)' , 'Anti-Inflammatory' , 'Analgesic; Anti-Inflamma
            # tory' , 'Anti-Inflammatory; Antipyretic; Analgesic' , 'Antineoplastic' , 'Tranquilizer' , 'Anti-Urolithic 
            # (cystine calculi)' , 'Antihyperlipoproteinemic'
            'inorganic_flag': 'NUMERIC',
            # EXAMPLES:
            # '-1' , '-1' , '-1' , '-1' , '-1' , '-1' , '-1' , '-1' , '-1' , '-1'
            'max_phase': 'NUMERIC',
            # EXAMPLES:
            # '0' , '0' , '0' , '0' , '0' , '0' , '0' , '0' , '0' , '0'
            'molecule_chembl_id': 'TEXT',
            # EXAMPLES:
            # 'CHEMBL1584351' , 'CHEMBL1584358' , 'CHEMBL1584363' , 'CHEMBL1584365' , 'CHEMBL1584367' , 'CHEMBL1584370' 
            # , 'CHEMBL1584374' , 'CHEMBL1584379' , 'CHEMBL1584380' , 'CHEMBL1584381'
            'molecule_hierarchy': 
            {
                'properties': 
                {
                    'molecule_chembl_id': 'TEXT',
                    # EXAMPLES:
                    # 'CHEMBL1584351' , 'CHEMBL1584358' , 'CHEMBL1584363' , 'CHEMBL1584365' , 'CHEMBL1584367' , 'CHEMBL1
                    # 584370' , 'CHEMBL1584374' , 'CHEMBL1584379' , 'CHEMBL1584380' , 'CHEMBL1584381'
                    'parent_chembl_id': 'TEXT',
                    # EXAMPLES:
                    # 'CHEMBL1584351' , 'CHEMBL1584358' , 'CHEMBL1584363' , 'CHEMBL1584365' , 'CHEMBL1584367' , 'CHEMBL1
                    # 584370' , 'CHEMBL1584374' , 'CHEMBL1584379' , 'CHEMBL1625293' , 'CHEMBL1625294'
                }
            },
            'molecule_properties': 
            {
                'properties': 
                {
                    'alogp': 'NUMERIC',
                    # EXAMPLES:
                    # '1.64' , '1.52' , '3.34' , '-0.63' , '3.44' , '3.20' , '3.97' , '4.16' , '1.01' , '0.43'
                    'aromatic_rings': 'NUMERIC',
                    # EXAMPLES:
                    # '2' , '1' , '3' , '2' , '3' , '2' , '3' , '3' , '1' , '0'
                    'cx_logd': 'NUMERIC',
                    # EXAMPLES:
                    # '2.06' , '1.13' , '1.07' , '-0.04' , '3.11' , '3.59' , '4.19' , '5.46' , '0.89' , '-3.39'
                    'cx_logp': 'NUMERIC',
                    # EXAMPLES:
                    # '2.06' , '1.13' , '3.84' , '-0.04' , '3.11' , '3.59' , '4.19' , '5.46' , '0.89' , '-3.39'
                    'cx_most_apka': 'NUMERIC',
                    # EXAMPLES:
                    # '2.04' , '11.76' , '11.46' , '13.06' , '13.90' , '4.23' , '9.18' , '12.94' , '12.54' , '12.60'
                    'cx_most_bpka': 'NUMERIC',
                    # EXAMPLES:
                    # '2.97' , '1.86' , '4.14' , '1.13' , '1.66' , '1.04' , '8.13' , '7.25' , '9.26' , '9.04'
                    'full_molformula': 'TEXT',
                    # EXAMPLES:
                    # 'C14H12N2O4S2' , 'C17H22N2O3' , 'C19H12N2O5' , 'C17H19ClN4O7S' , 'C23H28N4O4S2' , 'C19H24N4O' , 'C
                    # 18H17NO2S' , 'C16H11ClN2O' , 'C17H18N4O6' , 'C10H16ClNO2'
                    'full_mwt': 'NUMERIC',
                    # EXAMPLES:
                    # '336.39' , '302.37' , '348.31' , '458.88' , '488.64' , '324.43' , '311.41' , '282.73' , '374.35' ,
                    #  '217.70'
                    'hba': 'NUMERIC',
                    # EXAMPLES:
                    # '6' , '3' , '5' , '10' , '7' , '4' , '2' , '3' , '4' , '2'
                    'hba_lipinski': 'NUMERIC',
                    # EXAMPLES:
                    # '6' , '5' , '7' , '11' , '8' , '5' , '3' , '3' , '6' , '3'
                    'hbd': 'NUMERIC',
                    # EXAMPLES:
                    # '1' , '0' , '1' , '1' , '1' , '1' , '0' , '1' , '2' , '0'
                    'hbd_lipinski': 'NUMERIC',
                    # EXAMPLES:
                    # '1' , '0' , '1' , '2' , '1' , '1' , '0' , '1' , '2' , '0'
                    'heavy_atoms': 'NUMERIC',
                    # EXAMPLES:
                    # '22' , '22' , '26' , '30' , '33' , '24' , '22' , '20' , '21' , '13'
                    'molecular_species': 'TEXT',
                    # EXAMPLES:
                    # 'NEUTRAL' , 'NEUTRAL' , 'ACID' , 'NEUTRAL' , 'NEUTRAL' , 'NEUTRAL' , 'NEUTRAL' , 'NEUTRAL' , 'NEUT
                    # RAL' , 'NEUTRAL'
                    'mw_freebase': 'NUMERIC',
                    # EXAMPLES:
                    # '336.39' , '302.37' , '348.31' , '458.88' , '488.64' , '324.43' , '311.41' , '282.73' , '284.32' ,
                    #  '182.24'
                    'mw_monoisotopic': 'NUMERIC',
                    # EXAMPLES:
                    # '336.0238' , '302.1630' , '348.0746' , '458.0663' , '488.1552' , '324.1950' , '311.0980' , '282.05
                    # 60' , '284.1273' , '182.1176'
                    'num_lipinski_ro5_violations': 'NUMERIC',
                    # EXAMPLES:
                    # '0' , '0' , '0' , '1' , '0' , '0' , '0' , '0' , '0' , '0'
                    'num_ro5_violations': 'NUMERIC',
                    # EXAMPLES:
                    # '0' , '0' , '0' , '0' , '0' , '0' , '0' , '0' , '0' , '0'
                    'psa': 'NUMERIC',
                    # EXAMPLES:
                    # '84.83' , '49.85' , '110.40' , '150.77' , '93.53' , '58.12' , '37.38' , '46.01' , '82.92' , '26.30
                    # '
                    'qed_weighted': 'NUMERIC',
                    # EXAMPLES:
                    # '0.68' , '0.83' , '0.33' , '0.42' , '0.44' , '0.94' , '0.73' , '0.77' , '0.87' , '0.27'
                    'ro3_pass': 'TEXT',
                    # EXAMPLES:
                    # 'N' , 'N' , 'N' , 'N' , 'N' , 'N' , 'N' , 'N' , 'N' , 'N'
                    'rtb': 'NUMERIC',
                    # EXAMPLES:
                    # '4' , '2' , '5' , '7' , '10' , '4' , '3' , '2' , '3' , '5'
                }
            },
            'molecule_structures': 
            {
                'properties': 
                {
                    'canonical_smiles': 'TEXT',
                    # EXAMPLES:
                    # 'O=C(OCCNC1=NS(=O)(=O)c2ccccc21)c1cccs1' , 'Cc1ccc(N2CC(C(=O)N3CCOCC3)CC2=O)cc1C' , 'O=C(O)C(=O)/C
                    # (=C\c1ccc([N+](=O)[O-])cc1)c1ccc2ccccc2n1' , 'CN(CC(=O)OCC(=O)c1c(N)n(C)c(=O)n(C)c1=O)S(=O)(=O)c1c
                    # cc(Cl)cc1' , 'CCN(CC)S(=O)(=O)c1ccc2c(c1)nc(SCC(=O)NC1CC1)n2-c1ccccc1OC' , 'CCc1ccccc1NC(=O)C1CCCN
                    # (c2nccc(C)n2)C1' , 'Cc1ccc(S(=O)(=O)N(C)c2ccc3ccccc3c2)cc1' , 'Oc1nc(/C=C/c2ccccc2Cl)nc2ccccc12' ,
                    #  'CC1=NNC(=O)C1C(c1ccccc1)C1C(=O)NN=C1C.O=C(O)C(=O)O' , 'C#CCOC(=O)C[N+](C)(C)CC=C.[Cl-]'
                    'standard_inchi': 'TEXT',
                    # EXAMPLES:
                    # 'InChI=1S/C14H12N2O4S2/c17-14(11-5-3-9-21-11)20-8-7-15-13-10-4-1-2-6-12(10)22(18,19)16-13/h1-6,9H,
                    # 7-8H2,(H,15,16)' , 'InChI=1S/C17H22N2O3/c1-12-3-4-15(9-13(12)2)19-11-14(10-16(19)20)17(21)18-5-7-2
                    # 2-8-6-18/h3-4,9,14H,5-8,10-11H2,1-2H3' , 'InChI=1S/C19H12N2O5/c22-18(19(23)24)15(11-12-5-8-14(9-6-
                    # 12)21(25)26)17-10-7-13-3-1-2-4-16(13)20-17/h1-11H,(H,23,24)/b15-11-' , 'InChI=1S/C17H19ClN4O7S/c1-
                    # 20(30(27,28)11-6-4-10(18)5-7-11)8-13(24)29-9-12(23)14-15(19)21(2)17(26)22(3)16(14)25/h4-7H,8-9,19H
                    # 2,1-3H3' , 'InChI=1S/C23H28N4O4S2/c1-4-26(5-2)33(29,30)17-12-13-19-18(14-17)25-23(32-15-22(28)24-1
                    # 6-10-11-16)27(19)20-8-6-7-9-21(20)31-3/h6-9,12-14,16H,4-5,10-11,15H2,1-3H3,(H,24,28)' , 'InChI=1S/
                    # C19H24N4O/c1-3-15-7-4-5-9-17(15)22-18(24)16-8-6-12-23(13-16)19-20-11-10-14(2)21-19/h4-5,7,9-11,16H
                    # ,3,6,8,12-13H2,1-2H3,(H,22,24)' , 'InChI=1S/C18H17NO2S/c1-14-7-11-18(12-8-14)22(20,21)19(2)17-10-9
                    # -15-5-3-4-6-16(15)13-17/h3-13H,1-2H3' , 'InChI=1S/C16H11ClN2O/c17-13-7-3-1-5-11(13)9-10-15-18-14-8
                    # -4-2-6-12(14)16(20)19-15/h1-10H,(H,18,19,20)/b10-9+' , 'InChI=1S/C15H16N4O2.C2H2O4/c1-8-11(14(20)1
                    # 8-16-8)13(10-6-4-3-5-7-10)12-9(2)17-19-15(12)21;3-1(4)2(5)6/h3-7,11-13H,1-2H3,(H,18,20)(H,19,21);(
                    # H,3,4)(H,5,6)' , 'InChI=1S/C10H16NO2.ClH/c1-5-7-11(3,4)9-10(12)13-8-6-2;/h2,5H,1,7-9H2,3-4H3;1H/q+
                    # 1;/p-1'
                    'standard_inchi_key': 'TEXT',
                    # EXAMPLES:
                    # 'QTNRRYNCUTVURP-UHFFFAOYSA-N' , 'LUNLRCJOOSYTLZ-UHFFFAOYSA-N' , 'PSAKHUYUMWVJHU-PTNGSMBKSA-N' , 'O
                    # ATSQMAOFAXJRE-UHFFFAOYSA-N' , 'QKMFWQIPIYXGII-UHFFFAOYSA-N' , 'MBSXNOVOZXJLHZ-UHFFFAOYSA-N' , 'ZTV
                    # NQCYDGPRVLJ-UHFFFAOYSA-N' , 'GVTQWTBKPKRCFL-MDZDMXLPSA-N' , 'VDKWMTHFXXNSNH-UHFFFAOYSA-N' , 'UFNGJ
                    # UDWMLFVFD-UHFFFAOYSA-M'
                }
            },
            'molecule_synonyms': 
            {
                'properties': 
                {
                    'molecule_synonym': 'TEXT',
                    # EXAMPLES:
                    # 'DNDI1417155' , 'Decamethrin' , 'Harmine HCl' , '29866' , 'RP-49356' , 'Chartreusin' , '24, 25-dih
                    # ydroxycholecalciferol' , 'NSC-368252' , '2-Cinnamamidobenzamide' , 'Menthofuran'
                    'syn_type': 'TEXT',
                    # EXAMPLES:
                    # 'OTHER' , 'INN' , 'OTHER' , 'RESEARCH_CODE' , 'RESEARCH_CODE' , 'OTHER' , 'OTHER' , 'RESEARCH_CODE
                    # ' , 'OTHER' , 'OTHER'
                    'synonyms': 'TEXT',
                    # EXAMPLES:
                    # 'DNDI1417155' , 'Decamethrin' , 'Harmine Hydrochloride' , '29866' , 'RP-49356' , 'Chartreusin' , '
                    # 24, 25-DIHYDROXYCHOLECALCIFEROL' , 'NSC-368252' , '2-Cinnamamidobenzamide' , 'Menthofuran'
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
            # 'DELTAMETHRIN' , 'SERICETIN DIACETATE' , 'HARMINE HYDROCHLORIDE' , 'LEVOPROPOXYPHENE NAPSYLATE' , '2-HYDRO
            # XY-5 (6)EPOXY-TETRAHYDROCARYOPHYLLENE' , 'RHODOMYRTOXIN B' , 'ROTOXAMINE' , 'CHARTREUSIN' , 'SECALCIFEROL'
            #  , 'MENTHOFURAN'
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
            # '-calci-' , '-prazole' , '-imod' , '-ac' , '-pine' , '-profen' , '-citabine' , '-antrone' , '-afil' , '-ac
            # '
            'usan_stem_definition': 'TEXT',
            # EXAMPLES:
            # 'vitamin D analogues' , 'antiulcer agents (benzimidazole derivatives)' , 'immunomodulators' , 'anti-inflam
            # matory agents (acetic acid derivatives)' , 'tricyclic compounds' , 'anti-inflammatory/analgesic agents (ib
            # uprofen type)' , 'nucleoside antiviral or antineoplastic agents, cytarabine or azarabine derivatives' , 'a
            # ntineoplastics, anthraquinone derivatives' , 'PDE5 inhibitors' , 'anti-inflammatory agents (acetic acid de
            # rivatives)'
            'usan_substem': 'TEXT',
            # EXAMPLES:
            # '-calci-' , '-prazole' , '-imod' , '-ac' , '-pine' , '-profen' , '-citabine' , '-antrone' , '-afil' , '-ac
            # '
            'usan_year': 'NUMERIC',
            # EXAMPLES:
            # '1962' , '1989' , '2000' , '1978' , '1976' , '2003' , '1965' , '1992' , '1989' , '2001'
            'withdrawn_class': 'TEXT',
            # EXAMPLES:
            # 'Carcinogenicity; Dermatological toxicity' , 'Hematological toxicity' , 'Carcinogenicity; Gastrotoxicity' 
            # , 'Cardiotoxicity' , 'Dermatological toxicity' , 'Dermatological toxicity; Hematological toxicity; Hepatot
            # oxicity' , 'Hepatotoxicity; Misuse' , 'Cardiotoxicity' , 'Cardiotoxicity' , 'Neurotoxicity'
            'withdrawn_country': 'TEXT',
            # EXAMPLES:
            # 'United Kingdom' , 'France' , 'United Kingdom; Spain; Germany' , 'United States; United Kingdom; United St
            # ates; Germany' , 'United States' , 'United States' , 'Spain; Germany; France' , 'Germany' , 'Saudi Arabia;
            #  United States' , 'United Kingdom; Germany; Italy; Ireland; Netherlands; European Union'
            'withdrawn_flag': 'BOOLEAN',
            # EXAMPLES:
            # 'False' , 'False' , 'False' , 'False' , 'False' , 'False' , 'False' , 'False' , 'False' , 'False'
            'withdrawn_reason': 'TEXT',
            # EXAMPLES:
            # 'Cutaneous Reactions; Animal Carcinogenicity' , 'Agranulocytosis' , 'Animal Carcinogenicity (rodent); Gast
            # rointestinal Toxicity' , 'Cardiac repolarization; QTc interval prolongation' , 'Stevens Johnson Syndrome; 
            # Toxic Epidermal Necrolysis' , 'Dermatologic, Hematologic and Hepatic Reactions' , 'Severe hepatitis and li
            # ver failure (some requiring transplantation); Hepatic Failure; Off-Label Abuse' , 'Arrhythmias and Sudden 
            # Cardiac Death (Arrhythmias and Sudden)' , 'Torsade de pointes' , 'Polyneuropathy'
            'withdrawn_year': 'NUMERIC',
            # EXAMPLES:
            # '1984' , '1985' , '1983' , '1999' , '1983' , '1988' , '1998' , '1998' , '1998' , '1987'
        }
    }
