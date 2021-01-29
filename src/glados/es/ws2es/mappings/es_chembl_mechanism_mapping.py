# Elastic search mapping definition for the Molecule entity
from glados.es.ws2es.es_util import DefaultMappings

# Shards size - can be overridden from the default calculated value here
# shards = 3,
replicas = 0

analysis = DefaultMappings.COMMON_ANALYSIS

mappings = \
    {
        'properties':
        {
            'action_type': DefaultMappings.KEYWORD,
            # EXAMPLES:
            # 'ANTAGONIST' , 'ANTAGONIST' , 'ANTAGONIST' , 'ANTAGONIST' , 'ANTAGONIST' , 'ANTAGONIST' , 'ANTAGONIST'
            #  , 'ANTAGONIST' , 'ANTAGONIST' , 'ANTAGONIST'
            'binding_site_comment': DefaultMappings.TEXT_STD,
            # EXAMPLES:
            # 'Beta subunit is binding site' , 'Alpha subunit is likely binding site' , 'Alpha subunit is likely bin
            # ding site' , 'Alpha subunit is likely binding site' , 'Alpha subunit is likely binding site' , 'Alpha
            # subunit is likely binding site' , 'Alpha subunit is likely binding site' , 'Alpha subunit is likely bi
            # nding site' , 'Alpha subunit is likely binding site' , 'Binds to beta tubulin'
            'direct_interaction': DefaultMappings.BOOLEAN,
            # EXAMPLES:
            # 'True' , 'True' , 'True' , 'True' , 'True' , 'True' , 'True' , 'True' , 'True' , 'True'
            'disease_efficacy': DefaultMappings.BOOLEAN,
            # EXAMPLES:
            # 'True' , 'True' , 'True' , 'True' , 'True' , 'True' , 'True' , 'True' , 'True' , 'True'
            'max_phase': DefaultMappings.SHORT,
            # EXAMPLES:
            # '4' , '4' , '4' , '4' , '4' , '4' , '4' , '4' , '4' , '4'
            'mec_id': DefaultMappings.ID_REF,
            # EXAMPLES:
            # '166' , '167' , '168' , '169' , '170' , '171' , '172' , '173' , '174' , '175'
            'mechanism_comment': DefaultMappings.TEXT_STD,
            # EXAMPLES:
            # 'Antiemetic' , 'Long acting' , 'Should be protein complex but not trivial to define' , 'targets ozogam
            # icin to cell' , 'Prodrug enzyme: FAD-containing monooxygenase (EthA)' , 'It's LH, used to stimulate de
            # velopment of a potentially competent follicle and to indirectly prepare the reproductive tract for imp
            # lantation and pregnancy' , 'Role in regulating gastric secretion, M1 likely involved' , 'Role in regul
            # ating gastric secretion, M1 likely involved' , 'Role in regulating gastric secretion, M1 likely involv
            # ed' , 'Role in regulating gastric secretion, M1 likely involved'
            'mechanism_of_action': DefaultMappings.TEXT_STD,
            # EXAMPLES:
            # 'Histamine H1 receptor antagonist' , 'Histamine H1 receptor antagonist' , 'Histamine H1 receptor antag
            # onist' , 'Histamine H1 receptor antagonist' , 'Histamine H1 receptor antagonist' , 'Histamine H1 recep
            # tor antagonist' , 'Histamine H1 receptor antagonist' , 'Histamine H1 receptor antagonist' , 'Histamine
            #  H1 receptor antagonist' , 'Histamine H1 receptor antagonist'
            'mechanism_refs':
            {
                'properties':
                {
                    'ref_id': DefaultMappings.ID_REF,
                    # EXAMPLES:
                    # '6113566' , 'setid=2965ef46-18db-4615-9dce-bfb0f0b3366a' , 'setid=adba6255-f2be-4958-9e95-9300
                    # 0aff74f6' , '22445882' , '9780702034718 PP. 332' , 'D02089' , '11835984' , 'setid=98a010d5-490
                    # 5-4abf-a9d2-c85a07daa23b' , '19790517' , '16702624'
                    'ref_type': DefaultMappings.KEYWORD,
                    # EXAMPLES:
                    # 'PubMed' , 'DailyMed' , 'DailyMed' , 'PubMed' , 'ISBN' , 'KEGG' , 'PubMed' , 'DailyMed' , 'Pub
                    # Med' , 'PubMed'
                    'ref_url': DefaultMappings.KEYWORD,
                    # EXAMPLES:
                    # 'http://europepmc.org/abstract/MED/6113566' , 'http://dailymed.nlm.nih.gov/dailymed/lookup.cfm
                    # ?setid=2965ef46-18db-4615-9dce-bfb0f0b3366a' , 'http://dailymed.nlm.nih.gov/dailymed/lookup.cf
                    # m?setid=adba6255-f2be-4958-9e95-93000aff74f6' , 'http://europepmc.org/abstract/MED/22445882' ,
                    #  'http://www.isbnsearch.org/isbn/9780702034718' , 'http://www.kegg.jp/dbget-bin/www_bget?dr:D0
                    # 2089' , 'http://europepmc.org/abstract/MED/11835984' , 'http://dailymed.nlm.nih.gov/dailymed/l
                    # ookup.cfm?setid=98a010d5-4905-4abf-a9d2-c85a07daa23b' , 'http://europepmc.org/abstract/MED/197
                    # 90517' , 'http://europepmc.org/abstract/MED/16702624'
                }
            },
            'molecular_mechanism': DefaultMappings.BOOLEAN,
            # EXAMPLES:
            # 'True' , 'True' , 'True' , 'True' , 'True' , 'True' , 'True' , 'True' , 'True' , 'True'
            'molecule_chembl_id': DefaultMappings.CHEMBL_ID_REF,
            # EXAMPLES:
            # 'CHEMBL1200550' , 'CHEMBL1201190' , 'CHEMBL1201759' , 'CHEMBL1564' , 'CHEMBL1633' , 'CHEMBL1200403' ,
            # 'CHEMBL1200406' , 'CHEMBL2103739' , 'CHEMBL1200959' , 'CHEMBL1201089'
            'parent_molecule_chembl_id': DefaultMappings.CHEMBL_ID_REF,
            # EXAMPLES:
            # 'CHEMBL1200550' , 'CHEMBL1201190' , 'CHEMBL1201759' , 'CHEMBL1564' , 'CHEMBL1633' , 'CHEMBL1200403' ,
            # 'CHEMBL1200406' , 'CHEMBL2103739' , 'CHEMBL1200959' , 'CHEMBL1201089'
            'record_id': DefaultMappings.ID_REF,
            # EXAMPLES:
            # '1343582' , '1344728' , '1344930' , '1344448' , '1343356' , '1343121' , '1344489' , '1343469' , '13435
            # 46' , '1344509'
            'selectivity_comment': DefaultMappings.KEYWORD,
            # EXAMPLES:
            # 'Selective' , 'Selective' , 'Selective' , 'Selective' , 'Selective' , 'Selective' , 'Selective' , 'Sel
            # ective' , 'Selective' , 'Selective'
            'site_id': DefaultMappings.ID_REF,
            # EXAMPLES:
            # '2643' , '2651' , '2651' , '2651' , '2651' , '2651' , '2651' , '2651' , '2651' , '2627'
            'target_chembl_id': DefaultMappings.CHEMBL_ID_REF,
            # EXAMPLES:
            # 'CHEMBL231' , 'CHEMBL231' , 'CHEMBL231' , 'CHEMBL231' , 'CHEMBL231' , 'CHEMBL231' , 'CHEMBL231' , 'CHE
            # MBL231' , 'CHEMBL231' , 'CHEMBL231'
            'variant_sequence':
            {
                'properties':
                {
                    'accession': DefaultMappings.LOWER_CASE_KEYWORD,
                    # EXAMPLES:
                    # 'P12931' , 'Q72874' , 'Q72874' , 'P41597' , 'P0DMS8' , 'P29274' , 'P29274' , 'P29274' , 'P41597' ,
                    #  'P16455'
                    'isoform': DefaultMappings.SHORT,
                    # EXAMPLES:
                    # '1' , '1' , '1' , '1' , '1' , '1' , '1' , '1' , '1' , '1'
                    'mutation': DefaultMappings.LOWER_CASE_KEYWORD,
                    # EXAMPLES:
                    # 'C188A' , 'G48V' , 'V82F' , 'D284A' , 'H95A' , 'H278D' , 'H278E' , 'T88E' , 'H121A' , 'G160R'
                    'organism': DefaultMappings.LOWER_CASE_KEYWORD,
                    # EXAMPLES:
                    # 'Homo sapiens' , 'Human immunodeficiency virus 1' , 'Human immunodeficiency virus 1' , 'Homo sapie
                    # ns' , 'Homo sapiens' , 'Homo sapiens' , 'Homo sapiens' , 'Homo sapiens' , 'Homo sapiens' , 'Homo s
                    # apiens'
                    'sequence': DefaultMappings.LOWER_CASE_KEYWORD,
                    # EXAMPLES:
                    # 'MGSNKSKPKDASQRRRSLEPAENVHGAGGGAFPASQTPSKPASADGHRGPSAAFAPAAAEPKLFGGFNSSDTVTSPQRAGPLAGGVTTFVALYDYES
                    # RTETDLSFKKGERLQIVNNTEGDWWLAHSLSTGQTGYIPSNYVAPSDSIQAEEWYFGKITRRESERLLLNAENPRGTFLVRESETTKGAYALSVSDFD
                    # NAKGLNVKHYKIRKLDSGGFYITSRTQFNSLQQLVAYYSKHADGLCHRLTTVCPTSKPQTQGLAKDAWEIPRESLRLEVKLGQGCFGEVWMGTWNGTT
                    # RVAIKTLKPGTMSPEAFLQEAQVMKKLRHEKLVQLYAVVSEEPIYIVTEYMSKGSLLDFLKGETGKYLRLPQLVDMAAQIASGMAYVERMNYVHRDLR
                    # AANILVGENLVCKVADFGLARLIEDNEYTARQGAKFPIKWTAPEAALYGRFTIKSDVWSFGILLTELTTKGRVPYPGMVNREVLDQVERGYRMPCPPE
                    # CPESLHDLMCQCWRKEPEERPTFEYLQAFLEDYFTSTEPQYQPGENL' , 'PQVTLWQRPLVTIKIGGQLKEALLDTGADDTVLEEMSLPGRWKPKM
                    # IVGIGGFIKVRQYDQILIEICGHKAIGTVLVGPTPVNIIGRNLLTQIGCTLNF' , 'PQVTLWQRPLVTIKIGGQLKEALLDTGADDTVLEEMSLPG
                    # RWKPKMIGGIGGFIKVRQYDQILIEICGHKAIGTVLVGPTPFNIIGRNLLTQIGCTLNF' , 'MLSTSRSRFIRNTNESGEEVTTFFDYDYGAPCHK
                    # FDVKQIGAQLLPPLYSLVFIFGFVGNMLVVLILINCKKLKCLTDIYLLNLAISDLLFLITLPLWAHSAANEWVFGNAMCKLFTGLYHIGYFGGIFFII
                    # LLTIDRYLAIVHAVFALKARTVTFGVVTSVITWLVAVFASVPGIIFTKCQKEDSVYVCGPYFPRGWNNFHTIMRNILGLVLPLLIMVICYSGILKTLL
                    # RCRNEKKRHRAVRVIFTIMIVYFLFWTPYNIVILLNTFQEFFGLSNCESTSQLAQATQVTETLGMTHCCINPIIYAFVGEKFRSLFHIALGCRIAPLQ
                    # KPVCGGPGVRPGKNVKVTTQGLLDGRGKGKSIGRAPEASLQDKEGA' , 'MPNNSTALSLANVTYITMEIFIGLCAIVGNVLVICVVKLNPSLQTTT
                    # FYFIVSLALADIAVGVLVMPLAIVVSLGITIHFYSCLFMTCLLLIFTAASIMSLLAIAVDRYLRVKLTVRYKRVTTHRRIWLALGLCWLVSFLVGLTP
                    # MFGWNMKLTSEYHRNVTFLSCQFVSVMRMDYMVYFSFLTWIFIPLVVMCAIYLDIFYIIRNKLSLNLSNSKETGAFYGREFKTAKSLFLVLFLFALSW
                    # LPLSIINCIIYFNGEVPQLVLYMGILLSHANSMMNPIVYAYKIKKFKETYLLILKACVVCHPSDSLDTSIEKNSE' , 'MPIMGSSVYITVELAIAV
                    # LAILGNVLVCWAVWLNSNLQNVTNYFVVSLAAADIAVGVLAIPFAITISTGFCAACHGCLFIACFVLVLTQSSIFSLLAIAIDRYIAIRIPLRYNGLV
                    # TGTRAKGIIAICWVLSFAIGLTPMLGWNNCGQPKEGKNHSQGCGEGQVACLFEDVVPMNYMVYFNFFACVLVPLLLMLGVYLRIFLAARRQLKQMESQ
                    # PLPGERARSTLQKEVHAAKSLAIIVGLFALCWLPLHIINCFTFFCPDCSHAPLWLMYLAIVLSDTNSVVNPFIYAYRIREFRQTFRKIIRSHVLRQQE
                    # PFKAAGTSARVLAAHGSDGEQVSLRLNGHPPGVWANGSAPHPERRPNGYALGLVSGGSAQESQGNTGLPDVELLSHELKGVCPEPPGLDDPLAQDGAG
                    # VS' , 'MPIMGSSVYITVELAIAVLAILGNVLVCWAVWLNSNLQNVTNYFVVSLAAADIAVGVLAIPFAITISTGFCAACHGCLFIACFVLVLTQSS
                    # IFSLLAIAIDRYIAIRIPLRYNGLVTGTRAKGIIAICWVLSFAIGLTPMLGWNNCGQPKEGKNHSQGCGEGQVACLFEDVVPMNYMVYFNFFACVLVP
                    # LLLMLGVYLRIFLAARRQLKQMESQPLPGERARSTLQKEVHAAKSLAIIVGLFALCWLPLHIINCFTFFCPDCSHAPLWLMYLAIVLSETNSVVNPFI
                    # YAYRIREFRQTFRKIIRSHVLRQQEPFKAAGTSARVLAAHGSDGEQVSLRLNGHPPGVWANGSAPHPERRPNGYALGLVSGGSAQESQGNTGLPDVEL
                    # LSHELKGVCPEPPGLDDPLAQDGAGVS' , 'MPIMGSSVYITVELAIAVLAILGNVLVCWAVWLNSNLQNVTNYFVVSLAAADIAVGVLAIPFAITI
                    # STGFCAACHGCLFIACFVLVLEQSSIFSLLAIAIDRYIAIRIPLRYNGLVTGTRAKGIIAICWVLSFAIGLTPMLGWNNCGQPKEGKNHSQGCGEGQV
                    # ACLFEDVVPMNYMVYFNFFACVLVPLLLMLGVYLRIFLAARRQLKQMESQPLPGERARSTLQKEVHAAKSLAIIVGLFALCWLPLHIINCFTFFCPDC
                    # SHAPLWLMYLAIVLSHTNSVVNPFIYAYRIREFRQTFRKIIRSHVLRQQEPFKAAGTSARVLAAHGSDGEQVSLRLNGHPPGVWANGSAPHPERRPNG
                    # YALGLVSGGSAQESQGNTGLPDVELLSHELKGVCPEPPGLDDPLAQDGAGVS' , 'MLSTSRSRFIRNTNESGEEVTTFFDYDYGAPCHKFDVKQIG
                    # AQLLPPLYSLVFIFGFVGNMLVVLILINCKKLKCLTDIYLLNLAISDLLFLITLPLWAHSAANEWVFGNAMCKLFTGLYAIGYFGGIFFIILLTIDRY
                    # LAIVHAVFALKARTVTFGVVTSVITWLVAVFASVPGIIFTKCQKEDSVYVCGPYFPRGWNNFHTIMRNILGLVLPLLIMVICYSGILKTLLRCRNEKK
                    # RHRAVRVIFTIMIVYFLFWTPYNIVILLNTFQEFFGLSNCESTSQLDQATQVTETLGMTHCCINPIIYAFVGEKFRSLFHIALGCRIAPLQKPVCGGP
                    # GVRPGKNVKVTTQGLLDGRGKGKSIGRAPEASLQDKEGA' , 'MDKDCEMKRTTLDSPLGKLELSGCEQGLHEIKLLGKGTSAADAVEVPAPAAVLG
                    # GPEPLMQCTAWLNAYFHQPEAIEEFPVPALHHPVFQQESFTRQVLWKLLKVVKFGEVISYQQLAALAGNPKAARAVGGAMRGNPVPILIPCHRVVCSS
                    # GAVGNYSRGLAVKEWLLAHEGHRLGKPGLGGSSGLAGAWLKGAGATSGSPPAGRN'
                    'tax_id': DefaultMappings.ID_REF,
                    # EXAMPLES:
                    # '9606' , '11676' , '11676' , '9606' , '9606' , '9606' , '9606' , '9606' , '9606' , '9606'
                    'version': DefaultMappings.SHORT,
                    # EXAMPLES:
                    # '3' , '1' , '1' , '1' , '1' , '2' , '2' , '2' , '1' , '1'
                }
            }
        }
    }
