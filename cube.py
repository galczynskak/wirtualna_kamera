import numpy as np
import pygame

colors = [(255, 102, 217), (255, 0, 191), (128, 0, 96), (112, 112, 219), (46, 46, 184), (140, 26, 255)]


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


def project(cubes, distance, window_height, window_width):
    projections = []
    for cube in cubes:
        projection = []
        projection_matrix = np.array([[1, 0, 0, 0], [0, 1, 0, 0], [0, 0, 0, 0], [0, 0, 1 / distance, 1]])
        for i in range(len(cube)):
            projection.append(projection_matrix.dot(cube[i]))
            projection[i] *= (distance / (cube[i][2] + distance))
            projection[i][1] += window_height/2
            projection[i][0] += window_width/2
        projections.append(projection)
    return projections


def draw(projections, window):
    for i, projection in enumerate(projections):
        projection = np.delete(projection, [2, 3], 1)
        color = colors[i]
        for coordinates in projection:
            pygame.draw.circle(window, color, coordinates, 3)

        pygame.draw.line(window, color, projection[0], projection[1])
        pygame.draw.line(window, color, projection[0], projection[2])
        pygame.draw.line(window, color, projection[0], projection[4])
        pygame.draw.line(window, color, projection[7], projection[6])
        pygame.draw.line(window, color, projection[7], projection[5])
        pygame.draw.line(window, color, projection[7], projection[3])
        pygame.draw.line(window, color, projection[2], projection[6])
        pygame.draw.line(window, color, projection[2], projection[3])
        pygame.draw.line(window, color, projection[5], projection[1])
        pygame.draw.line(window, color, projection[5], projection[4])
        pygame.draw.line(window, color, projection[3], projection[1])
        pygame.draw.line(window, color, projection[6], projection[4])
