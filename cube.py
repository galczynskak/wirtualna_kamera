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
            projection[i][1] += window_height / 2
            projection[i][0] += window_width / 2
        projections.append(projection)
    return projections


def draw(projections, window):
    for i, projection in enumerate(projections):
        projection = np.delete(projection, [2, 3], 1)
        color = colors[i]
        for coordinates in projection:
            pygame.draw.circle(window, color, coordinates, 3)

        pygame.draw.line(window, color, projection[0], projection[1], 3)
        pygame.draw.line(window, color, projection[0], projection[2], 3)
        pygame.draw.line(window, color, projection[0], projection[4], 3)
        pygame.draw.line(window, color, projection[7], projection[6], 3)
        pygame.draw.line(window, color, projection[7], projection[5], 3)
        pygame.draw.line(window, color, projection[7], projection[3], 3)
        pygame.draw.line(window, color, projection[2], projection[6], 3)
        pygame.draw.line(window, color, projection[2], projection[3], 3)
        pygame.draw.line(window, color, projection[5], projection[1], 3)
        pygame.draw.line(window, color, projection[5], projection[4], 3)
        pygame.draw.line(window, color, projection[3], projection[1], 3)
        pygame.draw.line(window, color, projection[6], projection[4], 3)


def project_point(point, distance, window_height, window_width):
    projection_matrix = np.array([[1, 0, 0, 0], [0, 1, 0, 0], [0, 0, 0, 0], [0, 0, 1 / distance, 1]])

    projection = projection_matrix.dot(point)
    projection *= (distance / (point[2] + distance))
    projection[1] += window_height / 2
    projection[0] += window_width / 2

    return projection


def draw_triangles(triangles, window, distance, window_height, window_width):
    for i, triangle in enumerate(triangles):
        color = colors[(i if (i % 2) == 0 else i-1) % 6]
        projected_triangle = []
        for point in triangle:
            projected_triangle.append(project_point(point, distance, window_height, window_width))
        projected_triangle = np.delete(projected_triangle, [2, 3], 1)
        pygame.draw.polygon(window, color, projected_triangle)


def get_triangles(cube):
    return np.array([[cube[0], cube[1], cube[2]],
                     [cube[1], cube[2], cube[3]],
                     [cube[0], cube[1], cube[5]],
                     [cube[0], cube[5], cube[4]],
                     [cube[4], cube[2], cube[0]],
                     [cube[2], cube[4], cube[6]],
                     [cube[2], cube[3], cube[6]],
                     [cube[7], cube[6], cube[3]],
                     [cube[1], cube[3], cube[5]],
                     [cube[7], cube[5], cube[3]],
                     [cube[4], cube[5], cube[6]],
                     [cube[7], cube[6], cube[5]]])


# def find_plane(wall):
#     a, b, c = wall[0][:3]
#     d, e, f = wall[1][:3]
#     g, h, i = wall[2][:3]
#
#     A = b*(f-i) + e*(i-c) + h*(c-f)
#     B = a*(i-f) + d*(c-i) + g*(f-c)
#     C = a*(e-h) + d*(h-b) + g*(b-e)
#     D = a*(h*f - e*i) + d*(b*i - c*h) + g*(c*e - b*f)
#
#     return A, B, C, D
#
#
# def find_crossing_point(p1, p2, plane):
#     a, b, c = p1[:3]
#     d, e, f = p2[:3]
#     A, B, C, D = plane
#
#     i = d-a
#     j = e-b
#     k = f-c
#
#     r = -(A*a + B*b + C*c + D)/(A*i + B*j + C*k)
#
#     x = a + r*i
#     y = b + r*j
#     z = c + r*k
#
#     return x, y, z
