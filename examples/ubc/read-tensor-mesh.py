"""
Read Tensor Mesh
~~~~~~~~~~~~~~~~

Read a UBC tensor mesh file
"""
# sphinx_gallery_thumbnail_number = 1
import PVGeo
import pyvista
from pyvista import examples

###############################################################################
# Download sample data files and keep track of names:
mesh_file ="./tests/data/Craig-Chile/craig_chile.msh"
model_file = './tests/data/Craig-Chile/Lpout.mod'

###############################################################################
# Read the mesh and model
reader = PVGeo.ubc.TensorMeshReader()
reader.set_mesh_filename(mesh_file)
reader.add_model_file_name(model_file)
mesh = reader.apply()
print(mesh)

###############################################################################
# Use a `PyVista` ``threshold`` filter to remove ``NaN`` data values
mesh.threshold().plot()


###############################################################################
# Or inspect slices of the model
mesh.slice_orthogonal().plot()


###############################################################################
# Or threshold a data range
mesh.threshold([-0.6, -0.3]).plot(clim=[-0.6, 0.3])
