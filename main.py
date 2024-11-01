import open3d as o3d

# Create a sphere geometry
sphere = o3d.geometry.TriangleMesh.create_sphere(radius=1.0)

# Compute vertex normals for better visualization
sphere.compute_vertex_normals()

# Visualize the sphere
o3d.visualization.draw_geometries([sphere])
