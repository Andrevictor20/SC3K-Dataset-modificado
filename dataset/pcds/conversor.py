import open3d as o3d
import numpy as np

# Carrega o arquivo PCD
pcd = o3d.io.read_point_cloud("airplane/airplane_0001_001.pcd")

# Obtém os pontos, cores (se disponíveis) e normais
points = np.asarray(pcd.points)
colors = np.asarray(pcd.colors)
normals = np.asarray(pcd.normals)

# Salva em um arquivo NPZ
np.savez("airplane/airplane_0010_001.npz", points=points, colors=colors, normals=normals)