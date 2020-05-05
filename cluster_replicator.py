import os
import sys
SCRIPT_PATH = os.path.realpath(__file__)
SCRIPT_DIR = os.path.abspath(os.path.join(SCRIPT_PATH, os.pardir))
GLADOS_ES_PATH = os.path.join(SCRIPT_DIR, 'src')
sys.path.append(GLADOS_ES_PATH)

import glados.es.ws2es.cluster_replication.cluster_replicator as cluster_replicator
cluster_replicator.main()
