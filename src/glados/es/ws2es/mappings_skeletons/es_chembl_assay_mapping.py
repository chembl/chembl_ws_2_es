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
                    # '{'input': 'CHEMBL1125695', 'weight': 10}' , '{'input': 'CHEMBL1125695', 'weight': 10}' , '{'input
                    # ': 'CHEMBL1125695', 'weight': 10}' , '{'input': 'CHEMBL1125695', 'weight': 10}' , '{'input': 'CHEM
                    # BL1125695', 'weight': 10}' , '{'input': 'CHEMBL1125695', 'weight': 10}' , '{'input': 'CHEMBL112569
                    # 5', 'weight': 10}' , '{'input': 'CHEMBL1125695', 'weight': 10}' , '{'input': 'CHEMBL1126449', 'wei
                    # ght': 10}' , '{'input': 'BAO_0000019', 'weight': 10}'
                }
            },
            'assay_category': 'TEXT',
            # EXAMPLES:
            # 'confirmatory' , 'confirmatory' , 'confirmatory' , 'confirmatory' , 'confirmatory' , 'confirmatory' , 'con
            # firmatory' , 'confirmatory' , 'confirmatory' , 'confirmatory'
            'assay_cell_type': 'TEXT',
            # EXAMPLES:
            # 'ATH-8 cell line' , 'ATH-8 cell line' , 'ATH-8 cell line' , 'ATH-8 cell line' , 'ATH-8 cell line' , 'ATH-8
            #  cell line' , 'ATH-8 cell line' , 'ATH-8 cell line' , 'CHO' , 'ATH-8 cell line'
            'assay_chembl_id': 'TEXT',
            # EXAMPLES:
            # 'CHEMBL645191' , 'CHEMBL645192' , 'CHEMBL645193' , 'CHEMBL645194' , 'CHEMBL641996' , 'CHEMBL641997' , 'CHE
            # MBL642665' , 'CHEMBL642666' , 'CHEMBL642834' , 'CHEMBL642837'
            'assay_classifications': 
            {
                'properties': 
                {
                    'assay_class_id': 'NUMERIC',
                    # EXAMPLES:
                    # '114' , '267' , '267' , '267' , '267' , '267' , '140' , '91' , '91' , '115'
                    'class_type': 'TEXT',
                    # EXAMPLES:
                    # 'In vivo efficacy' , 'In vivo efficacy' , 'In vivo efficacy' , 'In vivo efficacy' , 'In vivo effic
                    # acy' , 'In vivo efficacy' , 'In vivo efficacy' , 'In vivo efficacy' , 'In vivo efficacy' , 'In viv
                    # o efficacy'
                    'l1': 'TEXT',
                    # EXAMPLES:
                    # 'ANTINEOPLASTIC AND IMMUNOMODULATING AGENTS' , 'GENITO URINARY SYSTEM AND SEX HORMONES' , 'GENITO 
                    # URINARY SYSTEM AND SEX HORMONES' , 'GENITO URINARY SYSTEM AND SEX HORMONES' , 'GENITO URINARY SYST
                    # EM AND SEX HORMONES' , 'GENITO URINARY SYSTEM AND SEX HORMONES' , 'CARDIOVASCULAR SYSTEM' , 'ANTIN
                    # EOPLASTIC AND IMMUNOMODULATING AGENTS' , 'ANTINEOPLASTIC AND IMMUNOMODULATING AGENTS' , 'ANTINEOPL
                    # ASTIC AND IMMUNOMODULATING AGENTS'
                    'l2': 'TEXT',
                    # EXAMPLES:
                    # 'Methods for Testing Immunological Factors' , 'Diuretic and Saluretic Activity' , 'Diuretic and Sa
                    # luretic Activity' , 'Diuretic and Saluretic Activity' , 'Diuretic and Saluretic Activity' , 'Diure
                    # tic and Saluretic Activity' , 'Anti-Arrhythmic Activity' , 'Melanoma Oncology Models' , 'Melanoma 
                    # Oncology Models' , 'Neoplasm Oncology Models'
                    'l3': 'TEXT',
                    # EXAMPLES:
                    # 'Spontaneous Autoimmune Diseases In Animals' , 'Saluretic Activity in Rats' , 'Saluretic Activity 
                    # in Rats' , 'Saluretic Activity in Rats' , 'Saluretic Activity in Rats' , 'Saluretic Activity in Ra
                    # ts' , 'General Anti-Arrhythmic Activity' , 'Experimental Melanoma' , 'Experimental Melanoma' , 'Ne
                    # oplasms'
                    'source': 'TEXT',
                    # EXAMPLES:
                    # 'Vogel_2008' , 'Vogel_2008' , 'Vogel_2008' , 'Vogel_2008' , 'Vogel_2008' , 'Vogel_2008' , 'phenoty
                    # pe' , 'phenotype' , 'phenotype' , 'phenotype'
                }
            },
            'assay_organism': 'TEXT',
            # EXAMPLES:
            # 'Homo sapiens' , 'Homo sapiens' , 'Homo sapiens' , 'Homo sapiens' , 'Homo sapiens' , 'Homo sapiens' , 'Hom
            # o sapiens' , 'Homo sapiens' , 'Rattus norvegicus' , 'Rattus norvegicus'
            'assay_parameters': 
            {
                'properties': 
                {
                    'active': 'NUMERIC',
                    # EXAMPLES:
                    # '1' , '1' , '1' , '1' , '1' , '1' , '1' , '1' , '1' , '1'
                    'comments': 'TEXT',
                    # EXAMPLES:
                    # 'Is the measured interaction considered due to direct binding to target?' , 'Is the measured inter
                    # action considered due to direct binding to target?' , 'Is the measured interaction considered due 
                    # to direct binding to target?' , 'Is the measured interaction considered due to direct binding to t
                    # arget?' , 'Is the measured interaction considered due to direct binding to target?' , 'Is the meas
                    # ured interaction considered due to direct binding to target?' , 'Is the measured interaction consi
                    # dered due to direct binding to target?' , 'Is the measured interaction considered due to direct bi
                    # nding to target?' , 'Is the measured interaction considered due to direct binding to target?' , 'I
                    # s the measured interaction considered due to direct binding to target?'
                    'relation': 'TEXT',
                    # EXAMPLES:
                    # '=' , '=' , '=' , '=' , '=' , '=' , '=' , '=' , '=' , '='
                    'standard_relation': 'TEXT',
                    # EXAMPLES:
                    # '=' , '=' , '=' , '=' , '=' , '=' , '=' , '=' , '=' , '='
                    'standard_text_value': 'TEXT',
                    # EXAMPLES:
                    # 'Oral' , 'Oral' , 'Oral' , 'Oral' , 'Oral' , 'Oral' , 'Subcutaneous' , 'Subcutaneous' , 'Intraperi
                    # toneal' , 'Oral'
                    'standard_type': 'TEXT',
                    # EXAMPLES:
                    # 'DOSE' , 'DOSE' , 'DOSE' , 'DOSE' , 'DOSE' , 'ROUTE' , 'ROUTE' , 'ROUTE' , 'DOSE' , 'DOSE'
                    'standard_type_fixed': 'NUMERIC',
                    # EXAMPLES:
                    # '0' , '0' , '0' , '0' , '0' , '0' , '0' , '0' , '0' , '0'
                    'standard_units': 'TEXT',
                    # EXAMPLES:
                    # 'mg.kg-1' , 'mg.kg-1' , 'mg.kg-1' , 'mg.kg-1' , 'mg.kg-1' , 'mg.kg-1' , 'mg.kg-1' , 'mg.kg-1' , 'm
                    # g.kg-1' , 'mg.kg-1'
                    'standard_value': 'NUMERIC',
                    # EXAMPLES:
                    # '10.0' , '10.0' , '60.0' , '20.0' , '200.0' , '50.0' , '0.0625' , '1.0' , '0.0' , '10.0'
                    'text_value': 'TEXT',
                    # EXAMPLES:
                    # 'Oral' , 'Oral' , 'Oral' , 'Oral' , 'Oral' , 'Oral' , 'Subcutaneous' , 'Subcutaneous' , 'Intraperi
                    # toneal' , 'Oral'
                    'type': 'TEXT',
                    # EXAMPLES:
                    # 'DOSE' , 'DOSE' , 'DOSE' , 'DOSE' , 'DOSE' , 'ROUTE' , 'ROUTE' , 'ROUTE' , 'DOSE' , 'DOSE'
                    'units': 'TEXT',
                    # EXAMPLES:
                    # 'mg/kg' , 'mg/kg' , 'mg/kg' , 'mg/kg' , 'mg/kg' , 'mg/kg' , 'mg/kg' , 'mg/kg' , 'mg/kg' , 'mg/kg'
                    'value': 'NUMERIC',
                    # EXAMPLES:
                    # '10.0' , '10.0' , '60.0' , '20.0' , '200.0' , '50.0' , '0.0625' , '1.0' , '0.0' , '10.0'
                }
            },
            'assay_strain': 'TEXT',
            # EXAMPLES:
            # 'nigeriensis' , 'nigeriensis' , 'nigeriensis' , 'nigeriensis' , 'nigeriensis' , 'WRL CN 375' , 'Sprague-Da
            # wley' , 'beagle' , 'SR3637' , 'SR26840'
            'assay_subcellular_fraction': 'TEXT',
            # EXAMPLES:
            # 'Brain membranes' , 'Brain membranes' , 'Membrane' , 'Brain membranes' , 'Membrane' , 'Membrane' , 'Brain 
            # membranes' , 'Membrane' , 'Membrane' , 'Membrane'
            'assay_tax_id': 'NUMERIC',
            # EXAMPLES:
            # '9606' , '9606' , '9606' , '9606' , '9606' , '9606' , '9606' , '9606' , '10116' , '10116'
            'assay_test_type': 'TEXT',
            # EXAMPLES:
            # 'In vitro' , 'In vivo' , 'In vivo' , 'In vivo' , 'In vivo' , 'In vivo' , 'In vivo' , 'In vivo' , 'In vivo'
            #  , 'In vivo'
            'assay_tissue': 'TEXT',
            # EXAMPLES:
            # 'Brain' , 'Brain' , 'Brain' , 'Ileum' , 'Brain' , 'Brain' , 'Brain' , 'Cardiac atrium' , 'Lung' , 'Liver'
            'assay_type': 'TEXT',
            # EXAMPLES:
            # 'F' , 'F' , 'F' , 'F' , 'F' , 'F' , 'A' , 'A' , 'B' , 'B'
            'assay_type_description': 'TEXT',
            # EXAMPLES:
            # 'Functional' , 'Functional' , 'Functional' , 'Functional' , 'Functional' , 'Functional' , 'ADME' , 'ADME' 
            # , 'Binding' , 'Binding'
            'bao_format': 'TEXT',
            # EXAMPLES:
            # 'BAO_0000219' , 'BAO_0000219' , 'BAO_0000219' , 'BAO_0000219' , 'BAO_0000219' , 'BAO_0000219' , 'BAO_00002
            # 19' , 'BAO_0000219' , 'BAO_0000218' , 'BAO_0000019'
            'bao_label': 'TEXT',
            # EXAMPLES:
            # 'cell-based format' , 'cell-based format' , 'cell-based format' , 'cell-based format' , 'cell-based format
            # ' , 'cell-based format' , 'cell-based format' , 'cell-based format' , 'organism-based format' , 'assay for
            # mat'
            'cell_chembl_id': 'TEXT',
            # EXAMPLES:
            # 'CHEMBL3307903' , 'CHEMBL3307903' , 'CHEMBL3307903' , 'CHEMBL3307903' , 'CHEMBL3307903' , 'CHEMBL3307903' 
            # , 'CHEMBL3307903' , 'CHEMBL3307903' , 'CHEMBL3308072' , 'CHEMBL3307903'
            'confidence_description': 'TEXT',
            # EXAMPLES:
            # 'Default value - Target unknown or has yet to be assigned' , 'Default value - Target unknown or has yet to
            #  be assigned' , 'Default value - Target unknown or has yet to be assigned' , 'Default value - Target unkno
            # wn or has yet to be assigned' , 'Default value - Target unknown or has yet to be assigned' , 'Default valu
            # e - Target unknown or has yet to be assigned' , 'Default value - Target unknown or has yet to be assigned'
            #  , 'Default value - Target unknown or has yet to be assigned' , 'Homologous single protein target assigned
            # ' , 'Homologous single protein target assigned'
            'confidence_score': 'NUMERIC',
            # EXAMPLES:
            # '0' , '0' , '0' , '0' , '0' , '0' , '0' , '0' , '8' , '8'
            'description': 'TEXT',
            # EXAMPLES:
            # 'Anti-HIV activity (% protection) in ATH-8 cells at 5 uM in presence of 2'-deoxycoformycin at 50 uM' , 'An
            # ti-HIV activity (% protection) in ATH-8 cells at 5 uM in absence of 2'-deoxycoformycin at 0 uM' , 'Anti-HI
            # V activity (% protection) in ATH-8 cells at 5 uM in absence of 2'-deoxycoformycin at 20 uM' , 'Anti-HIV ac
            # tivity (% protection) in ATH-8 cells at 5 uM in absence of 2'-deoxycoformycin at 50 uM' , 'Anti-HIV activi
            # ty (%protection) in ATH-8 cells at 5 uM in absence of 2''-deoxycoformycin at 100 uM' , 'Anti-HIV activity 
            # (%protection) in ATH-8 cells at 5 uM in absence of 2''-deoxycoformycin at 50 uM' , 'Anti-HIV activity (% t
            # oxicity) in ATH-8 cells at 5 uM in absence of 2'-deoxycoformycin at 10 uM' , 'Anti-HIV activity (% toxicit
            # y) in ATH-8 cells at 5 uM in absence of 2'-deoxycoformycin at 100 uM' , 'Acetylcholinesterase (AChE) enzym
            # e was inhibited after oral administration of 10 mg/kg of compound in rat brain ex vivo assay; NI means no 
            # inhibition' , 'Percent activity of rat brain acetylcholinesterase on 5 hours incubation with 5 uM of compo
            # und at 25 degree C followed by reactivation with 0.5 mM 2-PAM after 20h'
            'document_chembl_id': 'TEXT',
            # EXAMPLES:
            # 'CHEMBL1125695' , 'CHEMBL1125695' , 'CHEMBL1125695' , 'CHEMBL1125695' , 'CHEMBL1125695' , 'CHEMBL1125695' 
            # , 'CHEMBL1125695' , 'CHEMBL1125695' , 'CHEMBL1126449' , 'CHEMBL1122429'
            'relationship_description': 'TEXT',
            # EXAMPLES:
            # 'Default value - Target has yet to be curated' , 'Default value - Target has yet to be curated' , 'Default
            #  value - Target has yet to be curated' , 'Default value - Target has yet to be curated' , 'Default value -
            #  Target has yet to be curated' , 'Default value - Target has yet to be curated' , 'Default value - Target 
            # has yet to be curated' , 'Default value - Target has yet to be curated' , 'Homologous protein target assig
            # ned' , 'Homologous protein target assigned'
            'relationship_type': 'TEXT',
            # EXAMPLES:
            # 'U' , 'U' , 'U' , 'U' , 'U' , 'U' , 'U' , 'U' , 'H' , 'H'
            'src_assay_id': 'NUMERIC',
            # EXAMPLES:
            # '566219' , '566216' , '567033' , '566896' , '566888' , '566887' , '566886' , '566878' , '566876' , '566874
            # '
            'src_id': 'NUMERIC',
            # EXAMPLES:
            # '1' , '1' , '1' , '1' , '1' , '1' , '1' , '1' , '1' , '1'
            'target_chembl_id': 'TEXT',
            # EXAMPLES:
            # 'CHEMBL612558' , 'CHEMBL612558' , 'CHEMBL612558' , 'CHEMBL612558' , 'CHEMBL612558' , 'CHEMBL612558' , 'CHE
            # MBL612558' , 'CHEMBL612558' , 'CHEMBL3199' , 'CHEMBL3199'
            'tissue_chembl_id': 'TEXT',
            # EXAMPLES:
            # 'CHEMBL3638188' , 'CHEMBL3638188' , 'CHEMBL3638188' , 'CHEMBL3638244' , 'CHEMBL3638188' , 'CHEMBL3638188' 
            # , 'CHEMBL3638188' , 'CHEMBL3638237' , 'CHEMBL3638235' , 'CHEMBL3559723'
            'variant_sequence': 
            {
                'properties': 
                {
                    'accession': 'TEXT',
                    # EXAMPLES:
                    # 'P12931' , 'Q72874' , 'Q72874' , 'P41597' , 'P0DMS8' , 'P29274' , 'P29274' , 'P29274' , 'P41597' ,
                    #  'P16455'
                    'isoform': 'NUMERIC',
                    # EXAMPLES:
                    # '1' , '1' , '1' , '1' , '1' , '1' , '1' , '1' , '1' , '1'
                    'mutation': 'TEXT',
                    # EXAMPLES:
                    # 'C188A' , 'G48V' , 'V82F' , 'D284A' , 'H95A' , 'H278D' , 'H278E' , 'T88E' , 'H121A' , 'G160R'
                    'organism': 'TEXT',
                    # EXAMPLES:
                    # 'Homo sapiens' , 'Human immunodeficiency virus 1' , 'Human immunodeficiency virus 1' , 'Homo sapie
                    # ns' , 'Homo sapiens' , 'Homo sapiens' , 'Homo sapiens' , 'Homo sapiens' , 'Homo sapiens' , 'Homo s
                    # apiens'
                    'sequence': 'TEXT',
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
                    'tax_id': 'NUMERIC',
                    # EXAMPLES:
                    # '9606' , '11676' , '11676' , '9606' , '9606' , '9606' , '9606' , '9606' , '9606' , '9606'
                    'version': 'NUMERIC',
                    # EXAMPLES:
                    # '3' , '1' , '1' , '1' , '1' , '2' , '2' , '2' , '1' , '1'
                }
            }
        }
    }
