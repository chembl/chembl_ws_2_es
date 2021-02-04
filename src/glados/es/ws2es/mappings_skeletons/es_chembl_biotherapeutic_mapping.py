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
            'biocomponents': 
            {
                'properties': 
                {
                    'component_id': 'NUMERIC',
                    # EXAMPLES:
                    # '6578' , '6579' , '6580' , '6582' , '6747' , '9846' , '9848' , '9850' , '9860' , '9862'
                    'component_type': 'TEXT',
                    # EXAMPLES:
                    # 'PROTEIN' , 'PROTEIN' , 'PROTEIN' , 'PROTEIN' , 'PROTEIN' , 'PROTEIN' , 'PROTEIN' , 'PROTEIN' , 'P
                    # ROTEIN' , 'PROTEIN'
                    'description': 'TEXT',
                    # EXAMPLES:
                    # 'Caplacizumab' , 'Delantercept fusion protein' , 'Ocaratuzumab heavy chain' , 'Simtuzumab heavy ch
                    # ain' , 'Enfuvirtide peptide' , 'OPICINUMAB HEAVY CHAIN' , 'LABETUZUMAB GOVITECAN HEAVY CHAIN' , 'I
                    # ODINE I 131 DERLOTUXIMAB BIOTIN HEAVY CHAIN' , 'IDARUCIZUMAB HEAVY CHAIN FAB FRAGMENT' , 'ISATUXIM
                    # AB HEAVY CHAIN'
                    'organism': 'TEXT',
                    # EXAMPLES:
                    # 'Homo sapiens' , 'Homo sapiens' , 'Homo sapiens' , 'Homo sapiens' , 'Homo sapiens' , 'Homo sapiens
                    # ' , 'Homo sapiens' , 'Homo sapiens' , 'Homo sapiens' , 'Homo sapiens'
                    'sequence': 'TEXT',
                    # EXAMPLES:
                    # 'EVQLVESGGGLVQPGGSLRLSCAASGRTFSYNPMGWFRQAPGKGRELVAAISRTGGSTYYPDSVEGRFTISRDNAKRMVYLQMNSLRAEDTAVYYCA
                    # AAGVRAEDGRVRTLPSEYTFWGQGTQVTVSSAAAEVQLVESGGGLVQPGGSLRLSCAASGRTFSYNPMGWFRQAPGKGRELVAAISRTGGSTYYPDSV
                    # EGRFTISRDNAKRMVYLQMNSLRAEDTAVYYCAAAGVRAEDGRVRTLPSEYTFWGQGTQVTVSS' , 'DPVKPSRGPLVTCTCESPHCKGPTCRGAW
                    # CTVVLVREEGRHPQEHRGCGNLHRELCRGRPTEFVNHYCCDSHLCNHNVSLVLEATQPPSEQPGTDGQLATGGGTHTCPPCPAPEALGAPSVFLFPPK
                    # PKDTLMISRTPEVTCVVVDVSHEDPEVKFNWYVDGVEVHNAKTKPREEQYNSTYRVVSVLTVLHQDWLNGKEYKCKVSNKALPVPIEKTISKAKGQPR
                    # EPQVYTLPPSREEMTKNQVSLTCLVKGFYPSDIAVEWESNGQPENNYKTTPPVLDSDGPFFLYSKLTVDKSRWQQGNVFSCSVMHEALHNHYTQKSLS
                    # LSPGK' , 'EVQLVQSGAEVKKPGESLKISCKGSGRTFTSYNMHWVRQMPGKGLEWMGAIYPLTGDTSYNQKSKLQVTISADKSISTAYLQWSSLKA
                    # SDTAMYYCARSTYVGGDWQFDVWGKGTTVTVSSASTKGPSVFPLAPSSKSTSGGTAALGCLVKDYFPEPVTVSWNSGALTSGVHTFPAVLQSSGLYSL
                    # SSVVTVPSSSLGTQTYICNVNHKPSNTKVDKKVEPKSCDKTHTCPPCPAPELLGGPSVFLFPPKIKDTLMISRTPEVTCVVVDVSHEDPEVKFNWYVD
                    # GVEVHNAKTKPREEQYNSTYRVVSVLTVLHQDWLNGKEYKCKVSNKALPAPIEKTISKQKGQPREPQVYTLPPSRDELTKNQVSLTCLVKGFYPSDIA
                    # VEWESNGQPENNYKTTPPVLDSDGSFFLYSKLTVDKSRWQQGNVFSCSVMHEALHNHYTQKSLSLSPG' , 'QVQLVQSGAEVKKPGASVKVSCKAS
                    # GYAFTYYLIEWVRQAPGQGLEWIGVINPGSGGTNYNEKFKGRATITADKSTSTAYMELSSLRSEDTAVYFCARNWMNFDYWGQGTTVTVSSASTKGPS
                    # VFPLAPCSRSTSESTAALGCLVKDYFPEPVTVSWNSGALTSGVHTFPAVLQSSGLYSLSSVVTVPSSSLGTKTYTCNVDHKPSNTKVDKRVESKYGPP
                    # CPPCPAPEFLGGPSVFLFPPKPKDTLMISRTPEVTCVVVDVSQEDPEVQFNWYVDGVEVHNAKTKPREEQFNSTYRVVSVLTVLHQDWLNGKEYKCKV
                    # SNKGLPSSIEKTISKAKGQPREPQVYTLPPSQEEMTKNQVSLTCLVKGFYPSDIAVEWESNGQPENNYKTTPPVLDSDGSFFLYSRLTVDKSRWQEGN
                    # VFSCSVMHEALHNHYTQKSLSLSLGK' , 'FWNWLSAWKDLELLEQENKEQQNQSEEILSHILSTY' , 'EVQLLESGGGLVQPGGSLRLSCAASG
                    # FTFSAYEMKWVRQAPGKGLEWVSVIGPSGGFTFYADSVKGRFTISRDNSKNTLYLQMNSLRAEDTAVYYCATEGDNDAFDIWGQGTTVTVSSASTKGP
                    # SVFPLAPSSKSTSGGTAALGCLVKDYFPEPVTVSWNSGALTSGVHTFPAVLQSSGLYSLSSVVTVPSSSLGTQTYICNVNHKPSNTKVDKKVEPKSCD
                    # KTHTCPPCPAPELLGGPSVFLFPPKPKDTLMISRTPEVTCVVVDVSHEDPEVKFNWYVDGVEVHNAKTKPREEQYNSAYRVVSVLTVLHQDWLNGKEY
                    # KCKVSNKALPAPIEKTISKAKGQPREPQVYTLPPSRDELTKNQVSLTCLVKGFYPSDIAVEWESNGQPENNYKTTPPVLDSDGSFFLYSKLTVDKSRW
                    # QQGNVFSCSVMHEALHNHYTQKSLSLSPG' , 'EVQLVESGGGVVQPGRSLRLSCSASGFDFTTYWMSWVRQAPGKGLEWIGEIHPDSSTINYAPSL
                    # KDRFTISRDNAKNTLFLQMDSLRPEDTGVYFCASLYFGFPWFAYWGQGTPVTVSSASTKGPSVFPLAPSSKSTSGGTAALGCLVKDYFPEPVTVSWNS
                    # GALTSGVHTFPAVLQSSGLYSLSSVVTVPSSSLGTQTYICNVNHKPSNTKVDKRVEPKSCDKTHTCPPCPAPELLGGPSVFLFPPKPKDTLMISRTPE
                    # VTCVVVDVSHEDPEVKFNWYVDGVEVHNAKTKPREEQYNSTYRVVSVLTVLHQDWLNGKEYKCKVSNKALPAPIEKTISKAKGQPREPQVYTLPPSRE
                    # EMTKNQVSLTCLVKGFYPSDIAVEWESNGQPENNYKTTPPVLDSDGSFFLYSKLTVDKSRWQQGNVFSCSVMHEALHNHYTQKSLSLSPGK' , 'QV
                    # QLKESGPGLVAPSQSLSITCTVSGFSLTDYGVRWIRQPPGKGLEWLGVIWGGGSTYYNSALKSRLSISKDNSKSQVFLKMNSLQTDDTAMYYCAKEKR
                    # RGYYYAMDYWGQGTSVTVSSASTKGPSVFPLAPSSKSTSGGTAALGCLVKDYFPEPVTVSWNSGALTSGVHTFPAVLQSSGLYSLSSVVTVPSSSLGT
                    # QTYICNVNHKPSNTKVDKKAEPKSCDKTHTCPPCPAPELLGGPSVFLFPPKPKDTLMISRTPEVTCVVVDVSHEDPEVKFNWYVDGVEVHNAKTKPRE
                    # EQYNSTYRVVSVLTVLHQDWLNGKEYKCKVSNKALPAPIEKTISKAKGQPREPQVYTLPPSRDELTKNQVSLTCLVKGFYPSDIAVEWESNGQPENNY
                    # KTTPPVLDSDGSFFLYSKLTVDKSRWQQGNVFSCSVMHEALHNHYTQKSLSLSPGK' , 'QVQLQESGPGLVKPSETLSLTCTVSGFSLTSYIVDWI
                    # RQPPGKGLEWIGVIWAGGSTGYNSALRSRVSITKDTSKNQFSLKLSSVTAADTAVYYCASAAYYSYYNYDGFAYWGQGTLVTVSSASTKGPSVFPLAP
                    # SSKSTSGGTAALGCLVKDYFPEPVTVSWNSGALTSGVHTFPAVLQSSGLYSLSSVVTVPSSSLGTQTYICNVNHKPSNTKVDKKVEPKSC' , 'VVG
                    # GTEAGRNSWPSQISLQYRSGGSWYHTCGGTLIRQNWVMTAAHCVDYQKTFRVVAGDHNLSQNDGTEQYVSVQKIVVHPYWNSDNVAAGYDIALLRLAQ
                    # SVTLNSYVQLGVLPQEGAILANNSPCYITGWGKTKTNGQLAQTLQQAYLPSVDYAICSSSSYWGSTVKNTMVCAGGDGVRSGCQGDSGGPLHCLVNGK
                    # YSLHGVTSFVSSRGCNVSRKPTVFTRVSAYISWINNVIASN'
                    'tax_id': 'NUMERIC',
                    # EXAMPLES:
                    # '9606' , '9606' , '9606' , '9606' , '9606' , '9606' , '9606' , '9606' , '9606' , '9606'
                }
            },
            'description': 'TEXT',
            # EXAMPLES:
            # 'ENKEPHALIN' , '[Val5] - ANGIOTENSIN II' , 'MAGAININ 2' , 'DYNORPHIN' , 'NEUROPEPTIDE-Y' , 'NPY[TYR32,LEU3
            # 4]' , 'SCALCITONIN' , 'HUMAN CORTICOTROPIN RELEASING FACTOR' , 'TYROCIDINE A' , 'OXYTOCIN DIMER'
            'helm_notation': 'TEXT',
            # EXAMPLES:
            # 'PEPTIDE1{A.L.Y.A.S.K.L.S.[am]}$$$$' , 'PEPTIDE1{[meR].K.P.W.[Tle].L}$$$$' , 'PEPTIDE1{[X833].[dP].W.[Tle]
            # .[X454]}$$$$' , 'PEPTIDE1{[X12].[dP].W.[Tle].[X454]}$$$$' , 'PEPTIDE1{K.P.W.[Tle].L}$$$$' , 'PEPTIDE1{[X12
            # ].[dP].W.I.L}$$$$' , 'PEPTIDE1{[X500].[dP].W.[Tle].[X454]}$$$$' , 'PEPTIDE1{K.F.Y.C.N.G.K.R.V.C.V.C.R.[am]
            # }$$$$' , 'PEPTIDE1{G.R.G.D.S.P}$$$$' , 'PEPTIDE1{[X12].[dP].Y.[Tle].L}$$$$'
            'molecule_chembl_id': 'TEXT',
            # EXAMPLES:
            # 'CHEMBL448105' , 'CHEMBL266571' , 'CHEMBL268600' , 'CHEMBL6562' , 'CHEMBL380726' , 'CHEMBL427604' , 'CHEMB
            # L265671' , 'CHEMBL266306' , 'CHEMBL6602' , 'CHEMBL6508'
        }
    }
