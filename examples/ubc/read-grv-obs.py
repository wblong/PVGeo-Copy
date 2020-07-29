"""
Read UBC Gravity Observations
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Read a UBC gravity observations file
"""
# sphinx_gallery_thumbnail_number = 1
import PVGeo
import pyvista
###############################################################################
# Download sample data files and keep track of names:
grav_file='./tests/data/Craig-Chile/LdM_grav_obs.grv'

###############################################################################
grav = PVGeo.ubc.GravObsReader().apply(grav_file)
print(grav)

###############################################################################
grav.plot(render_points_as_spheres=True, point_size=10)
