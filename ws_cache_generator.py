import os
import sys
SCRIPT_PATH = os.path.realpath(__file__)
SCRIPT_DIR = os.path.abspath(os.path.join(SCRIPT_PATH, os.pardir))
GLADOS_ES_PATH = os.path.join(SCRIPT_DIR, 'src')
sys.path.append(GLADOS_ES_PATH)

import glados.es.ws2es.resource_iterator as resource_iterator
resource_iterator.iterate_all_ws_resources()
