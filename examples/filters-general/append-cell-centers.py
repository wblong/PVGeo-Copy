"""
Append Cell Centers
~~~~~~~~~~~~~~~~~~~

This example will demonstrate how to append a dataset's cell centers as a length 3 tuple array.

This example demonstrates :class:`PVGeo.filters.AppendCellCenters`
"""
import pyvista
import os
from pyvista import examples
from PVGeo.filters import AppendCellCenters

###############################################################################
# Use an example mesh from pyvista
dir_path="./data"
rectfile = os.path.join(dir_path, 'rectilinear.vtk')
mesh = pyvista.RectilinearGrid(rectfile)
print(mesh)

###############################################################################
#  Run the PVGeo algorithm
centers = AppendCellCenters().apply(mesh)
print(centers)

###############################################################################
centers.plot()
