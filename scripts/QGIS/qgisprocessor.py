import qgis.core

#set qgis path by checking QgisApplication.prefixPath()
QgisApplication.prefixPath('/Application/QGIS.app/Contents/MacOS',True)

# Create a reference to the QgsApplication.  Setting the
# second argument to False disables the GUI.

qgs = QgsApplication([], False)

print('Initializing QGIS processing')
# Load providers
qgs.initQgis()

print('Performing QGIS processing')
# Write your code here to load some layers, use processing
# algorithms, etc.

# Finally, exitQgis() is called to remove the
# provider and layer registries from memory
qgs.exitQgis()

print('Exiting QGIS processing')

