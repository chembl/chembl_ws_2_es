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
                    # '26' , '8527' , '8527' , '8527' , '8527' , '8527' , '8527' , '8527' , '8527' , '8527'
                    'domain': 
                    {
                        'properties': 
                        {
                            'domain_id': 'NUMERIC',
                            # EXAMPLES:
                            # '3658' , '3119' , '3119' , '3119' , '3119' , '3119' , '3119' , '3119' , '3119' , '3119'
                            'domain_name': 'TEXT',
                            # EXAMPLES:
                            # 'Neur_chan_LBD' , 'ASC' , 'ASC' , 'ASC' , 'ASC' , 'ASC' , 'ASC' , 'ASC' , 'ASC' , 'ASC'
                            'domain_type': 'TEXT',
                            # EXAMPLES:
                            # 'Pfam-A' , 'Pfam-A' , 'Pfam-A' , 'Pfam-A' , 'Pfam-A' , 'Pfam-A' , 'Pfam-A' , 'Pfam-A' , 'P
                            # fam-A' , 'Pfam-A'
                            'source_domain_id': 'TEXT',
                            # EXAMPLES:
                            # 'PF02931' , 'PF00858' , 'PF00858' , 'PF00858' , 'PF00858' , 'PF00858' , 'PF00858' , 'PF008
                            # 58' , 'PF00858' , 'PF00858'
                        }
                    },
                    'sitecomp_id': 'NUMERIC',
                    # EXAMPLES:
                    # '7067' , '28309' , '30253' , '25293' , '23850' , '33439' , '26112' , '30478' , '24026' , '33842'
                }
            },
            'site_id': 'NUMERIC',
            # EXAMPLES:
            # '6275' , '21851' , '21852' , '21853' , '21854' , '21855' , '21856' , '21857' , '21858' , '21859'
            'site_name': 'TEXT',
            # EXAMPLES:
            # 'Nicotinic acetylcholine receptor alpha2/beta4, Neur_chan_LBD domain' , 'Acid-sensing ion channel 2, ASC d
            # omain' , 'Acid-sensing ion channel 1/2, ASC domain' , 'Acid-sensing ion channel 2, ASC domain' , 'Acid-sen
            # sing ion channel 1/2, ASC domain' , 'Acid-sensing ion channel 2, ASC domain' , 'Acid-sensing ion channel 1
            # /2, ASC domain' , 'Acid-sensing ion channel 2, ASC domain' , 'Acid-sensing ion channel 1/2, ASC domain' , 
            # 'Acid-sensing ion channel 2, ASC domain'
        }
    }
