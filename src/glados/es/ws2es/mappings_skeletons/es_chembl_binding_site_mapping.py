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
            'site_components': 
            {
                'properties': 
                {
                    'component_id': 'NUMERIC',
                    # EXAMPLES:
                    # '4262' , '47' , '5624' , '47' , '47' , '18307' , '41' , '17307' , '5624' , '47'
                    'domain': 
                    {
                        'properties': 
                        {
                            'domain_id': 'NUMERIC',
                            # EXAMPLES:
                            # '2640' , '3658' , '2712' , '3658' , '3658' , '2683' , '3658' , '3173' , '2712' , '3658'
                            'domain_name': 'TEXT',
                            # EXAMPLES:
                            # 'SH2' , 'Neur_chan_LBD' , 'Hormone_recep' , 'Neur_chan_LBD' , 'Neur_chan_LBD' , 'Pkinase' 
                            # , 'Neur_chan_LBD' , 'Na_H_Exchanger' , 'Hormone_recep' , 'Neur_chan_LBD'
                            'domain_type': 'TEXT',
                            # EXAMPLES:
                            # 'Pfam-A' , 'Pfam-A' , 'Pfam-A' , 'Pfam-A' , 'Pfam-A' , 'Pfam-A' , 'Pfam-A' , 'Pfam-A' , 'P
                            # fam-A' , 'Pfam-A'
                            'source_domain_id': 'TEXT',
                            # EXAMPLES:
                            # 'PF00017' , 'PF02931' , 'PF00104' , 'PF02931' , 'PF02931' , 'PF00069' , 'PF02931' , 'PF009
                            # 99' , 'PF00104' , 'PF02931'
                        }
                    },
                    'sitecomp_id': 'NUMERIC',
                    # EXAMPLES:
                    # '3085' , '29571' , '8963' , '33167' , '32581' , '21264' , '20208' , '12880' , '4345' , '33166'
                }
            },
            'site_id': 'NUMERIC',
            # EXAMPLES:
            # '3012' , '17416' , '3836' , '17675' , '18149' , '13430' , '12417' , '8218' , '3838' , '17676'
            'site_name': 'TEXT',
            # EXAMPLES:
            # 'Signal transducer and activator of transcription 5B, SH2 domain' , 'Gamma-aminobutyric acid receptor subu
            # nit alpha-2/beta-2, Neur_chan_LBD domain' , 'COUP transcription factor 2, Hormone_recep domain' , 'GABA A 
            # receptor alpha-2/beta-2/gamma-2, Neur_chan_LBD domain' , 'GABA A receptor alpha-4/beta-3/gamma-2, Neur_cha
            # n_LBD domain' , 'Calcium/calmodulin-dependent protein kinase kinase 2, Pkinase domain' , 'GABA A receptor 
            # alpha-6/beta-2/gamma-2, Neur_chan_LBD domain' , 'Sodium/hydrogen exchanger 2, Na_H_Exchanger domain' , 'CO
            # UP transcription factor 2, Hormone_recep domain' , 'GABA-A receptor; agonist GABA site, Neur_chan_LBD doma
            # in'
        }
    }
