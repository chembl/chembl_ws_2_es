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
                    # '{'input': 'BAO_0000019', 'weight': 10}' , '{'input': 'CHEMBL615129', 'weight': 10}' , '{'input': 
                    # 'BAO_0000357', 'weight': 10}' , '{'input': 'Inhibitory activity against 15-lipoxygenase in rat pol
                    # ymorphonuclear leukocytes', 'weight': 80}' , '{'input': 'Glycine max', 'weight': 30}' , '{'input':
                    #  'CHEMBL1125500', 'weight': 10}' , '{'input': 'Dissociation constant towards 16S rRNA construct B'
                    # , 'weight': 80}' , '{'input': 'BAO_0000225', 'weight': 10}' , '{'input': 'Homo sapiens', 'weight':
                    #  30}' , '{'input': 'CHEMBL1124902', 'weight': 10}'
                }
            },
            'assay_category': 'TEXT',
            # EXAMPLES:
            # 'confirmatory' , 'confirmatory' , 'confirmatory' , 'confirmatory' , 'confirmatory' , 'confirmatory' , 'con
            # firmatory' , 'confirmatory' , 'confirmatory' , 'confirmatory'
            'assay_cell_type': 'TEXT',
            # EXAMPLES:
            # '1A9' , '1A9' , '1A9' , '1A9' , 'SCLC' , 'HepG2' , 'HepG2' , 'HepG2 2.2.15' , 'HepG2 2.2.15' , 'HepG2 2.2.
            # 15'
            'assay_chembl_id': 'TEXT',
            # EXAMPLES:
            # 'CHEMBL615119' , 'CHEMBL615129' , 'CHEMBL615138' , 'CHEMBL615141' , 'CHEMBL615147' , 'CHEMBL615148' , 'CHE
            # MBL615152' , 'CHEMBL615153' , 'CHEMBL615158' , 'CHEMBL615159'
            'assay_classifications': 
            {
                'properties': 
                {
                    'assay_class_id': 'NUMERIC',
                    # EXAMPLES:
                    # '84' , '115' , '322' , '322' , '322' , '115' , '259' , '82' , '82' , '91'
                    'class_type': 'TEXT',
                    # EXAMPLES:
                    # 'In vivo efficacy' , 'In vivo efficacy' , 'In vivo efficacy' , 'In vivo efficacy' , 'In vivo effic
                    # acy' , 'In vivo efficacy' , 'In vivo efficacy' , 'In vivo efficacy' , 'In vivo efficacy' , 'In viv
                    # o efficacy'
                    'l1': 'TEXT',
                    # EXAMPLES:
                    # 'ANTINEOPLASTIC AND IMMUNOMODULATING AGENTS' , 'ANTINEOPLASTIC AND IMMUNOMODULATING AGENTS' , 'NER
                    # VOUS SYSTEM' , 'NERVOUS SYSTEM' , 'NERVOUS SYSTEM' , 'ANTINEOPLASTIC AND IMMUNOMODULATING AGENTS' 
                    # , 'GENITO URINARY SYSTEM AND SEX HORMONES' , 'ANTINEOPLASTIC AND IMMUNOMODULATING AGENTS' , 'ANTIN
                    # EOPLASTIC AND IMMUNOMODULATING AGENTS' , 'ANTINEOPLASTIC AND IMMUNOMODULATING AGENTS'
                    'l2': 'TEXT',
                    # EXAMPLES:
                    # 'Carcinoma Oncology Models' , 'Neoplasm Oncology Models' , 'Anti-Depressant Activity' , 'Anti-Depr
                    # essant Activity' , 'Anti-Depressant Activity' , 'Neoplasm Oncology Models' , 'Assessment of Renal 
                    # Function' , 'Carcinoma Oncology Models' , 'Carcinoma Oncology Models' , 'Melanoma Oncology Models'
                    'l3': 'TEXT',
                    # EXAMPLES:
                    # 'Lewis Lung Carcinoma' , 'Neoplasms' , 'General Hypothermia' , 'General Hypothermia' , 'General Hy
                    # pothermia' , 'Neoplasms' , 'Fractional Excretion Methods' , 'Carcinoma' , 'Carcinoma' , 'Experimen
                    # tal Melanoma'
                    'source': 'TEXT',
                    # EXAMPLES:
                    # 'phenotype' , 'phenotype' , 'phenotype' , 'phenotype' , 'phenotype' , 'phenotype' , 'Hock_2016' , 
                    # 'phenotype' , 'phenotype' , 'phenotype'
                }
            },
            'assay_organism': 'TEXT',
            # EXAMPLES:
            # 'Staphylococcus aureus' , 'Glycine max' , 'Rattus norvegicus' , 'Escherichia coli' , 'Homo sapiens' , 'Rat
            # tus norvegicus' , 'Rattus norvegicus' , 'Homo sapiens' , 'Homo sapiens' , 'Homo sapiens'
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
                    # 'Intraperitoneal' , 'Intraperitoneal' , 'Intraperitoneal' , 'Oral' , 'Oral' , 'Intravenous' , 'Ora
                    # l' , 'Oral' , 'Oral' , 'Oral'
                    'standard_type': 'TEXT',
                    # EXAMPLES:
                    # 'DOSE' , 'DOSE' , 'DOSE' , 'DOSE' , 'DOSE' , 'DOSE' , 'DOSE' , 'DOSE' , 'DOSE' , 'DOSE'
                    'standard_type_fixed': 'NUMERIC',
                    # EXAMPLES:
                    # '0' , '0' , '0' , '0' , '0' , '0' , '0' , '0' , '0' , '0'
                    'standard_units': 'TEXT',
                    # EXAMPLES:
                    # 'mg.kg-1' , 'mg.kg-1' , 'mg.kg-1' , 'mg.kg-1' , 'mg.kg-1' , 'mg.kg-1' , 'mg.kg-1' , 'mg.kg-1' , 'm
                    # g.kg-1' , 'mg.kg-1'
                    'standard_value': 'NUMERIC',
                    # EXAMPLES:
                    # '128.0' , '100.0' , '100.0' , '100.0' , '10.0' , '10.0' , '1.0' , '10.0' , '5.0' , '15.0'
                    'text_value': 'TEXT',
                    # EXAMPLES:
                    # 'Intraperitoneal' , 'Intraperitoneal' , 'Intraperitoneal' , 'Oral' , 'Oral' , 'Intravenous' , 'Ora
                    # l' , 'Oral' , 'Oral' , 'Oral'
                    'type': 'TEXT',
                    # EXAMPLES:
                    # 'DOSE' , 'DOSE' , 'DOSE' , 'DOSE' , 'DOSE' , 'DOSE' , 'DOSE' , 'DOSE' , 'DOSE' , 'DOSE'
                    'units': 'TEXT',
                    # EXAMPLES:
                    # 'mg/kg' , 'mg/kg' , 'mg/kg' , 'mg/kg' , 'mg/kg' , 'mg/kg' , 'mg/kg' , 'mg/kg' , 'mg/kg' , 'mg/kg'
                    'value': 'NUMERIC',
                    # EXAMPLES:
                    # '128.0' , '100.0' , '100.0' , '100.0' , '10.0' , '10.0' , '1.0' , '10.0' , '5.0' , '15.0'
                }
            },
            'assay_strain': 'TEXT',
            # EXAMPLES:
            # 'beagle' , 'Sprague-Dawley' , 'nigeriensis' , 'nigeriensis' , 'nigeriensis' , 'nigeriensis' , 'WRL CN 375'
            #  , 'nigeriensis' , 'T9/94RC17' , 'TM91C235'
            'assay_subcellular_fraction': 'TEXT',
            # EXAMPLES:
            # 'Microsome' , 'Microsome' , 'Membrane' , 'Membrane' , 'Membrane' , 'Membrane' , 'Microsome' , 'Microsome' 
            # , 'Microsome' , 'Brain membranes'
            'assay_tax_id': 'NUMERIC',
            # EXAMPLES:
            # '1280' , '3847' , '10116' , '562' , '9606' , '10116' , '10116' , '9606' , '9606' , '9606'
            'assay_test_type': 'TEXT',
            # EXAMPLES:
            # 'In vivo' , 'In vivo' , 'In vivo' , 'In vivo' , 'In vivo' , 'In vivo' , 'In vivo' , 'In vivo' , 'In vivo' 
            # , 'In vivo'
            'assay_tissue': 'TEXT',
            # EXAMPLES:
            # 'Testis' , 'Plasma' , 'Ileum' , 'Frontal cortex' , 'Hippocampus' , 'Ileum' , 'Ileum' , 'Heart' , 'Liver' ,
            #  'Liver'
            'assay_type': 'TEXT',
            # EXAMPLES:
            # 'B' , 'F' , 'B' , 'B' , 'B' , 'A' , 'B' , 'B' , 'B' , 'B'
            'assay_type_description': 'TEXT',
            # EXAMPLES:
            # 'Binding' , 'Functional' , 'Binding' , 'Binding' , 'Binding' , 'ADME' , 'Binding' , 'Binding' , 'Binding' 
            # , 'Binding'
            'bao_format': 'TEXT',
            # EXAMPLES:
            # 'BAO_0000019' , 'BAO_0000218' , 'BAO_0000357' , 'BAO_0000219' , 'BAO_0000357' , 'BAO_0000019' , 'BAO_00002
            # 25' , 'BAO_0000225' , 'BAO_0000019' , 'BAO_0000221'
            'bao_label': 'TEXT',
            # EXAMPLES:
            # 'assay format' , 'organism-based format' , 'single protein format' , 'cell-based format' , 'single protein
            #  format' , 'assay format' , 'nucleic acid format' , 'nucleic acid format' , 'assay format' , 'tissue-based
            #  format'
            'cell_chembl_id': 'TEXT',
            # EXAMPLES:
            # 'CHEMBL3307529' , 'CHEMBL3307529' , 'CHEMBL3307529' , 'CHEMBL3307529' , 'CHEMBL3307967' , 'CHEMBL3307718' 
            # , 'CHEMBL3307718' , 'CHEMBL3833241' , 'CHEMBL3833241' , 'CHEMBL3833241'
            'confidence_description': 'TEXT',
            # EXAMPLES:
            # 'Default value - Target unknown or has yet to be assigned' , 'Target assigned is non-molecular' , 'Homolog
            # ous single protein target assigned' , 'Homologous single protein target assigned' , 'Homologous single pro
            # tein target assigned' , 'Default value - Target unknown or has yet to be assigned' , 'Target assigned is m
            # olecular non-protein target' , 'Target assigned is molecular non-protein target' , 'Homologous single prot
            # ein target assigned' , 'Direct single protein target assigned'
            'confidence_score': 'NUMERIC',
            # EXAMPLES:
            # '0' , '1' , '8' , '8' , '8' , '0' , '3' , '3' , '8' , '9'
            'description': 'TEXT',
            # EXAMPLES:
            # 'The compound was tested for minimum inhibitory concentration in Staphylococcus aureus,147N penicillin sen
            # sitive Staphylococcus aureus' , 'Inhibitory activity against human reticulocyte 15-lipoxygenase (15-HLO); 
            # NI is no inhibition' , 'Inhibitory activity against 15-lipoxygenase in rat polymorphonuclear leukocytes' ,
            #  'Compound at 100 uM was tested in vitro for inhibition of 15-lipoxygenase soybean' , 'Inhibition of cytoc
            # hrome P450 progesterone 16-alpha hydroxylase' , 'Dissociation constant towards 16S rRNA construct B' , 'Bi
            # nding affinity of aminoglycoside to 16S ribosomal RNA A-site in Escherichia coli' , 'The compound was test
            # ed at a concentration of 1 uM for inhibitory activity against 17 beta-hydroxysteroid dehydrogenase from hu
            # man placental microsomes' , 'Inhibition of 17-alpha-hydroxylase/17,20 lyase from rat testes microsomal pre
            # paration' , 'Percent inhibition of 17-alpha-hydroxylase/17,20 lyase of rat testes microsomes at 100 uM'
            'document_chembl_id': 'TEXT',
            # EXAMPLES:
            # 'CHEMBL1133101' , 'CHEMBL1126299' , 'CHEMBL1135472' , 'CHEMBL1125679' , 'CHEMBL1129426' , 'CHEMBL1125500' 
            # , 'CHEMBL1133237' , 'CHEMBL1133989' , 'CHEMBL1128186' , 'CHEMBL1124902'
            'relationship_description': 'TEXT',
            # EXAMPLES:
            # 'Default value - Target has yet to be curated' , 'Non-molecular target assigned' , 'Homologous protein tar
            # get assigned' , 'Homologous protein target assigned' , 'Homologous protein target assigned' , 'Default val
            # ue - Target has yet to be curated' , 'Molecular target other than protein assigned' , 'Molecular target ot
            # her than protein assigned' , 'Homologous protein target assigned' , 'Direct protein target assigned'
            'relationship_type': 'TEXT',
            # EXAMPLES:
            # 'U' , 'N' , 'H' , 'H' , 'H' , 'U' , 'M' , 'M' , 'H' , 'D'
            'src_assay_id': 'NUMERIC',
            # EXAMPLES:
            # '1771' , '987' , '961' , '2511' , '715' , '2487' , '928' , '1396' , '1454' , '463214'
            'src_id': 'NUMERIC',
            # EXAMPLES:
            # '1' , '1' , '1' , '1' , '1' , '1' , '1' , '1' , '1' , '1'
            'target_chembl_id': 'TEXT',
            # EXAMPLES:
            # 'CHEMBL2362975' , 'CHEMBL352' , 'CHEMBL2903' , 'CHEMBL3289' , 'CHEMBL2903' , 'CHEMBL612558' , 'CHEMBL345' 
            # , 'CHEMBL614640' , 'CHEMBL3925' , 'CHEMBL4430'
            'tissue_chembl_id': 'TEXT',
            # EXAMPLES:
            # 'CHEMBL3638183' , 'CHEMBL3559721' , 'CHEMBL3638244' , 'CHEMBL3638220' , 'CHEMBL3638273' , 'CHEMBL3638244' 
            # , 'CHEMBL3638244' , 'CHEMBL3638187' , 'CHEMBL3559723' , 'CHEMBL3559723'
            'variant_sequence': 
            {
                'properties': 
                {
                    'accession': 'TEXT',
                    # EXAMPLES:
                    # 'P29274' , 'P29274' , 'P0DMS8' , 'P41597' , 'P41597' , 'Q72874' , 'P29274' , 'P12931' , 'Q72874' ,
                    #  'P16455'
                    'isoform': 'NUMERIC',
                    # EXAMPLES:
                    # '1' , '1' , '1' , '1' , '1' , '1' , '1' , '1' , '1' , '1'
                    'mutation': 'TEXT',
                    # EXAMPLES:
                    # 'H278D' , 'H278E' , 'H95A' , 'D284A' , 'H121A' , 'G48V' , 'T88E' , 'C188A' , 'V82F' , 'G160R'
                    'organism': 'TEXT',
                    # EXAMPLES:
                    # 'Homo sapiens' , 'Homo sapiens' , 'Homo sapiens' , 'Homo sapiens' , 'Homo sapiens' , 'Human immuno
                    # deficiency virus 1' , 'Homo sapiens' , 'Homo sapiens' , 'Human immunodeficiency virus 1' , 'Homo s
                    # apiens'
                    'sequence': 'TEXT',
                    # EXAMPLES:
                    # 'MPIMGSSVYITVELAIAVLAILGNVLVCWAVWLNSNLQNVTNYFVVSLAAADIAVGVLAIPFAITISTGFCAACHGCLFIACFVLVLTQSSIFSLLA
                    # IAIDRYIAIRIPLRYNGLVTGTRAKGIIAICWVLSFAIGLTPMLGWNNCGQPKEGKNHSQGCGEGQVACLFEDVVPMNYMVYFNFFACVLVPLLLMLG
                    # VYLRIFLAARRQLKQMESQPLPGERARSTLQKEVHAAKSLAIIVGLFALCWLPLHIINCFTFFCPDCSHAPLWLMYLAIVLSDTNSVVNPFIYAYRIR
                    # EFRQTFRKIIRSHVLRQQEPFKAAGTSARVLAAHGSDGEQVSLRLNGHPPGVWANGSAPHPERRPNGYALGLVSGGSAQESQGNTGLPDVELLSHELK
                    # GVCPEPPGLDDPLAQDGAGVS' , 'MPIMGSSVYITVELAIAVLAILGNVLVCWAVWLNSNLQNVTNYFVVSLAAADIAVGVLAIPFAITISTGFCA
                    # ACHGCLFIACFVLVLTQSSIFSLLAIAIDRYIAIRIPLRYNGLVTGTRAKGIIAICWVLSFAIGLTPMLGWNNCGQPKEGKNHSQGCGEGQVACLFED
                    # VVPMNYMVYFNFFACVLVPLLLMLGVYLRIFLAARRQLKQMESQPLPGERARSTLQKEVHAAKSLAIIVGLFALCWLPLHIINCFTFFCPDCSHAPLW
                    # LMYLAIVLSETNSVVNPFIYAYRIREFRQTFRKIIRSHVLRQQEPFKAAGTSARVLAAHGSDGEQVSLRLNGHPPGVWANGSAPHPERRPNGYALGLV
                    # SGGSAQESQGNTGLPDVELLSHELKGVCPEPPGLDDPLAQDGAGVS' , 'MPNNSTALSLANVTYITMEIFIGLCAIVGNVLVICVVKLNPSLQTTT
                    # FYFIVSLALADIAVGVLVMPLAIVVSLGITIHFYSCLFMTCLLLIFTAASIMSLLAIAVDRYLRVKLTVRYKRVTTHRRIWLALGLCWLVSFLVGLTP
                    # MFGWNMKLTSEYHRNVTFLSCQFVSVMRMDYMVYFSFLTWIFIPLVVMCAIYLDIFYIIRNKLSLNLSNSKETGAFYGREFKTAKSLFLVLFLFALSW
                    # LPLSIINCIIYFNGEVPQLVLYMGILLSHANSMMNPIVYAYKIKKFKETYLLILKACVVCHPSDSLDTSIEKNSE' , 'MLSTSRSRFIRNTNESGE
                    # EVTTFFDYDYGAPCHKFDVKQIGAQLLPPLYSLVFIFGFVGNMLVVLILINCKKLKCLTDIYLLNLAISDLLFLITLPLWAHSAANEWVFGNAMCKLF
                    # TGLYHIGYFGGIFFIILLTIDRYLAIVHAVFALKARTVTFGVVTSVITWLVAVFASVPGIIFTKCQKEDSVYVCGPYFPRGWNNFHTIMRNILGLVLP
                    # LLIMVICYSGILKTLLRCRNEKKRHRAVRVIFTIMIVYFLFWTPYNIVILLNTFQEFFGLSNCESTSQLAQATQVTETLGMTHCCINPIIYAFVGEKF
                    # RSLFHIALGCRIAPLQKPVCGGPGVRPGKNVKVTTQGLLDGRGKGKSIGRAPEASLQDKEGA' , 'MLSTSRSRFIRNTNESGEEVTTFFDYDYGAP
                    # CHKFDVKQIGAQLLPPLYSLVFIFGFVGNMLVVLILINCKKLKCLTDIYLLNLAISDLLFLITLPLWAHSAANEWVFGNAMCKLFTGLYAIGYFGGIF
                    # FIILLTIDRYLAIVHAVFALKARTVTFGVVTSVITWLVAVFASVPGIIFTKCQKEDSVYVCGPYFPRGWNNFHTIMRNILGLVLPLLIMVICYSGILK
                    # TLLRCRNEKKRHRAVRVIFTIMIVYFLFWTPYNIVILLNTFQEFFGLSNCESTSQLDQATQVTETLGMTHCCINPIIYAFVGEKFRSLFHIALGCRIA
                    # PLQKPVCGGPGVRPGKNVKVTTQGLLDGRGKGKSIGRAPEASLQDKEGA' , 'PQVTLWQRPLVTIKIGGQLKEALLDTGADDTVLEEMSLPGRWKP
                    # KMIVGIGGFIKVRQYDQILIEICGHKAIGTVLVGPTPVNIIGRNLLTQIGCTLNF' , 'MPIMGSSVYITVELAIAVLAILGNVLVCWAVWLNSNLQ
                    # NVTNYFVVSLAAADIAVGVLAIPFAITISTGFCAACHGCLFIACFVLVLEQSSIFSLLAIAIDRYIAIRIPLRYNGLVTGTRAKGIIAICWVLSFAIG
                    # LTPMLGWNNCGQPKEGKNHSQGCGEGQVACLFEDVVPMNYMVYFNFFACVLVPLLLMLGVYLRIFLAARRQLKQMESQPLPGERARSTLQKEVHAAKS
                    # LAIIVGLFALCWLPLHIINCFTFFCPDCSHAPLWLMYLAIVLSHTNSVVNPFIYAYRIREFRQTFRKIIRSHVLRQQEPFKAAGTSARVLAAHGSDGE
                    # QVSLRLNGHPPGVWANGSAPHPERRPNGYALGLVSGGSAQESQGNTGLPDVELLSHELKGVCPEPPGLDDPLAQDGAGVS' , 'MGSNKSKPKDASQ
                    # RRRSLEPAENVHGAGGGAFPASQTPSKPASADGHRGPSAAFAPAAAEPKLFGGFNSSDTVTSPQRAGPLAGGVTTFVALYDYESRTETDLSFKKGERL
                    # QIVNNTEGDWWLAHSLSTGQTGYIPSNYVAPSDSIQAEEWYFGKITRRESERLLLNAENPRGTFLVRESETTKGAYALSVSDFDNAKGLNVKHYKIRK
                    # LDSGGFYITSRTQFNSLQQLVAYYSKHADGLCHRLTTVCPTSKPQTQGLAKDAWEIPRESLRLEVKLGQGCFGEVWMGTWNGTTRVAIKTLKPGTMSP
                    # EAFLQEAQVMKKLRHEKLVQLYAVVSEEPIYIVTEYMSKGSLLDFLKGETGKYLRLPQLVDMAAQIASGMAYVERMNYVHRDLRAANILVGENLVCKV
                    # ADFGLARLIEDNEYTARQGAKFPIKWTAPEAALYGRFTIKSDVWSFGILLTELTTKGRVPYPGMVNREVLDQVERGYRMPCPPECPESLHDLMCQCWR
                    # KEPEERPTFEYLQAFLEDYFTSTEPQYQPGENL' , 'PQVTLWQRPLVTIKIGGQLKEALLDTGADDTVLEEMSLPGRWKPKMIGGIGGFIKVRQYD
                    # QILIEICGHKAIGTVLVGPTPFNIIGRNLLTQIGCTLNF' , 'MDKDCEMKRTTLDSPLGKLELSGCEQGLHEIKLLGKGTSAADAVEVPAPAAVLG
                    # GPEPLMQCTAWLNAYFHQPEAIEEFPVPALHHPVFQQESFTRQVLWKLLKVVKFGEVISYQQLAALAGNPKAARAVGGAMRGNPVPILIPCHRVVCSS
                    # GAVGNYSRGLAVKEWLLAHEGHRLGKPGLGGSSGLAGAWLKGAGATSGSPPAGRN'
                    'tax_id': 'NUMERIC',
                    # EXAMPLES:
                    # '9606' , '9606' , '9606' , '9606' , '9606' , '11676' , '9606' , '9606' , '11676' , '9606'
                    'version': 'NUMERIC',
                    # EXAMPLES:
                    # '2' , '2' , '1' , '1' , '1' , '1' , '2' , '3' , '1' , '1'
                }
            }
        }
    }
