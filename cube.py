import numpy as np
import pygame

colors_lines    = [(255, 102, 217), (255, 0, 191), (128, 0, 96), (112, 112, 219), (46, 46, 184), (140, 26, 255)]
colors_polygons = [(220, 220, 220), (211, 211, 211), (192, 192, 192), (169, 169, 169), (128, 128, 128), (105, 105, 105)]


def load_cubes_from_file(filename):
    positions = []
    dimensions = []
    with open(filename, 'r') as f:
        for line in f.readlines():
            cube_data = [float(cell) for cell in line.split(", ")]
            positions.append(cube_data[0:3])
            dimensions.append(cube_data[3:6])
    return positions, dimensions


def create_cube(position, dimensions):
    x, y, z = position
    lx, ly, lz = dimensions
    return np.array([[x, y, z, 1], [x + lx, y, z, 1], [x, y, z + lz, 1], [x + lx, y, z + lz, 1],
                     [x, y + ly, z, 1], [x + lx, y + ly, z, 1], [x, y + ly, z + lz, 1], [x + lx, y + ly, z + lz, 1]])


def project_point(point, distance, window_height, window_width):
    projection_matrix = np.array([[1, 0, 0, 0], [0, 1, 0, 0], [0, 0, 0, 0], [0, 0, 1 / distance, 1]])

    projection = projection_matrix.dot(point)
    projection *= (distance / (point[2] + distance))
    projection[1] += window_height / 2
    projection[0] += window_width / 2

    return projection


def get_triangles(cube):
    return np.array([
                    # dół
                     [cube[0], cube[1], cube[2], colors_polygons[0]],
                     [cube[1], cube[2], cube[3], colors_polygons[0]],
                    # przód, colors_polygons[]
                     [cube[0], cube[1], cube[5], colors_polygons[1]],
                     [cube[0], cube[5], cube[4], colors_polygons[1]],
                    # lewo, colors_polygons[]
                     [cube[4], cube[2], cube[0], colors_polygons[2]],
                     [cube[2], cube[4], cube[6], colors_polygons[2]],
                    # tył, colors_polygons[]
                     [cube[2], cube[3], cube[6], colors_polygons[3]],
                     [cube[7], cube[6], cube[3], colors_polygons[3]],
                    # prawo , colors_polygons[]
                     [cube[1], cube[3], cube[5], colors_polygons[4]],
                     [cube[7], cube[5], cube[3], colors_polygons[4]],
                    #góra , colors_polygons[]
                     [cube[4], cube[5], cube[6], colors_polygons[5]],
                     [cube[7], cube[6], cube[5], colors_polygons[5]]], dtype=object)
