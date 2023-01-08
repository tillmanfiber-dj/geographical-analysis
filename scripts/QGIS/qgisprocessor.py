import os
import sys
import json
import pandas as pd

# set up system paths
qspath = './qgis_sys_paths.csv' 
# provide the path where you saved this file.
paths = pd.read_csv(qspath).paths.tolist()
sys.path += paths

# set up environment variables
qepath = './qgis_env.json'
js = json.loads(open(qepath, 'r').read())
for k, v in js.items():
    os.environ[k] = v

# map the PROJ_LIB to handle the projections
# for mac OS
os.environ['PROJ_LIB'] = '/Applications/Qgis.app/Contents/Resources/proj'


# qgis library imports
import PyQt5.QtCore
import gdal
import qgis.PyQt.QtCore
from qgis.core import (QgsApplication,
                       QgsProcessingFeedback,
                       QgsProcessingRegistry)
from qgis.analysis import QgsNativeAlgorithms

#set qgis path by checking QgisApplication.prefixPath()
QgsApplication.prefixPath('/Application/QGIS.app/Contents/MacOS',True)

# Create a reference to the QgsApplication.  Setting the
# second argument to False disables the GUI.

qgs = QgsApplication([], False)

print('Initializing QGIS processing')
# Load providers
qgs.initQgis()

print('Performing QGIS processing')
# Write your code here to load some layers, use processing
# algorithms, etc.
layer = QgsVectorLayer(data_source, layer_name, provider_name)


# Finally, exitQgis() is called to remove the
# provider and layer registries from memory
qgs.exitQgis()

print('Exiting QGIS processing')

