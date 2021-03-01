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
                    # '{'input': 'CDw131', 'weight': 75}' , '{'input': 'Large envelope protein', 'weight': 75}' , '{'inp
                    # ut': 'Homo sapiens', 'weight': 20}' , '{'input': 'gyrA', 'weight': 75}' , '{'input': 'Homo sapiens
                    # ', 'weight': 20}' , '{'input': 'MT-CYB', 'weight': 75}' , '{'input': 'Homo sapiens', 'weight': 20}
                    # ' , '{'input': 'Homo sapiens', 'weight': 20}' , '{'input': 'Homo sapiens', 'weight': 20}' , '{'inp
                    # ut': 'Homo sapiens', 'weight': 20}'
                    'organism_taxonomy': 
                    {
                        'properties': 
                        {
                            'l1': 'TEXT',
                            # EXAMPLES:
                            # 'Eukaryotes' , 'Viruses' , 'Eukaryotes' , 'Bacteria' , 'Eukaryotes' , 'Eukaryotes' , 'Euka
                            # ryotes' , 'Eukaryotes' , 'Eukaryotes' , 'Eukaryotes'
                            'l2': 'TEXT',
                            # EXAMPLES:
                            # 'Mammalia' , 'retro-transcribing' , 'Mammalia' , 'Gram-Negative' , 'Mammalia' , 'Apicomple
                            # xa' , 'Mammalia' , 'Mammalia' , 'Mammalia' , 'Mammalia'
                            'l3': 'TEXT',
                            # EXAMPLES:
                            # 'Primates' , 'Primates' , 'Neisseria' , 'Primates' , 'Plasmodium' , 'Primates' , 'Primates
                            # ' , 'Primates' , 'Primates' , 'Primates'
                            'oc_id': 'NUMERIC',
                            # EXAMPLES:
                            # '7' , '711' , '7' , '366' , '7' , '19' , '7' , '7' , '7' , '7'
                            'tax_id': 'NUMERIC',
                            # EXAMPLES:
                            # '9606' , '489449' , '9606' , '485' , '9606' , '5833' , '9606' , '9606' , '9606' , '9606'
                        }
                    },
                    'protein_classification': 
                    {
                        'properties': 
                        {
                            'l1': 'TEXT',
                            # EXAMPLES:
                            # 'Membrane receptor' , 'Surface antigen' , 'Secreted protein' , 'Enzyme' , 'Unclassified pr
                            # otein' , 'Other cytosolic protein' , 'Surface antigen' , 'Secreted protein' , 'Secreted pr
                            # otein' , 'Enzyme'
                            'l2': 'TEXT',
                            # EXAMPLES:
                            # 'Isomerase' , 'Oxidoreductase' , 'Transferase' , 'Oxidoreductase' , 'Protease' , 'Ligase' 
                            # , 'Family A G protein-coupled receptor' , 'Transferase' , 'Voltage-gated ion channel' , 'O
                            # xidoreductase'
                            'l3': 'TEXT',
                            # EXAMPLES:
                            # 'Serine protease' , 'Peptide receptor (family A GPCR)' , 'Potassium channels' , 'Nicotinic
                            #  acetylcholine receptor' , 'Vesicular neurotransmitter transporter family' , 'Small molecu
                            # le receptor (family A GPCR)' , 'Potassium channels' , 'Cytochrome P450 family 3' , 'SLC su
                            # perfamily of solute carriers' , 'Serine protease'
                            'l4': 'TEXT',
                            # EXAMPLES:
                            # 'Serine protease unclassified' , 'Short peptide receptor (family A GPCR)' , 'Voltage-gated
                            #  potassium channel' , 'Nicotinic acetylcholine receptor alpha subunit' , 'Lipid-like ligan
                            # d receptor (family A GPCR)' , 'Voltage-gated potassium channel' , 'Cytochrome P450 family 
                            # 3A' , 'SLC12 family of cation-coupled chloride transporters' , 'Serine protease unclassifi
                            # ed' , 'CD20 Ca2+ channel family'
                            'l5': 'TEXT',
                            # EXAMPLES:
                            # 'Serine protease S13 family' , 'Orexin receptor' , 'EDG receptor' , 'Nuclear hormone recep
                            # tor subfamily 2 group B member 3' , 'GABA-B receptor' , 'Tyrosine protein kinase Src famil
                            # y' , 'AGC protein kinase PKN family' , 'Aspartic protease A1A subfamily' , 'Metallo protea
                            # se M1 family' , 'Serine protease S8B subfamily'
                            'l6': 'TEXT',
                            # EXAMPLES:
                            # 'Tyrosine protein kinase Srm' , 'CAMK protein kinase AMPK subfamily' , 'Other protein kina
                            # se WEE1' , 'CMGC protein kinase CDC2 subfamily' , 'Cysteine protease C14A subfamily' , 'CM
                            # GC protein kinase ERK3' , 'STE protein kinase PAKA subfamily' , 'AGC protein kinase RSK su
                            # bfamily' , 'CAMK protein kinase AMPK subfamily' , 'CMGC protein kinase ERK subfamily'
                            'protein_class_id': 'NUMERIC',
                            # EXAMPLES:
                            # '11' , '9' , '3' , '644' , '601' , '8' , '9' , '3' , '3' , '10'
                        }
                    },
                    'related_activities': 
                    {
                        'properties': 
                        {
                            'count': 'NUMERIC',
                            # EXAMPLES:
                            # '37' , '139' , '157' , '556' , '7' , '10' , '71' , '2' , '229' , '2'
                        }
                    },
                    'related_assays': 
                    {
                        'properties': 
                        {
                            'all_chembl_ids': 'TEXT',
                            # EXAMPLES:
                            # 'CHEMBL872140 CHEMBL1218969 CHEMBL2329441 CHEMBL883649 CHEMBL2329317 CHEMBL882464 CHEMBL88
                            # 5364 CHEMBL885384 CHEMBL872134' , 'CHEMBL1634018 CHEMBL1634170 CHEMBL1633164 CHEMBL1633143
                            #  CHEMBL1633173 CHEMBL1635655 CHEMBL1633172 CHEMBL1635635 CHEMBL1633170 CHEMBL1633144 CHEMB
                            # L1634169 CHEMBL1633174 CHEMBL1633988 CHEMBL1633156 CHEMBL1633987 CHEMBL1634016 CHEMBL16331
                            # 68 CHEMBL1633184 CHEMBL1633160 CHEMBL1634014 CHEMBL1633171 CHEMBL1633155 CHEMBL1633157 CHE
                            # MBL1633181 CHEMBL1633150 CHEMBL1633167 CHEMBL1633177 CHEMBL1633151 CHEMBL1634017 CHEMBL163
                            # 5634 CHEMBL1633165 CHEMBL1634165 CHEMBL1633146 CHEMBL1635653 CHEMBL1633180 CHEMBL1633175 C
                            # HEMBL1633986 CHEMBL1633166 CHEMBL1633140 CHEMBL1635656 CHEMBL1633159 CHEMBL1633139 CHEMBL1
                            # 633169 CHEMBL1633152 CHEMBL1633178 CHEMBL1635648 CHEMBL1635654 CHEMBL1633158 CHEMBL1633148
                            #  CHEMBL833503 CHEMBL1634168 CHEMBL1633161 CHEMBL1634171 CHEMBL1634019 CHEMBL1633142 CHEMBL
                            # 1633147 CHEMBL1635652 CHEMBL1635650 CHEMBL1633154 CHEMBL1633985 CHEMBL1633163 CHEMBL163317
                            # 6 CHEMBL1633179 CHEMBL1634166 CHEMBL1634015 CHEMBL1634013 CHEMBL1633162 CHEMBL1634172 CHEM
                            # BL1633141 CHEMBL1635651 CHEMBL1633149 CHEMBL1633145 CHEMBL1635649 CHEMBL1634167 CHEMBL1634
                            # 012 CHEMBL1633153 CHEMBL1633984 CHEMBL1633185' , 'CHEMBL4328215 CHEMBL3991832 CHEMBL435251
                            # 8 CHEMBL3630944 CHEMBL4366564 CHEMBL4327851 CHEMBL3750018 CHEMBL4328579' , 'CHEMBL3082964 
                            # CHEMBL3059947 CHEMBL3079684 CHEMBL3082030 CHEMBL3082022 CHEMBL3048782 CHEMBL3084090 CHEMBL
                            # 3083660 CHEMBL3059945 CHEMBL3060611 CHEMBL3070382 CHEMBL3059944 CHEMBL3052568 CHEMBL306072
                            # 0 CHEMBL3059943 CHEMBL3060721 CHEMBL3084091 CHEMBL3074428 CHEMBL3074422 CHEMBL3059946 CHEM
                            # BL3083661 CHEMBL3082085 CHEMBL3060587 CHEMBL3076241 CHEMBL3060598 CHEMBL3082144 CHEMBL3076
                            # 250 CHEMBL3084089 CHEMBL3079685 CHEMBL3060722' , 'CHEMBL1030640 CHEMBL3128616 CHEMBL822871
                            #  CHEMBL665978' , 'CHEMBL1011828' , 'CHEMBL1112803 CHEMBL1112801 CHEMBL1112805 CHEMBL111280
                            # 6 CHEMBL1112809' , 'CHEMBL4396434 CHEMBL4396433' , 'CHEMBL3991729' , 'CHEMBL4150990'
                            'count': 'NUMERIC',
                            # EXAMPLES:
                            # '9' , '78' , '8' , '30' , '4' , '1' , '5' , '2' , '1' , '1'
                        }
                    },
                    'related_cell_lines': 
                    {
                        'properties': 
                        {
                            'all_chembl_ids': 'TEXT',
                            # EXAMPLES:
                            # 'CHEMBL3307715' , 'CHEMBL4483126' , 'CHEMBL3308043' , 'CHEMBL4295474' , 'CHEMBL3307715 CHE
                            # MBL3308006' , 'CHEMBL3706569 CHEMBL3308860' , 'CHEMBL3307469' , 'CHEMBL3308859 CHEMBL33077
                            # 15 CHEMBL3308861' , 'CHEMBL3307512' , 'CHEMBL3307525 CHEMBL3307520'
                            'count': 'NUMERIC',
                            # EXAMPLES:
                            # '1' , '1' , '1' , '1' , '2' , '2' , '1' , '3' , '1' , '2'
                        }
                    },
                    'related_compounds': 
                    {
                        'properties': 
                        {
                            'all_chembl_ids': 'TEXT',
                            # EXAMPLES:
                            # 'CHEMBL1214871 CHEMBL1743884 CHEMBL1923943 CHEMBL2368686 CHEMBL2323425 CHEMBL2323432 CHEMB
                            # L3217238 CHEMBL2323435 CHEMBL3216808 CHEMBL3216135 CHEMBL3216130 CHEMBL2323433 CHEMBL23234
                            # 34 CHEMBL2323429 CHEMBL2323423 CHEMBL1923929 CHEMBL2368691 CHEMBL2368693 CHEMBL1923933 CHE
                            # MBL2368692 CHEMBL1923944 CHEMBL2323440 CHEMBL2323431 CHEMBL1923941 CHEMBL2323437 CHEMBL232
                            # 3427 CHEMBL1923931 CHEMBL1923935 CHEMBL2323438 CHEMBL2368683 CHEMBL1923939 CHEMBL2323439 C
                            # HEMBL2368470 CHEMBL2323430 CHEMBL2368685 CHEMBL2368684' , 'CHEMBL425706 CHEMBL425169 CHEMB
                            # L181657 CHEMBL182304 CHEMBL424799 CHEMBL185520 CHEMBL362023 CHEMBL369122 CHEMBL181335 CHEM
                            # BL181496 CHEMBL182821 CHEMBL182225 CHEMBL182767 CHEMBL160841 CHEMBL183110 CHEMBL182604 CHE
                            # MBL1631216 CHEMBL185486 CHEMBL426613 CHEMBL2096779 CHEMBL182960 CHEMBL361747 CHEMBL161864 
                            # CHEMBL368020 CHEMBL180309 CHEMBL360130 CHEMBL182064 CHEMBL359928 CHEMBL361649 CHEMBL369342
                            #  CHEMBL360789 CHEMBL368875 CHEMBL361759 CHEMBL182263 CHEMBL359723 CHEMBL182414 CHEMBL36869
                            # 0 CHEMBL361788 CHEMBL180289 CHEMBL182650 CHEMBL183022' , 'CHEMBL38380 CHEMBL1090090 CHEMBL
                            # 2029988 CHEMBL1090479 CHEMBL3991931 CHEMBL571948 CHEMBL3218575 CHEMBL3991935 CHEMBL1738757
                            #  CHEMBL2103839 CHEMBL405130 CHEMBL2408045 CHEMBL4438024 CHEMBL3991927 CHEMBL270995 CHEMBL1
                            # 289926 CHEMBL2079588 CHEMBL1952329 CHEMBL1950289 CHEMBL4521353 CHEMBL3182444 CHEMBL1789941
                            #  CHEMBL1738797 CHEMBL1084546 CHEMBL189963 CHEMBL3545137 CHEMBL2001019 CHEMBL574737 CHEMBL1
                            # 614713 CHEMBL535 CHEMBL1615025 CHEMBL502835 CHEMBL2336325 CHEMBL521851 CHEMBL1946170 CHEMB
                            # L223360 CHEMBL217092 CHEMBL3991932 CHEMBL1229517 CHEMBL598797 CHEMBL495727 CHEMBL1801204 C
                            # HEMBL553 CHEMBL482967 CHEMBL253969 CHEMBL3188267 CHEMBL3545307 CHEMBL1908397 CHEMBL3545328
                            #  CHEMBL1289601 CHEMBL1879463 CHEMBL101253 CHEMBL3745885 CHEMBL3544983 CHEMBL3989868 CHEMBL
                            # 2103842 CHEMBL482767 CHEMBL2103840 CHEMBL3688339 CHEMBL1614710 CHEMBL601719 CHEMBL2323775 
                            # CHEMBL603469 CHEMBL564829 CHEMBL3218576 CHEMBL1088752 CHEMBL607707 CHEMBL2105728 CHEMBL123
                            # 0165 CHEMBL3353410 CHEMBL2087361 CHEMBL1173655 CHEMBL1094408 CHEMBL483321 CHEMBL402548 CHE
                            # MBL2103875 CHEMBL255863 CHEMBL3628628 CHEMBL1614766 CHEMBL2403108 CHEMBL1421 CHEMBL939 CHE
                            # MBL1231124 CHEMBL475251 CHEMBL3039525 CHEMBL1241855 CHEMBL2107832 CHEMBL4528675 CHEMBL4961
                            # 02 CHEMBL483158 CHEMBL230011 CHEMBL3348923 CHEMBL1088751 CHEMBL3264002 CHEMBL3128043 CHEMB
                            # L1336 CHEMBL124660 CHEMBL488436 CHEMBL3545157 CHEMBL3137331 CHEMBL572878 CHEMBL4446405 CHE
                            # MBL388978 CHEMBL428690 CHEMBL1233300 CHEMBL522892 CHEMBL514201 CHEMBL3301610 CHEMBL1091644
                            #  CHEMBL1079175 CHEMBL24828 CHEMBL3184679 CHEMBL3991933 CHEMBL3301612 CHEMBL551064 CHEMBL20
                            # 6834 CHEMBL274654 CHEMBL281948 CHEMBL14762 CHEMBL554 CHEMBL403989 CHEMBL1976040 CHEMBL2590
                            # 84 CHEMBL507361 CHEMBL1614725 CHEMBL3628627 CHEMBL2103851 CHEMBL1289494 CHEMBL2216870 CHEM
                            # BL2165191 CHEMBL3187723 CHEMBL3991934 CHEMBL941 CHEMBL1614701 CHEMBL477772 CHEMBL2028663 C
                            # HEMBL2146883 CHEMBL1908360 CHEMBL400402 CHEMBL3039517 CHEMBL2133806 CHEMBL254760 CHEMBL565
                            # 612 CHEMBL491473 CHEMBL1201182 CHEMBL2325741 CHEMBL413 CHEMBL2220486 CHEMBL3182621 CHEMBL1
                            # 66031 CHEMBL1230609 CHEMBL592445 CHEMBL1908394 CHEMBL2138625 CHEMBL377300 CHEMBL1233528' ,
                            #  'CHEMBL2268980 CHEMBL2271890 CHEMBL2288059 CHEMBL2288051 CHEMBL2269479 CHEMBL2269760 CHEM
                            # BL2288049 CHEMBL2268981 CHEMBL2269705 CHEMBL2268985 CHEMBL2271541 CHEMBL2268968 CHEMBL2287
                            # 827 CHEMBL2269718 CHEMBL2271897 CHEMBL2271519 CHEMBL2271513 CHEMBL2269710 CHEMBL2271893 CH
                            # EMBL2271855 CHEMBL2268697 CHEMBL2288029 CHEMBL2288048 CHEMBL2271902 CHEMBL2271901 CHEMBL22
                            # 89748 CHEMBL2288047 CHEMBL2287861 CHEMBL2271879 CHEMBL2269516 CHEMBL2269767 CHEMBL2271521 
                            # CHEMBL2268694 CHEMBL2269484 CHEMBL2271522 CHEMBL2271526 CHEMBL2269523 CHEMBL2287833 CHEMBL
                            # 2289764 CHEMBL2271887 CHEMBL2269478 CHEMBL2268973 CHEMBL2288042 CHEMBL2288066 CHEMBL228783
                            # 4 CHEMBL2287832 CHEMBL2271515 CHEMBL2268955 CHEMBL2269780 CHEMBL2271531 CHEMBL2271881 CHEM
                            # BL2271527 CHEMBL2271535 CHEMBL2269714 CHEMBL2271514 CHEMBL2271864 CHEMBL2268992 CHEMBL2271
                            # 899 CHEMBL2288027 CHEMBL2269774 CHEMBL2268982 CHEMBL2288061 CHEMBL2271518 CHEMBL2268956 CH
                            # EMBL2271895 CHEMBL2269719 CHEMBL2269476 CHEMBL2269522 CHEMBL2271862 CHEMBL2269775 CHEMBL22
                            # 68971 CHEMBL2271889 CHEMBL2271861 CHEMBL2271532 CHEMBL2268960 CHEMBL2269715 CHEMBL2268989 
                            # CHEMBL2268972 CHEMBL2288056 CHEMBL2287831 CHEMBL2271530 CHEMBL2287867 CHEMBL2268977 CHEMBL
                            # 2268699 CHEMBL2269521 CHEMBL2269770 CHEMBL2271849 CHEMBL2269778 CHEMBL2287829 CHEMBL227154
                            # 0 CHEMBL2287863 CHEMBL2269772 CHEMBL2288030 CHEMBL2268991 CHEMBL2269763 CHEMBL2272226 CHEM
                            # BL2288031 CHEMBL2271868 CHEMBL2271537 CHEMBL2269526 CHEMBL2271884 CHEMBL2271878 CHEMBL2268
                            # 983 CHEMBL1399036 CHEMBL2287826 CHEMBL2269768 CHEMBL2269477 CHEMBL2271848 CHEMBL2204209 CH
                            # EMBL2269707 CHEMBL2288028 CHEMBL2288038 CHEMBL2288054 CHEMBL2271863 CHEMBL2268969 CHEMBL22
                            # 88032 CHEMBL2272219 CHEMBL2288035 CHEMBL2271529 CHEMBL2272222 CHEMBL2271844 CHEMBL2269530 
                            # CHEMBL2269868 CHEMBL2269481 CHEMBL513221 CHEMBL2271516 CHEMBL2288053 CHEMBL2204208 CHEMBL2
                            # 269716 CHEMBL2269524 CHEMBL2269480 CHEMBL2271875 CHEMBL2287825 CHEMBL2204210 CHEMBL2271891
                            #  CHEMBL2269519 CHEMBL2269720 CHEMBL2288062 CHEMBL2271533 CHEMBL2271854 CHEMBL2272223 CHEMB
                            # L2269764 CHEMBL2268974 CHEMBL2268967 CHEMBL2271512 CHEMBL1080648 CHEMBL2268698 CHEMBL22689
                            # 78 CHEMBL2269709 CHEMBL2269712 CHEMBL2269525 CHEMBL2271847 CHEMBL2271520 CHEMBL2268994 CHE
                            # MBL2287865 CHEMBL2271845 CHEMBL2271860 CHEMBL2287835 CHEMBL2271525 CHEMBL2205104 CHEMBL228
                            # 8033 CHEMBL2272229 CHEMBL2269711 CHEMBL2269704 CHEMBL2271871 CHEMBL2271866 CHEMBL2288057 C
                            # HEMBL2288058 CHEMBL2272227 CHEMBL2271886 CHEMBL2288060 CHEMBL2288063 CHEMBL2271904 CHEMBL2
                            # 288037 CHEMBL2271900 CHEMBL2271872 CHEMBL2269761 CHEMBL2271867 CHEMBL2268700 CHEMBL2268963
                            #  CHEMBL2268961 CHEMBL2288045 CHEMBL2287830 CHEMBL2271517 CHEMBL2272231 CHEMBL2268964 CHEMB
                            # L2288041 CHEMBL2287828 CHEMBL2271876 CHEMBL2269769 CHEMBL2268519 CHEMBL2271905 CHEMBL22689
                            # 79 CHEMBL2271846 CHEMBL2269520 CHEMBL2268984 CHEMBL2269777 CHEMBL2271843 CHEMBL2287864 CHE
                            # MBL2288064 CHEMBL2268970 CHEMBL2268953 CHEMBL2268986 CHEMBL2269483 CHEMBL2272230 CHEMBL226
                            # 8995 CHEMBL2271850 CHEMBL2268987 CHEMBL2269771 CHEMBL2271874 CHEMBL2268975 CHEMBL2271851 C
                            # HEMBL2288040 CHEMBL2271885 CHEMBL2268990 CHEMBL2272221 CHEMBL2269528 CHEMBL2269706 CHEMBL2
                            # 271903 CHEMBL2288046 CHEMBL2271894 CHEMBL2287866 CHEMBL2271856 CHEMBL2272224 CHEMBL2288034
                            #  CHEMBL2271896 CHEMBL2288055 CHEMBL2271534 CHEMBL2271873 CHEMBL2287858 CHEMBL2288039 CHEMB
                            # L2269717 CHEMBL2288052 CHEMBL2271892 CHEMBL2288044 CHEMBL2271539 CHEMBL2268954 CHEMBL22718
                            # 65 CHEMBL2271869 CHEMBL2269518 CHEMBL2271882 CHEMBL2269781 CHEMBL2287862 CHEMBL2269482 CHE
                            # MBL2269703 CHEMBL2268966 CHEMBL2288050 CHEMBL2268965 CHEMBL2271858 CHEMBL2271880 CHEMBL227
                            # 1842 CHEMBL2269779 CHEMBL2271888 CHEMBL2271870 CHEMBL2272218 CHEMBL2271528 CHEMBL2269762 C
                            # HEMBL2269708 CHEMBL2288036 CHEMBL2287860 CHEMBL2204207 CHEMBL2271883 CHEMBL2269766 CHEMBL2
                            # 269702 CHEMBL2271857 CHEMBL2271524 CHEMBL2288065 CHEMBL2271538 CHEMBL2269527 CHEMBL2287859
                            #  CHEMBL2268993 CHEMBL2271523 CHEMBL2269517 CHEMBL2268695 CHEMBL2268958 CHEMBL2268988 CHEMB
                            # L2269776 CHEMBL2269765 CHEMBL2272220 CHEMBL2271898 CHEMBL2269529 CHEMBL2271877 CHEMBL22718
                            # 52 CHEMBL2272228 CHEMBL2288043 CHEMBL2271536 CHEMBL2268959 CHEMBL2268976 CHEMBL2269773 CHE
                            # MBL2268962 CHEMBL2268693 CHEMBL2269475 CHEMBL2271853 CHEMBL1895913 CHEMBL2268957 CHEMBL227
                            # 2225 CHEMBL2269713 CHEMBL2271859 CHEMBL2268696 CHEMBL2285952' , 'CHEMBL473058 CHEMBL610647
                            #  CHEMBL610081 CHEMBL506180 CHEMBL11250 CHEMBL3126842 CHEMBL473885' , 'CHEMBL454279 CHEMBL4
                            # 92714 CHEMBL449892 CHEMBL493316 CHEMBL450552 CHEMBL443088 CHEMBL506684 CHEMBL522670 CHEMBL
                            # 197199 CHEMBL492713' , 'CHEMBL129 CHEMBL1090133 CHEMBL1091719 CHEMBL1098660 CHEMBL1096815 
                            # CHEMBL1090132 CHEMBL1098194 CHEMBL1097850 CHEMBL1098217 CHEMBL1097849 CHEMBL1096828 CHEMBL
                            # 1098218 CHEMBL1098549 CHEMBL52609 CHEMBL1098498' , 'CHEMBL4571835' , 'CHEMBL38380 CHEMBL17
                            # 21885 CHEMBL1822792 CHEMBL283120 CHEMBL3137336 CHEMBL1090090 CHEMBL2029988 CHEMBL1090479 C
                            # HEMBL221959 CHEMBL3120215 CHEMBL571948 CHEMBL3991931 CHEMBL3218575 CHEMBL2105717 CHEMBL399
                            # 1935 CHEMBL1908391 CHEMBL4084193 CHEMBL1738757 CHEMBL2103839 CHEMBL2103882 CHEMBL405130 CH
                            # EMBL3991927 CHEMBL2408045 CHEMBL270995 CHEMBL1289926 CHEMBL3544944 CHEMBL2079588 CHEMBL195
                            # 2329 CHEMBL2219422 CHEMBL1950289 CHEMBL3182444 CHEMBL1667969 CHEMBL3039513 CHEMBL1873475 C
                            # HEMBL1789941 CHEMBL1084546 CHEMBL1738797 CHEMBL189963 CHEMBL3545137 CHEMBL513909 CHEMBL200
                            # 1019 CHEMBL574737 CHEMBL2364611 CHEMBL1614713 CHEMBL411907 CHEMBL2336325 CHEMBL502835 CHEM
                            # BL1922094 CHEMBL535 CHEMBL1615025 CHEMBL521851 CHEMBL1946170 CHEMBL415049 CHEMBL2048872 CH
                            # EMBL223360 CHEMBL3991932 CHEMBL1229517 CHEMBL598797 CHEMBL3544964 CHEMBL3991928 CHEMBL1287
                            # 853 CHEMBL1801204 CHEMBL1236682 CHEMBL462018 CHEMBL553 CHEMBL253969 CHEMBL3188267 CHEMBL38
                            # 13873 CHEMBL3545307 CHEMBL495727 CHEMBL1908397 CHEMBL1614707 CHEMBL3544960 CHEMBL482967 CH
                            # EMBL3545328 CHEMBL1289601 CHEMBL1879463 CHEMBL101253 CHEMBL3544983 CHEMBL3989868 CHEMBL354
                            # 4966 CHEMBL2103842 CHEMBL601719 CHEMBL3545085 CHEMBL482767 CHEMBL1614710 CHEMBL3688339 CHE
                            # MBL2323775 CHEMBL2103840 CHEMBL603469 CHEMBL2041933 CHEMBL3109738 CHEMBL1230607 CHEMBL3218
                            # 576 CHEMBL3907479 CHEMBL2140408 CHEMBL1088752 CHEMBL607707 CHEMBL2105728 CHEMBL3186534 CHE
                            # MBL3353410 CHEMBL2087361 CHEMBL1173655 CHEMBL1983268 CHEMBL1094408 CHEMBL483321 CHEMBL5728
                            # 81 CHEMBL402548 CHEMBL3545396 CHEMBL2103875 CHEMBL558752 CHEMBL1234354 CHEMBL1236962 CHEMB
                            # L2396661 CHEMBL255863 CHEMBL1944698 CHEMBL180022 CHEMBL2103830 CHEMBL3545076 CHEMBL1614766
                            #  CHEMBL2403108 CHEMBL536151 CHEMBL1421 CHEMBL939 CHEMBL2035187 CHEMBL1231124 CHEMBL2180604
                            #  CHEMBL475251 CHEMBL3039525 CHEMBL2105759 CHEMBL3402762 CHEMBL1236107 CHEMBL1241855 CHEMBL
                            # 2107832 CHEMBL496102 CHEMBL230011 CHEMBL483158 CHEMBL2386889 CHEMBL1233528 CHEMBL571546 CH
                            # EMBL587723 CHEMBL3348923 CHEMBL1088751 CHEMBL3264002 CHEMBL91829 CHEMBL3128043 CHEMBL57544
                            # 8 CHEMBL3301607 CHEMBL1336 CHEMBL124660 CHEMBL2017974 CHEMBL3334567 CHEMBL2376648 CHEMBL48
                            # 8436 CHEMBL296468 CHEMBL3188551 CHEMBL3545157 CHEMBL3137331 CHEMBL572878 CHEMBL3545308 CHE
                            # MBL428690 CHEMBL1233300 CHEMBL3545215 CHEMBL300138 CHEMBL522892 CHEMBL3301610 CHEMBL514201
                            #  CHEMBL372764 CHEMBL1091644 CHEMBL24828 CHEMBL1079175 CHEMBL1078178 CHEMBL3184679 CHEMBL21
                            # 10732 CHEMBL3301612 CHEMBL3991933 CHEMBL14762 CHEMBL274654 CHEMBL206834 CHEMBL281948 CHEMB
                            # L288441 CHEMBL576982 CHEMBL403989 CHEMBL554 CHEMBL1976040 CHEMBL259084 CHEMBL507361 CHEMBL
                            # 1614725 CHEMBL2103851 CHEMBL1289494 CHEMBL2216870 CHEMBL2165191 CHEMBL31965 CHEMBL3187723 
                            # CHEMBL3991934 CHEMBL941 CHEMBL1614701 CHEMBL2146883 CHEMBL2028663 CHEMBL477772 CHEMBL19083
                            # 60 CHEMBL1645462 CHEMBL400402 CHEMBL3039517 CHEMBL3545083 CHEMBL3545360 CHEMBL3545110 CHEM
                            # BL2133806 CHEMBL254760 CHEMBL565612 CHEMBL491473 CHEMBL1201182 CHEMBL2325741 CHEMBL3218578
                            #  CHEMBL413 CHEMBL2220486 CHEMBL482968 CHEMBL3182621 CHEMBL3301622 CHEMBL1230609 CHEMBL5924
                            # 45 CHEMBL384304 CHEMBL3545154 CHEMBL445813 CHEMBL1908394 CHEMBL2138625 CHEMBL3991929 CHEMB
                            # L377300 CHEMBL215152' , 'CHEMBL4169587 CHEMBL4176713'
                            'count': 'NUMERIC',
                            # EXAMPLES:
                            # '36' , '41' , '156' , '300' , '7' , '10' , '15' , '1' , '229' , '2'
                        }
                    },
                    'related_documents': 
                    {
                        'properties': 
                        {
                            'all_chembl_ids': 'TEXT',
                            # EXAMPLES:
                            # 'CHEMBL1141090 CHEMBL1212919 CHEMBL2321737' , 'CHEMBL1137118 CHEMBL1629614' , 'CHEMBL39916
                            # 01 CHEMBL4350963 CHEMBL4325871 CHEMBL3627608 CHEMBL4364276 CHEMBL3745707' , 'CHEMBL3046648
                            #  CHEMBL3046126 CHEMBL3046607 CHEMBL3046200 CHEMBL3046635 CHEMBL3045604 CHEMBL3046317 CHEMB
                            # L3046654 CHEMBL3046383' , 'CHEMBL1125167 CHEMBL1136856 CHEMBL1148473 CHEMBL3124792' , 'CHE
                            # MBL1153397' , 'CHEMBL1158545' , 'CHEMBL4393722' , 'CHEMBL3991601' , 'CHEMBL4145653'
                            'count': 'NUMERIC',
                            # EXAMPLES:
                            # '3' , '2' , '6' , '9' , '4' , '1' , '1' , '1' , '1' , '1'
                        }
                    },
                    'related_tissues': 
                    {
                        'properties': 
                        {
                            'all_chembl_ids': 'TEXT',
                            # EXAMPLES:
                            # 'CHEMBL3638255 CHEMBL3638233 CHEMBL3638188' , 'CHEMBL3559722 CHEMBL3638241' , 'CHEMBL36381
                            # 78' , 'CHEMBL3638190' , 'CHEMBL3638187 CHEMBL3987561 CHEMBL3638188 CHEMBL3638244 CHEMBL363
                            # 8237' , 'CHEMBL3987572' , 'CHEMBL3638280 CHEMBL3638255 CHEMBL3638233 CHEMBL3638220 CHEMBL3
                            # 559724 CHEMBL3987979 CHEMBL3638273 CHEMBL3638188' , 'CHEMBL3833541' , 'CHEMBL3559722 CHEMB
                            # L3638230 CHEMBL3559723' , 'CHEMBL3638185'
                            'count': 'NUMERIC',
                            # EXAMPLES:
                            # '3' , '2' , '1' , '1' , '5' , '1' , '8' , '1' , '3' , '1'
                        }
                    },
                    'target_component': 
                    {
                        'properties': 
                        {
                            'accession': 'TEXT',
                            # EXAMPLES:
                            # 'P32927' , 'P31873' , 'P22301' , 'P48371' , 'O43653' , 'Q02768' , 'P15391' , 'P23510' , 'P
                            # 15248' , 'P43304'
                            'component_id': 'NUMERIC',
                            # EXAMPLES:
                            # '354' , '247' , '15074' , '7270' , '15115' , '67' , '9733' , '15054' , '15086' , '8364'
                            'component_type': 'TEXT',
                            # EXAMPLES:
                            # 'PROTEIN' , 'PROTEIN' , 'PROTEIN' , 'PROTEIN' , 'PROTEIN' , 'PROTEIN' , 'PROTEIN' , 'PROTE
                            # IN' , 'PROTEIN' , 'PROTEIN'
                            'description': 'TEXT',
                            # EXAMPLES:
                            # 'Cytokine receptor common subunit beta' , 'Large envelope protein' , 'Interleukin-10' , 'D
                            # NA gyrase subunit A' , 'Prostate stem cell antigen' , 'Cytochrome b' , 'B-lymphocyte antig
                            # en CD19' , 'Tumor necrosis factor ligand superfamily member 4' , 'Interleukin-9' , 'Glycer
                            # ol-3-phosphate dehydrogenase, mitochondrial'
                            'go_slims': 
                            {
                                'properties': 
                                {
                                    'go_id': 'TEXT',
                                    # EXAMPLES:
                                    # 'GO:0003674' , 'GO:0016020' , 'GO:0002376' , 'GO:0000166' , 'GO:0005102' , 'GO:000
                                    # 5575' , 'GO:0002376' , 'GO:0002376' , 'GO:0002376' , 'GO:0005575'
                                }
                            },
                            'organism': 'TEXT',
                            # EXAMPLES:
                            # 'Homo sapiens' , 'Hepatitis B virus adw2/Southern-Africa/Cai' , 'Homo sapiens' , 'Neisseri
                            # a gonorrhoeae' , 'Homo sapiens' , 'Plasmodium falciparum' , 'Homo sapiens' , 'Homo sapiens
                            # ' , 'Homo sapiens' , 'Homo sapiens'
                            'protein_classifications': 
                            {
                                'properties': 
                                {
                                    'protein_classification_id': 'NUMERIC',
                                    # EXAMPLES:
                                    # '11' , '9' , '3' , '644' , '601' , '8' , '9' , '3' , '3' , '10'
                                }
                            },
                            'sequence': 'TEXT',
                            # EXAMPLES:
                            # 'MVLAQGLLSMALLALCWERSLAGAEETIPLQTLRCYNDYTSHITCRWADTQDAQRLVNVTLIRRVNEDLLEPVSCDLSDDMPWSACPHP
                            # RCVPRRCVIPCQSFVVTDVDYFSFQPDRPLGTRLTVTLTQHVQPPEPRDLQISTDQDHFLLTWSVALGSPQSHWLSPGDLEFEVVYKRLQ
                            # DSWEDAAILLSNTSQATLGPEHLMPSSTYVARVRTRLAPGSRLSGRPSKWSPEVCWDSQPGDEAQPQNLECFFDGAAVLSCSWEVRKEVA
                            # SSVSFGLFYKPSPDAGEEECSPVLREGLGSLHTRHHCQIPVPDPATHGQYIVSVQPRRAEKHIKSSVNIQMAPPSLNVTKDGDSYSLRWE
                            # TMKMRYEHIDHTFEIQYRKDTATWKDSKTETLQNAHSMALPALEPSTRYWARVRVRTSRTGYNGIWSEWSEARSWDTESVLPMWVLALIV
                            # IFLTIAVLLALRFCGIYGYRLRRKWEEKIPNPSKSHLFQNGSAELWPPGSMSAFTSGSPPHQGPWGSRFPELEGVFPVGFGDSEVSPLTI
                            # EDPKHVCDPPSGPDTTPAASDLPTEQPPSPQPGPPAASHTPEKQASSFDFNGPYLGPPHSRSLPDILGQPEPPQEGGSQKSPPPGSLEYL
                            # CLPAGGQVQLVPLAQAMGPGQAVEVERRPSQGAAGSPSLESGGGPAPPALGPRVGGQDQKDSPVAIPMSSGDTEDPGVASGYVSSADLVF
                            # TPNSGASSVSLVPSLGLPSDQTPSLCPGLASGPPGAPGPVKSGFEGYVELPPIEGRSPRSPRNNPVPPEAKSPVLNPGERPADVSPTSPQ
                            # PEGLLVLQQVGDYCFLPGLGPGPLSLRSKPSSPGPGPEIKNLDQAFQVKKPPGQAVPQVPVIQLFKALKQQDYLSLPPWEVNKPGEVC' 
                            # , 'MGGWSAKPRKGMGTNLSVPNPLGFFPDHQLDPAFGANSNNPDWDFNPNKDHWPEANQVGVGAFGPGFTPPHGGLLGWSSQAQGTLHT
                            # VPAVPPPASTNRQTGRQPTPISPPLRDSHPQAMQWNSTAFQQALQDPRVRGLFFPAGGSSSGTVNPAPNIASHISSISSRTGDPALNMEN
                            # ITSGFLGPLLVLQAGFFLLTRILTIPQSLDSWWTSLNFLGGSPVCLGQNSQSPTSNHSPTSCPPICPGYRWMCLRRFIIFLFILLLCLIF
                            # LLVLLDYQGMLPVCPLIPGSTTTSTGPCKTCTTPAQGNSMFPSCCCTKPTDGNCTCIPIPSSWAFAKYLWEWASVRFSWLSLLVPFVQWF
                            # VGLSPTVWLSVIWMMWYWGPSLYNILSPFIPLLPIFFCLWVYI' , 'MHSSALLCCLVLLTGVRASPGQGTQSENSCTHFPGNLPNMLR
                            # DLRDAFSRVKTFFQMKDQLDNLLLKESLLEDFKGYLGCQALSEMIQFYLEEVMPQAENQDPDIKAHVNSLGENLKTLRLRLRRCHRFLPC
                            # ENKSKAVEQVKNAFNKLQEKGIYKAMSEFDIFINYIEAYMTMKIRN' , 'MTDATIRHDHKFALETLPVSLEDEMRKSYLDYAMSVIVG
                            # RALPDVRDGLKPVHRRVLYAMHELKNNWNAAYKKSARIVGDVIGKYHPHGDSAVYDTIVRMAQNFAMRYVLIDGQGNFGSVDGLAAAAMR
                            # YTEIRMAKISHEMLADIEEETVNFGPNYDGSEHEPLVLPTRFPTLLVNGSSGIAVGMATNIPPHNLTDTINACLRLLDEPKTEIDELIDI
                            # IQAPDFPTGATIYGLGGVREGYKTGRGRVVMRGKTHIEPIGKNGERERIVIDEIPYQVNKAKLVEKIGDLVREKTLEGISELRDESDKSG
                            # MRVVIELKRNENAEVVLNQLYKLTPLQDSFGINMVVLVDGQPRLLNLKQILSEFLRHRREVVTRRTLFRLKKARHEGHIAERKAVALSNI
                            # DEIIKLIKESPNAAEAKEKLLARPWASSLVEEMLTRSGLDLEMMRPEGLVANIGLKKQGYYLSEIQADAILRMSLRNLTGLDQKEIIESY
                            # KNLMGKIIDFVDILSKPERITQIIRDELEEIKTNYGDERRSEINPFGGDIADEDLIPQREMVVTLTHGGYIKTQPTTDYQAQRRGGRGKQ
                            # AAATKDEDFIETLFVANTHDYLMCFTNLGKCHWIKVYKLPEGGRNSRGRPINNVIQLEEGEKVSAILAVREFPEDQYVFFATAQGMVKKV
                            # QLSAFKNVRAQGIKAIALKEGDYLVGAAQTGGADDIMLFSNLGKAIRFNEYWEKSGNDEAEDADIETEISDDLEDETADNENTLPSGKNG
                            # VRPSGRGSGGLRGMRLPADGKIVSLITFAPETEESGLQVLTATANGYGKRTPIADYSRKNKGGQGSIAINTGERNGDLVAATLVGETDDL
                            # MLITSGGVLIRTKVEQIRETGRAAAGVKLINLDEGETLVSLERVAEDESELSGASVISNVTEPEAEN' , 'MAGLALQPGTALLCYSCK
                            # AQVSNEDCLQVENCTQLGEQCWTARIRAVGLLTVISKGCSLNCVDDSQDYYVGKKNITCCDTDLCNASGAHALQPAAAILALLPALGLLL
                            # WGPGQL' , 'MNFYSINLVKAHLINYPCPLNINFLWNYGFLLGIIFFIQIITGVFLASRYTPDVSYAYYSIQHILRELWSGWCFRYMHA
                            # TGASLVFLLTYLHILRGLNYSYMYLPLSWISGLILFMIFIVTAFVGYVLPWGQMSYWGATVITNLLSSIPVAVIWICGGYTVSDPTIKRF
                            # FVLHFILPFIGLCIVFIHIFFLHLHGSTNPLGYDTALKIPFYPNLLSLDVKGFNNVIILFLIQSLFGIIPLSHPDNAIVVNTYVTPSQIV
                            # PEWYFLPFYAMLKTVPSKPAGLVIVLLSLQLLFLLAEQRSLTTIIQFKMIFGARDYSVPIIWFMCAFYALLWIGCQLPQDIFILYGRLFI
                            # VLFFCSGLFVLVHYRRTHYDYSSQANI' , 'MPPPRLLFFLLFLTPMEVRPEEPLVVKVEEGDNAVLQCLKGTSDGPTQQLTWSRESPL
                            # KPFLKLSLGLPGLGIHMRPLAIWLFIFNVSQQMGGFYLCQPGPPSEKAWQPGWTVNVEGSGELFRWNVSDLGGLGCGLKNRSSEGPSSPS
                            # GKLMSPKLYVWAKDRPEIWEGEPPCLPPRDSLNQSLSQDLTMAPGSTLWLSCGVPPDSVSRGPLSWTHVHPKGPKSLLSLELKDDRPARD
                            # MWVMETGLLLPRATAQDAGKYYCHRGNLTMSFHLEITARPVLWHWLLRTGGWKVSAVTLAYLIFCLCSLVGILHLQRALVLRRKRKRMTD
                            # PTRRFFKVTPPPGSGPQNQYGNVLSLPTPTSGLGRAQRWAAGLGGTAPSYGNPSSDVQADGALGSRSPPGVGPEEEEGEGYEEPDSEEDS
                            # EFYENDSNLGQDQLSQDGSGYENPEDEPLGPEDEDSFSNAESYENEDEELTQPVARTMDFLSPHGSAWDPSREATSLGSQSYEDMRGILY
                            # AAPQLRSIRGQPGPNHEEDADSYENMDNPDGPDPAWGGGGRMGTWSTR' , 'MERVQPLEENVGNAARPRFERNKLLLVASVIQGLGLL
                            # LCFTYICLHFSALQVSHRYPRIQSIKVQFTEYKKEKGFILTSQKEDEIMKVQNNSVIINCDGFYLISLKGYFSQEVNISLHYQKDEEPLF
                            # QLKKVRSVNSLMVASLTYKDKVYLNVTTDNTSLDDFHVNGGELILIHQNPGEFCVL' , 'MLLAMVLTSALLLCSVAGQGCPTLAGILD
                            # INFLINKMQEDPASKCHCSANVTSCLCLGIPSDNCTRPCFSERLSQMTNTTMQTRYPLIFSRVKKSVEVLKNNKCPYFSCEQPCNQTTAG
                            # NALTFLKSLLEIFQKEKMRGMRGKI' , 'MAFQKAVKGTILVGGGALATVLGLSQFAHYRRKQMNLAYVKAADCISEPVNREPPSREAQ
                            # LLTLQNTSEFDILVIGGGATGSGCALDAVTRGLKTALVERDDFSSGTSSRSTKLIHGGVRYLQKAIMKLDIEQYRMVKEALHERANLLEI
                            # APHLSAPLPIMLPVYKWWQLPYYWVGIKLYDLVAGSNCLKSSYVLSKSRALEHFPMLQKDKLVGAIVYYDGQHNDARMNLAIALTAARYG
                            # AATANYMEVVSLLKKTDPQTGKVRVSGARCKDVLTGQEFDVRAKCVINATGPFTDSVRKMDDKDAAAICQPSAGVHIVMPGYYSPESMGL
                            # LDPATSDGRVIFFLPWQKMTIAGTTDTPTDVTHHPIPSEEDINFILNEVRNYLSCDVEVRRGDVLAAWSGIRPLVTDPKSADTQSISRNH
                            # VVDISESGLITIAGGKWTTYRSMAEDTINAAVKTHNLKAGPSRTVGLFLQGGKDWSPTLYIRLVQDYGLESEVAQHLAATYGDKAFEVAK
                            # MASVTGKRWPIVGVRLVSEFPYIEAEVKYGIKEYACTAVDMISRRTRLAFLNVQAAEEALPRIVELMGRELNWDDYKKQEQLETARKFLY
                            # YEMGYKSRSEQLTDRSEISLLPSDIDRYKKRFHKFDADQKGFITIVDVQRVLESINVQMDENTLHEILNEVDLNKNGQVELNEFLQLMSA
                            # IQKGRVSGSRLAILMKTAEENLDRRVPIPVDRSCGGL'
                            'target_component_synonyms': 
                            {
                                'properties': 
                                {
                                    'component_synonym': 'TEXT',
                                    # EXAMPLES:
                                    # 'CD_antigen=CD131' , 'Large envelope protein' , 'CSIF' , '5.6.2.2' , 'Prostate ste
                                    # m cell antigen' , 'COB' , 'B-lymphocyte antigen CD19' , 'CD_antigen=CD252' , 'Cyto
                                    # kine P40' , '1.1.5.3'
                                    'syn_type': 'TEXT',
                                    # EXAMPLES:
                                    # 'UNIPROT' , 'UNIPROT' , 'UNIPROT' , 'EC_NUMBER' , 'UNIPROT' , 'GENE_SYMBOL_OTHER' 
                                    # , 'UNIPROT' , 'UNIPROT' , 'UNIPROT' , 'EC_NUMBER'
                                }
                            },
                            'target_component_xrefs': 
                            {
                                'properties': 
                                {
                                    'xref_id': 'TEXT',
                                    # EXAMPLES:
                                    # 'CSF2RB' , 'GO:0016020' , 'ENSG00000136634' , 'GO:0005694' , 'ENSG00000167653' , '
                                    # GO:0005739' , 'ENSG00000177455' , 'ENSG00000117586' , 'ENSG00000145839' , 'ENSG000
                                    # 00115159'
                                    'xref_name': 'TEXT',
                                    # EXAMPLES:
                                    # 'Surfactant metabolism dysfunction, pulmonary, 5' , 'membrane' , 'extracellular re
                                    # gion' , 'chromosome' , 'extracellular region' , 'mitochondrion' , 'plasma membrane
                                    # ' , 'extracellular space' , 'extracellular region' , 'mitochondrion'
                                    'xref_src_db': 'TEXT',
                                    # EXAMPLES:
                                    # 'CGD' , 'GoComponent' , 'EnsemblGene' , 'GoComponent' , 'EnsemblGene' , 'GoCompone
                                    # nt' , 'EnsemblGene' , 'EnsemblGene' , 'EnsemblGene' , 'EnsemblGene'
                                    'xref_src_url': 'TEXT',
                                    # EXAMPLES:
                                    # 'http://research.nhgri.nih.gov/CGD/' , 'http://www.ebi.ac.uk/QuickGO/' , 'http://w
                                    # ww.ensembl.org/' , 'http://www.ebi.ac.uk/QuickGO/' , 'http://www.ensembl.org/' , '
                                    # http://www.ebi.ac.uk/QuickGO/' , 'http://www.ensembl.org/' , 'http://www.ensembl.o
                                    # rg/' , 'http://www.ensembl.org/' , 'http://www.ensembl.org/'
                                    'xref_url': 'TEXT',
                                    # EXAMPLES:
                                    # 'http://research.nhgri.nih.gov/CGD/view/?g=CSF2RB' , 'http://www.ebi.ac.uk/QuickGO
                                    # /GTerm?id=GO:0016020' , 'http://www.ensembl.org/Gene/Summary?g=ENSG00000136634' , 
                                    # 'http://www.ebi.ac.uk/QuickGO/GTerm?id=GO:0005694' , 'http://www.ensembl.org/Gene/
                                    # Summary?g=ENSG00000167653' , 'http://www.ebi.ac.uk/QuickGO/GTerm?id=GO:0005739' , 
                                    # 'http://www.ensembl.org/Gene/Summary?g=ENSG00000177455' , 'http://www.ensembl.org/
                                    # Gene/Summary?g=ENSG00000117586' , 'http://www.ensembl.org/Gene/Summary?g=ENSG00000
                                    # 145839' , 'http://www.ensembl.org/Gene/Summary?g=ENSG00000115159'
                                }
                            },
                            'targets': 
                            {
                                'properties': 
                                {
                                    'target_chembl_id': 'TEXT',
                                    # EXAMPLES:
                                    # 'CHEMBL2364169' , 'CHEMBL1928' , 'CHEMBL3712920' , 'CHEMBL2311244' , 'CHEMBL371296
                                    # 1' , 'CHEMBL1777' , 'CHEMBL3390821' , 'CHEMBL3712900' , 'CHEMBL3712932' , 'CHEMBL3
                                    # 391681'
                                }
                            },
                            'tax_id': 'NUMERIC',
                            # EXAMPLES:
                            # '9606' , '489449' , '9606' , '485' , '9606' , '5833' , '9606' , '9606' , '9606' , '9606'
                        }
                    }
                }
            },
            'cross_references': 
            {
                'properties': 
                {
                    'xref_id': 'TEXT',
                    # EXAMPLES:
                    # 'Q02768' , 'P95029' , 'Q25704' , 'O96760' , 'Q7L0J3' , 'Q14626' , 'P11836' , 'O75899' , 'Osteopont
                    # in' , 'P15291'
                    'xref_name': 'TEXT',
                    # EXAMPLES:
                    # 'CD20 antigen on B-cell non-Hodgkins lymphoma' , 'Urokinase-type plasminogen activator' , 'Galecti
                    # n-3' , 'Peripheral-type benzodiazepine receptor' , 'Albumin' , 'Gastrin-releasing peptide receptor
                    #  (GRP-R)' , 'Albumin' , 'Muscarinic M2 receptor' , 'Somatostatin receptor (sst3)' , 'Neuronal alph
                    # a-4/beta-2 nicotinic acetylcholine receptor (nAChR)'
                    'xref_src': 'TEXT',
                    # EXAMPLES:
                    # 'canSAR-Target' , 'canSAR-Target' , 'canSAR-Target' , 'canSAR-Target' , 'canSAR-Target' , 'canSAR-
                    # Target' , 'canSAR-Target' , 'canSAR-Target' , 'Wikipedia' , 'canSAR-Target'
                    'xref_src_url': 'TEXT',
                    # EXAMPLES:
                    # 'https://cansar.icr.ac.uk/cansar' , 'https://cansar.icr.ac.uk/cansar' , 'https://cansar.icr.ac.uk/
                    # cansar' , 'https://cansar.icr.ac.uk/cansar' , 'https://cansar.icr.ac.uk/cansar' , 'https://cansar.
                    # icr.ac.uk/cansar' , 'https://cansar.icr.ac.uk/cansar' , 'https://cansar.icr.ac.uk/cansar' , 'http:
                    # //www.wikipedia.org' , 'https://cansar.icr.ac.uk/cansar'
                    'xref_url': 'TEXT',
                    # EXAMPLES:
                    # 'https://cansar.icr.ac.uk/cansar/protein-targets/Q02768/' , 'https://cansar.icr.ac.uk/cansar/prote
                    # in-targets/P95029/' , 'https://cansar.icr.ac.uk/cansar/protein-targets/Q25704/' , 'https://cansar.
                    # icr.ac.uk/cansar/protein-targets/O96760/' , 'https://cansar.icr.ac.uk/cansar/protein-targets/Q7L0J
                    # 3/' , 'https://cansar.icr.ac.uk/cansar/protein-targets/Q14626/' , 'https://cansar.icr.ac.uk/cansar
                    # /protein-targets/P11836/' , 'https://cansar.icr.ac.uk/cansar/protein-targets/O75899/' , 'http://en
                    # .wikipedia.org/wiki/Osteopontin' , 'https://cansar.icr.ac.uk/cansar/protein-targets/P15291/'
                }
            },
            'organism': 'TEXT',
            # EXAMPLES:
            # 'Homo sapiens' , 'Hepatitis B virus adw2/Southern-Africa/Cai' , 'Homo sapiens' , 'Neisseria gonorrhoeae' ,
            #  'Homo sapiens' , 'Plasmodium falciparum' , 'Homo sapiens' , 'Homo sapiens' , 'Homo sapiens' , 'Homo sapie
            # ns'
            'pref_name': 'TEXT',
            # EXAMPLES:
            # 'Granulocyte-macrophage colony-stimulating factor receptor' , 'Major surface antigen' , 'Interleukin-10' ,
            #  'DNA gyrase' , 'Prostate stem cell antigen' , 'Cytochrome b' , 'B-lymphocyte antigen CD19' , 'Tumor necro
            # sis factor ligand superfamily member 4' , 'Interleukin-9' , 'Mitochondrial glycerol-3-phosphate dehydrogen
            # ase'
            'species_group_flag': 'BOOLEAN',
            # EXAMPLES:
            # 'False' , 'False' , 'False' , 'False' , 'False' , 'False' , 'False' , 'False' , 'False' , 'False'
            'target_chembl_id': 'TEXT',
            # EXAMPLES:
            # 'CHEMBL2364169' , 'CHEMBL1928' , 'CHEMBL3712920' , 'CHEMBL2311244' , 'CHEMBL3712961' , 'CHEMBL1777' , 'CHE
            # MBL3390821' , 'CHEMBL3712900' , 'CHEMBL3712932' , 'CHEMBL3391681'
            'target_components': 
            {
                'properties': 
                {
                    'accession': 'TEXT',
                    # EXAMPLES:
                    # 'P15509' , 'P31873' , 'P22301' , 'P48371' , 'O43653' , 'Q02768' , 'P15391' , 'P23510' , 'P15248' ,
                    #  'P43304'
                    'component_description': 'TEXT',
                    # EXAMPLES:
                    # 'Granulocyte-macrophage colony-stimulating factor receptor subunit alpha' , 'Large envelope protei
                    # n' , 'Interleukin-10' , 'DNA gyrase subunit A' , 'Prostate stem cell antigen' , 'Cytochrome b' , '
                    # B-lymphocyte antigen CD19' , 'Tumor necrosis factor ligand superfamily member 4' , 'Interleukin-9'
                    #  , 'Glycerol-3-phosphate dehydrogenase, mitochondrial'
                    'component_id': 'NUMERIC',
                    # EXAMPLES:
                    # '353' , '247' , '15074' , '7270' , '15115' , '67' , '9733' , '15054' , '15086' , '8364'
                    'component_type': 'TEXT',
                    # EXAMPLES:
                    # 'PROTEIN' , 'PROTEIN' , 'PROTEIN' , 'PROTEIN' , 'PROTEIN' , 'PROTEIN' , 'PROTEIN' , 'PROTEIN' , 'P
                    # ROTEIN' , 'PROTEIN'
                    'relationship': 'TEXT',
                    # EXAMPLES:
                    # 'PROTEIN SUBUNIT' , 'SINGLE PROTEIN' , 'SINGLE PROTEIN' , 'PROTEIN SUBUNIT' , 'SINGLE PROTEIN' , '
                    # SINGLE PROTEIN' , 'SINGLE PROTEIN' , 'SINGLE PROTEIN' , 'SINGLE PROTEIN' , 'SINGLE PROTEIN'
                    'target_component_synonyms': 
                    {
                        'properties': 
                        {
                            'component_synonym': 'TEXT',
                            # EXAMPLES:
                            # 'CD_antigen=CD116' , 'Large envelope protein' , 'CSIF' , '5.6.2.2' , 'Prostate stem cell a
                            # ntigen' , 'COB' , 'B-lymphocyte antigen CD19' , 'CD_antigen=CD252' , 'Cytokine P40' , '1.1
                            # .5.3'
                            'syn_type': 'TEXT',
                            # EXAMPLES:
                            # 'UNIPROT' , 'UNIPROT' , 'UNIPROT' , 'EC_NUMBER' , 'UNIPROT' , 'GENE_SYMBOL_OTHER' , 'UNIPR
                            # OT' , 'UNIPROT' , 'UNIPROT' , 'EC_NUMBER'
                        }
                    },
                    'target_component_xrefs': 
                    {
                        'properties': 
                        {
                            'xref_id': 'TEXT',
                            # EXAMPLES:
                            # 'CSF2RA' , 'GO:0016020' , 'ENSG00000136634' , 'GO:0005694' , 'ENSG00000167653' , 'GO:00057
                            # 39' , 'ENSG00000177455' , 'ENSG00000117586' , 'ENSG00000145839' , 'ENSG00000115159'
                            'xref_name': 'TEXT',
                            # EXAMPLES:
                            # 'Surfactant metabolism dysfunction, pulmonary, 4' , 'membrane' , 'extracellular region' , 
                            # 'chromosome' , 'extracellular region' , 'mitochondrion' , 'plasma membrane' , 'extracellul
                            # ar space' , 'extracellular region' , 'mitochondrion'
                            'xref_src_db': 'TEXT',
                            # EXAMPLES:
                            # 'CGD' , 'GoComponent' , 'EnsemblGene' , 'GoComponent' , 'EnsemblGene' , 'GoComponent' , 'E
                            # nsemblGene' , 'EnsemblGene' , 'EnsemblGene' , 'EnsemblGene'
                            'xref_src_url': 'TEXT',
                            # EXAMPLES:
                            # 'http://research.nhgri.nih.gov/CGD/' , 'http://www.ebi.ac.uk/QuickGO/' , 'http://www.ensem
                            # bl.org/' , 'http://www.ebi.ac.uk/QuickGO/' , 'http://www.ensembl.org/' , 'http://www.ebi.a
                            # c.uk/QuickGO/' , 'http://www.ensembl.org/' , 'http://www.ensembl.org/' , 'http://www.ensem
                            # bl.org/' , 'http://www.ensembl.org/'
                            'xref_url': 'TEXT',
                            # EXAMPLES:
                            # 'http://research.nhgri.nih.gov/CGD/view/?g=CSF2RA' , 'http://www.ebi.ac.uk/QuickGO/GTerm?i
                            # d=GO:0016020' , 'http://www.ensembl.org/Gene/Summary?g=ENSG00000136634' , 'http://www.ebi.
                            # ac.uk/QuickGO/GTerm?id=GO:0005694' , 'http://www.ensembl.org/Gene/Summary?g=ENSG0000016765
                            # 3' , 'http://www.ebi.ac.uk/QuickGO/GTerm?id=GO:0005739' , 'http://www.ensembl.org/Gene/Sum
                            # mary?g=ENSG00000177455' , 'http://www.ensembl.org/Gene/Summary?g=ENSG00000117586' , 'http:
                            # //www.ensembl.org/Gene/Summary?g=ENSG00000145839' , 'http://www.ensembl.org/Gene/Summary?g
                            # =ENSG00000115159'
                        }
                    }
                }
            },
            'target_type': 'TEXT',
            # EXAMPLES:
            # 'PROTEIN COMPLEX' , 'SINGLE PROTEIN' , 'SINGLE PROTEIN' , 'PROTEIN COMPLEX' , 'SINGLE PROTEIN' , 'SINGLE P
            # ROTEIN' , 'SINGLE PROTEIN' , 'SINGLE PROTEIN' , 'SINGLE PROTEIN' , 'SINGLE PROTEIN'
            'tax_id': 'NUMERIC',
            # EXAMPLES:
            # '9606' , '489449' , '9606' , '485' , '9606' , '5833' , '9606' , '9606' , '9606' , '9606'
        }
    }
