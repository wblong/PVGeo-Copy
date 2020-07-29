"""
Read Surfer Grid File
~~~~~~~~~~~~~~~~~~~~~

Read an Surfer ASCII grid file
"""
import pyvista
from PVGeo.grids import SurferGridReader
from pyvista import examples

###############################################################################
# Download a sample Surfer grid file
fname = 'surfer-grid.grd'
filename= './tests/data/{}'.format(fname)
dem = SurferGridReader().apply(filename)

###############################################################################
# Apply a filter to the DEM to have realistic topography
warped = dem.warp_by_scalar(scale_factor=300.)
warped.plot(cmap='terrain')
