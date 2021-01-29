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
            'action_type': 'TEXT',
            # EXAMPLES:
            # 'CHELATING AGENT' , 'INHIBITOR' , 'CHELATING AGENT' , 'INHIBITOR' , 'INHIBITOR' , 'OPENER' , 'HYDROLYTIC E
            # NZYME' , 'HYDROLYTIC ENZYME' , 'HYDROLYTIC ENZYME' , 'HYDROLYTIC ENZYME'
            'binding_site_comment': 'TEXT',
            # EXAMPLES:
            # 'Binds to a cysteine residue in the BTK active site' , 'Alpha subunit is likely binding site' , '23S RRNA'
            #  , 'Beta-5 subunit' , 'Binds to LBD (ligand binding domain) of GRIA2.' , 'ATP-binding site' , 'Binds to if
            # enprodil site on N-terminal domain.' , 'Binds to ifenprodil site on N-terminal domain.' , 'Partial agonist
            #  of the glycin-site on GRIN1-subunits.' , 'Binds to ifenprodil site on N-terminal domain.'
            'direct_interaction': 'BOOLEAN',
            # EXAMPLES:
            # 'True' , 'True' , 'True' , 'True' , 'True' , 'True' , 'True' , 'True' , 'True' , 'True'
            'disease_efficacy': 'BOOLEAN',
            # EXAMPLES:
            # 'True' , 'True' , 'True' , 'True' , 'True' , 'True' , 'True' , 'True' , 'True' , 'True'
            'max_phase': 'NUMERIC',
            # EXAMPLES:
            # '4' , '4' , '4' , '4' , '4' , '4' , '4' , '4' , '4' , '4'
            'mec_id': 'NUMERIC',
            # EXAMPLES:
            # '2201' , '2202' , '2203' , '2204' , '2205' , '2206' , '2207' , '2209' , '2210' , '2211'
            'mechanism_comment': 'TEXT',
            # EXAMPLES:
            # 'Scavenge of radioactive and non-radioactive cesium and thalium' , 'Inhibition of protein synthesis indepe
            # ndent of direct BCR-ABL binding' , 'Mode of action not fully understood; it seems to interact with GABA A 
            # receptors as other carbinol hypnotic drugs' , 'Iodine seems to lead to protein precipitation' , 'Photodyna
            # mic therapy' , 'Mode of action not fully understood; it seems to interact with IKKB, which may play a role
            #  in its anti-rheumatic effects' , 'Antitussive drug; probable action in the CNS cough centre' , 'Trivalent
            #  metal cations chelating agent; inhibition of the metal-dependent enzymes that are responsible for the deg
            # radation of peroxides within the fungal cell' , 'Nitogen mustard component is DNA alkylating agent' , 'FAA
            # H converts acetaminophen into the active metabolite AM404, but this conversion also competes with degradat
            # ion of anandamide increasing its concentration and effects'
            'mechanism_of_action': 'TEXT',
            # EXAMPLES:
            # 'Unknown' , 'Unknown' , 'Radioactive metals chelating agent' , 'Unknown' , 'Unknown' , 'Unknown' , 'Unknow
            # n' , 'Unknown' , 'Unknown' , 'Unknown'
            'mechanism_refs': 
            {
                'properties': 
                {
                    'ref_id': 'TEXT',
                    # EXAMPLES:
                    # 'nda/2002/20-855_Mesnex_Prntlbl.pdf' , 'label/2008/021626s007lbl.pdf' , 'label/2000/21214lbl.pdf' 
                    # , 'label/2012/022372s004lbledt.pdf' , 'anda/2000/75-271_Cromolyn%20Sodium_prntlbl.pdf' , '428168' 
                    # , 'setid=7b74f590-e698-02da-9878-5dc80902dbb4' , '2009/07/new-drug-approvals-part-x-benzyl.html' ,
                    #  '10515429' , 'label/2006/013217s046lbl.pdf'
                    'ref_type': 'TEXT',
                    # EXAMPLES:
                    # 'FDA' , 'FDA' , 'FDA' , 'FDA' , 'FDA' , 'PubMed' , 'DailyMed' , 'Expert' , 'PubMed' , 'FDA'
                    'ref_url': 'TEXT',
                    # EXAMPLES:
                    # 'http://www.accessdata.fda.gov/drugsatfda_docs/nda/2002/20-855_Mesnex_Prntlbl.pdf' , 'http://www.a
                    # ccessdata.fda.gov/drugsatfda_docs/label/2008/021626s007lbl.pdf' , 'http://www.accessdata.fda.gov/d
                    # rugsatfda_docs/label/2000/21214lbl.pdf' , 'http://www.accessdata.fda.gov/drugsatfda_docs/label/201
                    # 2/022372s004lbledt.pdf' , 'http://www.accessdata.fda.gov/drugsatfda_docs/anda/2000/75-271_Cromolyn
                    # %20Sodium_prntlbl.pdf' , 'http://europepmc.org/abstract/MED/428168' , 'http://dailymed.nlm.nih.gov
                    # /dailymed/lookup.cfm?setid=7b74f590-e698-02da-9878-5dc80902dbb4' , 'http://chembl.blogspot.co.uk/2
                    # 009/07/new-drug-approvals-part-x-benzyl.html' , 'http://europepmc.org/abstract/MED/10515429' , 'ht
                    # tp://www.accessdata.fda.gov/drugsatfda_docs/label/2006/013217s046lbl.pdf'
                }
            },
            'molecular_mechanism': 'BOOLEAN',
            # EXAMPLES:
            # 'True' , 'True' , 'True' , 'True' , 'True' , 'True' , 'True' , 'True' , 'True' , 'True'
            'molecule_chembl_id': 'TEXT',
            # EXAMPLES:
            # 'CHEMBL975' , 'CHEMBL361497' , 'CHEMBL2096629' , 'CHEMBL1200661' , 'CHEMBL2021424' , 'CHEMBL74' , 'CHEMBL2
            # 107525' , 'CHEMBL1200625' , 'CHEMBL1239' , 'CHEMBL980'
            'parent_molecule_chembl_id': 'TEXT',
            # EXAMPLES:
            # 'CHEMBL1098319' , 'CHEMBL361497' , 'CHEMBL2096629' , 'CHEMBL1200661' , 'CHEMBL2021424' , 'CHEMBL428880' , 
            # 'CHEMBL1060' , 'CHEMBL2219640' , 'CHEMBL1239' , 'CHEMBL980'
            'record_id': 'NUMERIC',
            # EXAMPLES:
            # '1344110' , '1641027' , '1343347' , '1343190' , '1344046' , '1344901' , '1344128' , '1343168' , '1343700' 
            # , '1344867'
            'selectivity_comment': 'TEXT',
            # EXAMPLES:
            # 'Selective' , 'FGFR 1, 2 + 3' , 'HCN4 is predominant form in sinoatrial node and atrioventricular node' , 
            # 'High selectivity for CXCR2 over CXCR1' , 'Inhibits multiple receptor tyrosine kinases. Active against FLT
            # 3 and certain FLT3 variants.' , 'Binding affinity is high at GABAAa1, a2 and a3 (Ki of 0.5, 0.3 and 1.3 nM
            # , respectively), but not GA' , 'Binding affinity is high at GABAAa1, a2 and a3 (Ki of 0.5, 0.3 and 1.3 nM,
            #  respectively), but not GA' , 'GRIN2B selective.' , 'GRIN2B selective.' , 'Partial agonist of the glycin-s
            # ite on GRIN1-subunits, preferentially modulates NR2B-containing NMDAR'
            'site_id': 'NUMERIC',
            # EXAMPLES:
            # '248' , '2651' , '2621' , '1744' , '2150' , '2633' , '2617' , '2617' , '2617' , '2649'
            'target_chembl_id': 'TEXT',
            # EXAMPLES:
            # 'CHEMBL2366037' , 'CHEMBL2311221' , 'CHEMBL2366381' , 'CHEMBL2311221' , 'CHEMBL2243' , 'CHEMBL4794' , 'CHE
            # MBL2364706' , 'CHEMBL2364711' , 'CHEMBL2364180' , 'CHEMBL2364181'
            'variant_sequence': 
            {
                'properties': 
                {
                    'accession': 'TEXT',
                    # EXAMPLES:
                    # 'P00533' , 'P00533' , 'P00533' , 'P15056' , 'P15056' , 'P15056'
                    'isoform': 'NUMERIC',
                    # EXAMPLES:
                    # '1' , '1' , '1'
                    'mutation': 'TEXT',
                    # EXAMPLES:
                    # 'T790M' , 'T790M' , 'T790M' , 'V600E' , 'V600E' , 'V600E'
                    'organism': 'TEXT',
                    # EXAMPLES:
                    # 'Homo sapiens' , 'Homo sapiens' , 'Homo sapiens' , 'Homo sapiens' , 'Homo sapiens' , 'Homo sapiens
                    # '
                    'sequence': 'TEXT',
                    # EXAMPLES:
                    # 'MRPSGTAGAALLALLAALCPASRALEEKKVCQGTSNKLTQLGTFEDHFLSLQRMFNNCEVVLGNLEITYVQRNYDLSFLKTIQEVAGYVLIALNTVE
                    # RIPLENLQIIRGNMYYENSYALAVLSNYDANKTGLKELPMRNLQEILHGAVRFSNNPALCNVESIQWRDIVSSDFLSNMSMDFQNHLGSCQKCDPSCP
                    # NGSCWGAGEENCQKLTKIICAQQCSGRCRGKSPSDCCHNQCAAGCTGPRESDCLVCRKFRDEATCKDTCPPLMLYNPTTYQMDVNPEGKYSFGATCVK
                    # KCPRNYVVTDHGSCVRACGADSYEMEEDGVRKCKKCEGPCRKVCNGIGIGEFKDSLSINATNIKHFKNCTSISGDLHILPVAFRGDSFTHTPPLDPQE
                    # LDILKTVKEITGFLLIQAWPENRTDLHAFENLEIIRGRTKQHGQFSLAVVSLNITSLGLRSLKEISDGDVIISGNKNLCYANTINWKKLFGTSGQKTK
                    # IISNRGENSCKATGQVCHALCSPEGCWGPEPRDCVSCRNVSRGRECVDKCNLLEGEPREFVENSECIQCHPECLPQAMNITCTGRGPDNCIQCAHYID
                    # GPHCVKTCPAGVMGENNTLVWKYADAGHVCHLCHPNCTYGCTGPGLEGCPTNGPKIPSIATGMVGALLLLLVVALGIGLFMRRRHIVRKRTLRRLLQE
                    # RELVEPLTPSGEAPNQALLRILKETEFKKIKVLGSGAFGTVYKGLWIPEGEKVKIPVAIKELREATSPKANKEILDEAYVMASVDNPHVCRLLGICLT
                    # STVQLIMQLMPFGCLLDYVREHKDNIGSQYLLNWCVQIAKGMNYLEDRRLVHRDLAARNVLVKTPQHVKITDFGLAKLLGAEEKEYHAEGGKVPIKWM
                    # ALESILHRIYTHQSDVWSYGVTVWELMTFGSKPYDGIPASEISSILEKGERLPQPPICTIDVYMIMVKCWMIDADSRPKFRELIIEFSKMARDPQRYL
                    # VIQGDERMHLPSPTDSNFYRALMDEEDMDDVVDADEYLIPQQGFFSSPSTSRTPLLSSLSATSNNSTVACIDRNGLQSCPIKEDSFLQRYSSDPTGAL
                    # TEDSIDDTFLPVPEYINQSVPKRPAGSVQNPVYHNQPLNPAPSRDPHYQDPHSTAVGNPEYLNTVQPTCVNSTFDSPAHWAQKGSHQISLDNPDYQQD
                    # FFPKEAKPNGIFKGSTAENAEYLRVAPQSSEFIGA' , 'MRPSGTAGAALLALLAALCPASRALEEKKVCQGTSNKLTQLGTFEDHFLSLQRMFNNC
                    # EVVLGNLEITYVQRNYDLSFLKTIQEVAGYVLIALNTVERIPLENLQIIRGNMYYENSYALAVLSNYDANKTGLKELPMRNLQEILHGAVRFSNNPAL
                    # CNVESIQWRDIVSSDFLSNMSMDFQNHLGSCQKCDPSCPNGSCWGAGEENCQKLTKIICAQQCSGRCRGKSPSDCCHNQCAAGCTGPRESDCLVCRKF
                    # RDEATCKDTCPPLMLYNPTTYQMDVNPEGKYSFGATCVKKCPRNYVVTDHGSCVRACGADSYEMEEDGVRKCKKCEGPCRKVCNGIGIGEFKDSLSIN
                    # ATNIKHFKNCTSISGDLHILPVAFRGDSFTHTPPLDPQELDILKTVKEITGFLLIQAWPENRTDLHAFENLEIIRGRTKQHGQFSLAVVSLNITSLGL
                    # RSLKEISDGDVIISGNKNLCYANTINWKKLFGTSGQKTKIISNRGENSCKATGQVCHALCSPEGCWGPEPRDCVSCRNVSRGRECVDKCNLLEGEPRE
                    # FVENSECIQCHPECLPQAMNITCTGRGPDNCIQCAHYIDGPHCVKTCPAGVMGENNTLVWKYADAGHVCHLCHPNCTYGCTGPGLEGCPTNGPKIPSI
                    # ATGMVGALLLLLVVALGIGLFMRRRHIVRKRTLRRLLQERELVEPLTPSGEAPNQALLRILKETEFKKIKVLGSGAFGTVYKGLWIPEGEKVKIPVAI
                    # KELREATSPKANKEILDEAYVMASVDNPHVCRLLGICLTSTVQLIMQLMPFGCLLDYVREHKDNIGSQYLLNWCVQIAKGMNYLEDRRLVHRDLAARN
                    # VLVKTPQHVKITDFGLAKLLGAEEKEYHAEGGKVPIKWMALESILHRIYTHQSDVWSYGVTVWELMTFGSKPYDGIPASEISSILEKGERLPQPPICT
                    # IDVYMIMVKCWMIDADSRPKFRELIIEFSKMARDPQRYLVIQGDERMHLPSPTDSNFYRALMDEEDMDDVVDADEYLIPQQGFFSSPSTSRTPLLSSL
                    # SATSNNSTVACIDRNGLQSCPIKEDSFLQRYSSDPTGALTEDSIDDTFLPVPEYINQSVPKRPAGSVQNPVYHNQPLNPAPSRDPHYQDPHSTAVGNP
                    # EYLNTVQPTCVNSTFDSPAHWAQKGSHQISLDNPDYQQDFFPKEAKPNGIFKGSTAENAEYLRVAPQSSEFIGA' , 'MRPSGTAGAALLALLAALC
                    # PASRALEEKKVCQGTSNKLTQLGTFEDHFLSLQRMFNNCEVVLGNLEITYVQRNYDLSFLKTIQEVAGYVLIALNTVERIPLENLQIIRGNMYYENSY
                    # ALAVLSNYDANKTGLKELPMRNLQEILHGAVRFSNNPALCNVESIQWRDIVSSDFLSNMSMDFQNHLGSCQKCDPSCPNGSCWGAGEENCQKLTKIIC
                    # AQQCSGRCRGKSPSDCCHNQCAAGCTGPRESDCLVCRKFRDEATCKDTCPPLMLYNPTTYQMDVNPEGKYSFGATCVKKCPRNYVVTDHGSCVRACGA
                    # DSYEMEEDGVRKCKKCEGPCRKVCNGIGIGEFKDSLSINATNIKHFKNCTSISGDLHILPVAFRGDSFTHTPPLDPQELDILKTVKEITGFLLIQAWP
                    # ENRTDLHAFENLEIIRGRTKQHGQFSLAVVSLNITSLGLRSLKEISDGDVIISGNKNLCYANTINWKKLFGTSGQKTKIISNRGENSCKATGQVCHAL
                    # CSPEGCWGPEPRDCVSCRNVSRGRECVDKCNLLEGEPREFVENSECIQCHPECLPQAMNITCTGRGPDNCIQCAHYIDGPHCVKTCPAGVMGENNTLV
                    # WKYADAGHVCHLCHPNCTYGCTGPGLEGCPTNGPKIPSIATGMVGALLLLLVVALGIGLFMRRRHIVRKRTLRRLLQERELVEPLTPSGEAPNQALLR
                    # ILKETEFKKIKVLGSGAFGTVYKGLWIPEGEKVKIPVAIKELREATSPKANKEILDEAYVMASVDNPHVCRLLGICLTSTVQLIMQLMPFGCLLDYVR
                    # EHKDNIGSQYLLNWCVQIAKGMNYLEDRRLVHRDLAARNVLVKTPQHVKITDFGLAKLLGAEEKEYHAEGGKVPIKWMALESILHRIYTHQSDVWSYG
                    # VTVWELMTFGSKPYDGIPASEISSILEKGERLPQPPICTIDVYMIMVKCWMIDADSRPKFRELIIEFSKMARDPQRYLVIQGDERMHLPSPTDSNFYR
                    # ALMDEEDMDDVVDADEYLIPQQGFFSSPSTSRTPLLSSLSATSNNSTVACIDRNGLQSCPIKEDSFLQRYSSDPTGALTEDSIDDTFLPVPEYINQSV
                    # PKRPAGSVQNPVYHNQPLNPAPSRDPHYQDPHSTAVGNPEYLNTVQPTCVNSTFDSPAHWAQKGSHQISLDNPDYQQDFFPKEAKPNGIFKGSTAENA
                    # EYLRVAPQSSEFIGA' , 'MAALSGGGGGGAEPGQALFNGDMEPEAGAGAGAAASSAADPAIPEEVWNIKQMIKLTQEHIEALLDKFGGEHNPPSIY
                    # LEAYEEYTSKLDALQQREQQLLESLGNGTDFSVSSSASMDTVTSSSSSSLSVLPSSLSVFQNPTDVARSNPKSPQKPIVRVFLPNKQRTVVPARCGVT
                    # VRDSLKKALMMRGLIPECCAVYRIQDGEKKPIGWDTDISWLTGEELHVEVLENVPLTTHNFVRKTFFTLAFCDFCRKLLFQGFRCQTCGYKFHQRCST
                    # EVPLMCVNYDQLDLLFVSKFFEHHPIPQEEASLAETALTSGSSPSAPASDSIGPQILTSPSPSKSIPIPQPFRPADEDHRNQFGQRDRSSSAPNVHIN
                    # TIEPVNIDDLIRDQGFRGDGGSTTGLSATPPASLPGSLTNVKALQKSPGPQRERKSSSSSEDRNRMKTLGRRDSSDDWEIPDGQITVGQRIGSGSFGT
                    # VYKGKWHGDVAVKMLNVTAPTPQQLQAFKNEVGVLRKTRHVNILLFMGYSTKPQLAIVTQWCEGSSLYHHLHIIETKFEMIKLIDIARQTAQGMDYLH
                    # AKSIIHRDLKSNNIFLHEDLTVKIGDFGLATEKSRWSGSHQFEQLSGSILWMAPEVIRMQDKNPYSFQSDVYAFGIVLYELMTGQLPYSNINNRDQII
                    # FMVGRGYLSPDLSKVRSNCPKAMKRLMAECLKKKRDERPLFPQILASIELLARSLPKIHRSASEPSLNRAGFQTEDFSLYACASPKTPIQAGGYGAFP
                    # VH' , 'MAALSGGGGGGAEPGQALFNGDMEPEAGAGAGAAASSAADPAIPEEVWNIKQMIKLTQEHIEALLDKFGGEHNPPSIYLEAYEEYTSKLDA
                    # LQQREQQLLESLGNGTDFSVSSSASMDTVTSSSSSSLSVLPSSLSVFQNPTDVARSNPKSPQKPIVRVFLPNKQRTVVPARCGVTVRDSLKKALMMRG
                    # LIPECCAVYRIQDGEKKPIGWDTDISWLTGEELHVEVLENVPLTTHNFVRKTFFTLAFCDFCRKLLFQGFRCQTCGYKFHQRCSTEVPLMCVNYDQLD
                    # LLFVSKFFEHHPIPQEEASLAETALTSGSSPSAPASDSIGPQILTSPSPSKSIPIPQPFRPADEDHRNQFGQRDRSSSAPNVHINTIEPVNIDDLIRD
                    # QGFRGDGGSTTGLSATPPASLPGSLTNVKALQKSPGPQRERKSSSSSEDRNRMKTLGRRDSSDDWEIPDGQITVGQRIGSGSFGTVYKGKWHGDVAVK
                    # MLNVTAPTPQQLQAFKNEVGVLRKTRHVNILLFMGYSTKPQLAIVTQWCEGSSLYHHLHIIETKFEMIKLIDIARQTAQGMDYLHAKSIIHRDLKSNN
                    # IFLHEDLTVKIGDFGLATEKSRWSGSHQFEQLSGSILWMAPEVIRMQDKNPYSFQSDVYAFGIVLYELMTGQLPYSNINNRDQIIFMVGRGYLSPDLS
                    # KVRSNCPKAMKRLMAECLKKKRDERPLFPQILASIELLARSLPKIHRSASEPSLNRAGFQTEDFSLYACASPKTPIQAGGYGAFPVH' , 'MAALSG
                    # GGGGGAEPGQALFNGDMEPEAGAGAGAAASSAADPAIPEEVWNIKQMIKLTQEHIEALLDKFGGEHNPPSIYLEAYEEYTSKLDALQQREQQLLESLG
                    # NGTDFSVSSSASMDTVTSSSSSSLSVLPSSLSVFQNPTDVARSNPKSPQKPIVRVFLPNKQRTVVPARCGVTVRDSLKKALMMRGLIPECCAVYRIQD
                    # GEKKPIGWDTDISWLTGEELHVEVLENVPLTTHNFVRKTFFTLAFCDFCRKLLFQGFRCQTCGYKFHQRCSTEVPLMCVNYDQLDLLFVSKFFEHHPI
                    # PQEEASLAETALTSGSSPSAPASDSIGPQILTSPSPSKSIPIPQPFRPADEDHRNQFGQRDRSSSAPNVHINTIEPVNIDDLIRDQGFRGDGGSTTGL
                    # SATPPASLPGSLTNVKALQKSPGPQRERKSSSSSEDRNRMKTLGRRDSSDDWEIPDGQITVGQRIGSGSFGTVYKGKWHGDVAVKMLNVTAPTPQQLQ
                    # AFKNEVGVLRKTRHVNILLFMGYSTKPQLAIVTQWCEGSSLYHHLHIIETKFEMIKLIDIARQTAQGMDYLHAKSIIHRDLKSNNIFLHEDLTVKIGD
                    # FGLATEKSRWSGSHQFEQLSGSILWMAPEVIRMQDKNPYSFQSDVYAFGIVLYELMTGQLPYSNINNRDQIIFMVGRGYLSPDLSKVRSNCPKAMKRL
                    # MAECLKKKRDERPLFPQILASIELLARSLPKIHRSASEPSLNRAGFQTEDFSLYACASPKTPIQAGGYGAFPVH'
                    'tax_id': 'NUMERIC',
                    # EXAMPLES:
                    # '9606' , '9606' , '9606' , '9606' , '9606' , '9606'
                    'version': 'NUMERIC',
                    # EXAMPLES:
                    # '2' , '2' , '2' , '4' , '4' , '4'
                }
            }
        }
    }
