"""
Read ESRI Grid File
~~~~~~~~~~~~~~~~~~~

Read an ESRI ASCII grid file
"""
import pyvista
from PVGeo.grids import EsriGridReader
from pyvista import examples

###############################################################################
# Download a sample ESRI grid file
filename= './data/esri_grid.dem'
dem = EsriGridReader().apply(filename)

###############################################################################
# Apply a filter to the DEM to have realistic topography
warped = dem.warp_by_scalar()
warped.plot(cmap='terrain', clim=[-100, 400])
