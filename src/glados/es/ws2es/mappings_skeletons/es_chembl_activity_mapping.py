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
                    'activity_generated': 
                    {
                        'properties': 
                        {
                        }
                    },
                    'assay_data': 
                    {
                        'properties': 
                        {
                            'assay_cell_type': 'TEXT',
                            # EXAMPLES:
                            # 'LOX IMVI ' , 'MCF7' , 'MCF7' , 'K562' , 'MDA-MB-231' , 'HRCE' , 'MDA-MB-435' , 'PC-3' , '
                            # Caco-2' , 'HRCE'
                            'assay_organism': 'TEXT',
                            # EXAMPLES:
                            # 'Homo sapiens' , 'Mus musculus' , 'Homo sapiens' , 'Homo sapiens' , 'Pseudomonas aeruginos
                            # a' , 'Homo sapiens' , 'Homo sapiens' , 'Homo sapiens' , 'Homo sapiens' , 'Homo sapiens'
                            'assay_parameters': 
                            {
                                'properties': 
                                {
                                    'active': 'NUMERIC',
                                    # EXAMPLES:
                                    # '1' , '1' , '1' , '1' , '1' , '1' , '1' , '1' , '1' , '1'
                                    'comments': 'TEXT',
                                    # EXAMPLES:
                                    # 'Is the measured interaction considered due to direct binding to target?' , 'Is th
                                    # e measured interaction considered due to direct binding to target?' , 'Is the meas
                                    # ured interaction considered due to direct binding to target?' , 'Is the measured i
                                    # nteraction considered due to direct binding to target?' , 'Is the measured interac
                                    # tion considered due to direct binding to target?' , 'Is the measured interaction c
                                    # onsidered due to direct binding to target?' , 'Is the measured interaction conside
                                    # red due to direct binding to target?' , 'Is the measured interaction considered du
                                    # e to direct binding to target?' , 'Is the measured interaction considered due to d
                                    # irect binding to target?' , 'Is the measured interaction considered due to direct 
                                    # binding to target?'
                                    'relation': 'TEXT',
                                    # EXAMPLES:
                                    # '=' , '=' , '=' , '=' , '=' , '=' , '=' , '=' , '=' , '='
                                    'standard_relation': 'TEXT',
                                    # EXAMPLES:
                                    # '=' , '=' , '=' , '=' , '=' , '=' , '=' , '=' , '=' , '='
                                    'standard_text_value': 'TEXT',
                                    # EXAMPLES:
                                    # 'Inhibition of Bacterial Growth' , 'Inhibition of Bacterial Growth' , 'Inhibition 
                                    # of Fungal Growth' , 'Inhibition of Bacterial Growth' , 'Inhibition of Bacterial Gr
                                    # owth' , 'Inhibition of Bacterial Growth' , 'Inhibition of Fungal Growth' , 'Inhibi
                                    # tion of Fungal Growth' , 'Inhibition of Bacterial Growth' , 'Inhibition of Fungal 
                                    # Growth'
                                    'standard_type': 'TEXT',
                                    # EXAMPLES:
                                    # 'ASSAY_TEST' , 'ASSAY_TEST' , 'ASSAY_TEST' , 'ASSAY_TEST' , 'ASSAY_TEST' , 'ASSAY_
                                    # TEST' , 'ASSAY_TEST' , 'ASSAY_TEST' , 'ASSAY_TEST' , 'ASSAY_TEST'
                                    'standard_type_fixed': 'NUMERIC',
                                    # EXAMPLES:
                                    # '0' , '0' , '0' , '0' , '0' , '0' , '0' , '0' , '0' , '0'
                                    'standard_units': 'TEXT',
                                    # EXAMPLES:
                                    # 'hr' , 'hr' , 'hr' , 'hr' , 'hr' , 'hr' , 'hr' , 'hr' , 'hr' , 'hr'
                                    'standard_value': 'NUMERIC',
                                    # EXAMPLES:
                                    # '18.0' , '18.0' , '18.0' , '18.0' , '18.0' , '18.0' , '18.0' , '18.0' , '18.0' , '
                                    # 18.0'
                                    'text_value': 'TEXT',
                                    # EXAMPLES:
                                    # 'Inhibition of Bacterial Growth' , 'Inhibition of Bacterial Growth' , 'Inhibition 
                                    # of Fungal Growth' , 'Inhibition of Bacterial Growth' , 'Inhibition of Bacterial Gr
                                    # owth' , 'Inhibition of Bacterial Growth' , 'Inhibition of Fungal Growth' , 'Inhibi
                                    # tion of Fungal Growth' , 'Inhibition of Bacterial Growth' , 'Inhibition of Fungal 
                                    # Growth'
                                    'type': 'TEXT',
                                    # EXAMPLES:
                                    # 'ASSAY_TEST' , 'ASSAY_TEST' , 'ASSAY_TEST' , 'ASSAY_TEST' , 'ASSAY_TEST' , 'ASSAY_
                                    # TEST' , 'ASSAY_TEST' , 'ASSAY_TEST' , 'ASSAY_TEST' , 'ASSAY_TEST'
                                    'units': 'TEXT',
                                    # EXAMPLES:
                                    # 'hr' , 'hr' , 'hr' , 'hr' , 'hr' , 'hr' , 'hr' , 'hr' , 'hr' , 'hr'
                                    'value': 'NUMERIC',
                                    # EXAMPLES:
                                    # '18.0' , '18.0' , '18.0' , '18.0' , '18.0' , '18.0' , '18.0' , '18.0' , '18.0' , '
                                    # 18.0'
                                }
                            },
                            'assay_strain': 'TEXT',
                            # EXAMPLES:
                            # 'Kunming' , 'ATCC 27853' , 'Kunming' , 'H37Rv' , 'ATCC 27853' , 'K1' , 'ATCC 9950' , 'ATCC
                            #  25922' , 'ATCC 25923' , 'Kunming'
                            'assay_subcellular_fraction': 'TEXT',
                            # EXAMPLES:
                            # 'Cell membrane' , 'Microsomes' , 'Microsomes' , 'Microsome' , 'Microsomes' , 'Microsome' ,
                            #  'Microsome' , 'Mitochondria' , 'Cytosol' , 'S9'
                            'assay_tax_id': 'NUMERIC',
                            # EXAMPLES:
                            # '9606' , '10090' , '9606' , '9606' , '287' , '9606' , '9606' , '9606' , '9606' , '9606'
                            'assay_tissue': 'TEXT',
                            # EXAMPLES:
                            # 'Brain' , 'Liver' , 'Liver' , 'Liver' , 'Liver' , 'Plasma' , 'Brain' , 'Liver' , 'Liver' ,
                            #  'Plasma'
                            'assay_type': 'TEXT',
                            # EXAMPLES:
                            # 'B' , 'F' , 'F' , 'F' , 'F' , 'B' , 'B' , 'F' , 'P' , 'B'
                            'cell_chembl_id': 'TEXT',
                            # EXAMPLES:
                            # 'CHEMBL3307535' , 'CHEMBL3308403' , 'CHEMBL3308403' , 'CHEMBL3308378' , 'CHEMBL3307960' , 
                            # 'CHEMBL4303839' , 'CHEMBL3307686' , 'CHEMBL3307570' , 'CHEMBL3307519' , 'CHEMBL4303839'
                            'src_desc': 'TEXT',
                            # EXAMPLES:
                            # 'Scientific Literature' , 'Scientific Literature' , 'Scientific Literature' , 'Scientific 
                            # Literature' , 'Scientific Literature' , 'Scientific Literature' , 'Scientific Literature' 
                            # , 'Scientific Literature' , 'Scientific Literature' , 'Scientific Literature'
                            'src_id': 'NUMERIC',
                            # EXAMPLES:
                            # '1' , '1' , '1' , '1' , '1' , '1' , '1' , '1' , '1' , '1'
                            'tissue_chembl_id': 'TEXT',
                            # EXAMPLES:
                            # 'CHEMBL3638188' , 'CHEMBL3559723' , 'CHEMBL3559723' , 'CHEMBL3559723' , 'CHEMBL3559723' , 
                            # 'CHEMBL3559721' , 'CHEMBL3638188' , 'CHEMBL3559723' , 'CHEMBL3559723' , 'CHEMBL3559721'
                            'type_label': 'TEXT',
                            # EXAMPLES:
                            # 'B - Binding' , 'F - Functional' , 'F - Functional' , 'F - Functional' , 'F - Functional' 
                            # , 'B - Binding' , 'B - Binding' , 'F - Functional' , 'P - Physicochemical' , 'B - Binding'
                        }
                    },
                    'document_data': 
                    {
                        'properties': 
                        {
                            'first_page': 'NUMERIC',
                            # EXAMPLES:
                            # '1205' , '111650' , '230' , '230' , '376' , '744' , '6876' , '230' , '1159' , '285'
                            'pubmed_id': 'NUMERIC',
                            # EXAMPLES:
                            # '31413806' , '31539780' , '30006168' , '30006168' , '31260891' , '31284084' , '31282155' ,
                            #  '30006168' , '31413800' , '30553624'
                            'volume': 'NUMERIC',
                            # EXAMPLES:
                            # '10' , '183' , '156' , '156' , '179' , '179' , '62' , '156' , '10' , '27'
                            'year': 'NUMERIC',
                            # EXAMPLES:
                            # '2019' , '2019' , '2018' , '2018' , '2019' , '2019' , '2019' , '2018' , '2019' , '2019'
                        }
                    },
                    'organism_taxonomy': 
                    {
                        'properties': 
                        {
                            'l1': 'TEXT',
                            # EXAMPLES:
                            # 'Eukaryotes' , 'Eukaryotes' , 'Eukaryotes' , 'Bacteria' , 'Eukaryotes' , 'Eukaryotes' , 'E
                            # ukaryotes' , 'Eukaryotes' , 'Eukaryotes' , 'Viruses'
                            'l2': 'TEXT',
                            # EXAMPLES:
                            # 'Mammalia' , 'Mammalia' , 'Mammalia' , 'Gram-Negative' , 'Mammalia' , 'Mammalia' , 'Mammal
                            # ia' , 'Mammalia' , 'Mammalia' , 'ssRNA'
                            'l3': 'TEXT',
                            # EXAMPLES:
                            # 'Rodentia' , 'Primates' , 'Primates' , 'Pseudomonas' , 'Primates' , 'Primates' , 'Primates
                            # ' , 'Primates' , 'Primates' , 'ssRNA negative-strand viruses'
                            'oc_id': 'NUMERIC',
                            # EXAMPLES:
                            # '35' , '7' , '7' , '396' , '7' , '7' , '7' , '7' , '7' , '765'
                            'tax_id': 'NUMERIC',
                            # EXAMPLES:
                            # '10090' , '9606' , '9606' , '287' , '9606' , '9606' , '9606' , '9606' , '9606' , '211044'
                        }
                    },
                    'parent_molecule_data': 
                    {
                        'properties': 
                        {
                            'alogp': 'NUMERIC',
                            # EXAMPLES:
                            # '3.58' , '8.21' , '8.28' , '6.25' , '4.84' , '3.29' , '8.25' , '1.57' , '5.56' , '5.10'
                            'compound_key': 'TEXT',
                            # EXAMPLES:
                            # '2b' , '86' , '1b' , '1i' , '51n' , '14; C130-0049' , '2; PT2977' , '2j' , '35' , '59a'
                            'full_mwt': 'NUMERIC',
                            # EXAMPLES:
                            # '379.97' , '443.50' , '564.86' , '584.39' , '626.07' , '335.35' , '383.35' , '602.92' , '3
                            # 90.38' , '313.32'
                            'image_file': 'TEXT',
                            # EXAMPLES:
                            # 'unknown.svg' , 'unknown.svg' , 'unknown.svg' , 'unknown.svg' , 'unknown.svg' , 'unknown.s
                            # vg' , 'unknown.svg' , 'unknown.svg' , 'unknown.svg' , 'unknown.svg'
                            'max_phase': 'NUMERIC',
                            # EXAMPLES:
                            # '0' , '0' , '0' , '0' , '0' , '0' , '2' , '0' , '0' , '0'
                            'num_ro5_violations': 'NUMERIC',
                            # EXAMPLES:
                            # '0' , '2' , '2' , '2' , '0' , '0' , '2' , '0' , '1' , '1'
                            'psa': 'NUMERIC',
                            # EXAMPLES:
                            # '84.48' , '81.07' , '92.07' , '124.91' , '37.81' , '87.39' , '80.04' , '134.87' , '78.97' 
                            # , '78.01'
                        }
                    },
                    'protein_classification': 
                    {
                        'properties': 
                        {
                            'l1': 'TEXT',
                            # EXAMPLES:
                            # 'Membrane receptor' , 'Enzyme' , 'Enzyme' , 'Ion channel' , 'Enzyme' , 'Enzyme' , 'Epigene
                            # tic regulator' , 'Ion channel' , 'Enzyme' , 'Enzyme'
                            'l2': 'TEXT',
                            # EXAMPLES:
                            # 'Toll-like and Il-1 receptors' , 'Kinase' , 'Cytochrome P450' , 'Voltage-gated ion channel
                            # ' , 'Hydrolase' , 'Cytochrome P450' , 'Eraser' , 'Voltage-gated ion channel' , 'Oxidoreduc
                            # tase' , 'Oxidoreductase'
                            'l3': 'TEXT',
                            # EXAMPLES:
                            # 'Protein Kinase' , 'Cytochrome P450 family 1' , 'Potassium channels' , 'Cytochrome P450 fa
                            # mily 1' , 'Histone deacetylase' , 'Transient receptor potential channel' , 'Small molecule
                            #  receptor (family A GPCR)' , 'Protein Kinase' , 'Protein Kinase' , 'Small molecule recepto
                            # r (family A GPCR)'
                            'l4': 'TEXT',
                            # EXAMPLES:
                            # 'CAMK protein kinase group' , 'Cytochrome P450 family 1B' , 'Voltage-gated potassium chann
                            # el' , 'Cytochrome P450 family 1B' , 'HDAC class III' , 'Lipid-like ligand receptor (family
                            #  A GPCR)' , 'TK protein kinase group' , 'TK protein kinase group' , 'Lipid-like ligand rec
                            # eptor (family A GPCR)' , 'Nuclear hormone receptor subfamily 1 group F'
                            'l5': 'TEXT',
                            # EXAMPLES:
                            # 'CAMK protein kinase CAMK1 family' , 'Cytochrome P450 1B1' , 'Cytochrome P450 1B1' , 'Free
                            #  fatty acid receptor' , 'Tyrosine protein kinase Axl family' , 'Tyrosine protein kinase PD
                            # GFR family' , 'Free fatty acid receptor' , 'Nuclear hormone receptor subfamily 1 group F m
                            # ember 3' , 'Tyrosine protein kinase Axl family' , 'AGC protein kinase AKT family'
                            'l6': 'TEXT',
                            # EXAMPLES:
                            # 'TKL protein kinase STKR Type 1 subfamily' , 'CMGC protein kinase p38 subfamily' , 'CMGC p
                            # rotein kinase p38 subfamily' , 'STE protein kinase MEKK2' , 'CMGC protein kinase CDC2 subf
                            # amily' , 'AGC protein kinase PKC delta subfamily' , 'CAMK protein kinase MARK subfamily' ,
                            #  'CMGC protein kinase p38 subfamily' , 'CMGC protein kinase p38 subfamily' , 'CMGC protein
                            #  kinase Dyrk1 subfamily'
                            'protein_class_id': 'NUMERIC',
                            # EXAMPLES:
                            # '649' , '1702' , '169' , '118' , '646' , '169' , '844' , '1018' , '10' , '10'
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
                    },
                    'target_data': 
                    {
                        'properties': 
                        {
                            'target_type': 'TEXT',
                            # EXAMPLES:
                            # 'UNCHECKED' , 'ORGANISM' , 'CELL-LINE' , 'CELL-LINE' , 'ORGANISM' , 'SINGLE PROTEIN' , 'SI
                            # NGLE PROTEIN' , 'CELL-LINE' , 'NO TARGET' , 'SINGLE PROTEIN'
                        }
                    }
                }
            },
            'activity_comment': 'TEXT',
            # EXAMPLES:
            # 'Active' , 'Not Active' , 'Not Active' , 'Active' , 'Active' , 'Not Active' , 'Not Active' , 'Not Active' 
            # , 'Active' , 'Not Active'
            'activity_id': 'NUMERIC',
            # EXAMPLES:
            # '18855735' , '18887885' , '18865140' , '18869888' , '18853789' , '18853954' , '18883561' , '18869892' , '1
            # 8855620' , '18878595'
            'activity_properties': 
            {
                'properties': 
                {
                    'relation': 'TEXT',
                    # EXAMPLES:
                    # '=' , '=' , '=' , '=' , '=' , '=' , '=' , '=' , '=' , '='
                    'result_flag': 'NUMERIC',
                    # EXAMPLES:
                    # '0' , '0' , '0' , '0' , '0' , '0' , '0' , '0' , '0' , '0'
                    'standard_relation': 'TEXT',
                    # EXAMPLES:
                    # '=' , '=' , '=' , '=' , '=' , '=' , '=' , '=' , '=' , '='
                    'standard_text_value': 'TEXT',
                    # EXAMPLES:
                    # 'HEPATOCYTE, PERIPORTAL, CYTOPLASM, EOSINOPHILIA' , 'MCHC (Ery. Mean Corpuscular HGB Concentration
                    # )' , 'HEPATOCYTE, CENTRILOBULAR, LIPID ACCUMULATION, MACROVESICULAR' , 'CAPSULE, INFLAMMATORY CELL
                    #  INFILTRATE, MIXED CELL' , 'HEPATOCYTE, CENTRILOBULAR, GLYCOGEN ACCUMULATION' , 'HEPATOCYTE, CENTR
                    # ILOBULAR, CYTOPLASM, EOSINOPHILIA' , 'INTRAMYOCARDIAL ARTERIES, DEGENERATION' , 'BILE DUCT, NECROS
                    # IS, ONCOCYTIC' , 'TUBULE, REGENERATION' , 'HEPATOCYTE, CENTRILOBULAR, LIPID ACCUMULATION, MICROVES
                    # ICULAR'
                    'standard_type': 'TEXT',
                    # EXAMPLES:
                    # 'Concentration' , 'Concentration' , 'Concentration' , 'PBLUC_HILL_SLOPE' , 'PBLUC_HILL_SLOPE' , 'P
                    # BLUC_HILL_SLOPE' , 'PBLUC_HILL_SLOPE' , 'PBLUC_HILL_SLOPE' , 'PBLUC_HILL_SLOPE' , 'PBLUC_HILL_SLOP
                    # E'
                    'standard_units': 'TEXT',
                    # EXAMPLES:
                    # 'uM' , 'uM' , 'uM' , 'uM' , 'uM' , 'uM' , 'uM' , 'uM' , 'uM' , 'uM'
                    'standard_value': 'NUMERIC',
                    # EXAMPLES:
                    # '20.0' , '20.0' , '20.0' , '2.74' , '27.4' , '20.8' , '16.3' , '10.1' , '10.2' , '0.525'
                    'text_value': 'TEXT',
                    # EXAMPLES:
                    # 'HEPATOCYTE, PERIPORTAL, CYTOPLASM, EOSINOPHILIA' , 'MCHC (Ery. Mean Corpuscular HGB Concentration
                    # )' , 'HEPATOCYTE, CENTRILOBULAR, LIPID ACCUMULATION, MACROVESICULAR' , 'CAPSULE, INFLAMMATORY CELL
                    #  INFILTRATE, MIXED CELL' , 'HEPATOCYTE, CENTRILOBULAR, GLYCOGEN ACCUMULATION' , 'HEPATOCYTE, CENTR
                    # ILOBULAR, CYTOPLASM, EOSINOPHILIA' , 'INTRAMYOCARDIAL ARTERIES, DEGENERATION' , 'BILE DUCT, NECROS
                    # IS, ONCOCYTIC' , 'TUBULE, REGENERATION' , 'HEPATOCYTE, CENTRILOBULAR, LIPID ACCUMULATION, MICROVES
                    # ICULAR'
                    'type': 'TEXT',
                    # EXAMPLES:
                    # 'Concentration' , 'Concentration' , 'Concentration' , 'PBLUC_HILL_SLOPE' , 'PBLUC_HILL_SLOPE' , 'P
                    # BLUC_HILL_SLOPE' , 'PBLUC_HILL_SLOPE' , 'PBLUC_HILL_SLOPE' , 'PBLUC_HILL_SLOPE' , 'PBLUC_HILL_SLOP
                    # E'
                    'units': 'TEXT',
                    # EXAMPLES:
                    # 'uM' , 'uM' , 'uM' , 'uM' , 'uM' , 'uM' , 'uM' , 'uM' , 'uM' , 'uM'
                    'value': 'NUMERIC',
                    # EXAMPLES:
                    # '20.0' , '20.0' , '20.0' , '2.74' , '27.4' , '20.8' , '16.3' , '10.1' , '10.2' , '0.525'
                }
            },
            'assay_chembl_id': 'TEXT',
            # EXAMPLES:
            # 'CHEMBL4307488' , 'CHEMBL4313659' , 'CHEMBL4309541' , 'CHEMBL4309775' , 'CHEMBL4306954' , 'CHEMBL4306978' 
            # , 'CHEMBL4312661' , 'CHEMBL4309775' , 'CHEMBL4307472' , 'CHEMBL4311585'
            'assay_description': 'TEXT',
            # EXAMPLES:
            # 'Selectivity ratio of Ki for human carbonic anhydrase 2 to Ki for human carbonic anhydrase 12' , 'Anticonv
            # ulsant activity in Kunming mouse assessed as MES-induced hind limb extension at 100 mg/kg, ip administered
            #  0. 5 to 2 hrs before MES stimulation' , 'Growth inhibition of human LOXIMVI cells incubated for 48 hrs by
            #  sulforhodamine B assay' , 'Growth inhibition of human MCF7 cells assessed as cell growth at 1 uM incubate
            # d for 48 hrs by sulforhodamine B assay relative to control' , 'Antibacterial activity against Pseudomonas 
            # aeruginosa ATCC 27853 after 24 hrs' , 'Activity at human CAMK4 at 10 uM' , 'Growth inhibition of human MCF
            # 7 cells assessed as cell growth at 1 uM incubated for 48 hrs by sulforhodamine B assay relative to control
            # ' , 'Dissociation constant, pKa of compound' , 'Inhibition of human recombinant CYP1B1 using 7-ethoxyresor
            # ufin as substrate after 30 mins in presence of NADPH by EROD assay' , 'Effect on acetylated-p53 expression
            #  in human MGHU1 cells after 3 to 24 hrs by Western blot analysis'
            'assay_type': 'TEXT',
            # EXAMPLES:
            # 'B' , 'F' , 'F' , 'F' , 'F' , 'B' , 'B' , 'F' , 'P' , 'B'
            'assay_variant_accession': 'TEXT',
            # EXAMPLES:
            # 'O75874' , 'Q9WKE8' , 'P01116' , 'O75874' , 'P47205' , 'P0A725' , 'Q9WKE8' , 'Q5S007' , 'P36888' , 'P0A725
            # '
            'assay_variant_mutation': 'TEXT',
            # EXAMPLES:
            # 'R132C' , 'UNDEFINED MUTATION' , 'UNDEFINED MUTATION' , 'UNDEFINED MUTATION' , 'K103N,Y181C' , 'G12D' , 'R
            # 132C' , 'C40S' , 'C125S' , 'V106M'
            'bao_endpoint': 'TEXT',
            # EXAMPLES:
            # 'BAO_0000179' , 'BAO_0000375' , 'BAO_0002145' , 'BAO_0001103' , 'BAO_0002146' , 'BAO_0000201' , 'BAO_00003
            # 75' , 'BAO_0001103' , 'BAO_0002131' , 'BAO_0000190'
            'bao_format': 'TEXT',
            # EXAMPLES:
            # 'BAO_0000019' , 'BAO_0000218' , 'BAO_0000219' , 'BAO_0000219' , 'BAO_0000218' , 'BAO_0000219' , 'BAO_00003
            # 57' , 'BAO_0000219' , 'BAO_0000100' , 'BAO_0000357'
            'bao_label': 'TEXT',
            # EXAMPLES:
            # 'assay format' , 'organism-based format' , 'cell-based format' , 'cell-based format' , 'organism-based for
            # mat' , 'cell-based format' , 'single protein format' , 'cell-based format' , 'small-molecule physicochemic
            # al format' , 'single protein format'
            'canonical_smiles': 'TEXT',
            # EXAMPLES:
            # 'O=C(CCC(=O)Nc1ccc2c(c1)B(O)OC2)Nc1ccc2c(c1)B(O)OC2' , 'COc1cc(OC)c(OC)cc1/C=C/CNC(=O)/C=C/c1cc(OC)c(OC)c(
            # OC)c1' , 'COc1cc(Cl)cc(-c2nn(-c3cccc(NC(=O)Nc4ccc(Cl)c(Cl)c4)c3)cc2-c2ccncc2)c1' , 'O=C(Nc1cccc(-n2cc(-c3c
            # cncc3)c(-c3cc(O)cc(Cl)c3)n2)c1)Nc1ccc(Cl)c(C(F)(F)F)c1' , 'COc1cc(/C=C(\C#N)n2cc([N+](=O)[O-])nc2C)c2c(c1O
            # Cc1cccc(Cl)c1)CN1CCc3cc4c(cc3C1C2)OCO4' , 'FC(F)(F)c1cc(-c2ccccc2)nc(NCc2cccs2)n1' , 'CS(=O)(=O)c1ccc(Oc2c
            # c(F)cc(C#N)c2)c2c1[C@H](O)[C@H](F)[C@@H]2F' , 'O=C(Nc1cccc(-n2cc(-c3ccncc3)c(-c3cc(O)cc(Cl)c3)n2)c1)c1cc(C
            # (F)(F)F)cc(C(F)(F)F)c1' , 'C[C@@]1(c2cc(NC(=O)c3ccc(C#N)cn3)ccc2F)Cn2cnnc2C(N)=N1' , '[N-]=[N+]=Nc1ccc(-c2
            # cc(=O)c3ccc4ccccc4c3o2)cc1'
            'data_validity_comment': 'TEXT',
            # EXAMPLES:
            # 'Outside typical range' , 'Outside typical range' , 'Outside typical range' , 'Non standard unit for type'
            #  , 'Non standard unit for type' , 'Non standard unit for type' , 'Non standard unit for type' , 'Outside t
            # ypical range' , 'Non standard unit for type' , 'Non standard unit for type'
            'data_validity_description': 'TEXT',
            # EXAMPLES:
            # 'Values for this activity type are unusually large/small, so may not be accurate' , 'Values for this activ
            # ity type are unusually large/small, so may not be accurate' , 'Values for this activity type are unusually
            #  large/small, so may not be accurate' , 'Units for this activity type are unusual and may be incorrect (or
            #  the standard_type may be incorrect)' , 'Units for this activity type are unusual and may be incorrect (or
            #  the standard_type may be incorrect)' , 'Units for this activity type are unusual and may be incorrect (or
            #  the standard_type may be incorrect)' , 'Units for this activity type are unusual and may be incorrect (or
            #  the standard_type may be incorrect)' , 'Values for this activity type are unusually large/small, so may n
            # ot be accurate' , 'Units for this activity type are unusual and may be incorrect (or the standard_type may
            #  be incorrect)' , 'Units for this activity type are unusual and may be incorrect (or the standard_type may
            #  be incorrect)'
            'document_chembl_id': 'TEXT',
            # EXAMPLES:
            # 'CHEMBL4304795' , 'CHEMBL4311969' , 'CHEMBL4308841' , 'CHEMBL4308841' , 'CHEMBL4304773' , 'CHEMBL4304775' 
            # , 'CHEMBL4311943' , 'CHEMBL4308841' , 'CHEMBL4304793' , 'CHEMBL4308906'
            'document_journal': 'TEXT',
            # EXAMPLES:
            # 'ACS Med Chem Lett' , 'Eur J Med Chem' , 'Eur J Med Chem' , 'Eur J Med Chem' , 'Eur J Med Chem' , 'Eur J M
            # ed Chem' , 'J Med Chem' , 'Eur J Med Chem' , 'ACS Med Chem Lett' , 'Bioorg Med Chem'
            'document_year': 'NUMERIC',
            # EXAMPLES:
            # '2019' , '2019' , '2018' , '2018' , '2019' , '2019' , '2019' , '2018' , '2019' , '2019'
            'ligand_efficiency': 
            {
                'properties': 
                {
                    'bei': 'NUMERIC',
                    # EXAMPLES:
                    # '27.40' , '12.22' , '15.36' , '14.00' , '15.16' , '15.82' , '15.59' , '13.19' , '21.82' , '11.16'
                    'le': 'NUMERIC',
                    # EXAMPLES:
                    # '0.49' , '0.23' , '0.30' , '0.28' , '0.28' , '0.32' , '0.30' , '0.27' , '0.43' , '0.21'
                    'lle': 'NUMERIC',
                    # EXAMPLES:
                    # '3.03' , '0.44' , '1.62' , '2.37' , '1.04' , '1.19' , '1.56' , '2.16' , '3.77' , '-0.35'
                    'sei': 'NUMERIC',
                    # EXAMPLES:
                    # '10.87' , '10.64' , '7.85' , '6.65' , '7.76' , '13.83' , '7.95' , '16.84' , '20.23' , '7.90'
                }
            },
            'molecule_chembl_id': 'TEXT',
            # EXAMPLES:
            # 'CHEMBL4464046' , 'CHEMBL4591271' , 'CHEMBL4576108' , 'CHEMBL4440394' , 'CHEMBL4577375' , 'CHEMBL1401818' 
            # , 'CHEMBL4585668' , 'CHEMBL4455749' , 'CHEMBL4473647' , 'CHEMBL4474660'
            'molecule_pref_name': 'TEXT',
            # EXAMPLES:
            # 'BELZUTIFAN' , 'AMOXICILLIN SODIUM' , 'AMIFAMPRIDINE' , 'ANIDULAFUNGIN' , 'BUTEIN' , 'PECTOLINARIGENIN' , 
            # 'SINAPIC ACID METHYL ETHER' , 'N-PHENYLBENZAMIDE' , 'NOR-BETA-LAPACHONE' , 'FASIGLIFAM'
            'parent_molecule_chembl_id': 'TEXT',
            # EXAMPLES:
            # 'CHEMBL4464046' , 'CHEMBL4591271' , 'CHEMBL4576108' , 'CHEMBL4440394' , 'CHEMBL4577375' , 'CHEMBL1401818' 
            # , 'CHEMBL4585668' , 'CHEMBL4455749' , 'CHEMBL4473647' , 'CHEMBL4474660'
            'pchembl_value': 'NUMERIC',
            # EXAMPLES:
            # '8.59' , '6.24' , '6.71' , '4.58' , '4.58' , '4.12' , '4.56' , '6.35' , '5.66' , '5.28'
            'potential_duplicate': 'BOOLEAN',
            # EXAMPLES:
            # 'False' , 'False' , 'False' , 'False' , 'False' , 'False' , 'False' , 'False' , 'False' , 'False'
            'qudt_units': 'TEXT',
            # EXAMPLES:
            # 'http://www.openphacts.org/units/Nanomolar' , 'http://qudt.org/vocab/unit#Percent' , 'http://www.openphact
            # s.org/units/Nanomolar' , 'http://qudt.org/vocab/unit#Percent' , 'http://qudt.org/vocab/unit#Percent' , 'ht
            # tp://www.openphacts.org/units/Nanomolar' , 'http://www.openphacts.org/units/Nanomolar' , 'http://qudt.org/
            # vocab/unit#Percent' , 'http://qudt.org/vocab/unit#Percent' , 'http://qudt.org/vocab/unit#Percent'
            'record_id': 'NUMERIC',
            # EXAMPLES:
            # '3147475' , '3151533' , '3148972' , '3148977' , '3147106' , '3147154' , '3150918' , '3148983' , '3147467' 
            # , '3150277'
            'relation': 'TEXT',
            # EXAMPLES:
            # '=' , '>' , '=' , '=' , '<' , '=' , '=' , '=' , '>' , '='
            'src_id': 'NUMERIC',
            # EXAMPLES:
            # '1' , '1' , '1' , '1' , '1' , '1' , '1' , '1' , '1' , '1'
            'standard_flag': 'BOOLEAN',
            # EXAMPLES:
            # 'False' , 'False' , 'True' , 'False' , 'True' , 'True' , 'False' , 'False' , 'False' , 'True'
            'standard_relation': 'TEXT',
            # EXAMPLES:
            # '=' , '>' , '=' , '=' , '<' , '=' , '=' , '=' , '>' , '='
            'standard_text_value': 'TEXT',
            # EXAMPLES:
            # 'Active' , 'Not Determined' , 'Active' , 'Not Determined' , 'Linear Fit' , 'Not Active' , 'Active' , 'Acti
            # ve' , 'Active' , 'Active'
            'standard_type': 'TEXT',
            # EXAMPLES:
            # 'Ratio Ki' , 'Activity' , 'LC50' , 'Activity' , 'MIC' , 'Inhibition' , 'Activity' , 'Activity' , 'pKa' , '
            # IC50'
            'standard_units': 'TEXT',
            # EXAMPLES:
            # 'nM' , '%' , 'nM' , '%' , '%' , 'nM' , 'nM' , '%' , '%' , '%'
            'standard_value': 'NUMERIC',
            # EXAMPLES:
            # '0.85' , '100000.0' , '91.0' , '3000.0' , '50.0' , '54.0' , '6.4' , '2.6' , '50000.0' , '7.6'
            'target_chembl_id': 'TEXT',
            # EXAMPLES:
            # 'CHEMBL612545' , 'CHEMBL375' , 'CHEMBL614096' , 'CHEMBL387' , 'CHEMBL348' , 'CHEMBL5805' , 'CHEMBL2494' , 
            # 'CHEMBL387' , 'CHEMBL2362975' , 'CHEMBL4878'
            'target_organism': 'TEXT',
            # EXAMPLES:
            # 'Mus musculus' , 'Homo sapiens' , 'Homo sapiens' , 'Pseudomonas aeruginosa' , 'Homo sapiens' , 'Homo sapie
            # ns' , 'Homo sapiens' , 'Homo sapiens' , 'Homo sapiens' , 'Influenza A virus (A/Puerto Rico/8/1934(H1N1))'
            'target_pref_name': 'TEXT',
            # EXAMPLES:
            # 'Unchecked' , 'Mus musculus' , 'LOX IMVI' , 'MCF7' , 'Pseudomonas aeruginosa' , 'Toll-like receptor 8' , '
            # CaM kinase IV' , 'MCF7' , 'No relevant target' , 'Cytochrome P450 1B1'
            'target_tax_id': 'NUMERIC',
            # EXAMPLES:
            # '10090' , '9606' , '9606' , '287' , '9606' , '9606' , '9606' , '9606' , '9606' , '211044'
            'text_value': 'TEXT',
            # EXAMPLES:
            # 'Active' , 'Not Determined' , 'Active' , 'Not Determined' , 'Linear Fit' , 'Not Active' , 'Active' , 'Acti
            # ve' , 'Active' , 'Active'
            'toid': 'NUMERIC',
            # EXAMPLES:
            # '11551' , '5136' , '12478' , '12478' , '12480' , '11433' , '12586' , '11887' , '12132' , '13608'
            'type': 'TEXT',
            # EXAMPLES:
            # 'Ratio Ki' , 'Activity' , 'LC50' , 'Activity' , 'MIC' , 'INH' , 'Activity' , 'Activity' , 'pKa' , 'IC50'
            'units': 'TEXT',
            # EXAMPLES:
            # '10'-4M' , '%' , 'uM' , '%' , '%' , 'nM' , 'uM' , '%' , '%' , '%'
            'uo_units': 'TEXT',
            # EXAMPLES:
            # 'UO_0000065' , 'UO_0000187' , 'UO_0000065' , 'UO_0000187' , 'UO_0000187' , 'UO_0000065' , 'UO_0000065' , '
            # UO_0000187' , 'UO_0000187' , 'UO_0000187'
            'upper_value': 'NUMERIC',
            # EXAMPLES:
            # '1021.0' , '211.0' , '18.0' , '35.0' , '1020.0' , '35.0' , '1021.0' , '85.0' , '32.0' , '32.0'
            'value': 'NUMERIC',
            # EXAMPLES:
            # '0.85' , '1.0' , '91.0' , '3.0' , '50.0' , '54.0' , '6.4' , '2.6' , '50.0' , '7.6'
        }
    }
