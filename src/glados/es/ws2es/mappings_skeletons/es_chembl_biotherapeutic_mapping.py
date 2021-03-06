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
                    # '9860' , '9865' , '9867' , '9869' , '9874' , '9876' , '9880' , '9882' , '9886' , '9888'
                    'component_type': 'TEXT',
                    # EXAMPLES:
                    # 'PROTEIN' , 'PROTEIN' , 'PROTEIN' , 'PROTEIN' , 'PROTEIN' , 'PROTEIN' , 'PROTEIN' , 'PROTEIN' , 'P
                    # ROTEIN' , 'PROTEIN'
                    'description': 'TEXT',
                    # EXAMPLES:
                    # 'IDARUCIZUMAB HEAVY CHAIN FAB FRAGMENT' , 'LANDOGROZUMAB HEAVY CHAIN' , 'ISATUXIMAB HEAVY CHAIN' ,
                    #  'MIRVETUXIMAB SORAVTANSINE HEAVY CHAIN' , 'EVINACUMAB HEAVY CHAIN' , 'VANUCIZUMAB HEAVY CHAIN 1' 
                    # , 'LIFASTUZUMAB HEAVY CHAIN' , 'BRONTICTUZUMAB HEAVY CHAIN' , 'RINUCUMAB HEAVY CHAIN' , 'REFANEZUM
                    # AB HEAVY CHAIN'
                    'organism': 'TEXT',
                    # EXAMPLES:
                    # 'Homo sapiens' , 'Homo sapiens' , 'Homo sapiens' , 'Clostridium botulinum' , 'Homo sapiens' , 'Hom
                    # o sapiens' , 'Homo sapiens' , 'Corynephage beta' , 'Homo sapiens' , 'Homo sapiens'
                    'sequence': 'TEXT',
                    # EXAMPLES:
                    # 'QVQLQESGPGLVKPSETLSLTCTVSGFSLTSYIVDWIRQPPGKGLEWIGVIWAGGSTGYNSALRSRVSITKDTSKNQFSLKLSSVTAADTAVYYCAS
                    # AAYYSYYNYDGFAYWGQGTLVTVSSASTKGPSVFPLAPSSKSTSGGTAALGCLVKDYFPEPVTVSWNSGALTSGVHTFPAVLQSSGLYSLSSVVTVPS
                    # SSLGTQTYICNVNHKPSNTKVDKKVEPKSC' , 'EVQLVESGGGLVQPGGSLRLSCAASGLTFSRYPMSWVRQAPGKGLVWVSAITSSGGSTYYSDT
                    # VKGRFTISRDNAKNTLYLQMNSLRAEDTAVYYCARLPDYWGQGTLVTVSSASTKGPSVFPLAPCSRSTSESTAALGCLVKDYFPEPVTVSWNSGALTS
                    # GVHTFPAVLQSSGLYSLSSVVTVPSSSLGTKTYTCNVDHKPSNTKVDKRVESKYGPPCPPCPAPEFLGGPSVFLFPPKPKDTLMISRTPEVTCVVVDV
                    # SQEDPEVQFNWYVDGVEVHNAKTKPREEQFNSTYRVVSVLTVLHQDWLNGKEYKCKVSNKGLPSSIEKTISKAKGQPREPQVYTLPPSQEEMTKNQVS
                    # LTCLVKGFYPSDIAVEWESNGQPENNYKTTPPVLDSDGSFFLYSRLTVDKSRWQEGNVFSCSVMHEALHNHYTQKSLSLSLG' , 'QVQLVQSGAEV
                    # AKPGTSVKLSCKASGYTFTDYWMQWVKQRPGQGLEWIGTIYPGDGDTGYAQKFQGKATLTADKSSKTVYMHLSSLASEDSAVYYCARGDYYGSNSLDY
                    # WGQGTSVTVSSASTKGPSVFPLAPSSKSTSGGTAALGCLVKDYFPEPVTVSWNSGALTSGVHTFPAVLQSSGLYSLSSVVTVPSSSLGTQTYICNVNH
                    # KPSNTKVDKKVEPKSCDKTHTCPPCPAPELLGGPSVFLFPPKPKDTLMISRTPEVTCVVVDVSHEDPEVKFNWYVDGVEVHNAKTKPREEQYNSTYRV
                    # VSVLTVLHQDWLNGKEYKCKVSNKALPAPIEKTISKAKGQPREPQVYTLPPSRDELTKNQVSLTCLVKGFYPSDIAVEWESNGQPENNYKTTPPVLDS
                    # DGSFFLYSKLTVDKSRWQQGNVFSCSVMHEALHNHYTQKSLSLSPGK' , 'QVQLVQSGAEVVKPGASVKISCKASGYTFTGYFMNWVKQSPGQSLE
                    # WIGRIHPYDGDTFYNQKFQGKATLTVDKSSNTAHMELLSLTSEDFAVYYCTRYDGSRAMDYWGQGTTVTVSSASTKGPSVFPLAPSSKSTSGGTAALG
                    # CLVKDYFPEPVTVSWNSGALTSGVHTFPAVLQSSGLYSLSSVVTVPSSSLGTQTYICNVNHKPSNTKVDKKVEPKSCDKTHTCPPCPAPELLGGPSVF
                    # LFPPKPKDTLMISRTPEVTCVVVDVSHEDPEVKFNWYVDGVEVHNAKTKPREEQYNSTYRVVSVLTVLHQDWLNGKEYKCKVSNKALPAPIEKTISKA
                    # KGQPREPQVYTLPPSRDELTKNQVSLTCLVKGFYPSDIAVEWESNGQPENNYKTTPPVLDSDGSFFLYSKLTVDKSRWQQGNVFSCSVMHEALHNHYT
                    # QKSLSLSPG' , 'EVQLVESGGGVIQPGGSLRLSCAASGFTFDDYAMNWVRQGPGKGLEWVSAISGDGGSTYYADSVKGRFTISRDNSKNSLYLQMN
                    # SLRAEDTAFFYCAKDLRNTIFGVVIPDAFDIWGQGTMVTVSSASTKGPSVFPLAPCSRSTSESTAALGCLVKDYFPEPVTVSWNSGALTSGVHTFPAV
                    # LQSSGLYSLSSVVTVPSSSLGTKTYTCNVDHKPSNTKVDKRVESKYGPPCPPCPAPEFLGGPSVFLFPPKPKDTLMISRTPEVTCVVVDVSQEDPEVQ
                    # FNWYVDGVEVHNAKTKPREEQFNSTYRVVSVLTVLHQDWLNGKEYKCKVSNKGLPSSIEKTISKAKGQPREPQVYTLPPSQEEMTKNQVSLTCLVKGF
                    # YPSDIAVEWESNGQPENNYKTTPPVLDSDGSFFLYSRLTVDKSRWQEGNVFSCSVMHEALHNHYTQKSLSLSLGK' , 'QVQLVQSGAEVKKPGASV
                    # KVSCKASGYTFTGYYMHWVRQAPGQGLEWMGWINPNSGGTNYAQKFQGRVTMTRDTSISTAYMELSRLRSDDTAVYYCARSPNPYYYDSSGYYYPGAF
                    # DIWGQGTMVTVSSASVAAPSVFIFPPSDEQLKSGTASVVCLLNNFYPREAKVQWKVDNALQSGNSQESVTEQDSKDSTYSLSSTLTLSKADYEKHKVY
                    # ACEVTHQGLSSPVTKSFNRGECDKTHTCPPCPAPELLGGPSVFLFPPKPKDTLMISRTPEVTCVVVDVSHEDPEVKFNWYVDGVEVHNAKTKPREEQY
                    # NSTYRVVSVLTVLHQDWLNGKEYKCKVSNKALPAPIEKTISKAKGQPREPQVCTLPPSRDELTKNQVSLSCAVKGFYPSDIAVEWESNGQPENNYKTT
                    # PPVLDSDGSFFLVSKLTVDKSRWQQGNVFSCSVMHEALHNHYTQKSLSLSPGK' , 'EVQLVESGGGLVQPGGSLRLSCAASGFSFSDFAMSWVRQA
                    # PGKGLEWVATIGRVAFHTYYPDSMKGRFTISRDNSKNTLYLQMNSLRAEDTAVYYCARHRGFDVGHFDFWGQGTLVTVSSASTKGPSVFPLAPSSKST
                    # SGGTAALGCLVKDYFPEPVTVSWNSGALTSGVHTFPAVLQSSGLYSLSSVVTVPSSSLGTQTYICNVNHKPSNTKVDKKVEPKSCDKTHTCPPCPAPE
                    # LLGGPSVFLFPPKPKDTLMISRTPEVTCVVVDVSHEDPEVKFNWYVDGVEVHNAKTKPREEQYNSTYRVVSVLTVLHQDWLNGKEYKCKVSNKALPAP
                    # IEKTISKAKGQPREPQVYTLPPSREEMTKNQVSLTCLVKGFYPSDIAVEWESNGQPENNYKTTPPVLDSDGSFFLYSKLTVDKSRWQQGNVFSCSVMH
                    # EALHNHYTQKSLSLSPGK' , 'QVQLVQSGAEVKKPGASVKISCKVSGYTLRGYWIEWVRQAPGKGLEWIGQILPGTGRTNYNEKFKGRVTMTADTS
                    # TDTAYMELSSLRSEDTAVYYCARFDGNYGYYAMDYWGQGTTVTVSSASTKGPSVFPLAPCSRSTSESTAALGCLVKDYFPEPVTVSWNSGALTSGVHT
                    # FPAVLQSSGLYSLSSVVTVPSSNFGTQTYTCNVDHKPSNTKVDKTVERKCCVECPPCPAPPVAGPSVFLFPPKPKDTLMISRTPEVTCVVVDVSHEDP
                    # EVQFNWYVDGVEVHNAKTKPREEQFNSTFRVVSVLTVVHQDWLNGKEYKCKVSNKGLPAPIEKTISKTKGQPREPQVYTLPPSREEMTKNQVSLTCLV
                    # KGFYPSDIAVEWESNGQPENNYKTTPPMLDSDGSFFLYSKLTVDKSRWQQGNVFSCSVMHEALHNHYTQKSLSLSPGK' , 'QLQLQESGPGLVKPS
                    # ETLSLTCTVSGGSITSSSYYWGWIRQPPGKGLEWIGSIYYRGSTNYNPSLKSRVTISVDSSKNQFYLKVSSVTAVDTAVYYCARQNGAARPSWFDPWG
                    # QGTLVTVSSASTKGPSVFPLAPCSRSTSESTAALGCLVKDYFPEPVTVSWNSGALTSGVHTFPAVLQSSGLYSLSSVVTVPSSSLGTKTYTCNVDHKP
                    # SNTKVDKRVESKYGPPCPPCPAPEFLGGPSVFLFPPKPKDTLMISRTPEVTCVVVDVSQEDPEVQFNWYVDGVEVHNAKTKPREEQFNSTYRVVSVLT
                    # VLHQDWLNGKEYKCKVSNKGLPSSIEKTISKAKGQPREPQVYTLPPSQEEMTKNQVSLTCLVKGFYPSDIAVEWESNGQPENNYKTTPPVLDSDGSFF
                    # LYSRLTVDKSRWQEGNVFSCSVMHEALHNHYTQKSLSLSLG' , 'QVQLVQSGSELKKPGASVKVSCKASGYTFTNYGMNWVRQAPGQGLEWMGWIN
                    # TYTGEPTYADDFTGRFVFSLDTSVSTAYLQISSLKAEDTAVYYCARNPINYYGINYEGYVMDYWGQGTLVTVSSASTKGPSVFPLAPSSKSTSGGTAA
                    # LGCLVKDYFPEPVTVSWNSGALTSGVHTFPAVLQSSGLYSLSSVVTVPSSSLGTQTYICNVNHKPSNTKVDKKVEPKSCDKTHTCPPCPAPELAGAPS
                    # VFLFPPKPKDTLMISRTPEVTCVVVDVSHEDPEVKFNWYVDGVEVHNAKTKPREEQYNSTYRVVSVLTVLHQDWLNGKEYKCKVSNKALPAPIEKTIS
                    # KAKGQPREPQVYTLPPSRDELTKNQVSLTCLVKGFYPSDIAVEWESNGQPENNYKTTPPVLDSDGSFFLYSKLTVDKSRWQQGNVFSCSVMHEALHNH
                    # YTQKSLSLSPGK'
                    'tax_id': 'NUMERIC',
                    # EXAMPLES:
                    # '9606' , '9606' , '9606' , '1491' , '9606' , '9606' , '9606' , '10703' , '9606' , '9606'
                }
            },
            'description': 'TEXT',
            # EXAMPLES:
            # 'beta-Endorphin' , 'OREXIN B' , 'ANNUMURICATIN C' , 'NOVEXATIN' , 'THYMOPENTIN' , 'PROCALCITONIN' , 'GALAN
            # TIDE' , 'METKEPHAMID ACETATE' , 'LUSUPULTIDE' , 'TCIPSGQPCPYNENCCSQSCTFKENENGNTVKRCD'
            'helm_notation': 'TEXT',
            # EXAMPLES:
            # 'PEPTIDE1{[Sar].R.V.[X417].I.H.P.F}$$$$' , 'PEPTIDE1{[ac].[X127].T.G.L.N.T.R.S.Q.E.T.[X127].E.T.L.[am]}$$$
            # $' , 'PEPTIDE1{[Sar].R.V.[Phe(4-Cl)].I.H.P.F}$$$$' , 'PEPTIDE1{[Phe(4-Cl)].C.[3-Pal].[dW].K.[dT].[Me_dC].[
            # Nal].[am]}$PEPTIDE1,PEPTIDE1,7:R3-2:R3$$$' , 'PEPTIDE1{[Phe(4-Cl)].C.[3-Pal].[dW].[meK].[dT].[dC].W.[am]}$
            # PEPTIDE1,PEPTIDE1,7:R3-2:R3$$$' , 'PEPTIDE1{D.R.V.[X3].I.H.P.F}$$$$' , 'PEPTIDE1{Q.[dA].[dK].S.N.R.K.L.[Nl
            # e].E.I.I.[am]}|PEPTIDE2{[dF].H.L.L.R.E.V.L.E.[Nle].A.R.A.E.Q.L.A.E}$PEPTIDE2,PEPTIDE1,18:R2-1:R1|PEPTIDE2,
            # PEPTIDE1,18:R3-3:R3$$$' , 'PEPTIDE1{D.R.V.Y.I.H.P.C}$$$$' , 'PEPTIDE1{[Phe(4-Cl)].C.[3-Pal].[dW].K.[dT].[d
            # C].[Nal].[am]}$PEPTIDE1,PEPTIDE1,7:R3-2:R3$$$' , 'PEPTIDE1{[Sar].R.V.[X998].I.H.P.F}$$$$'
            'molecule_chembl_id': 'TEXT',
            # EXAMPLES:
            # 'CHEMBL3350962' , 'CHEMBL2369726' , 'CHEMBL3350963' , 'CHEMBL2369734' , 'CHEMBL2369735' , 'CHEMBL3350967' 
            # , 'CHEMBL2369741' , 'CHEMBL3350973' , 'CHEMBL2369749' , 'CHEMBL3351042'
        }
    }
