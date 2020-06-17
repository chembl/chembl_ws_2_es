import os
import sys
SCRIPT_PATH = os.path.realpath(__file__)
SCRIPT_DIR = os.path.abspath(os.path.join(SCRIPT_PATH, os.pardir))
GLADOS_ES_PATH = os.path.join(SCRIPT_DIR, 'src')
sys.path.append(GLADOS_ES_PATH)

import glados.es.ws2es.sachem.chembl_elchem_loader as chembl_elchem_loader
chembl_elchem_loader.main()
