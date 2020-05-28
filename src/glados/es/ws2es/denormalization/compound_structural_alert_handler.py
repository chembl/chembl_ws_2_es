from glados.es.ws2es.denormalization import DenormalizationHandler
from glados.es.ws2es.es_util import DefaultMappings, SummableDict
from glados.es.ws2es.mappings.es_chembl_compound_structural_alert_mapping import mappings
from glados.es.ws2es.util import put_js_path_in_dict


class CompoundStructuralAlertDenormalizationHandler(DenormalizationHandler):

    RESOURCE = DenormalizationHandler.AVAILABLE_RESOURCES.COMPOUND_STRUCTURAL_ALERT

    ALERTS_MAPPINGS = SummableDict(mappings)
    put_js_path_in_dict(ALERTS_MAPPINGS, 'properties.cpd_str_alert_id', DefaultMappings.ID_REF)

    COMPOUND_MAPPING = {
        'properties':
        {
            '_metadata':
            {
                'properties':
                {
                    'compound_structural_alerts':
                    {
                        'properties':
                        {
                            'alert_count': DefaultMappings.LONG,
                            'alerts': ALERTS_MAPPINGS
                        }
                    }
                }
            }
        }
    }

    def __init__(self):
        super().__init__()
        self.compound_dict = {}

    def handle_doc(self, es_doc: dict, total_docs: int, index: int, first: bool, last: bool):
        molecule_c_id = es_doc.get('molecule_chembl_id', None)

        if molecule_c_id:
            if molecule_c_id not in self.compound_dict:
                self.compound_dict[molecule_c_id] = []
            self.compound_dict[molecule_c_id].append(es_doc)

    def save_denormalization(self):
        def get_update_script_and_size(compound_chembl_id, compound_alerts):
            compound_alerts_list = list(compound_alerts)
            update_size = len(compound_alerts)*2

            update_doc = {
                '_metadata': {
                    'compound_structural_alerts': {
                        'alert_count': len(compound_alerts_list),
                        'alerts': compound_alerts_list
                    }
                }
            }

            return update_doc, update_size

        self.save_denormalization_dict(
            DenormalizationHandler.AVAILABLE_RESOURCES.MOLECULE,
            self.compound_dict,
            get_update_script_and_size, new_mappings=self.COMPOUND_MAPPING
        )
