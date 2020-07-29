"""
Read UBC Topography File
~~~~~~~~~~~~~~~~~~~~~~~~~

Read a UBC topography file
"""
# sphinx_gallery_thumbnail_number = 1
import PVGeo
import pyvista

###############################################################################
# Download sample data files and keep track of names:
#url = 'https://github.com/OpenGeoVis/PVGeo/raw/master/tests/data/Craig-Chile/LdM_topo.topo'
topo_file='./tests/data/Craig-Chile/LdM_topo.topo'

###############################################################################
topo = PVGeo.ubc.TopoReader().apply(topo_file)
print(topo)

###############################################################################
topo.plot(cmap='terrain')
