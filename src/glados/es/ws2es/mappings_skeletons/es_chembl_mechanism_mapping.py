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
                    'all_molecule_chembl_ids': 'TEXT',
                    # EXAMPLES:
                    # 'CHEMBL229430' , 'CHEMBL398338' , 'CHEMBL3545148' , 'CHEMBL504652' , 'CHEMBL1783256' , 'CHEMBL1783
                    # 256' , 'CHEMBL3545206' , 'CHEMBL3678076' , 'CHEMBL3545208' , 'CHEMBL3545091'
                    'parent_molecule_chembl_id': 'TEXT',
                    # EXAMPLES:
                    # 'CHEMBL229430' , 'CHEMBL398338' , 'CHEMBL3545148' , 'CHEMBL504652' , 'CHEMBL1783256' , 'CHEMBL1783
                    # 256' , 'CHEMBL3545206' , 'CHEMBL3678076' , 'CHEMBL3545208' , 'CHEMBL3545091'
                    'should_appear_in_browser': 'BOOLEAN',
                    # EXAMPLES:
                    # 'True' , 'True' , 'True' , 'True' , 'True' , 'True' , 'True' , 'True' , 'True' , 'True'
                }
            },
            'action_type': 'TEXT',
            # EXAMPLES:
            # 'ANTAGONIST' , 'ANTAGONIST' , 'ANTAGONIST' , 'ANTAGONIST' , 'POSITIVE ALLOSTERIC MODULATOR' , 'POSITIVE AL
            # LOSTERIC MODULATOR' , 'NEGATIVE ALLOSTERIC MODULATOR' , 'BLOCKER' , 'BLOCKER' , 'BLOCKER'
            'binding_site_comment': 'TEXT',
            # EXAMPLES:
            # '30S subunit' , 'Beta subunit RpoB' , 'Interacts with the so-called vinca-alkaloid-binding-domain of tubul
            # in' , 'Binding site 23S and 16S RNA (interface)' , 'Benzodiazepine site' , 'It binds to a different site o
            # n the COX-2 enzyme than other COX-2 inhibitors.' , 'Alpha subunit is likely binding site' , 'Benzodiazepin
            # e site' , 'Binds to the ATP-binding domain at the N-terminus of Hsp90' , 'Binds with high affinity to the 
            # restricted A3B3 domain (Gold group 3) found on CEACAM5. '
            'direct_interaction': 'BOOLEAN',
            # EXAMPLES:
            # 'True' , 'True' , 'True' , 'True' , 'True' , 'True' , 'True' , 'True' , 'True' , 'True'
            'disease_efficacy': 'BOOLEAN',
            # EXAMPLES:
            # 'True' , 'True' , 'True' , 'True' , 'True' , 'True' , 'True' , 'True' , 'True' , 'True'
            'max_phase': 'NUMERIC',
            # EXAMPLES:
            # '1' , '1' , '1' , '1' , '1' , '1' , '1' , '2' , '1' , '1'
            'mec_id': 'NUMERIC',
            # EXAMPLES:
            # '4500' , '4501' , '4502' , '4503' , '4504' , '4505' , '4506' , '4507' , '4508' , '4509'
            'mechanism_comment': 'TEXT',
            # EXAMPLES:
            # 'Discontinued, causes increased core body temperature.' , 'Racemic compound.' , 'Backup to XEN402.' , 'Sho
            # ws no specificity among human SCN channel family members (SCN1A-11A).' , 'Type I positive allosteric modul
            # ator.' , 'Indication: Allergic diseases' , 'Indication: Allergic diseases' , 'Antimicrobial activity' , 'P
            # h1b trial planned, not yet recruiting (NCT02537028)' , 'Divalent and Trivalent metal chelating agent. Remo
            # ves Ca2+ in case of hypercalciemia'
            'mechanism_of_action': 'TEXT',
            # EXAMPLES:
            # 'Vanilloid receptor antagonist' , 'Vanilloid receptor antagonist' , 'Vanilloid receptor antagonist' , 'Neu
            # ronal acetylcholine receptor; alpha4/beta2 antagonist' , 'GABA receptor alpha-2 subunit positive allosteri
            # c modulator' , 'GABA receptor alpha-3 subunit positive allosteric modulator' , 'P2X purinoceptor 7 negativ
            # e allosteric modulator' , 'Sodium channel alpha subunit blocker' , 'Sodium channel protein type IX alpha s
            # ubunit blocker' , 'Sodium channel protein type IX alpha subunit blocker'
            'mechanism_refs': 
            {
                'properties': 
                {
                    'ref_id': 'TEXT',
                    # EXAMPLES:
                    # '18337008' , '18515644' , 'http://www.pharmeste.com/repository/contenuti/paragrafi/file/PharmEste_
                    # Leaflet_2012.pdf' , '1459956' , '25493397' , '25493397' , '22568863' , 'http://www.newron.com/ENG/
                    # Default.aspx?SEZ=3&PAG=44' , '25060923' , '25060923'
                    'ref_type': 'TEXT',
                    # EXAMPLES:
                    # 'PubMed' , 'PubMed' , 'Other' , 'PubMed' , 'PubMed' , 'PubMed' , 'PubMed' , 'Other' , 'PubMed' , '
                    # PubMed'
                    'ref_url': 'TEXT',
                    # EXAMPLES:
                    # 'http://europepmc.org/abstract/MED/18337008' , 'http://europepmc.org/abstract/MED/18515644' , 'htt
                    # p://www.pharmeste.com/repository/contenuti/paragrafi/file/PharmEste_Leaflet_2012.pdf' , 'http://eu
                    # ropepmc.org/abstract/MED/1459956' , 'http://europepmc.org/abstract/MED/25493397' , 'http://europep
                    # mc.org/abstract/MED/25493397' , 'http://europepmc.org/abstract/MED/22568863' , 'http://www.newron.
                    # com/ENG/Default.aspx?SEZ=3&PAG=44' , 'http://europepmc.org/abstract/MED/25060923' , 'http://europe
                    # pmc.org/abstract/MED/25060923'
                }
            },
            'molecular_mechanism': 'BOOLEAN',
            # EXAMPLES:
            # 'True' , 'True' , 'True' , 'True' , 'True' , 'True' , 'True' , 'True' , 'True' , 'True'
            'molecule_chembl_id': 'TEXT',
            # EXAMPLES:
            # 'CHEMBL229430' , 'CHEMBL398338' , 'CHEMBL3545148' , 'CHEMBL504652' , 'CHEMBL1783256' , 'CHEMBL1783256' , '
            # CHEMBL3545206' , 'CHEMBL3678076' , 'CHEMBL3545208' , 'CHEMBL3545091'
            'parent_molecule_chembl_id': 'TEXT',
            # EXAMPLES:
            # 'CHEMBL229430' , 'CHEMBL398338' , 'CHEMBL3545148' , 'CHEMBL504652' , 'CHEMBL1783256' , 'CHEMBL1783256' , '
            # CHEMBL3545206' , 'CHEMBL3678076' , 'CHEMBL3545208' , 'CHEMBL3545091'
            'record_id': 'NUMERIC',
            # EXAMPLES:
            # '2472865' , '2473139' , '2473140' , '2473700' , '2473580' , '2473580' , '2473280' , '2473281' , '2473282' 
            # , '2473008'
            'selectivity_comment': 'TEXT',
            # EXAMPLES:
            # 'Weak inhibitotor of COX-1 and COX-2' , 'Indicated for infections caused by Escherichia coli, Klebsiella p
            # neumoniae, Citrobacter freundii, Enterobacter cloacae, Klebsiella oxytoca, Enterococcus faecalis, Enteroco
            # ccus faecium, Staphylococcus aureus, Streptococcus anginosus group, Clostridium perfringens, Bacteroides s
            # pecies and Parabacteroides distasonis. Active in vitro against additional organisms but clinical signfican
            # ce unknown. ' , 'Active against enterotoxigenic and enteroaggregative E coli involved in traveller's diarr
            # hea.' , 'Isotype-selective Class I (HDAC1, -2, -3, and -8) and IV (HDAC11) HDAC inhibitor.' , 'May cause a
            # lternative splicing of additional non-target genes inc. FOXM1 and MADD which may contribute to adverse eff
            # ects.' , 'Selective for D2 over D1 and D3 receptors.' , 'Active against laboratory strains and clinical is
            # olates of HIV-1 and laboratory strains of HIV-2. Active against a broad panel of HIV-1 group M (A, B, C, D
            # , E, F, G), and group O primary isolates.' , 'IC50s for FGFR1/2/3 < 2 nM. The IC50 for FGFR4 is 100x highe
            # r in vitro. Indicated for cancers with FGFR2 fusions or other rearrangements as detected by an FDA-approve
            # d test.' , 'Active against Staphylococcus aureus (including MRSA), Streptococcus pneumoniae, Escherichia c
            # oli, and Klebsiella pneumoniae and Haemophilus influenzae. Binds bacterial PBPs. In gram-positive bacteria
            # , binds PBP2a incl. divergent mecA homologues (mecC or mecALGA251), PBP2a and PBP2x from penicillin-interm
            # ediate Streptococcus pneumoniae and binds to PBP5 in Enterococcus faecalis.' , 'Specifically directed agai
            # nst the alphav subunit of human integrins.'
            'site_id': 'NUMERIC',
            # EXAMPLES:
            # '2620' , '9799' , '9803' , '2623' , '2617' , '2651' , '2617' , '9801' , '2627' , '2629'
            'target_chembl_id': 'TEXT',
            # EXAMPLES:
            # 'CHEMBL4794' , 'CHEMBL4794' , 'CHEMBL4794' , 'CHEMBL1907589' , 'CHEMBL4956' , 'CHEMBL3026' , 'CHEMBL4805' 
            # , 'CHEMBL2331043' , 'CHEMBL4296' , 'CHEMBL4296'
            'variant_sequence': 
            {
                'properties': 
                {
                    'accession': 'TEXT',
                    # EXAMPLES:
                    # 'P00533' , 'P15056' , 'P15056' , 'P00533' , 'P00533' , 'P15056'
                    'isoform': 'NUMERIC',
                    # EXAMPLES:
                    # '1' , '1' , '1'
                    'mutation': 'TEXT',
                    # EXAMPLES:
                    # 'T790M' , 'V600E' , 'V600E' , 'T790M' , 'T790M' , 'V600E'
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
                    # FFPKEAKPNGIFKGSTAENAEYLRVAPQSSEFIGA' , 'MAALSGGGGGGAEPGQALFNGDMEPEAGAGAGAAASSAADPAIPEEVWNIKQMIKLTQ
                    # EHIEALLDKFGGEHNPPSIYLEAYEEYTSKLDALQQREQQLLESLGNGTDFSVSSSASMDTVTSSSSSSLSVLPSSLSVFQNPTDVARSNPKSPQKPI
                    # VRVFLPNKQRTVVPARCGVTVRDSLKKALMMRGLIPECCAVYRIQDGEKKPIGWDTDISWLTGEELHVEVLENVPLTTHNFVRKTFFTLAFCDFCRKL
                    # LFQGFRCQTCGYKFHQRCSTEVPLMCVNYDQLDLLFVSKFFEHHPIPQEEASLAETALTSGSSPSAPASDSIGPQILTSPSPSKSIPIPQPFRPADED
                    # HRNQFGQRDRSSSAPNVHINTIEPVNIDDLIRDQGFRGDGGSTTGLSATPPASLPGSLTNVKALQKSPGPQRERKSSSSSEDRNRMKTLGRRDSSDDW
                    # EIPDGQITVGQRIGSGSFGTVYKGKWHGDVAVKMLNVTAPTPQQLQAFKNEVGVLRKTRHVNILLFMGYSTKPQLAIVTQWCEGSSLYHHLHIIETKF
                    # EMIKLIDIARQTAQGMDYLHAKSIIHRDLKSNNIFLHEDLTVKIGDFGLATEKSRWSGSHQFEQLSGSILWMAPEVIRMQDKNPYSFQSDVYAFGIVL
                    # YELMTGQLPYSNINNRDQIIFMVGRGYLSPDLSKVRSNCPKAMKRLMAECLKKKRDERPLFPQILASIELLARSLPKIHRSASEPSLNRAGFQTEDFS
                    # LYACASPKTPIQAGGYGAFPVH' , 'MAALSGGGGGGAEPGQALFNGDMEPEAGAGAGAAASSAADPAIPEEVWNIKQMIKLTQEHIEALLDKFGGE
                    # HNPPSIYLEAYEEYTSKLDALQQREQQLLESLGNGTDFSVSSSASMDTVTSSSSSSLSVLPSSLSVFQNPTDVARSNPKSPQKPIVRVFLPNKQRTVV
                    # PARCGVTVRDSLKKALMMRGLIPECCAVYRIQDGEKKPIGWDTDISWLTGEELHVEVLENVPLTTHNFVRKTFFTLAFCDFCRKLLFQGFRCQTCGYK
                    # FHQRCSTEVPLMCVNYDQLDLLFVSKFFEHHPIPQEEASLAETALTSGSSPSAPASDSIGPQILTSPSPSKSIPIPQPFRPADEDHRNQFGQRDRSSS
                    # APNVHINTIEPVNIDDLIRDQGFRGDGGSTTGLSATPPASLPGSLTNVKALQKSPGPQRERKSSSSSEDRNRMKTLGRRDSSDDWEIPDGQITVGQRI
                    # GSGSFGTVYKGKWHGDVAVKMLNVTAPTPQQLQAFKNEVGVLRKTRHVNILLFMGYSTKPQLAIVTQWCEGSSLYHHLHIIETKFEMIKLIDIARQTA
                    # QGMDYLHAKSIIHRDLKSNNIFLHEDLTVKIGDFGLATEKSRWSGSHQFEQLSGSILWMAPEVIRMQDKNPYSFQSDVYAFGIVLYELMTGQLPYSNI
                    # NNRDQIIFMVGRGYLSPDLSKVRSNCPKAMKRLMAECLKKKRDERPLFPQILASIELLARSLPKIHRSASEPSLNRAGFQTEDFSLYACASPKTPIQA
                    # GGYGAFPVH' , 'MRPSGTAGAALLALLAALCPASRALEEKKVCQGTSNKLTQLGTFEDHFLSLQRMFNNCEVVLGNLEITYVQRNYDLSFLKTIQE
                    # VAGYVLIALNTVERIPLENLQIIRGNMYYENSYALAVLSNYDANKTGLKELPMRNLQEILHGAVRFSNNPALCNVESIQWRDIVSSDFLSNMSMDFQN
                    # HLGSCQKCDPSCPNGSCWGAGEENCQKLTKIICAQQCSGRCRGKSPSDCCHNQCAAGCTGPRESDCLVCRKFRDEATCKDTCPPLMLYNPTTYQMDVN
                    # PEGKYSFGATCVKKCPRNYVVTDHGSCVRACGADSYEMEEDGVRKCKKCEGPCRKVCNGIGIGEFKDSLSINATNIKHFKNCTSISGDLHILPVAFRG
                    # DSFTHTPPLDPQELDILKTVKEITGFLLIQAWPENRTDLHAFENLEIIRGRTKQHGQFSLAVVSLNITSLGLRSLKEISDGDVIISGNKNLCYANTIN
                    # WKKLFGTSGQKTKIISNRGENSCKATGQVCHALCSPEGCWGPEPRDCVSCRNVSRGRECVDKCNLLEGEPREFVENSECIQCHPECLPQAMNITCTGR
                    # GPDNCIQCAHYIDGPHCVKTCPAGVMGENNTLVWKYADAGHVCHLCHPNCTYGCTGPGLEGCPTNGPKIPSIATGMVGALLLLLVVALGIGLFMRRRH
                    # IVRKRTLRRLLQERELVEPLTPSGEAPNQALLRILKETEFKKIKVLGSGAFGTVYKGLWIPEGEKVKIPVAIKELREATSPKANKEILDEAYVMASVD
                    # NPHVCRLLGICLTSTVQLIMQLMPFGCLLDYVREHKDNIGSQYLLNWCVQIAKGMNYLEDRRLVHRDLAARNVLVKTPQHVKITDFGLAKLLGAEEKE
                    # YHAEGGKVPIKWMALESILHRIYTHQSDVWSYGVTVWELMTFGSKPYDGIPASEISSILEKGERLPQPPICTIDVYMIMVKCWMIDADSRPKFRELII
                    # EFSKMARDPQRYLVIQGDERMHLPSPTDSNFYRALMDEEDMDDVVDADEYLIPQQGFFSSPSTSRTPLLSSLSATSNNSTVACIDRNGLQSCPIKEDS
                    # FLQRYSSDPTGALTEDSIDDTFLPVPEYINQSVPKRPAGSVQNPVYHNQPLNPAPSRDPHYQDPHSTAVGNPEYLNTVQPTCVNSTFDSPAHWAQKGS
                    # HQISLDNPDYQQDFFPKEAKPNGIFKGSTAENAEYLRVAPQSSEFIGA' , 'MRPSGTAGAALLALLAALCPASRALEEKKVCQGTSNKLTQLGTFE
                    # DHFLSLQRMFNNCEVVLGNLEITYVQRNYDLSFLKTIQEVAGYVLIALNTVERIPLENLQIIRGNMYYENSYALAVLSNYDANKTGLKELPMRNLQEI
                    # LHGAVRFSNNPALCNVESIQWRDIVSSDFLSNMSMDFQNHLGSCQKCDPSCPNGSCWGAGEENCQKLTKIICAQQCSGRCRGKSPSDCCHNQCAAGCT
                    # GPRESDCLVCRKFRDEATCKDTCPPLMLYNPTTYQMDVNPEGKYSFGATCVKKCPRNYVVTDHGSCVRACGADSYEMEEDGVRKCKKCEGPCRKVCNG
                    # IGIGEFKDSLSINATNIKHFKNCTSISGDLHILPVAFRGDSFTHTPPLDPQELDILKTVKEITGFLLIQAWPENRTDLHAFENLEIIRGRTKQHGQFS
                    # LAVVSLNITSLGLRSLKEISDGDVIISGNKNLCYANTINWKKLFGTSGQKTKIISNRGENSCKATGQVCHALCSPEGCWGPEPRDCVSCRNVSRGREC
                    # VDKCNLLEGEPREFVENSECIQCHPECLPQAMNITCTGRGPDNCIQCAHYIDGPHCVKTCPAGVMGENNTLVWKYADAGHVCHLCHPNCTYGCTGPGL
                    # EGCPTNGPKIPSIATGMVGALLLLLVVALGIGLFMRRRHIVRKRTLRRLLQERELVEPLTPSGEAPNQALLRILKETEFKKIKVLGSGAFGTVYKGLW
                    # IPEGEKVKIPVAIKELREATSPKANKEILDEAYVMASVDNPHVCRLLGICLTSTVQLIMQLMPFGCLLDYVREHKDNIGSQYLLNWCVQIAKGMNYLE
                    # DRRLVHRDLAARNVLVKTPQHVKITDFGLAKLLGAEEKEYHAEGGKVPIKWMALESILHRIYTHQSDVWSYGVTVWELMTFGSKPYDGIPASEISSIL
                    # EKGERLPQPPICTIDVYMIMVKCWMIDADSRPKFRELIIEFSKMARDPQRYLVIQGDERMHLPSPTDSNFYRALMDEEDMDDVVDADEYLIPQQGFFS
                    # SPSTSRTPLLSSLSATSNNSTVACIDRNGLQSCPIKEDSFLQRYSSDPTGALTEDSIDDTFLPVPEYINQSVPKRPAGSVQNPVYHNQPLNPAPSRDP
                    # HYQDPHSTAVGNPEYLNTVQPTCVNSTFDSPAHWAQKGSHQISLDNPDYQQDFFPKEAKPNGIFKGSTAENAEYLRVAPQSSEFIGA' , 'MAALSG
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
                    # '2' , '4' , '4' , '2' , '2' , '4'
                }
            }
        }
    }
