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
                    'all_graph_chembl_ids': 'TEXT',
                    # EXAMPLES:
                    # 'CHEMBL3638309' , 'CHEMBL3526762' , 'CHEMBL3544730' , 'CHEMBL1083993' , 'CHEMBL4525790' , 'CHEMBL4
                    # 525790' , 'CHEMBL800' , 'CHEMBL1314' , 'CHEMBL3638309' , 'CHEMBL3544741'
                    'compound_data': 
                    {
                        'properties': 
                        {
                            'drug_pref_name': 'TEXT',
                            # EXAMPLES:
                            # 'DIFLUNISAL' , 'PKI-179' , 'ERYTHROMYCIN LACTOBIONATE' , 'AMIODARONE HYDROCHLORIDE' , 'alp
                            # ha-TOCHOPHEROL' , 'alpha-TOCHOPHEROL' , 'INDOMETHACIN' , 'TIOPRONIN' , 'DIFLUNISAL' , 'TRI
                            # HEXYPHENIDYL HYDROCHLORIDE'
                            'metabolite_image_file': 'TEXT',
                            # EXAMPLES:
                            # 'smallMolecule.svg' , 'smallMolecule.svg' , 'smallMolecule.svg' , 'unknown.svg' , 'unknown
                            # .svg' , 'smallMolecule.svg' , 'unknown.svg' , 'smallMolecule.svg' , 'smallMolecule.svg' , 
                            # 'unknown.svg'
                            'metabolite_pref_name': 'TEXT',
                            # EXAMPLES:
                            # 'DESETHYLAMIODARONE' , 'HYDROXY PIROXICAM METABOLITE' , 'DESCHLOROBENZOYL INDOMETHACIN' , 
                            # 'ACETOHYDROXAMIC ACID' , 'ADIPIC ACID' , 'M2,M3a' , 'M33,M42,M43' , 'DDCTP' , 'DIOSMETIN' 
                            # , 'unnamed DHD2'
                            'substrate_image_file': 'TEXT',
                            # EXAMPLES:
                            # 'unknown.svg' , 'unknown.svg' , 'unknown.svg' , 'unknown.svg' , 'unknown.svg' , 'smallMole
                            # cule.svg' , 'unknown.svg' , 'unknown.svg' , 'unknown.svg' , 'smallMolecule.svg'
                            'substrate_pref_name': 'TEXT',
                            # EXAMPLES:
                            # 'DIFLUNISAL' , 'PKI-179' , 'ERYTHROMYCIN' , 'AMIODARONE' , 'alpha-TOCHOPHEROL' , 'TIOPRONI
                            # N' , 'DIFLUNISAL' , 'TRIHEXYPHENIDYL' , 'PIROXICAM' , 'INDOMETHACIN'
                        }
                    }
                }
            },
            'drug_chembl_id': 'TEXT',
            # EXAMPLES:
            # 'CHEMBL898' , 'CHEMBL1258517' , 'CHEMBL1200506' , 'CHEMBL1083993' , 'CHEMBL49563' , 'CHEMBL49563' , 'CHEMB
            # L6' , 'CHEMBL1314' , 'CHEMBL898' , 'CHEMBL1092'
            'enzyme_name': 'TEXT',
            # EXAMPLES:
            # 'UGT2B7' , 'CYP3A4' , 'CYP2C8' , 'UGT2B7' , 'CYP2C9' , 'CYP2C9' , 'Urease' , 'CYP2C9' , 'CYP2D6' , 'CYP2C9
            # '
            'met_comment': 'TEXT',
            # EXAMPLES:
            # 'Organ: Liver|Comment: Found in urine.' , 'Species: Homo sapiens,Macaca fascicularis|Conditions:Liver micr
            # osomes' , 'Organ: Liver|Comment: erythromycin may inhibit the oxidation of other substrates of CYP3A4.' , 
            # 'Conditions: in-vitro in-vivo' , 'Conditions: in-vitro in-vivo' , 'Organ: Unknown|Comment: The principal m
            # etabolite. OTHER PATHWAYS OF METABOLISM SUCH AS OXIDATION AND DISULPHIDE FORMATION BUT THESE ARE LARGELY R
            # EVERSIBLE SO PROBABLY VERY HARD TO ISOLATE AND IDENTIFY SUCH METABOLITES' , 'Organ: Liver|Comment: The pre
            # dominant metabolite, found in urine' , 'Organ: Unknown|Comment: Exists as 3 isomers.' , 'Organ: Liver|Comm
            # ent: The major metabolic route and metabolism. Found in the plasma. INDOMETHACIN ITSELF IS EXCRETED IN THE
            #  URINE AS A GLUCURONIDE.' , 'Organ: Liver|Comment: One of the primary metabolites. Found in the plasma. IN
            # DOMETHACIN ITSELF IS EXCRETED IN THE URINE AS A GLUCURONIDE.'
            'met_conversion': 'TEXT',
            # EXAMPLES:
            # 'Glucuronide conjugation at the carboxylic acid forming an ester' , 'N-methylation' , 'removal of one of t
            # he ethane groups from the N atom.' , 'N-dealcyaltion' , 'Amide hydrolysis' , 'Glucuronide conjugation at a
            #  hydroxyl forming an ether' , 'hydroxylation' , 'Hydroxylation at the 5' position of the pyridyl side chai
            # n' , 'O-Demethylation' , 'N-dealcyaltion'
            'met_id': 'NUMERIC',
            # EXAMPLES:
            # '946' , '2201' , '1145' , '1152' , '2619' , '2620' , '1213' , '1278' , '1283' , '1345'
            'metabolism_refs': 
            {
                'properties': 
                {
                    'ref_id': 'TEXT',
                    # EXAMPLES:
                    # 'label/2007/018445s058lbl.pdf' , '20952552' , 'label/2013/060359s028lbl.pdf' , 'label/2014/018972s
                    # 048lbl.pdf' , '23160821' , '23160821' , 'label/2007/016059s097,017814s040,018332s030lbl.pdf' , '15
                    # 05618' , 'label/2007/018445s058lbl.pdf' , '10.3109/00498257809060395'
                    'ref_type': 'TEXT',
                    # EXAMPLES:
                    # 'FDA' , 'PMID' , 'FDA' , 'FDA' , 'PMID' , 'PMID' , 'FDA' , 'PMID' , 'FDA' , 'DOI'
                    'ref_url': 'TEXT',
                    # EXAMPLES:
                    # 'http://www.accessdata.fda.gov/drugsatfda_docs/label/2007/018445s058lbl.pdf' , 'http://europepmc.o
                    # rg/abstract/MED/20952552' , 'http://www.accessdata.fda.gov/drugsatfda_docs/label/2013/060359s028lb
                    # l.pdf' , 'http://www.accessdata.fda.gov/drugsatfda_docs/label/2014/018972s048lbl.pdf' , 'http://eu
                    # ropepmc.org/abstract/MED/23160821' , 'http://europepmc.org/abstract/MED/23160821' , 'http://www.ac
                    # cessdata.fda.gov/drugsatfda_docs/label/2007/016059s097,017814s040,018332s030lbl.pdf' , 'http://eur
                    # opepmc.org/abstract/MED/1505618' , 'http://www.accessdata.fda.gov/drugsatfda_docs/label/2007/01844
                    # 5s058lbl.pdf' , 'http://doi.org/10.3109/00498257809060395'
                }
            },
            'metabolite_chembl_id': 'TEXT',
            # EXAMPLES:
            # 'CHEMBL3638309' , 'CHEMBL3526762' , 'CHEMBL3544730' , 'CHEMBL1600' , 'CHEMBL4525790' , 'CHEMBL527285' , 'C
            # HEMBL3544533' , 'CHEMBL2158192' , 'CHEMBL3638308' , 'CHEMBL3544741'
            'metabolite_name': 'TEXT',
            # EXAMPLES:
            # 'ESTER GLUCURONIDE COJUGATE METABOLITE' , 'Rac-M1' , 'METHYLATED METABOLITES' , 'DESETHYLAMIODARONE' , '13
            # '-hydroxy-alpha-tocopherol' , 'alpha-carboxyethylhydroxychroman' , 'O-DESMETHYL-N-DESCHLOROBENZOYL INDOMET
            # HACIN' , '2-MERCAPTOPROPIONIC ACID' , 'ETHER GLUCURONIDE CONJUGATE METABOLITE' , '1-(HYDROXYCYCLOHEXYL)-1-
            # PHENYL-3-PIPERIDINOPROPAN-1-OL ISOMERS'
            'organism': 'TEXT',
            # EXAMPLES:
            # 'Mus musculus' , 'Mus musculus' , 'Homo sapiens' , 'Homo sapiens' , 'Homo sapiens' , 'Homo sapiens' , 'Rat
            # tus norvegicus' , 'Rattus norvegicus' , 'Rattus norvegicus' , 'Homo sapiens'
            'pathway_id': 'NUMERIC',
            # EXAMPLES:
            # '1' , '1' , '1' , '1' , '1' , '1' , '1' , '1' , '1' , '1'
            'pathway_key': 'TEXT',
            # EXAMPLES:
            # 'fig 1' , 'Scheme 1' , 'Scheme 1' , 'Fig S1' , 'Scheme 2' , 'Scheme 2' , 'fig 9' , 'fig 4' , 'Fig 5' , 'fi
            # g 9'
            'substrate_chembl_id': 'TEXT',
            # EXAMPLES:
            # 'CHEMBL898' , 'CHEMBL1258517' , 'CHEMBL532' , 'CHEMBL633' , 'CHEMBL49563' , 'CHEMBL4525790' , 'CHEMBL800' 
            # , 'CHEMBL1314' , 'CHEMBL898' , 'CHEMBL1490'
            'substrate_name': 'TEXT',
            # EXAMPLES:
            # 'DIFLUNISAL' , '1' , 'ERYTHROMYCIN' , 'AMIODARONE' , 'alpha-tocopherol' , '13'-hydroxy-alpha-tocopherol' ,
            #  'O-DESMETHYL INDOMETHACIN' , 'TIOPRONIN' , 'DIFLUNISAL' , 'TRIHEXYPHENIDYL'
            'target_chembl_id': 'TEXT',
            # EXAMPLES:
            # 'CHEMBL4370' , 'CHEMBL340' , 'CHEMBL3721' , 'CHEMBL612545' , 'CHEMBL612545' , 'CHEMBL4370' , 'CHEMBL612545
            # ' , 'CHEMBL3397' , 'CHEMBL3397' , 'CHEMBL612545'
            'tax_id': 'NUMERIC',
            # EXAMPLES:
            # '10090' , '10090' , '9606' , '9606' , '9606' , '9606' , '10116' , '10116' , '10116' , '9606'
        }
    }
