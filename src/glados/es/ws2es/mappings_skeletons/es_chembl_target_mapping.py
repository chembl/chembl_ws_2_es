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
                    # '{'input': 'Homo sapiens', 'weight': 20}' , '{'input': 'Homo sapiens', 'weight': 20}' , '{'input':
                    #  'CHEMBL1884', 'weight': 10}' , '{'input': 'Escherichia coli K-12', 'weight': 20}' , '{'input': 'H
                    # omo sapiens', 'weight': 20}' , '{'input': '3.5.2.6', 'weight': 75}' , '{'input': 'CHEMBL2051', 'we
                    # ight': 10}' , '{'input': 'Homo sapiens', 'weight': 20}' , '{'input': 'Homo sapiens', 'weight': 20}
                    # ' , '{'input': 'DNA polymerase catalytic subunit', 'weight': 75}'
                    'related_compounds': 
                    {
                        'properties': 
                        {
                        }
                    },
                }
            },
            'cross_references': 
            {
                'properties': 
                {
                    'xref_id': 'TEXT',
                    # EXAMPLES:
                    # 'O60706' , 'O95180' , 'O96760' , 'P0ABQ4' , 'P00533' , 'P03468' , 'P04035' , 'P04150' , 'P04293' ,
                    #  'P04818'
                    'xref_name': 'TEXT',
                    # EXAMPLES:
                    # 'Epidermal growth factor receptor' , 'Muscarinic M2 receptor' , '5-HT1A receptors' , 'Farnesyl dip
                    # hosphate synthase' , 'D2 dopamine receptors' , 'Aromatic L-amino acid decarboxylase (AAAD)' , 'Mon
                    # oamine oxidase A (MAO-A)' , 'D1 dopamine receptors' , 'Acetylcholinesterase (AChE)' , '5-HT1B sero
                    # tonin receptors'
                    'xref_src': 'TEXT',
                    # EXAMPLES:
                    # 'canSAR-Target' , 'canSAR-Target' , 'canSAR-Target' , 'canSAR-Target' , 'canSAR-Target' , 'canSAR-
                    # Target' , 'canSAR-Target' , 'canSAR-Target' , 'canSAR-Target' , 'canSAR-Target'
                }
            },
            'organism': 'TEXT',
            # EXAMPLES:
            # 'Homo sapiens' , 'Homo sapiens' , 'Ascaris suum' , 'Escherichia coli K-12' , 'Homo sapiens' , 'Escherichia
            #  coli' , 'Influenza A virus (A/Puerto Rico/8/1934(H1N1))' , 'Homo sapiens' , 'Homo sapiens' , 'Herpes simp
            # lex virus (type 1 / strain 17)'
            'pref_name': 'TEXT',
            # EXAMPLES:
            # 'Sulfonylurea receptor 2' , 'Voltage-gated T-type calcium channel alpha-1H subunit' , 'Nicotinic acetylcho
            # line receptor alpha subunit' , 'Dihydrofolate reductase' , 'Epidermal growth factor receptor erbB1' , 'Bet
            # a-lactamase TEM' , 'Neuraminidase' , 'HMG-CoA reductase' , 'Glucocorticoid receptor' , 'Human herpesvirus 
            # 1 DNA polymerase'
            'species_group_flag': 'BOOLEAN',
            # EXAMPLES:
            # 'False' , 'False' , 'False' , 'False' , 'False' , 'False' , 'False' , 'False' , 'False' , 'False'
            'target_chembl_id': 'TEXT',
            # EXAMPLES:
            # 'CHEMBL1971' , 'CHEMBL1859' , 'CHEMBL1884' , 'CHEMBL1809' , 'CHEMBL203' , 'CHEMBL2065' , 'CHEMBL2051' , 'C
            # HEMBL402' , 'CHEMBL2034' , 'CHEMBL1872'
            'target_components': 
            {
                'properties': 
                {
                    'accession': 'TEXT',
                    # EXAMPLES:
                    # 'O60706' , 'O95180' , 'O96760' , 'P0ABQ4' , 'P00533' , 'P62593' , 'P03468' , 'P04035' , 'P04150' ,
                    #  'P04293'
                    'component_description': 'TEXT',
                    # EXAMPLES:
                    # 'ATP-binding cassette sub-family C member 9' , 'Voltage-dependent T-type calcium channel subunit a
                    # lpha-1H' , 'Nicotinic acetylcholine receptor alpha subunit' , 'Dihydrofolate reductase' , 'Epiderm
                    # al growth factor receptor' , 'Beta-lactamase TEM' , 'Neuraminidase' , '3-hydroxy-3-methylglutaryl-
                    # coenzyme A reductase' , 'Glucocorticoid receptor' , 'DNA polymerase catalytic subunit'
                    'component_id': 'NUMERIC',
                    # EXAMPLES:
                    # '294' , '167' , '198' , '103' , '147' , '405' , '391' , '312' , '371' , '188'
                    'component_type': 'TEXT',
                    # EXAMPLES:
                    # 'PROTEIN' , 'PROTEIN' , 'PROTEIN' , 'PROTEIN' , 'PROTEIN' , 'PROTEIN' , 'PROTEIN' , 'PROTEIN' , 'P
                    # ROTEIN' , 'PROTEIN'
                    'relationship': 'TEXT',
                    # EXAMPLES:
                    # 'SINGLE PROTEIN' , 'SINGLE PROTEIN' , 'SINGLE PROTEIN' , 'SINGLE PROTEIN' , 'SINGLE PROTEIN' , 'SI
                    # NGLE PROTEIN' , 'SINGLE PROTEIN' , 'SINGLE PROTEIN' , 'SINGLE PROTEIN' , 'SINGLE PROTEIN'
                    'target_component_synonyms': 
                    {
                        'properties': 
                        {
                            'component_synonym': 'TEXT',
                            # EXAMPLES:
                            # 'ABCC9' , 'CACNA1H' , 'Nicotinic acetylcholine receptor alpha subunit' , '1.5.1.3' , '2.7.
                            # 10.1' , '3.5.2.6' , '3.2.1.18' , '1.1.1.34' , 'Glucocorticoid receptor' , '2.7.7.7'
                            'syn_type': 'TEXT',
                            # EXAMPLES:
                            # 'GENE_SYMBOL' , 'GENE_SYMBOL' , 'UNIPROT' , 'EC_NUMBER' , 'EC_NUMBER' , 'EC_NUMBER' , 'EC_
                            # NUMBER' , 'EC_NUMBER' , 'UNIPROT' , 'EC_NUMBER'
                        }
                    },
                    'target_component_xrefs': 
                    {
                        'properties': 
                        {
                            'xref_id': 'TEXT',
                            # EXAMPLES:
                            # 'ABCC9' , 'ENSG00000196557' , 'GO:0005886' , 'GO:0005829' , 'EGFR' , 'GO:0005515' , 'GO:00
                            # 00139' , 'HMGCR' , 'NR3C1' , 'GO:0042025'
                            'xref_name': 'TEXT',
                            # EXAMPLES:
                            # 'Cardiomyopathy, dilated, 10; Atrial fibrillation, familial 12; Cantu syndrome' , 'voltage
                            # -gated sodium channel complex' , 'plasma membrane' , 'cytosol' , 'Acute myeloid leukemia, 
                            # familial; Lung cancer, familial, susceptibilty to' , 'protein binding' , 'Golgi membrane' 
                            # , 'Statins, efficacy of' , 'Cortisol resistance' , 'host cell nucleus'
                            'xref_src_db': 'TEXT',
                            # EXAMPLES:
                            # 'CGD' , 'EnsemblGene' , 'GoComponent' , 'GoComponent' , 'CGD' , 'GoFunction' , 'GoComponen
                            # t' , 'CGD' , 'CGD' , 'GoComponent'
                        }
                    }
                }
            },
            'target_type': 'TEXT',
            # EXAMPLES:
            # 'SINGLE PROTEIN' , 'SINGLE PROTEIN' , 'SINGLE PROTEIN' , 'SINGLE PROTEIN' , 'SINGLE PROTEIN' , 'SINGLE PRO
            # TEIN' , 'SINGLE PROTEIN' , 'SINGLE PROTEIN' , 'SINGLE PROTEIN' , 'SINGLE PROTEIN'
            'tax_id': 'NUMERIC',
            # EXAMPLES:
            # '9606' , '9606' , '6253' , '83333' , '9606' , '562' , '211044' , '9606' , '9606' , '10299'
        }
    }
