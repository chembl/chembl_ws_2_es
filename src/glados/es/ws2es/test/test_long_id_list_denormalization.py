from glados.es.ws2es.es_util import es_util
import unittest
import logging
import pprint
__author__ = 'jfmosquera@ebi.ac.uk'

logging_level = logging.INFO

logging.basicConfig(level=logging_level)
log = logging.getLogger()
log.setLevel(logging_level)


def analyze(test_idx_name, text, analyzer, tokens_only=True):
    analyzed = es_util.es_conn.indices.analyze(index=test_idx_name, body=text, analyzer=analyzer)
    log.info("ANALYSIS FOR: '{0}' USING '{1}'".format(text, analyzer))
    res_tokens = []
    if tokens_only:
        for token_desc in analyzed['tokens']:
            log.info(token_desc['token'])
            res_tokens.append(token_desc['token'])
    else:
        log.info(pprint.pformat(analyzed, indent=2))
    return res_tokens


class TestCase(unittest.TestCase):

    def test_analyzer(self):


        test_idx_name = 'chembl_test_long_id_field_idx'
        custom_analysis = es_util.DefaultMappings.COMMON_ANALYSIS
        field_name = 'test_long_id_field'
        custom_mappings = {
            'properties': {
                field_name: es_util.DefaultMappings.TEXT_STD,
            }
        }

        es_util.create_idx(test_idx_name, 1, 0, mappings=custom_mappings,
                           analysis=custom_analysis, logger=logging.getLogger())

        test_text = ['0']*(10**6)

        analyze(test_idx_name, )

        es_util.delete_idx(test_idx_name)

    def test_analyzed_field(self):
        pass
