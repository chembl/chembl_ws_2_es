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
            # 'INHIBITOR' , 'INHIBITOR' , 'INHIBITOR' , 'RELEASING AGENT' , 'RELEASING AGENT' , 'RELEASING AGENT' , 'INH
            # IBITOR' , 'INHIBITOR' , 'INHIBITOR' , 'RELEASING AGENT'
            'binding_site_comment': 'TEXT',
            # EXAMPLES:
            # '23s rRNA (interacts with the A- and P-sites).' , 'Box B' , 'Hydrophobic cavity in the HA trimer stem at t
            # he interface between two protomers. ' , '3′ untranslated region at base position 489-508' , 'Effects poten
            # tially mediated by beta subunit.' , 'gp120 subunit' , 'Binds to both dihydropyridine and nondihydropyridin
            # e binding sites.' , 'Binds dihydropyridine and nondihydropyridine binding sites.' , 'gp120 subunit' , 'Ben
            # zodiazepine site'
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
            # '683' , '684' , '685' , '686' , '687' , '688' , '689' , '690' , '691' , '692'
            'mechanism_comment': 'TEXT',
            # EXAMPLES:
            # 'Expressed in eye' , 'Role in regulating gastric secretion, M3 likely involved' , 'Role in regulating gast
            # ric secretion, M3 likely involved' , 'Role in regulating gastric secretion, M3 likely involved' , 'Role in
            #  regulating gastric secretion, M3 likely involved' , 'Indicated in irritable bowel, M3 likely involved' , 
            # 'Role in regulating gastric secretion, M3 likely involved' , 'May be mixed agonist/antagonist' , 'Substitu
            # tes for deficient phenylalanine hydroxylase. Hydrolyses phenylalanine to reduce blood concentrations.' , '
            # Hydrolyses L-asparagine which is required by leukemic cells which have low level expression of L-asparagin
            # e synthetase.'
            'mechanism_of_action': 'TEXT',
            # EXAMPLES:
            # 'Tyrosine-protein kinase SRC inhibitor' , 'Dopamine transporter inhibitor' , 'Dopamine transporter inhibit
            # or' , 'Dopamine transporter releasing agent' , 'Dopamine transporter releasing agent' , 'Dopamine transpor
            # ter releasing agent' , 'Dopamine transporter inhibitor' , 'Dopamine transporter inhibitor' , 'Dopamine tra
            # nsporter inhibitor' , 'Dopamine transporter releasing agent'
            'mechanism_refs': 
            {
                'properties': 
                {
                    'ref_id': 'TEXT',
                    # EXAMPLES:
                    # 'setid=4dc7f0af-77fb-4eec-46b9-dd1c2dcb4525#section-13' , 'setid=2c824d4c-2309-4e2a-bc74-aa8d80a5c
                    # 454#nlm34090-1' , 'setid=2c824d4c-2309-4e2a-bc74-aa8d80a5c454' , 'D07445' , 'D07445' , 'D07445' , 
                    # 'setid=5cb7fd36-ae36-409b-af79-9c432e1cf5d9#nlm34090-1' , 'setid=5cb7fd36-ae36-409b-af79-9c432e1cf
                    # 5d9#nlm34090-1' , 'setid=d334e2f1-7497-4131-a5c0-7ac30d4741cb#nlm34090-1' , 'D07445'
                    'ref_type': 'TEXT',
                    # EXAMPLES:
                    # 'DailyMed' , 'DailyMed' , 'DailyMed' , 'KEGG' , 'KEGG' , 'KEGG' , 'DailyMed' , 'DailyMed' , 'Daily
                    # Med' , 'KEGG'
                    'ref_url': 'TEXT',
                    # EXAMPLES:
                    # 'http://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=4dc7f0af-77fb-4eec-46b9-dd1c2dcb4525#sectio
                    # n-13' , 'http://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=2c824d4c-2309-4e2a-bc74-aa8d80a5c45
                    # 4#nlm34090-1' , 'http://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=2c824d4c-2309-4e2a-bc74-aa8
                    # d80a5c454' , 'http://www.kegg.jp/dbget-bin/www_bget?dr:D07445' , 'http://www.kegg.jp/dbget-bin/www
                    # _bget?dr:D07445' , 'http://www.kegg.jp/dbget-bin/www_bget?dr:D07445' , 'http://dailymed.nlm.nih.go
                    # v/dailymed/lookup.cfm?setid=5cb7fd36-ae36-409b-af79-9c432e1cf5d9#nlm34090-1' , 'http://dailymed.nl
                    # m.nih.gov/dailymed/lookup.cfm?setid=5cb7fd36-ae36-409b-af79-9c432e1cf5d9#nlm34090-1' , 'http://dai
                    # lymed.nlm.nih.gov/dailymed/lookup.cfm?setid=d334e2f1-7497-4131-a5c0-7ac30d4741cb#nlm34090-1' , 'ht
                    # tp://www.kegg.jp/dbget-bin/www_bget?dr:D07445'
                }
            },
            'molecular_mechanism': 'BOOLEAN',
            # EXAMPLES:
            # 'True' , 'True' , 'True' , 'True' , 'True' , 'True' , 'True' , 'True' , 'True' , 'True'
            'molecule_chembl_id': 'TEXT',
            # EXAMPLES:
            # 'CHEMBL24828' , 'CHEMBL1373' , 'CHEMBL1201192' , 'CHEMBL1200377' , 'CHEMBL405' , 'CHEMBL501' , 'CHEMBL1201
            # 735' , 'CHEMBL1698' , 'CHEMBL904' , 'CHEMBL1200387'
            'parent_molecule_chembl_id': 'TEXT',
            # EXAMPLES:
            # 'CHEMBL24828' , 'CHEMBL1373' , 'CHEMBL1201192' , 'CHEMBL405' , 'CHEMBL405' , 'CHEMBL405' , 'CHEMBL894' , '
            # CHEMBL894' , 'CHEMBL827' , 'CHEMBL405'
            'record_id': 'NUMERIC',
            # EXAMPLES:
            # '1343277' , '1343811' , '1343365' , '1344287' , '1344593' , '1344804' , '1344610' , '1343619' , '1344109' 
            # , '1344586'
            'selectivity_comment': 'TEXT',
            # EXAMPLES:
            # 'Inhibits serine beta lactamases (SHV, TEM, CTX-M type and Enterobacter cloacae P99, Pseudomonase derived 
            # cephalosporinase PDC and Klebsiella pneumoniae carbapenemase KPC). Not active against MBLs, some oxacillin
            # ases and certain GES allelles. Can restore the activity of imipenem/cilastatin combinations against KPC-pr
            # oducing Enterobacteriaceae and PDC-producing Pseudomonas aeruginosa.' , 'Inhibits serine beta lactamases (
            # SHV, TEM, CTX-M type and Enterobacter cloacae P99, Pseudomonase derived cephalosporinase PDC and Klebsiell
            # a pneumoniae carbapenemase KPC). Not active against MBLs, some oxacillinases and certain GES allelles. Can
            #  restore the activity of imipenem/cilastatin combinations against KPC-producing Enterobacteriaceae and PDC
            # -producing Pseudomonas aeruginosa.' , 'Inhibits serine beta lactamases (SHV, TEM, CTX-M type and Enterobac
            # ter cloacae P99, Pseudomonase derived cephalosporinase PDC and Klebsiella pneumoniae carbapenemase KPC). N
            # ot active against MBLs, some oxacillinases and certain GES allelles. Can restore the activity of imipenem/
            # cilastatin combinations against KPC-producing Enterobacteriaceae and PDC-producing Pseudomonas aeruginosa.
            # ' , 'High selectivity for CXCR2 over CXCR1' , 'IC(50) inhibition PARP2 (2.1 nM)' , 'IC(50) inhibition PARP
            # 1 (3.8 nM) ' , 'Non-selective but type 5 receptor is overexpressed in Cushing's disease' , 'Selective' , '
            # Binds predominantly to MCR-1.' , 'Most active at the gamma subtype, > 20-fold selectivity over RAR alpha a
            # nd RAR beta.'
            'site_id': 'NUMERIC',
            # EXAMPLES:
            # '2621' , '2627' , '2617' , '2627' , '2627' , '2627' , '2627' , '2627' , '2627' , '2627'
            'target_chembl_id': 'TEXT',
            # EXAMPLES:
            # 'CHEMBL267' , 'CHEMBL238' , 'CHEMBL238' , 'CHEMBL238' , 'CHEMBL238' , 'CHEMBL238' , 'CHEMBL238' , 'CHEMBL2
            # 38' , 'CHEMBL238' , 'CHEMBL238'
            'variant_sequence': 
            {
                'properties': 
                {
                    'accession': 'TEXT',
                    # EXAMPLES:
                    # 'P15056' , 'P15056' , 'P15056' , 'P00533' , 'P00533' , 'P00533'
                    'isoform': 'NUMERIC',
                    # EXAMPLES:
                    # '1' , '1' , '1'
                    'mutation': 'TEXT',
                    # EXAMPLES:
                    # 'V600E' , 'V600E' , 'V600E' , 'T790M' , 'T790M' , 'T790M'
                    'organism': 'TEXT',
                    # EXAMPLES:
                    # 'Homo sapiens' , 'Homo sapiens' , 'Homo sapiens' , 'Homo sapiens' , 'Homo sapiens' , 'Homo sapiens
                    # '
                    'sequence': 'TEXT',
                    # EXAMPLES:
                    # 'MAALSGGGGGGAEPGQALFNGDMEPEAGAGAGAAASSAADPAIPEEVWNIKQMIKLTQEHIEALLDKFGGEHNPPSIYLEAYEEYTSKLDALQQREQ
                    # QLLESLGNGTDFSVSSSASMDTVTSSSSSSLSVLPSSLSVFQNPTDVARSNPKSPQKPIVRVFLPNKQRTVVPARCGVTVRDSLKKALMMRGLIPECC
                    # AVYRIQDGEKKPIGWDTDISWLTGEELHVEVLENVPLTTHNFVRKTFFTLAFCDFCRKLLFQGFRCQTCGYKFHQRCSTEVPLMCVNYDQLDLLFVSK
                    # FFEHHPIPQEEASLAETALTSGSSPSAPASDSIGPQILTSPSPSKSIPIPQPFRPADEDHRNQFGQRDRSSSAPNVHINTIEPVNIDDLIRDQGFRGD
                    # GGSTTGLSATPPASLPGSLTNVKALQKSPGPQRERKSSSSSEDRNRMKTLGRRDSSDDWEIPDGQITVGQRIGSGSFGTVYKGKWHGDVAVKMLNVTA
                    # PTPQQLQAFKNEVGVLRKTRHVNILLFMGYSTKPQLAIVTQWCEGSSLYHHLHIIETKFEMIKLIDIARQTAQGMDYLHAKSIIHRDLKSNNIFLHED
                    # LTVKIGDFGLATEKSRWSGSHQFEQLSGSILWMAPEVIRMQDKNPYSFQSDVYAFGIVLYELMTGQLPYSNINNRDQIIFMVGRGYLSPDLSKVRSNC
                    # PKAMKRLMAECLKKKRDERPLFPQILASIELLARSLPKIHRSASEPSLNRAGFQTEDFSLYACASPKTPIQAGGYGAFPVH' , 'MAALSGGGGGGA
                    # EPGQALFNGDMEPEAGAGAGAAASSAADPAIPEEVWNIKQMIKLTQEHIEALLDKFGGEHNPPSIYLEAYEEYTSKLDALQQREQQLLESLGNGTDFS
                    # VSSSASMDTVTSSSSSSLSVLPSSLSVFQNPTDVARSNPKSPQKPIVRVFLPNKQRTVVPARCGVTVRDSLKKALMMRGLIPECCAVYRIQDGEKKPI
                    # GWDTDISWLTGEELHVEVLENVPLTTHNFVRKTFFTLAFCDFCRKLLFQGFRCQTCGYKFHQRCSTEVPLMCVNYDQLDLLFVSKFFEHHPIPQEEAS
                    # LAETALTSGSSPSAPASDSIGPQILTSPSPSKSIPIPQPFRPADEDHRNQFGQRDRSSSAPNVHINTIEPVNIDDLIRDQGFRGDGGSTTGLSATPPA
                    # SLPGSLTNVKALQKSPGPQRERKSSSSSEDRNRMKTLGRRDSSDDWEIPDGQITVGQRIGSGSFGTVYKGKWHGDVAVKMLNVTAPTPQQLQAFKNEV
                    # GVLRKTRHVNILLFMGYSTKPQLAIVTQWCEGSSLYHHLHIIETKFEMIKLIDIARQTAQGMDYLHAKSIIHRDLKSNNIFLHEDLTVKIGDFGLATE
                    # KSRWSGSHQFEQLSGSILWMAPEVIRMQDKNPYSFQSDVYAFGIVLYELMTGQLPYSNINNRDQIIFMVGRGYLSPDLSKVRSNCPKAMKRLMAECLK
                    # KKRDERPLFPQILASIELLARSLPKIHRSASEPSLNRAGFQTEDFSLYACASPKTPIQAGGYGAFPVH' , 'MAALSGGGGGGAEPGQALFNGDMEP
                    # EAGAGAGAAASSAADPAIPEEVWNIKQMIKLTQEHIEALLDKFGGEHNPPSIYLEAYEEYTSKLDALQQREQQLLESLGNGTDFSVSSSASMDTVTSS
                    # SSSSLSVLPSSLSVFQNPTDVARSNPKSPQKPIVRVFLPNKQRTVVPARCGVTVRDSLKKALMMRGLIPECCAVYRIQDGEKKPIGWDTDISWLTGEE
                    # LHVEVLENVPLTTHNFVRKTFFTLAFCDFCRKLLFQGFRCQTCGYKFHQRCSTEVPLMCVNYDQLDLLFVSKFFEHHPIPQEEASLAETALTSGSSPS
                    # APASDSIGPQILTSPSPSKSIPIPQPFRPADEDHRNQFGQRDRSSSAPNVHINTIEPVNIDDLIRDQGFRGDGGSTTGLSATPPASLPGSLTNVKALQ
                    # KSPGPQRERKSSSSSEDRNRMKTLGRRDSSDDWEIPDGQITVGQRIGSGSFGTVYKGKWHGDVAVKMLNVTAPTPQQLQAFKNEVGVLRKTRHVNILL
                    # FMGYSTKPQLAIVTQWCEGSSLYHHLHIIETKFEMIKLIDIARQTAQGMDYLHAKSIIHRDLKSNNIFLHEDLTVKIGDFGLATEKSRWSGSHQFEQL
                    # SGSILWMAPEVIRMQDKNPYSFQSDVYAFGIVLYELMTGQLPYSNINNRDQIIFMVGRGYLSPDLSKVRSNCPKAMKRLMAECLKKKRDERPLFPQIL
                    # ASIELLARSLPKIHRSASEPSLNRAGFQTEDFSLYACASPKTPIQAGGYGAFPVH' , 'MRPSGTAGAALLALLAALCPASRALEEKKVCQGTSNKL
                    # TQLGTFEDHFLSLQRMFNNCEVVLGNLEITYVQRNYDLSFLKTIQEVAGYVLIALNTVERIPLENLQIIRGNMYYENSYALAVLSNYDANKTGLKELP
                    # MRNLQEILHGAVRFSNNPALCNVESIQWRDIVSSDFLSNMSMDFQNHLGSCQKCDPSCPNGSCWGAGEENCQKLTKIICAQQCSGRCRGKSPSDCCHN
                    # QCAAGCTGPRESDCLVCRKFRDEATCKDTCPPLMLYNPTTYQMDVNPEGKYSFGATCVKKCPRNYVVTDHGSCVRACGADSYEMEEDGVRKCKKCEGP
                    # CRKVCNGIGIGEFKDSLSINATNIKHFKNCTSISGDLHILPVAFRGDSFTHTPPLDPQELDILKTVKEITGFLLIQAWPENRTDLHAFENLEIIRGRT
                    # KQHGQFSLAVVSLNITSLGLRSLKEISDGDVIISGNKNLCYANTINWKKLFGTSGQKTKIISNRGENSCKATGQVCHALCSPEGCWGPEPRDCVSCRN
                    # VSRGRECVDKCNLLEGEPREFVENSECIQCHPECLPQAMNITCTGRGPDNCIQCAHYIDGPHCVKTCPAGVMGENNTLVWKYADAGHVCHLCHPNCTY
                    # GCTGPGLEGCPTNGPKIPSIATGMVGALLLLLVVALGIGLFMRRRHIVRKRTLRRLLQERELVEPLTPSGEAPNQALLRILKETEFKKIKVLGSGAFG
                    # TVYKGLWIPEGEKVKIPVAIKELREATSPKANKEILDEAYVMASVDNPHVCRLLGICLTSTVQLIMQLMPFGCLLDYVREHKDNIGSQYLLNWCVQIA
                    # KGMNYLEDRRLVHRDLAARNVLVKTPQHVKITDFGLAKLLGAEEKEYHAEGGKVPIKWMALESILHRIYTHQSDVWSYGVTVWELMTFGSKPYDGIPA
                    # SEISSILEKGERLPQPPICTIDVYMIMVKCWMIDADSRPKFRELIIEFSKMARDPQRYLVIQGDERMHLPSPTDSNFYRALMDEEDMDDVVDADEYLI
                    # PQQGFFSSPSTSRTPLLSSLSATSNNSTVACIDRNGLQSCPIKEDSFLQRYSSDPTGALTEDSIDDTFLPVPEYINQSVPKRPAGSVQNPVYHNQPLN
                    # PAPSRDPHYQDPHSTAVGNPEYLNTVQPTCVNSTFDSPAHWAQKGSHQISLDNPDYQQDFFPKEAKPNGIFKGSTAENAEYLRVAPQSSEFIGA' , 
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
                    # EYLNTVQPTCVNSTFDSPAHWAQKGSHQISLDNPDYQQDFFPKEAKPNGIFKGSTAENAEYLRVAPQSSEFIGA'
                    'tax_id': 'NUMERIC',
                    # EXAMPLES:
                    # '9606' , '9606' , '9606' , '9606' , '9606' , '9606'
                    'version': 'NUMERIC',
                    # EXAMPLES:
                    # '4' , '4' , '4' , '2' , '2' , '2'
                }
            }
        }
    }
