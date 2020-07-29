"""
Extract Points
~~~~~~~~~~~~~~

This example will demonstrate how to extract the points and PointData of
any input data set that has valid PointData into a `vtkPolyData` object.

This example demos :class:`PVGeo.filters.ExtractPoints`
"""
# sphinx_gallery_thumbnail_number = 2
import os
import pyvista
from PVGeo.filters import ExtractPoints

###############################################################################
# Have some input data source with valid PointData
"""Load a globe source."""
dir_path="./data"
globefile = os.path.join(dir_path, 'globe.vtk')
mapfile=os.path.join(dir_path, '2k_earth_daymap.jpg')
globe = pyvista.PolyData(globefile)
globe.textures['2k_earth_daymap'] = pyvista.read_texture(mapfile)
globe.plot()

###############################################################################
# Apply the filter:
polyData = ExtractPoints().apply(globe)
polyData.plot()
