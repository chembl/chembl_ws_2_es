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
                    # '{'input': 'Rational drug design based synthesis of novel arylquinolines as anti-tuberculosis agen
                    # ts.', 'weight': 100}' , '{'input': '25442308', 'weight': 10}' , '{'input': '2015', 'weight': 1}' ,
                    #  '{'input': '2015', 'weight': 1}' , '{'input': '2014', 'weight': 1}' , '{'input': '2015', 'weight'
                    # : 1}' , '{'input': '2015', 'weight': 1}' , '{'input': '10.1021/acs.jmedchem.5b01664', 'weight': 10
                    # }' , '{'input': 'CHEMBL3751780', 'weight': 10}' , '{'input': 'CHEMBL3351374', 'weight': 10}'
                }
            },
            'abstract': 'TEXT',
            # EXAMPLES:
            # '' , '' , '' , '' , '' , '' , '' , '' , '' , ''
            'authors': 'TEXT',
            # EXAMPLES:
            # 'Jain PP, Degani MS, Raju A, Ray M, Rajan MG.' , 'Naqvi A, Malasoni R, Srivastava A, Pandey RR, Dwivedi AK
            # .' , 'Yang S, K R J, Lim S, Choi TG, Kim JH, Akter S, Jang M, Ahn HJ, Kim HY, Windisch MP, Khadka DB, Zhao
            #  C, Jin Y, Kang I, Ha J, Oh BC, Kim M, Kim SS, Cho WJ.' , 'Abdel-Aziz AA, El-Azab AS, Ceruso M, Supuran CT
            # .' , 'Schembri LS, Stoddart LA, Briddon SJ, Kellam B, Canals M, Graham B, Scammells PJ.' , 'Jain P, Wadhwa
            #  PK, Rohilla S, Jadhav HR.' , 'Bereczki I, Kicsák M, Dobray L, Borbás A, Batta G, Kéki S, Nikodém ÉN, Osto
            # rházi E, Rozgonyi F, Vanderlinden E, Naesens L, Herczegh P.' , 'Galuppo M, Iori R, De Nicola GR, Bramanti 
            # P, Mazzon E.' , 'Chen J, Duan W, Bai R, Yao H, Shang J, Xu J.' , 'Barteselli A, Casagrande M, Basilico N, 
            # Parapini S, Rusconi CM, Tonelli M, Boido V, Taramelli D, Sparatore F, Sparatore A.'
            'doc_type': 'TEXT',
            # EXAMPLES:
            # 'PUBLICATION' , 'PUBLICATION' , 'PATENT' , 'PUBLICATION' , 'PUBLICATION' , 'PATENT' , 'PATENT' , 'PUBLICAT
            # ION' , 'PUBLICATION' , 'PUBLICATION'
            'document_chembl_id': 'TEXT',
            # EXAMPLES:
            # 'CHEMBL2440057' , 'CHEMBL3352563' , 'CHEMBL3714736' , 'CHEMBL3751796' , 'CHEMBL3351996' , 'CHEMBL3714747' 
            # , 'CHEMBL3638771' , 'CHEMBL3745681' , 'CHEMBL3751780' , 'CHEMBL3351374'
            'doi': 'TEXT',
            # EXAMPLES:
            # '10.1016/j.bmcl.2013.09.027' , '10.1016/j.bmcl.2014.09.080' , '10.1021/acs.jmedchem.5b01064' , '10.1016/j.
            # bmcl.2014.09.076' , '10.1021/acs.jmedchem.5b01664' , '10.1016/j.bmcl.2015.11.044' , '10.1016/j.bmcl.2014.0
            # 6.018' , '10.1016/j.bmc.2013.05.065' , '10.1016/j.bmcl.2014.05.078' , '10.1016/j.bmc.2014.11.028'
            'first_page': 'NUMERIC',
            # EXAMPLES:
            # '6097' , '5181' , '9546' , '5185' , '9754' , '33' , '3251' , '5532' , '3407' , '55'
            'issue': 'NUMERIC',
            # EXAMPLES:
            # '22' , '22' , '24' , '22' , '24' , '1' , '15' , '17' , '15' , '1'
            'journal': 'TEXT',
            # EXAMPLES:
            # 'Bioorg. Med. Chem. Lett.' , 'Bioorg. Med. Chem. Lett.' , 'J. Med. Chem.' , 'Bioorg. Med. Chem. Lett.' , '
            # J. Med. Chem.' , 'Bioorg. Med. Chem. Lett.' , 'Bioorg. Med. Chem. Lett.' , 'Bioorg. Med. Chem.' , 'Bioorg.
            #  Med. Chem. Lett.' , 'Bioorg. Med. Chem.'
            'last_page': 'NUMERIC',
            # EXAMPLES:
            # '6105' , '5184' , '9561' , '5189' , '9767' , '37' , '3254' , '5547' , '3411' , '65'
            'patent_id': 'TEXT',
            # EXAMPLES:
            # 'US-20150031679-A1' , 'US-20150094297-A1' , 'US-9115126-B2' , 'US-9045524-B2' , 'US-9051240-B2' , 'US-9056
            # 843-B2' , 'US-9056857-B2' , 'US-9056863-B2' , 'US-9056865-B2' , 'US-9061023-B2'
            'pubmed_id': 'NUMERIC',
            # EXAMPLES:
            # '24095091' , '25442308' , '26613291' , '25442309' , '26632862' , '26614409' , '24974341' , '23810671' , '2
            # 4928401' , '25497962'
            'src_id': 'NUMERIC',
            # EXAMPLES:
            # '1' , '1' , '38' , '1' , '1' , '38' , '37' , '1' , '1' , '1'
            'title': 'TEXT',
            # EXAMPLES:
            # 'Rational drug design based synthesis of novel arylquinolines as anti-tuberculosis agents.' , 'Design, syn
            # thesis and molecular docking of substituted 3-hydrazinyl-3-oxo-propanamides as anti-tubercular agents.' , 
            # 'Heterocyclic compounds for the inhibition of PASK' , 'Structure-Based Discovery of Novel Cyclophilin A In
            # hibitors for the Treatment of Hepatitis C Virus Infections.' , 'Carbonic anhydrase inhibitory activity of 
            # sulfonamides and carboxylic acids incorporating cyclic imide scaffolds.' , 'Imidazothiadiazole and imidazo
            # pyrazine derivatives as protease activated receptor 4 (par4) inhibitors for treating platelet aggregation'
            #  , '1H-[1,2,3]triazolo[4,5-c]pyridine-4-carbonitrile derivatives' , 'Synthesis, Biological Evaluation, and
            #  Utility of Fluorescent Ligands Targeting the μ-Opioid Receptor.' , 'Rational design, synthesis and in vit
            # ro evaluation of allylidene hydrazinecarboximidamide derivatives as BACE-1 inhibitors.' , 'Semisynthetic t
            # eicoplanin derivatives as new influenza virus binding inhibitors: synthesis and antiviral studies.'
            'volume': 'NUMERIC',
            # EXAMPLES:
            # '23' , '24' , '58' , '24' , '58' , '26' , '24' , '21' , '24' , '23'
            'year': 'NUMERIC',
            # EXAMPLES:
            # '2013' , '2014' , '2015' , '2015' , '2014' , '2015' , '2015' , '2015' , '2016' , '2014'
        }
    }
