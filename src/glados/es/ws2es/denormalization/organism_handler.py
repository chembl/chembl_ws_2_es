from glados.es.ws2es.denormalization import DenormalizationHandler
from glados.es.ws2es.es_util import DefaultMappings
import glados.es.ws2es.es_util as es_util
import glados.es.ws2es.progress_bar_handler as progress_bar_handler


class OrganismDenormalizationHandler(DenormalizationHandler):

    RESOURCE = DenormalizationHandler.AVAILABLE_RESOURCES.ORGANISM

    METADATA_MAPPING = {
        'properties':
        {
            '_metadata':
            {
                'properties':
                {
                    'organism_taxonomy':
                    {
                        'properties':
                        {
                            'l1': DefaultMappings.LOWER_CASE_KEYWORD,
                            'l2': DefaultMappings.LOWER_CASE_KEYWORD,
                            'l3': DefaultMappings.LOWER_CASE_KEYWORD,
                            'oc_id': DefaultMappings.ID_REF,
                            'tax_id': DefaultMappings.ID_REF,
                        }
                    }
                }

            }
        }
    }

    def __init__(self):
        super().__init__()
        self.organism_by_id = {}

    def handle_doc(self, es_doc: dict, total_docs: int, index: int, first: bool, last: bool):
        self.organism_by_id[es_doc['tax_id']] = es_doc
