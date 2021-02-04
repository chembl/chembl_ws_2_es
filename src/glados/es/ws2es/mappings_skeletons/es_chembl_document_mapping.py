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
                    # '{'input': 'CHEMBL1158643', 'weight': 10}' , '{'input': 'Clader JW.', 'weight': 100}' , '{'input':
                    #  '14695814', 'weight': 10}' , '{'input': '10.1021/jm030287l', 'weight': 10}' , '{'input': "The hem
                    # oglobin-degrading aspartic proteases plasmepsin I (Plm I) and plasmepsin II (Plm II) of the malari
                    # a parasite Plasmodium falciparum have lately emerged as putative drug targets. A series of C(2)-sy
                    # mmetric compounds encompassing the 1,2-dihydroxyethylene scaffold and a variety of elongated P1/P1
                    # ' side chains were synthesized via microwave-assisted palladium-catalyzed coupling reactions. Bind
                    # ing affinity calculations with the linear interaction energy method and molecular dynamics simulat
                    # ions reproduced the experimental binding data obtained in a Plm II assay with very good accuracy. 
                    # Bioactive conformations of the elongated P1/P1' chains were predicted and agreed essentially with 
                    # a recent X-ray structure. The compounds exhibited picomolar to nanomolar inhibition constants for 
                    # the plasmepsins and no measurable affinity to the human enzyme cathepsin D. Some of the compounds 
                    # also demonstrated significant inhibition of parasite growth in cell culture. To the best of our kn
                    # owledge, these plasmepsin inhibitors represent the most selective reported to date and constitute 
                    # promising lead compounds for further optimization.", 'weight': 60}' , '{'input': 'Goudreau N, Came
                    # ron DR, Bonneau P, Gorys V, Plouffe C, Poirier M, Lamarre D, Llinas-Brunet M.', 'weight': 100}' , 
                    # '{'input': 'Three-dimensional quantitative structure-activity relationship modeling of cocaine bin
                    # ding by a novel human monoclonal antibody.', 'weight': 100}' , '{'input': '2004', 'weight': 1}' , 
                    # '{'input': 'Recently we reported the pharmacological characterization of the 9,10-dihydropyrrolo[1
                    # ,3]benzothiazepine derivative (S)-(+)-8 as a novel atypical antipsychotic agent. This compound had
                    #  an optimum pK(i) 5-HT(2A)/D(2) ratio of 1.21 (pK(i) 5-HT(2A) = 8.83; pK(i) D(2) = 7.79). The lowe
                    # r D(2) receptor affinity of (S)-(+)-8 compared to its enantiomer was explained by the difficulty i
                    # n reaching the conformation required to optimally fulfill the D(2) pharmacophore. With the aim of 
                    # finding novel atypical antipsychotics we further investigated the core structure of (S)-(+)-8, syn
                    # thesizing analogues with specific substituents; the structure-activity relationship (SAR) study wa
                    # s also expanded with the design and synthesis of other analogues characterized by a pyrrolo[2,1-b]
                    # [1,3]benzothiazepine skeleton, substituted on the benzo-fused ring or on the pyrrole system. On th
                    # e 9,10-dihydro analogues the substituents introduced on the pyrrole ring were detrimental to affin
                    # ity for dopamine and for 5-HT(2A) receptors, but the introduction of a double bond at C-9/10 on th
                    # e structure of (S)-(+)-8 led to a potent D(2)/5-HT(2A) receptor ligand with a typical binding prof
                    # ile (9f, pK(i) 5-HT(2A)/D(2) ratio of 1.01, log Y = 8.43). Then, to reduce D(2) receptor affinity 
                    # and restore atypicality on unsaturated analogues, we exploited the effect of specific substitution
                    # s on the tricyclic system of 9f. Through a molecular modeling approach we generated a novel series
                    #  of potential atypical antipsychotic agents, with optimized 5HT(2A)/D(2) receptor affinity ratios 
                    # and that were easier to synthesize and purify than the reference compound (S)-(+)-8. A number of S
                    # AR trends were identified, and among the analogues synthesized and tested in binding assays, 9d an
                    # d 9m were identified as the most interesting, giving atypical log Y scores respectively 4.98 and 3
                    # .18 (pK(i) 5-HT(2A)/D(2) ratios of 1.20 and 1.30, respectively). They had a multireceptor affinity
                    #  profile and could be promising atypical agents. Compound 9d, whose synthesis is easier and whose 
                    # binding profile is atypical (log Y score similar to that of olanzapine, 3.89), was selected for fu
                    # rther biological investigation. Pharmacological and biochemical studies confirmed an atypical anti
                    # psychotic profile in vivo. The compound was active on conditioned avoidance response at 1.1 mg/kg,
                    #  a dose 100-times lower than that required to cause catalepsy (ED(50) >90 mg/kg), it induced a neg
                    # ligible increase of prolactin serum levels after single and multiple doses, and antagonized the co
                    # gnitive impairment induced by phencyclidine. In conclusion, the pharmacological profile of 9d prov
                    # ed better than clozapine and olanzapine, making this compound a potential clinical candidate.', 'w
                    # eight': 60}' , '{'input': '2004', 'weight': 1}'
                }
            },
            'abstract': 'TEXT',
            # EXAMPLES:
            # '' , '' , 'A number of substituted piperazinyl oxazolidinone derivatives have been synthesized and their a
            # ntibacterial activities were evaluated by MIC determination. A systematic SAR was carried out to get highl
            # y potent oxazolidinone derivatives.' , '' , '' , '' , '' , '' , '' , ''
            'authors': 'TEXT',
            # EXAMPLES:
            # 'Clader JW.' , 'Daranas AH, Fernández JJ, Morales EQ, Norte M, Gavín JA.' , 'Cho H, Murakami K, Nakanishi 
            # H, Fujisawa A, Isoshima H, Niwa M, Hayakawa K, Hase Y, Uchida I, Watanabe H, Wakitani K, Aisaka K.' , 'Ers
            # mark K, Feierberg I, Bjelic S, Hamelink E, Hackett F, Blackman MJ, Hultén J, Samuelsson B, Aqvist J, Hallb
            # erg A.' , 'Goudreau N, Cameron DR, Bonneau P, Gorys V, Plouffe C, Poirier M, Lamarre D, Llinas-Brunet M.' 
            # , 'Paula S, Tabet MR, Farr CD, Norman AB, Ball WJ.' , 'Summa V, Petrocchi A, Pace P, Matassa VG, De France
            # sco R, Altamura S, Tomei L, Koch U, Neuner P.' , 'Faucher AM, White PW, Brochu C, Grand-Maître C, Rancourt
            #  J, Fazal G.' , 'Rybczynski PJ, Zeck RE, Dudash J, Combs DW, Burris TP, Yang M, Osborne MC, Chen X, Demare
            # st KT.' , 'Stoyanovsky DA, Schor NF, Nylander KD, Salama G.'
            'doc_type': 'TEXT',
            # EXAMPLES:
            # 'DATASET' , 'PUBLICATION' , 'PUBLICATION' , 'PUBLICATION' , 'PUBLICATION' , 'PUBLICATION' , 'PUBLICATION' 
            # , 'PUBLICATION' , 'PUBLICATION' , 'PUBLICATION'
            'document_chembl_id': 'TEXT',
            # EXAMPLES:
            # 'CHEMBL1158643' , 'CHEMBL1139451' , 'CHEMBL1148466' , 'CHEMBL1139452' , 'CHEMBL1139453' , 'CHEMBL1139454' 
            # , 'CHEMBL1139455' , 'CHEMBL1139456' , 'CHEMBL1139457' , 'CHEMBL1139458'
            'doi': 'TEXT',
            # EXAMPLES:
            # '10.1021/jm030283g' , '10.1021/jm034189b' , '10.1021/jm030287l' , '10.1021/jm030933g' , '10.1021/jm0303002
            # ' , '10.1021/jm030351z' , '10.1021/jm0342109' , '10.1021/jm0309811' , '10.1021/jm034206x' , '10.1021/jm030
            # 1888'
            'first_page': 'NUMERIC',
            # EXAMPLES:
            # '1' , '10' , '101' , '110' , '123' , '133' , '14' , '143' , '18' , '196'
            'issue': 'NUMERIC',
            # EXAMPLES:
            # '1' , '1' , '1' , '1' , '1' , '1' , '1' , '1' , '1' , '1'
            'journal': 'TEXT',
            # EXAMPLES:
            # 'J. Med. Chem.' , 'J. Med. Chem.' , 'J. Med. Chem.' , 'J. Med. Chem.' , 'J. Med. Chem.' , 'J. Med. Chem.' 
            # , 'J. Med. Chem.' , 'J. Med. Chem.' , 'J. Med. Chem.' , 'J. Med. Chem.'
            'last_page': 'NUMERIC',
            # EXAMPLES:
            # '9' , '13' , '109' , '122' , '132' , '142' , '17' , '157' , '21' , '209'
            'patent_id': 'TEXT',
            # EXAMPLES:
            # 'US-9067935-B2' , 'US-9073853-B2' , 'US-9120761-B2' , 'US-9073870-B2' , 'US-9073876-B2' , 'WO-2012044993-A
            # 1' , 'US-9073911-B2' , 'US-9073925-B2' , 'WO-2013163244-A1' , 'US-9079834-B2'
            'pubmed_id': 'NUMERIC',
            # EXAMPLES:
            # '14695813' , '14695814' , '14695824' , '14695825' , '14695826' , '14695827' , '14695815' , '14695828' , '1
            # 4695816' , '14695833'
            'src_id': 'NUMERIC',
            # EXAMPLES:
            # '0' , '1' , '1' , '1' , '1' , '1' , '1' , '1' , '1' , '1'
            'title': 'TEXT',
            # EXAMPLES:
            # 'Unpublished dataset' , 'The discovery of ezetimibe: a view from outside the receptor.' , 'Self-associatio
            # n of okadaic acid upon complexation with potassium ion.' , 'Synthesis and structure-activity relationships
            #  of 5,6,7,8-tetrahydro-4H-thieno[3,2-b]azepine derivatives: novel arginine vasopressin antagonists.' , 'Po
            # tent inhibitors of the Plasmodium falciparum enzymes plasmepsin I and II devoid of cathepsin D inhibitory 
            # activity.' , 'NMR structural characterization of peptide inhibitors bound to the Hepatitis C virus NS3 pro
            # tease: design of a new P2 substituent.' , 'Three-dimensional quantitative structure-activity relationship 
            # modeling of cocaine binding by a novel human monoclonal antibody.' , 'Discovery of alpha,gamma-diketo acid
            # s as potent selective and reversible inhibitors of hepatitis C virus NS5b RNA-dependent RNA polymerase.' ,
            #  'Pyrrolo[1,3]benzothiazepine-based serotonin and dopamine receptor antagonists. Molecular modeling, furth
            # er structure-activity relationship studies, and identification of novel atypical antipsychotic agents.' , 
            # 'Discovery of small-molecule inhibitors of the ATPase activity of human papillomavirus E1 helicase.'
            'volume': 'NUMERIC',
            # EXAMPLES:
            # '47' , '47' , '47' , '47' , '47' , '47' , '47' , '47' , '47' , '47'
            'year': 'NUMERIC',
            # EXAMPLES:
            # '2004' , '2004' , '2004' , '2004' , '2004' , '2004' , '2004' , '2004' , '2004' , '2004'
        }
    }
