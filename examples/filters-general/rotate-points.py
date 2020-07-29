"""
Rotate Points
~~~~~~~~~~~~~

This example will demonstrate how to rotate points in a `vtkPolyData` object around some origin on the XY plane.

THis example demos :class:`PVGeo.filters.RotatePoints`

"""
import pyvista
import os
from PVGeo.filters import RotatePoints

###############################################################################
# Get :class:`pyvista.PolyData` sample input to rotate
dir_path="./data"
uniformfile = os.path.join(dir_path, 'uniform.vtk')
mesh =pyvista.UniformGrid(uniformfile).cell_centers()
mesh.plot()

###############################################################################
# Use the filter:
rotated = RotatePoints(angle=33.3).apply(mesh)
rotated.plot()
