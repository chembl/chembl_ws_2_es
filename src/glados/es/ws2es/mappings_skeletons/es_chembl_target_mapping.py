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
                    # '{'input': 'DEN1', 'weight': 75}' , '{'input': 'Cold-induced autoinflammatory syndrome 1 protein',
                    #  'weight': 75}' , '{'input': 'Glucose-6-phosphate dehydrogenase-6-phosphogluconolactonase', 'weigh
                    # t': 100}' , '{'input': 'KIAA1707', 'weight': 75}' , '{'input': 'Sentrin-specific protease 6', 'wei
                    # ght': 100}' , '{'input': 'Deoxycytidine deaminase', 'weight': 75}' , '{'input': 'Homo sapiens', 'w
                    # eight': 20}' , '{'input': 'CHEMBL1741263', 'weight': 10}' , '{'input': 'CHEMBL1741265', 'weight': 
                    # 10}' , '{'input': 'Homo sapiens', 'weight': 20}'
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
                    # 'SENP8' , 'NALP3' , 'SENP7' , 'SENP6' , 'APOBEC3F' , 'ATG4B' , 'Interleukin_18' , 'Osteopontin' , 
                    # 'SLC47A1' , 'SULT1A1'
                    'xref_name': 'TEXT',
                    # EXAMPLES:
                    # 'N-formylpeptide receptor (FPR)' , 'Phosphodiesterase type 10A' , 'Nicotinic acetylcholine recepto
                    # r (nAChR) alpha4/beta2' , 'Neuronal alpha-4/beta-2 nicotinic acetylcholine receptor (nAChR)' , 'N-
                    # Methyl D-aspartate (NMDA) receptor' , 'Alpha1-Adrenoceptor' , 'Epidermal growth factor receptor' ,
                    #  'Muscarinic M2 receptor' , '5-HT1A receptors' , 'Farnesyl diphosphate synthase'
                    'xref_src': 'TEXT',
                    # EXAMPLES:
                    # 'Wikipedia' , 'Wikipedia' , 'Wikipedia' , 'Wikipedia' , 'Wikipedia' , 'Wikipedia' , 'Wikipedia' , 
                    # 'Wikipedia' , 'Wikipedia' , 'Wikipedia'
                }
            },
            'organism': 'TEXT',
            # EXAMPLES:
            # 'Homo sapiens' , 'Homo sapiens' , 'Plasmodium berghei' , 'Homo sapiens' , 'Homo sapiens' , 'Homo sapiens' 
            # , 'Homo sapiens' , 'Plasmodium yoelii yoelii' , 'Plasmodium berghei str. ANKA' , 'Homo sapiens'
            'pref_name': 'TEXT',
            # EXAMPLES:
            # 'Sentrin-specific protease 8' , 'NACHT, LRR and PYD domains-containing protein 3' , 'Glucose-6-phosphate d
            # ehydrogenase-6-phosphogluconolactonase' , 'Sentrin-specific protease 7' , 'Sentrin-specific protease 6' , 
            # 'DNA dC->dU-editing enzyme APOBEC-3G' , 'Cysteine protease ATG4B' , 'Glutathione S-transferase' , 'Dihydro
            # pteroate synthetase, putative' , 'Interleukin-18'
            'species_group_flag': 'BOOLEAN',
            # EXAMPLES:
            # 'False' , 'False' , 'False' , 'False' , 'False' , 'False' , 'False' , 'False' , 'False' , 'False'
            'target_chembl_id': 'TEXT',
            # EXAMPLES:
            # 'CHEMBL1741207' , 'CHEMBL1741208' , 'CHEMBL1741212' , 'CHEMBL1741213' , 'CHEMBL1741215' , 'CHEMBL1741217' 
            # , 'CHEMBL1741221' , 'CHEMBL1741263' , 'CHEMBL1741265' , 'CHEMBL1741305'
            'target_components': 
            {
                'properties': 
                {
                    'accession': 'TEXT',
                    # EXAMPLES:
                    # 'Q96LD8' , 'Q96P20' , 'Q9BHT9' , 'Q9BQF6' , 'Q9GZR1' , 'Q9HC16' , 'Q9Y4P1' , 'Q7REH6' , 'A0A113T0T
                    # 6' , 'Q14116'
                    'component_description': 'TEXT',
                    # EXAMPLES:
                    # 'Sentrin-specific protease 8' , 'NACHT, LRR and PYD domains-containing protein 3' , 'Glucose-6-pho
                    # sphate dehydrogenase-6-phosphogluconolactonase' , 'Sentrin-specific protease 7' , 'Sentrin-specifi
                    # c protease 6' , 'DNA dC->dU-editing enzyme APOBEC-3G' , 'Cysteine protease ATG4B' , 'Glutathione S
                    # -transferase' , '6-hydroxymethyl-7,8-dihydropterin pyrophosphokinase' , 'Interleukin-18'
                    'component_id': 'NUMERIC',
                    # EXAMPLES:
                    # '5529' , '5431' , '5435' , '5436' , '5479' , '5481' , '5485' , '5257' , '5259' , '4858'
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
                            # 'None' , 'None' , 'None' , 'None' , 'None' , 'None' , 'None' , 'None' , 'None' , 'None'
                            'syn_type': 'TEXT',
                            # EXAMPLES:
                            # 'None' , 'None' , 'None' , 'None' , 'None' , 'None' , 'None' , 'None' , 'None' , 'None'
                        }
                    },
                    'target_component_xrefs': 
                    {
                        'properties': 
                        {
                            'xref_id': 'TEXT',
                            # EXAMPLES:
                            # 'None' , 'None' , 'None' , 'None' , 'None' , 'None' , 'None' , 'None' , 'None' , 'None'
                            'xref_name': 'TEXT',
                            # EXAMPLES:
                            # 'None' , 'None' , 'None' , 'None' , 'None' , 'None' , 'None' , 'None' , 'None' , 'None'
                            'xref_src_db': 'TEXT',
                            # EXAMPLES:
                            # 'None' , 'None' , 'None' , 'None' , 'None' , 'None' , 'None' , 'None' , 'None' , 'None'
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
            # '9606' , '9606' , '5821' , '9606' , '9606' , '9606' , '9606' , '73239' , '5823' , '9606'
        }
    }
