import glados.es.ws2es.progress_bar_handler as progress_bar_handler
from glados.es.ws2es.util import SummableDict
from glados.es.ws2es.denormalization import DenormalizationHandler
from glados.es.ws2es.denormalization.compound_family_helper import CompoundFamiliesDir
from glados.es.ws2es.es_util import DefaultMappings, es_util

from glados.es.ws2es.resources_description import MOLECULE, DRUG_WARNING, DRUG_WARNING_BY_PARENT
import sys


class DrugWarningDenormalizationHandler(DenormalizationHandler):

    RESOURCE = DenormalizationHandler.AVAILABLE_RESOURCES.DRUG_WARNING

    @staticmethod
    def get_new_index_mappings():
        return {
            'properties':
            {
                'parent_molecule': {
                    'properties': MOLECULE.get_resource_mapping_from_es()
                },
                'drug_warning': {
                    'properties': SummableDict(**DRUG_WARNING.get_resource_mapping_from_es()) -
                    ['warning_country', 'warning_year'] +
                    {
                        'where': {
                            'properties': {
                                'country': DefaultMappings.LOWER_CASE_KEYWORD + DefaultMappings.TEXT_STD,
                                'year': DefaultMappings.SHORT
                            }
                        }
                    }
                }
            }
        }

    def __init__(self, compound_families_dir: CompoundFamiliesDir=None):
        super().__init__(compound_families_dir is not None)
        self.compound_families_dir = compound_families_dir
        self.drug_warns_by_grouping_id = {}
        self.generated_resource = DRUG_WARNING_BY_PARENT

    def get_drug_warn_grouping_id_parts(self, doc):
        if self.compound_families_dir is None:
            raise Exception('The grouping will not be correct if the compound families directory is not provided!')
        family_data = self.compound_families_dir.find_node(doc['molecule_chembl_id'])
        parent_chembl_id = family_data.get_family_parent_id()
        return parent_chembl_id, doc.get('warning_type'), doc.get('warning_class')

    def get_drug_warn_grouping_id(self, doc):
        parent_chembl_id, warn_type, warn_class = self.get_drug_warn_grouping_id_parts(doc)
        return '{0}-{1}-{2}'.format(parent_chembl_id, warn_type, warn_class)

    def handle_doc(self, es_doc: dict, total_docs: int, index: int, first: bool, last: bool):
        molecule_c_id = es_doc.get('molecule_chembl_id', None)
        if not molecule_c_id:
            print('WARNING: drug-warning without compound :{0}'.format(molecule_c_id),
                  file=sys.stderr)

        if self.compound_families_dir:
            grouping_id = self.get_drug_warn_grouping_id(es_doc)
            if grouping_id not in self.drug_warns_by_grouping_id:
                self.drug_warns_by_grouping_id[grouping_id] = []
            self.drug_warns_by_grouping_id[grouping_id].append(es_doc)

    def save_denormalization(self):
        if self.compound_families_dir:
            self.save_denormalization_for_new_index()

    def get_custom_mappings_for_complete_data(self):
        mappings = SummableDict()
        mappings += {
            'properties':
            {
                '_metadata':
                {
                    'properties':
                    {
                        'all_molecule_chembl_ids': DefaultMappings.CHEMBL_ID_REF
                    }
                }
            }
        }
        return mappings

    def get_doc_for_complete_data(self, doc: dict):
        molecule_chembl_id = doc['molecule_chembl_id']
        all_branch_ids = self.compound_families_dir.find_node(molecule_chembl_id).get_all_branch_ids()
        return {
            '_metadata': {
                'all_molecule_chembl_ids': all_branch_ids
            }
        }

    def save_denormalization_for_new_index(self):
        es_util.delete_idx(self.generated_resource.idx_name)
        es_util.create_idx(
            self.generated_resource.idx_name, 3, 1, analysis=DefaultMappings.COMMON_ANALYSIS,
            mappings=DrugWarningDenormalizationHandler.get_new_index_mappings()
        )

        dn_dict = {}

        print('{0} GROUPED RECORDS WERE FOUND FOR DRUG WARNING'.format(len(self.drug_warns_by_grouping_id)),
              file=sys.stderr)
        p_bar = progress_bar_handler.get_new_progressbar('drug_warns_by_parent-dn-generation',
                                                         len(self.drug_warns_by_grouping_id))

        for i, group_drug_warns in enumerate(self.drug_warns_by_grouping_id.values()):
            base_drug_warn = group_drug_warns[0]
            warning_refs = []
            all_molecule_chembl_ids = set()
            country_year_set = set()
            for drug_warn_i in group_drug_warns:
                warning_refs += drug_warn_i.get('warning_refs', [])
                if drug_warn_i['warning_country']:
                    countries = drug_warn_i['warning_country'].split(';')
                    for country_i in countries:
                        country_i = country_i.strip()
                        if country_i:
                            country_year_set.add((country_i, drug_warn_i['warning_year']))
                        else:
                            print(
                                'WARNING: BADLY FORMATTED COUNTRIES IN DRUG WARNING {}'
                                .format(drug_warn_i['warning_id']),
                                file=sys.stderr
                            )
                elif drug_warn_i['warning_year']:
                    print(
                        'WARNING: YEAR WITHOUT COUNTRY IN DRUG WARNING {}'.format(drug_warn_i['warning_id']),
                        file=sys.stderr
                    )

                for c_id in drug_warn_i.get('_metadata').get('all_molecule_chembl_ids'):
                    all_molecule_chembl_ids.add(c_id)

            parent_chembl_id, warn_type, warn_class = self.get_drug_warn_grouping_id_parts(base_drug_warn)

            drug_warn_data = SummableDict(**DRUG_WARNING.get_doc_by_id_from_es(base_drug_warn['warning_id']))
            drug_warn_data -= ['warning_country', 'warning_year']
            where = []
            for c_y_tuple in country_year_set:
                country, year = c_y_tuple
                where.append({'country': country, 'year': year})
            drug_warn_data['where'] = where
            drug_warn_data['warning_refs'] = warning_refs
            drug_warn_data['_metadata']['all_molecule_chembl_ids'] = list(all_molecule_chembl_ids)

            new_warning_doc = {
                'parent_molecule': MOLECULE.get_doc_by_id_from_es(parent_chembl_id),
                'drug_warning': drug_warn_data
            }
            doc_id = self.generated_resource.get_doc_id(new_warning_doc)

            dn_dict[doc_id] = new_warning_doc
            p_bar.update(i+1)
        p_bar.finish()

        self.save_denormalization_dict(
            self.generated_resource, dn_dict, DenormalizationHandler.default_update_script_and_size, do_index=True
        )
