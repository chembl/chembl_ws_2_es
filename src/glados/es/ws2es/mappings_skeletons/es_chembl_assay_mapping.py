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
                    'assay_generated': 
                    {
                        'properties': 
                        {
                            'confidence_label': 'TEXT',
                            # EXAMPLES:
                            # '1 - Target assigned is non-molecular' , '9 - Direct single protein target assigned' , '1 
                            # - Target assigned is non-molecular' , '0 - Default value - Target unknown or has yet to be
                            #  assigned' , '1 - Target assigned is non-molecular' , '1 - Target assigned is non-molecula
                            # r' , '1 - Target assigned is non-molecular' , '1 - Target assigned is non-molecular' , '1 
                            # - Target assigned is non-molecular' , '1 - Target assigned is non-molecular'
                            'relationship_label': 'TEXT',
                            # EXAMPLES:
                            # 'N - Non-molecular target assigned' , 'D - Direct protein target assigned' , 'N - Non-mole
                            # cular target assigned' , 'U - Default value - Target has yet to be curated' , 'N - Non-mol
                            # ecular target assigned' , 'N - Non-molecular target assigned' , 'N - Non-molecular target 
                            # assigned' , 'N - Non-molecular target assigned' , 'N - Non-molecular target assigned' , 'N
                            #  - Non-molecular target assigned'
                            'type_label': 'TEXT',
                            # EXAMPLES:
                            # 'F - Functional' , 'B - Binding' , 'F - Functional' , 'A - ADME' , 'A - ADME' , 'F - Funct
                            # ional' , 'F - Functional' , 'F - Functional' , 'F - Functional' , 'F - Functional'
                        }
                    },
                    'document_data': 
                    {
                        'properties': 
                        {
                            'doi': 'TEXT',
                            # EXAMPLES:
                            # '10.1016/j.ejmech.2017.08.023' , '10.1016/j.ejmech.2019.111657' , '10.1021/jm4019614' , '1
                            # 0.1021/acsmedchemlett.8b00379' , '10.1016/j.bmcl.2007.04.069' , '10.1128/aac.00183-09' , '
                            # 10.1007/s00044-011-9950-4' , '10.1016/j.ejmech.2008.01.045' , '10.1016/S0960-894X(01)81127
                            # -6' , '10.1016/j.ejmech.2013.10.081'
                            'first_page': 'NUMERIC',
                            # EXAMPLES:
                            # '961' , '111657' , '2275' , '1217' , '4066' , '3118' , '4177' , '2656' , '87' , '135'
                            'journal': 'TEXT',
                            # EXAMPLES:
                            # 'Eur J Med Chem' , 'Eur J Med Chem' , 'J. Med. Chem.' , 'ACS Med Chem Lett' , 'Bioorg. Med
                            # . Chem. Lett.' , 'Antimicrob. Agents Chemother.' , 'Med Chem Res' , 'Eur. J. Med. Chem.' ,
                            #  'Bioorg. Med. Chem. Lett.' , 'Eur. J. Med. Chem.'
                            'last_page': 'NUMERIC',
                            # EXAMPLES:
                            # '981' , '111657' , '2291' , '1222' , '4069' , '3121' , '4192' , '2664' , '92' , '147'
                            'pubmed_id': 'NUMERIC',
                            # EXAMPLES:
                            # '28886509' , '31499361' , '24471873' , '30613329' , '17502140' , '19433566' , '18789558' ,
                            #  '24291567' , '30916555' , '24370012'
                            'title': 'TEXT',
                            # EXAMPLES:
                            # 'Acridone-pyrimidine hybrids- design, synthesis, cytotoxicity studies in resistant and sen
                            # sitive cancer cells and molecular docking studies.' , 'Recent advances in the targeting of
                            #  human DNA ligase I as a potential new strategy for cancer treatment.' , 'Discovery of (E)
                            # -3-((styrylsulfonyl)methyl)pyridine and (E)-2-((styrylsulfonyl)methyl)pyridine derivatives
                            #  as anticancer agents: synthesis, structure-activity relationships, and biological activit
                            # ies.' , 'Structure-Property Basis for Solving Transporter-Mediated Efflux and Pan-Genotypi
                            # c Inhibition in HCV NS5B Inhibitors.' , 'Synthesis and biodistribution of 8-iodo-11-(4-met
                            # hylpiperazino)-5H-dibenzo[b,e][1,4]-diazepine: Iozapine.' , 'Resistance selection studies 
                            # comparing the activity of razupenem (PTZ601) to vancomycin and linezolid against eight met
                            # hicillin-resistant and two methicillin-susceptible Staphylococcus aureus strains.' , 'Disc
                            # overy of 2-(4-cyano-3-trifluoromethylphenyl amino)-4-(4-quinazolinyloxy)-6-piperazinyl(pip
                            # eridinyl)-s-triazines as potential antibacterial agents' , '2/4-Substituted-9-fluorenones 
                            # and their O-glucosides as potential immunomodulators and anti-herpes simplex virus-2 agent
                            # s. Part 5.' , 'Substituted lactam biphenyltetrazoles as angiotensin II mediated antihypert
                            # ensives' , 'Carbonic anhydrase inhibitors. Synthesis, and molecular structure of novel ser
                            # ies N-substituted N'-(2-arylmethylthio-4-chloro-5-methylbenzenesulfonyl)guanidines and the
                            # ir inhibition of human cytosolic isozymes I and II and the transmembrane tumor-associated 
                            # isozymes IX and XII.'
                            'volume': 'NUMERIC',
                            # EXAMPLES:
                            # '139' , '182' , '57' , '9' , '17' , '53' , '21' , '43' , '4' , '71'
                            'year': 'NUMERIC',
                            # EXAMPLES:
                            # '2017' , '2019' , '2014' , '2018' , '2007' , '2009' , '2012' , '2008' , '1994' , '2014'
                        }
                    },
                    'es_completion': 'TEXT',
                    # EXAMPLES:
                    # '{'input': 'Homo sapiens', 'weight': 30}' , '{'input': 'Homo sapiens', 'weight': 30}' , '{'input':
                    #  'Homo sapiens', 'weight': 30}' , '{'input': 'Homo sapiens', 'weight': 30}' , '{'input': 'Brain', 
                    # 'weight': 30}' , '{'input': 'Antimicrobial activity against vancomycin-intermediate Staphylococcus
                    #  aureus 555 measured on day 10 by macrodilution method', 'weight': 80}' , '{'input': 'Shigella fle
                    # xneri', 'weight': 30}' , '{'input': 'CHEMBL1154501', 'weight': 10}' , '{'input': 'Rattus norvegicu
                    # s', 'weight': 30}' , '{'input': 'Homo sapiens', 'weight': 30}'
                    'organism_taxonomy': 
                    {
                        'properties': 
                        {
                            'l1': 'TEXT',
                            # EXAMPLES:
                            # 'Eukaryotes' , 'Eukaryotes' , 'Eukaryotes' , 'Eukaryotes' , 'Eukaryotes' , 'Bacteria' , 'B
                            # acteria' , 'Eukaryotes' , 'Eukaryotes' , 'Eukaryotes'
                            'l2': 'TEXT',
                            # EXAMPLES:
                            # 'Mammalia' , 'Mammalia' , 'Mammalia' , 'Mammalia' , 'Mammalia' , 'Gram-Positive' , 'Gram-N
                            # egative' , 'Mammalia' , 'Mammalia' , 'Mammalia'
                            'l3': 'TEXT',
                            # EXAMPLES:
                            # 'Primates' , 'Primates' , 'Primates' , 'Primates' , 'Lagomorpha' , 'Staphylococcus' , 'Shi
                            # gella' , 'Primates' , 'Rodentia' , 'Primates'
                            'oc_id': 'NUMERIC',
                            # EXAMPLES:
                            # '7' , '7' , '7' , '7' , '69' , '561' , '423' , '7' , '42' , '7'
                            'tax_id': 'NUMERIC',
                            # EXAMPLES:
                            # '9606' , '9606' , '9606' , '9606' , '9986' , '1280' , '623' , '9606' , '10116' , '9606'
                        }
                    },
                    'related_activities': 
                    {
                        'properties': 
                        {
                            'count': 'NUMERIC',
                            # EXAMPLES:
                            # '4' , '1' , '2' , '11' , '1' , '3' , '9' , '9' , '19' , '9'
                        }
                    },
                    'related_compounds': 
                    {
                        'properties': 
                        {
                            'all_chembl_ids': 'TEXT',
                            # EXAMPLES:
                            # 'CHEMBL4160580 CHEMBL4169321 CHEMBL4171390 CHEMBL4170874' , 'CHEMBL4483597' , 'CHEMBL32612
                            # 65 CHEMBL3261276' , 'CHEMBL4571040 CHEMBL4469782 CHEMBL4547789 CHEMBL4583513 CHEMBL4566001
                            #  CHEMBL4439859 CHEMBL4445911 CHEMBL4534277 CHEMBL4549638 CHEMBL4546966 CHEMBL4474552' , 'C
                            # HEMBL247741' , 'CHEMBL262777 CHEMBL126 CHEMBL1256722' , 'CHEMBL2235897 CHEMBL2235889 CHEMB
                            # L2235906 CHEMBL2235904 CHEMBL2235902 CHEMBL2235901 CHEMBL2235887 CHEMBL2235905 CHEMBL22359
                            # 00' , 'CHEMBL467567 CHEMBL468443 CHEMBL467568 CHEMBL457995 CHEMBL506989 CHEMBL467566 CHEMB
                            # L462913 CHEMBL518472 CHEMBL499151' , 'CHEMBL48459 CHEMBL122855 CHEMBL123208 CHEMBL122891 C
                            # HEMBL299151 CHEMBL49262 CHEMBL170196 CHEMBL51084 CHEMBL49207 CHEMBL51622 CHEMBL296731 CHEM
                            # BL422912 CHEMBL425139 CHEMBL191 CHEMBL49192 CHEMBL48602' , 'CHEMBL3104365 CHEMBL3104155 CH
                            # EMBL3104056 CHEMBL3104059 CHEMBL3104055 CHEMBL3104164 CHEMBL3104368 CHEMBL3104161 CHEMBL31
                            # 04369'
                            'count': 'NUMERIC',
                            # EXAMPLES:
                            # '4' , '1' , '2' , '11' , '1' , '3' , '9' , '9' , '16' , '9'
                        }
                    },
                    'related_documents': 
                    {
                        'properties': 
                        {
                            'all_chembl_ids': 'TEXT',
                            # EXAMPLES:
                            # 'CHEMBL4130433' , 'CHEMBL4334494' , 'CHEMBL3259791' , 'CHEMBL4325928' , 'CHEMBL1139986' , 
                            # 'CHEMBL1649524' , 'CHEMBL3044572' , 'CHEMBL1154501' , 'CHEMBL1127878' , 'CHEMBL3102853'
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
                            # 'CHEMBL612818' , 'CHEMBL5694' , 'CHEMBL400' , 'CHEMBL612558' , 'CHEMBL613445' , 'CHEMBL352
                            # ' , 'CHEMBL614396' , 'CHEMBL613107' , 'CHEMBL376' , 'CHEMBL614917'
                            'count': 'NUMERIC',
                            # EXAMPLES:
                            # '1' , '1' , '1' , '1' , '1' , '1' , '1' , '1' , '1' , '1'
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
                    }
                }
            },
            'assay_category': 'TEXT',
            # EXAMPLES:
            # 'other' , 'other' , 'confirmatory' , 'confirmatory' , 'other' , 'confirmatory' , 'confirmatory' , 'confirm
            # atory' , 'confirmatory' , 'confirmatory'
            'assay_cell_type': 'TEXT',
            # EXAMPLES:
            # '2008' , 'MDA-MB-231' , 'Caco-2' , 'PBMC' , 'SK-MEL-2' , 'Sf9' , 'MCF7' , 'MCF7' , 'Hs-578T' , 'HEK293'
            'assay_chembl_id': 'TEXT',
            # EXAMPLES:
            # 'CHEMBL4133612' , 'CHEMBL4337636' , 'CHEMBL3266234' , 'CHEMBL4329908' , 'CHEMBL888070' , 'CHEMBL1665575' ,
            #  'CHEMBL3060818' , 'CHEMBL1019498' , 'CHEMBL796563' , 'CHEMBL3106485'
            'assay_classifications': 
            {
                'properties': 
                {
                    'assay_class_id': 'NUMERIC',
                    # EXAMPLES:
                    # '115' , '254' , '437' , '157' , '341' , '339' , '82' , '33' , '89' , '87'
                    'class_type': 'TEXT',
                    # EXAMPLES:
                    # 'In vivo efficacy' , 'In vivo efficacy' , 'In vivo efficacy' , 'In vivo efficacy' , 'In vivo effic
                    # acy' , 'In vivo efficacy' , 'In vivo efficacy' , 'In vivo efficacy' , 'In vivo efficacy' , 'In viv
                    # o efficacy'
                    'l1': 'TEXT',
                    # EXAMPLES:
                    # 'ANTINEOPLASTIC AND IMMUNOMODULATING AGENTS' , 'GENITO URINARY SYSTEM AND SEX HORMONES' , 'NERVOUS
                    #  SYSTEM' , 'CARDIOVASCULAR SYSTEM' , 'NERVOUS SYSTEM' , 'NERVOUS SYSTEM' , 'ANTINEOPLASTIC AND IMM
                    # UNOMODULATING AGENTS' , 'ALIMENTARY TRACT AND METABOLISM' , 'ANTINEOPLASTIC AND IMMUNOMODULATING A
                    # GENTS' , 'ANTINEOPLASTIC AND IMMUNOMODULATING AGENTS'
                    'l2': 'TEXT',
                    # EXAMPLES:
                    # 'Neoplasm Oncology Models' , 'Assessment of Renal Function' , 'Neuroleptic Activity' , 'Cardiovasc
                    # ular Analysis' , 'Anti-Epileptic Activity' , 'Anti-Epileptic Activity' , 'Carcinoma Oncology Model
                    # s' , 'Genetically Diabetic Animals' , 'Leukemia Oncology Models' , 'Leukemia Oncology Models'
                    'l3': 'TEXT',
                    # EXAMPLES:
                    # 'Neoplasms' , 'Assessment of Glomerular Filtration Rate (GFR) by Plasma Chemistry' , 'Catalepsy in
                    #  Rodents ' , 'General Anti-Hypertensive Activity' , 'General Anti-Convulsant Activity' , 'Electros
                    # hock in Mice' , 'Carcinoma' , 'Spontaneously Diabetic Rats: BB Rat, WBN/Kob Rat, Cohen Diabetic Ra
                    # t, Goto-Kakizaki Rat, Zucker-Fatty Rat, Zucker Diabetic Fatty Rat Zdf/Drt-Fa, Wdf/Ta-Fa Rat, OLETF
                    #  Rat, ESS-Rat, Obese SHR Rat, SHR/N-cp Rat, BHE Rat, LEW.1AR1/Ztm-iddm RAT' , 'P388 Experimental L
                    # eukemia' , 'General Leukemia'
                    'source': 'TEXT',
                    # EXAMPLES:
                    # 'phenotype' , 'Hock_2016' , 'Hock_2016' , 'phenotype' , 'phenotype' , 'Hock_2016' , 'phenotype' , 
                    # 'Vogel_2008' , 'phenotype' , 'phenotype'
                }
            },
            'assay_organism': 'TEXT',
            # EXAMPLES:
            # 'Homo sapiens' , 'Homo sapiens' , 'Homo sapiens' , 'Homo sapiens' , 'Oryctolagus cuniculus' , 'Staphylococ
            # cus aureus' , 'Shigella flexneri' , 'Homo sapiens' , 'Rattus norvegicus' , 'Homo sapiens'
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
                    # arget?' , '+/- 0.0000033 (Mca-RPKPVE-Nval-WRK(Dnp)-NH2; ES002 from R&D Systems)' , 'Is the measure
                    # d interaction considered due to direct binding to target?' , 'Is the measured interaction consider
                    # ed due to direct binding to target?' , 'Is the measured interaction considered due to direct bindi
                    # ng to target?' , 'Is the measured interaction considered due to direct binding to target?' , 'Is t
                    # he measured interaction considered due to direct binding to target?'
                    'relation': 'TEXT',
                    # EXAMPLES:
                    # '=' , '=' , '=' , '=' , '=' , '=' , '=' , '=' , '=' , '='
                    'standard_relation': 'TEXT',
                    # EXAMPLES:
                    # '=' , '=' , '=' , '=' , '=' , '=' , '=' , '=' , '=' , '='
                    'standard_text_value': 'TEXT',
                    # EXAMPLES:
                    # 'Oral' , 'Inhibition of MAP4K4 (HGK)' , 'Oral' , 'Intraperitoneal' , 'Intravenous' , 'Intraperiton
                    # eal' , 'Oral' , 'Oral' , 'Oral' , 'PMID: 22017539'
                    'standard_type': 'TEXT',
                    # EXAMPLES:
                    # 'DOSE' , 'Method' , 'DOSE' , 'DOSE' , 'DOSE' , 'DOSE' , 'DOSE' , 'DOSE' , 'DOSE' , 'DOSE'
                    'standard_type_fixed': 'NUMERIC',
                    # EXAMPLES:
                    # '0' , '0' , '0' , '0' , '0' , '0' , '0' , '0' , '0' , '0'
                    'standard_units': 'TEXT',
                    # EXAMPLES:
                    # 'mg.kg-1' , 'mg.kg-1' , 'mg.kg-1' , 'mg.kg-1' , 'mg.kg-1' , 'mg.kg-1' , 'mg.kg-1' , 'mg.kg-1' , 'm
                    # g.kg-1' , 'mg.kg-1'
                    'standard_value': 'NUMERIC',
                    # EXAMPLES:
                    # '30.0' , '10.0' , '180.0' , '16.0' , '2.5' , '52.0' , '30.0' , '100.0' , '19.0' , '1.0'
                    'text_value': 'TEXT',
                    # EXAMPLES:
                    # 'Oral' , 'Inhibition of MAP4K4 (HGK)' , 'Oral' , 'Intraperitoneal' , 'Intravenous' , 'Intraperiton
                    # eal' , 'Oral' , 'Oral' , 'Oral' , 'PMID: 22017539'
                    'type': 'TEXT',
                    # EXAMPLES:
                    # 'DOSE' , 'Method' , 'DOSE' , 'DOSE' , 'DOSE' , 'DOSE' , 'DOSE' , 'DOSE' , 'DOSE' , 'DOSE'
                    'units': 'TEXT',
                    # EXAMPLES:
                    # 'mg/kg' , 'mg/kg' , 'mg/kg' , 'mg/kg' , 'mg/kg' , 'mg/kg' , 'mg/kg' , 'mg/kg' , 'mg/kg' , 'mg/kg'
                    'value': 'NUMERIC',
                    # EXAMPLES:
                    # '30.0' , '10.0' , '180.0' , '16.0' , '2.5' , '52.0' , '30.0' , '100.0' , '19.0' , '1.0'
                }
            },
            'assay_strain': 'TEXT',
            # EXAMPLES:
            # '555' , 'MTCC 1457' , 'Lewis' , 'MFI' , 'MTCC 3017' , 'CD1' , 'AB' , 'ATCC 11632' , 'isolate 080049Ty' , '
            # serogroup O7'
            'assay_subcellular_fraction': 'TEXT',
            # EXAMPLES:
            # 'Microsome' , 'Microsome' , 'Microsome' , 'Microsome' , 'Membranes' , 'Microsome' , 'microsomes' , 'Mitoch
            # ondria' , 'Microsome' , 'Microsome'
            'assay_tax_id': 'NUMERIC',
            # EXAMPLES:
            # '9606' , '9606' , '9606' , '9606' , '9986' , '1280' , '623' , '9606' , '10116' , '9606'
            'assay_test_type': 'TEXT',
            # EXAMPLES:
            # 'In vivo' , 'In vitro' , 'In vivo' , 'In vivo' , 'In vivo' , 'In vivo' , 'In vitro' , 'In vivo' , 'In vitr
            # o' , 'In vivo'
            'assay_tissue': 'TEXT',
            # EXAMPLES:
            # 'Brain' , 'Blood' , 'Plasma' , 'Ileum' , 'Eye' , 'Kidney' , 'Striatum' , 'Urine' , 'Striatum' , 'Lung'
            'assay_type': 'TEXT',
            # EXAMPLES:
            # 'F' , 'B' , 'F' , 'A' , 'A' , 'F' , 'F' , 'F' , 'F' , 'F'
            'assay_type_description': 'TEXT',
            # EXAMPLES:
            # 'Functional' , 'Binding' , 'Functional' , 'ADME' , 'ADME' , 'Functional' , 'Functional' , 'Functional' , '
            # Functional' , 'Functional'
            'bao_format': 'TEXT',
            # EXAMPLES:
            # 'BAO_0000219' , 'BAO_0000357' , 'BAO_0000219' , 'BAO_0000219' , 'BAO_0000218' , 'BAO_0000218' , 'BAO_00002
            # 18' , 'BAO_0000219' , 'BAO_0000218' , 'BAO_0000219'
            'bao_label': 'TEXT',
            # EXAMPLES:
            # 'cell-based format' , 'single protein format' , 'cell-based format' , 'cell-based format' , 'organism-base
            # d format' , 'organism-based format' , 'organism-based format' , 'cell-based format' , 'organism-based form
            # at' , 'cell-based format'
            'cell_chembl_id': 'TEXT',
            # EXAMPLES:
            # 'CHEMBL3308015' , 'CHEMBL3307960' , 'CHEMBL3307519' , 'CHEMBL3308021' , 'CHEMBL3307743' , 'CHEMBL3308860' 
            # , 'CHEMBL3308403' , 'CHEMBL3308403' , 'CHEMBL3307672' , 'CHEMBL3307715'
            'confidence_description': 'TEXT',
            # EXAMPLES:
            # 'Target assigned is non-molecular' , 'Direct single protein target assigned' , 'Target assigned is non-mol
            # ecular' , 'Default value - Target unknown or has yet to be assigned' , 'Target assigned is non-molecular' 
            # , 'Target assigned is non-molecular' , 'Target assigned is non-molecular' , 'Target assigned is non-molecu
            # lar' , 'Target assigned is non-molecular' , 'Target assigned is non-molecular'
            'confidence_score': 'NUMERIC',
            # EXAMPLES:
            # '1' , '9' , '1' , '0' , '1' , '1' , '1' , '1' , '1' , '1'
            'description': 'TEXT',
            # EXAMPLES:
            # 'Antiproliferative activity against human 2008 cells after 72 hrs by MTT assay' , 'Inhibition of human DNA
            #  ligase 1 using nicked DNA as substrate after 30 mins relative to control' , 'Ratio of ON01910 IC50 to com
            # pound IC50 for ER negative human MDA-MB-231 cells' , 'Efflux ratio of permeability from basolateral side t
            # o apical side over apical side to basolateral side in human Caco2 cells expressing p-gp at 3 uM incubated 
            # for 2 hrs by LC-MS/MS analysis' , 'Biodistribution in rabbit brain at 20 MBq after 0.5 hrs' , 'Antimicrobi
            # al activity against vancomycin-intermediate Staphylococcus aureus 555 measured on day 10 by macrodilution 
            # method' , 'Antimicrobial activity against Shigella flexneri MTCC 1457 at 100 ug/ml by paper-disk diffusion
            #  method' , 'Induction of IFNalpha release in human PBMC at 40 ug/mL after 24 hrs by ELISA' , 'Tested for p
            # ercent of maximal blood pressure drop in high renin rat after peroral administration of 30 mg/kg of dose' 
            # , 'Cytotoxicity against human SK-MEL-2 cells at 10 uM'
            'document_chembl_id': 'TEXT',
            # EXAMPLES:
            # 'CHEMBL4130433' , 'CHEMBL4334494' , 'CHEMBL3259791' , 'CHEMBL4325928' , 'CHEMBL1139986' , 'CHEMBL1649524' 
            # , 'CHEMBL3044572' , 'CHEMBL1154501' , 'CHEMBL1127878' , 'CHEMBL3102853'
            'relationship_description': 'TEXT',
            # EXAMPLES:
            # 'Non-molecular target assigned' , 'Direct protein target assigned' , 'Non-molecular target assigned' , 'De
            # fault value - Target has yet to be curated' , 'Non-molecular target assigned' , 'Non-molecular target assi
            # gned' , 'Non-molecular target assigned' , 'Non-molecular target assigned' , 'Non-molecular target assigned
            # ' , 'Non-molecular target assigned'
            'relationship_type': 'TEXT',
            # EXAMPLES:
            # 'N' , 'D' , 'N' , 'U' , 'N' , 'N' , 'N' , 'N' , 'N' , 'N'
            'src_assay_id': 'NUMERIC',
            # EXAMPLES:
            # '667909' , '509699' , '614457' , '615377' , '579992' , '742343' , '635367' , '511171' , '448930' , '391755
            # '
            'src_id': 'NUMERIC',
            # EXAMPLES:
            # '1' , '1' , '1' , '1' , '1' , '1' , '1' , '1' , '1' , '1'
            'target_chembl_id': 'TEXT',
            # EXAMPLES:
            # 'CHEMBL612818' , 'CHEMBL5694' , 'CHEMBL400' , 'CHEMBL612558' , 'CHEMBL613445' , 'CHEMBL352' , 'CHEMBL61439
            # 6' , 'CHEMBL613107' , 'CHEMBL376' , 'CHEMBL614917'
            'tissue_chembl_id': 'TEXT',
            # EXAMPLES:
            # 'CHEMBL3638188' , 'CHEMBL3638178' , 'CHEMBL3559721' , 'CHEMBL3638244' , 'CHEMBL3638193' , 'CHEMBL3638241' 
            # , 'CHEMBL3638255' , 'CHEMBL3638201' , 'CHEMBL3638255' , 'CHEMBL3638235'
            'variant_sequence': 
            {
                'properties': 
                {
                    'accession': 'TEXT',
                    # EXAMPLES:
                    # 'P51957' , 'Q8NY00' , 'P30556' , 'P56690' , 'Q06124' , 'P10721' , 'P00533' , 'P07949' , 'P42336' ,
                    #  'Q9WKE8'
                    'isoform': 'NUMERIC',
                    # EXAMPLES:
                    # '1' , '1' , '1' , '1' , '1' , '1' , '1' , '1' , '1' , '1'
                    'mutation': 'TEXT',
                    # EXAMPLES:
                    # 'P225A' , 'L213W' , 'N111G' , 'H581L,L583H' , 'F285S' , 'D816V' , 'T790M' , 'M918T' , 'I800L' , 'L
                    # 100I,K103N'
                    'organism': 'TEXT',
                    # EXAMPLES:
                    # 'Homo sapiens' , 'Staphylococcus aureus subsp. aureus MW2' , 'Homo sapiens' , 'Thermus thermophilu
                    # s' , 'Homo sapiens' , 'Homo sapiens' , 'Homo sapiens' , 'Homo sapiens' , 'Homo sapiens' , 'Human i
                    # mmunodeficiency virus 1'
                    'sequence': 'TEXT',
                    # EXAMPLES:
                    # 'MPLAAYCYLRVVGKGSYGEVTLVKHRRDGKQYVIKKLNLRNASSRERRAAEQEAQLLSQLKHPNIVTYKESWEGGDGLLYIVMGFCEGGDLYRKLKE
                    # QKGQLLPENQVVEWFVQIAMALQYLHEKHILHRDLKTQNVFLTRTNIIKVGDLGIARVLENHCDMASTLIGTPYYMSPELFSNKPYNYKSDVWALGCC
                    # VYEMATLKHAFNAKDMNSLVYRIIEGKLPAMPRDYSPELAELIRTMLSKRPEERPSVRSILRQPYIKRQISFFLEATKIKTSKNNIKNGDSQSKPFAT
                    # VVSGEAESNHEVIHPQPLSSEGSQTYIMGEGKCLSQEKPRASGLLKSPASLKAHTCKQDLSNTTELATISSVNIDILPAKGRDSVSDGFVQENQPRYL
                    # DASNELGGICSISQVEEEMLQDNTKSSAQPENLIPMWSSDIVTGEKNEPVKPLQPLIKEQKPKDQSLALSPKLECSGTILAHSNLRLLGSSDSPASAS
                    # RVAGITGVCHHAQDQVAGECIIEKQGRIHPDLQPHNSGSEPSLSRQRRQKRREQTEHRGEKRQVRRDLFAFQESPPRFLPSHPIVGKVDVTSTQKEAE
                    # NQRRVVTGSVSSSRSSEMSSSKDRPLSARERRRLKQSQEEMSSSGPSVRKASLSVAGPGKPQEEDQPLPARRLSSDCSVTQERKQIHCLSEDELSSST
                    # SSTDKSDGDYGEGKGQTNEINALVQLMTQTLKLDSKESCEDVPVANPVSEFKLHRKYRDTLILHGKVAEEAEEIHFKELPSAIMPGSEKIRRLVEVLR
                    # TDVIRGLGVQLLEQVYDLLEEEDEFDREVRLREHMGEKYTTYSVKARQLKFFEENMNF' , 'MAKETFYITTPIYYPSGNLHIGHAYSTVAGDVIAR
                    # YKRMQGYDVRYLTGTDEHGQKIQEKAQKAGKTEIEYLDEMIAGIKQLWAKLEISNDDFIRTTEERHKHVVEQVFERLLKQGDIYLGEYEGWYSVPDET
                    # YYTESQLVDPQYENGKIIGGKSPDSGHEVELVKEESYFFNISKYTDRLLEFYDQNPDFIQPPSRKNEMINNFIKPGLADWAVSRTSFNWGVHVPSNPK
                    # HVVYVWIDALVNYISALGYLSDDESLFNKYWPADIHLMAKEIVRFHSIIWPILLMALDLPLPKKVFAHGWILMKDGKMSKSKGNVVDPNILIDRYGLD
                    # ATRYYLMRELPFGSDGVFTPEAFVERTNFDLANDLGNLVNRTISMVNKYFDGELPAYQGPLHELDEEMEAMALETVKSYTESMESLQFSVALSTVWKF
                    # ISRTNKYIDETTPWVLAKDDSQKDMLGNVMAHLVENIRYAAVLLRPFLTHAPKEIFEQLNINNPQFMEFSSLEQYGVLTESIMVTGQPKPIFPRLDSE
                    # AEIAYIKESMQPPATEEEKEEIPSKPQIDIKDFDKVEIKAATIINAEHVKKSDKLLKIQVDLDSEQRQIVSGIAKFYTPDDIIGKKVAVVTNLKPAKL
                    # MGQKSEGMILSAEKDGVLTLVSLPSAIPNGAVIK' , 'MILNSSTEDGIKRIQDDCPKAGRHNYIFVMIPTLYSIIFVVGIFGNSLVVIVIYFYMKL
                    # KTVASVFLLNLALADLCFLLTLPLWAVYTAMEYRWPFGNYLCKIASASVSFGLYASVFLLTCLSIDRYLAIVHPMKSRLRRTMLVAKVTCIIIWLLAG
                    # LASLPAIIHRNVFFIENTNITVCAFHYESQNSTLPIGLGLTKNILGFLFPFLIILTSYTLIWKALKKAYEIQKNKPRNDDIFKIIMAIVLFFFFSWIP
                    # HQIFTFLDVLIQLGIIRDCRIADIVDTAMPITICIAYFNNCLNPLFYGFLGKKFKRYFLQLLKYIPPKAKSHSNLSTKMSTLSYRPSDNVSSSTKKPA
                    # PCFEVE' , 'MFKEVGEPNFPKLEEEVLAFWKREKIFQKSVENRKGGPRYTVYEGPPTANGLPHVGHAQARSYKDLFPRYKTMRGYYAPRRAGWDTH
                    # GLPVELEVEKKLGLKSKREIEAYGIERFNQACRESVFTYEKEWEAFTERIAYWVDLENAYATLEPTYIESIWWSLKNLFDRGLLYRDHKVVPYCPRCG
                    # TPLSSHEVALGYKEIQDPSVYVRFPLKEPKKLGLEKASLLIWTTTPWTLPGNVAAAVHPEYTYAAFQVGDEALILEEGLGRKLLGEGTPVLKTFPGKA
                    # LEGLPYTPPYPQALEKGYFVVLADYVSQEDGTGIVHQAPAFGAEDLETARVYGLPLLKTVDEEGKLLVEPFKGLYFREANRAILRDLRGRGLLFKEES
                    # YLHSYPHCWRCSTPLMYYATESWFIKNTLFKDELIRKNQEIHWVPPHIKEGRYGEWLKNLVDWALSRNRYWGTPLPIWVCQACGKEEAIGSFQELKAR
                    # ATKPLPEPFDPHRPYVDQVELACACGGTMRRVPYVIDVWYDSGAMPFASLHYPFEHEEVFRESFPADFIAEGIDQTRGWFNSLHQLGVMLFGSIAFKN
                    # VICLGHILDEKGQKMSKSKGNVVDPWDIIREFGADALRWYIYVSAPPEADRRFGPNLVRETVRDYFLTLWNVYSFFVTYANLDRPDLKNPPPPEKRPE
                    # MDRWLLARMQDLIQRVTEALEAYDPTTSARALRDFVVEDLSQWYVRRNRRRFWKNEDALDREAAYATLYEALVLVATLAAPFTPFLAEVLWQNLVRSV
                    # RPEAKESVHLADWPEADPALADEALVAQMRAVLKVVDLARAARAKSGVKTRTPLPLLLVTAPTALEREGLKRFAHEIAEELNVKEVRVLEPGEEILSY
                    # RVLPNLKLLGRKYGKLVPKIREALQRERERAAALALKGEAIPLEVEGEALTLLPEEVLLEAEAPKGYQALEKDGYVAALKVEVTEALRMEGLARDLIR
                    # LLQQARKDMGLKVSDRIRVGYEAEGPYLEALKRHGPWIAEEVLATAFGEGLFGGFEARVEDEEGKAVFHLARAE' , 'MTSRRWFHPNITGVEAENL
                    # LLTRGVDGSFLARPSKSNPGDFTLSVRRNGAVTHIKIQNTGDYYDLYGGEKFATLAELVQYYMEHHGQLKEKNGDVIELKYPLNCADPTSERWFHGHL
                    # SGKEAEKLLTEKGKHGSFLVRESQSHPGDFVLSVRTGDDKGESNDGKSKVTHVMIRCQELKYDVGGGERFDSLTDLVEHYKKNPMVETLGTVLQLKQP
                    # LNTTRINAAEIESRVRELSKLAETTDKVKQGFWEEFETLQQQECKLLYSRKEGQRQENKNKNRYKNILPSDHTRVVLHDGDPNEPVSDYINANIIMPE
                    # FETKCNNSKPKKSYIATQGCLQNTVNDFWRMVFQENSRVIVMTTKEVERGKSKCVKYWPDEYALKEYGVMRVRNVKESAAHDYTLRELKLSKVGQALL
                    # QGNTERTVWQYHFRTWPDHGVPSDPGGVLDFLEEVHHKQESIMDAGPVVVHCSAGIGRTGTFIVIDILIDIIREKGVDCDIDVPKTIQMVRSQRSGMV
                    # QTEAQYRFIYMAVQHYIETLQRRIEEEQKSKRKGHEYTNIKYSLADQTSGDQSPLPPCTPTPPCAEMREDSARVYENVGLMQQQKSFR' , 'MRGAR
                    # GAWDFLCVLLLLLRVQTGSSQPSVSPGEPSPPSIHPGKSDLIVRVGDEIRLLCTDPGFVKWTFEILDETNENKQNEWITEKAEATNTGKYTCTNKHGL
                    # SNSIYVFVRDPAKLFLVDRSLYGKEDNDTLVRCPLTDPEVTNYSLKGCQGKPLPKDLRFIPDPKAGIMIKSVKRAYHRLCLHCSVDQEGKSVLSEKFI
                    # LKVRPAFKAVPVVSVSKASYLLREGEEFTVTCTIKDVSSSVYSTWKRENSQTKLQEKYNSWHHGDFNYERQATLTISSARVNDSGVFMCYANNTFGSA
                    # NVTTTLEVVDKGFINIFPMINTTVFVNDGENVDLIVEYEAFPKPEHQQWIYMNRTFTDKWEDYPKSENESNIRYVSELHLTRLKGTEGGTYTFLVSNS
                    # DVNAAIAFNVYVNTKPEILTYDRLVNGMLQCVAAGFPEPTIDWYFCPGTEQRCSASVLPVDVQTLNSSGPPFGKLVVQSSIDSSAFKHNGTVECKAYN
                    # DVGKTSAYFNFAFKGNNKEQIHPHTLFTPLLIGFVIVAGMMCIIVMILTYKYLQKPMYEVQWKVVEEINGNNYVYIDPTQLPYDHKWEFPRNRLSFGK
                    # TLGAGAFGKVVEATAYGLIKSDAAMTVAVKMLKPSAHLTEREALMSELKVLSYLGNHMNIVNLLGACTIGGPTLVITEYCCYGDLLNFLRRKRDSFIC
                    # SKQEDHAEAALYKNLLHSKESSCSDSTNEYMDMKPGVSYVVPTKADKRRSVRIGSYIERDVTPAIMEDDELALDLEDLLSFSYQVAKGMAFLASKNCI
                    # HRDLAARNILLTHGRITKICDFGLARVIKNDSNYVVKGNARLPVKWMAPESIFNCVYTFESDVWSYGIFLWELFSLGSSPYPGMPVDSKFYKMIKEGF
                    # RMLSPEHAPAEMYDIMKTCWDADPLKRPTFKQIVQLIEKQISESTNHIYSNLANCSPNRQKPVVDHSVRINSVGSTASSSQPLLVHDDV' , 'MRPS
                    # GTAGAALLALLAALCPASRALEEKKVCQGTSNKLTQLGTFEDHFLSLQRMFNNCEVVLGNLEITYVQRNYDLSFLKTIQEVAGYVLIALNTVERIPLE
                    # NLQIIRGNMYYENSYALAVLSNYDANKTGLKELPMRNLQEILHGAVRFSNNPALCNVESIQWRDIVSSDFLSNMSMDFQNHLGSCQKCDPSCPNGSCW
                    # GAGEENCQKLTKIICAQQCSGRCRGKSPSDCCHNQCAAGCTGPRESDCLVCRKFRDEATCKDTCPPLMLYNPTTYQMDVNPEGKYSFGATCVKKCPRN
                    # YVVTDHGSCVRACGADSYEMEEDGVRKCKKCEGPCRKVCNGIGIGEFKDSLSINATNIKHFKNCTSISGDLHILPVAFRGDSFTHTPPLDPQELDILK
                    # TVKEITGFLLIQAWPENRTDLHAFENLEIIRGRTKQHGQFSLAVVSLNITSLGLRSLKEISDGDVIISGNKNLCYANTINWKKLFGTSGQKTKIISNR
                    # GENSCKATGQVCHALCSPEGCWGPEPRDCVSCRNVSRGRECVDKCNLLEGEPREFVENSECIQCHPECLPQAMNITCTGRGPDNCIQCAHYIDGPHCV
                    # KTCPAGVMGENNTLVWKYADAGHVCHLCHPNCTYGCTGPGLEGCPTNGPKIPSIATGMVGALLLLLVVALGIGLFMRRRHIVRKRTLRRLLQERELVE
                    # PLTPSGEAPNQALLRILKETEFKKIKVLGSGAFGTVYKGLWIPEGEKVKIPVAIKELREATSPKANKEILDEAYVMASVDNPHVCRLLGICLTSTVQL
                    # IMQLMPFGCLLDYVREHKDNIGSQYLLNWCVQIAKGMNYLEDRRLVHRDLAARNVLVKTPQHVKITDFGLAKLLGAEEKEYHAEGGKVPIKWMALESI
                    # LHRIYTHQSDVWSYGVTVWELMTFGSKPYDGIPASEISSILEKGERLPQPPICTIDVYMIMVKCWMIDADSRPKFRELIIEFSKMARDPQRYLVIQGD
                    # ERMHLPSPTDSNFYRALMDEEDMDDVVDADEYLIPQQGFFSSPSTSRTPLLSSLSATSNNSTVACIDRNGLQSCPIKEDSFLQRYSSDPTGALTEDSI
                    # DDTFLPVPEYINQSVPKRPAGSVQNPVYHNQPLNPAPSRDPHYQDPHSTAVGNPEYLNTVQPTCVNSTFDSPAHWAQKGSHQISLDNPDYQQDFFPKE
                    # AKPNGIFKGSTAENAEYLRVAPQSSEFIGA' , 'MAKATSGAAGLRLLLLLLLPLLGKVALGLYFSRDAYWEKLYVDQAAGTPLLYVHALRDAPEEV
                    # PSFRLGQHLYGTYRTRLHENNWICIQEDTGLLYLNRSLDHSSWEKLSVRNRGFPLLTVYLKVFLSPTSLREGECQWPGCARVYFSFFNTSFPACSSLK
                    # PRELCFPETRPSFRIRENRPPGTFHQFRLLPVQFLCPNISVAYRLLEGEGLPFRCAPDSLEVSTRWALDREQREKYELVAVCTVHAGAREEVVMVPFP
                    # VTVYDEDDSAPTFPAGVDTASAVVEFKRKEDTVVATLRVFDADVVPASGELVRRYTSTLLPGDTWAQQTFRVEHWPNETSVQANGSFVRATVHDYRLV
                    # LNRNLSISENRTMQLAVLVNDSDFQGPGAGVLLLHFNVSVLPVSLHLPSTYSLSVSRRARRFAQIGKVCVENCQAFSGINVQYKLHSSGANCSTLGVV
                    # TSAEDTSGILFVNDTKALRRPKCAELHYMVVATDQQTSRQAQAQLLVTVEGSYVAEEAGCPLSCAVSKRRLECEECGGLGSPTGRCEWRQGDGKGITR
                    # NFSTCSPSTKTCPDGHCDVVETQDINICPQDCLRGSIVGGHEPGEPRGIKAGYGTCNCFPEEEKCFCEPEDIQDPLCDELCRTVIAAAVLFSFIVSVL
                    # LSAFCIHCYHKFAHKPPISSAEMTFRRPAQAFPVSYSSSGARRPSLDSMENQVSVDAFKILEDPKWEFPRKNLVLGKTLGEGEFGKVVKATAFHLKGR
                    # AGYTTVAVKMLKENASPSELRDLLSEFNVLKQVNHPHVIKLYGACSQDGPLLLIVEYAKYGSLRGFLRESRKVGPGYLGSGGSRNSSSLDHPDERALT
                    # MGDLISFAWQISQGMQYLAEMKLVHRDLAARNILVAEGRKMKISDFGLSRDVYEEDSYVKRSQGRIPVKWTAIESLFDHIYTTQSDVWSFGVLLWEIV
                    # TLGGNPYPGIPPERLFNLLKTGHRMERPDNCSEEMYRLMLQCWKQEPDKRPVFADISKDLEKMMVKRRDYLDLAASTPSDSLIYDDGLSEEETPLVDC
                    # NNAPLPRALPSTWIENKLYGMSDPNWPGESPVPLTRADGTNTGFPRYPNDSVYANWMLSPSAAKLMDTFDS' , 'MPPRPSSGELWGIHLMPPRILV
                    # ECLLPNGMIVTLECLREATLITIKHELFKEARKYPLHQLLQDESSYIFVSVTQEAEREEFFDETRRLCDLRLFQPFLKVIEPVGNREEKILNREIGFA
                    # IGMPVCEFDMVKDPEVQDFRRNILNVCKEAVDLRDLNSPHSRAMYVYPPNVESSPELPKHIYNKLDKGQIIVVIWVIVSPNNDKQKYTLKINHDCVPE
                    # QVIAEAIRKKTRSMLLSSEQLKLCVLEYQGKYILKVCGCDEYFLEKYPLSQYKYIRSCIMLGRMPNLMLMAKESLYSQLPMDCFTMPSYSRRISTATP
                    # YMNGETSTKSLWVINSALRIKILCATYVNVNIRDIDKIYVRTGIYHGGEPLCDNVNTQRVPCSNPRWNEWLNYDIYIPDLPRAARLCLSICSVKGRKG
                    # AKEEHCPLAWGNINLFDYTDTLVSGKMALNLWPVPHGLEDLLNPIGVTGSNPNKETPCLELEFDWFSSVVKFPDMSVIEEHANWSVSREAGFSYSHAG
                    # LSNRLARDNELRENDKEQLKAISTRDPLSEITEQEKDFLWSHRHYCVTIPEILPKLLLSVKWNSRDEVAQMYCLVKDWPPIKPEQAMELLDCNYPDPM
                    # VRGFAVRCLEKYLTDDKLSQYLIQLVQVLKYEQYLDNLLVRFLLKKALTNQRIGHFFFWHLKSEMHNKTVSQRFGLLLESYCRACGMYLKHLNRQVEA
                    # MEKLINLTDILKQEKKDETQKVQMKFLVEQMRRPDFMDALQGFLSPLNPAHQLGNLRLEECRIMSSAKRPLWLNWENPDIMSELLFQNNEILFKNGDD
                    # LRQDMLTLQIIRIMENIWQNQGLDLRMLPYGCLSIGDCVGLIEVVRNSHTIMQIQCKGGLKGALQFNSHTLHQWLKDKNKGEIYDAAIDLFTRSCAGY
                    # CVATFILGIGDRHNSNIMVKDDGQLFHIDFGHFLDHKKKKFGYKRERVPFVLTQDFLIVISKGAQECTKTREFERFQEMCYKAYLAIRQHANLFINLF
                    # SMMLGSGMPELQSFDDIAYIRKTLALDKTEQEALEYFMKQMNDAHHGGWTTKMDWIFHTIKQHALN' , 'PISPIXTVPVKLKPGMDGPKVKQWPLT
                    # EEKIKALTEICTEMEKEGKIEKIGPENPYNTPVFAIKKKDSTKWRKVVDFRELNKRTQDFWEVQLGIPHPAGIKKNKSVTVLDVGDAYFSVPLDKDFR
                    # KYTAFTIPSINNETPGIRYQYNVLPQGWKGSPAIFQSSMTKILEPFRKQNPDIVIYQYMDDLYVGSDLEIEQHRAKIEELRQHLLRWGFTTPDKKHQK
                    # EPPFLWMGYELHPDKWTVQPIVLPEKDSWTVNXXXX'
                    'tax_id': 'NUMERIC',
                    # EXAMPLES:
                    # '9606' , '196620' , '9606' , '300852' , '9606' , '9606' , '9606' , '9606' , '9606' , '11676'
                    'version': 'NUMERIC',
                    # EXAMPLES:
                    # '2' , '1' , '1' , '2' , '1' , '2' , '3' , '2' , '2' , '1'
                }
            }
        }
    }
