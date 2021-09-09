# from cube import *
#
#
# def bsp(cubes, distance, window_height, window_width):
#
#     polygons = []
#
#     walls = []
#     for cube in cubes:
#         walls.append(get_walls(cube))
#
#     first_wall = walls.pop()
#     first_projection = project_wall(first_wall, distance, window_height, window_width)
#
#     for wall in walls:
#
#
#
#
#
#

# def project_wall(wall, distance, window_height, window_width):
#     projection_matrix = np.array([[1, 0, 0, 0], [0, 1, 0, 0], [0, 0, 0, 0], [0, 0, 1 / distance, 1]])
#     projection = []
#
#     for i in range(len(wall)):
#         projection.append(projection_matrix.dot(wall[i]))
#         projection[i] *= (distance / (wall[i][2] + distance))
#         projection[i][1] += window_height / 2
#         projection[i][0] += window_width / 2
#
#     center = max(wall[i][2] for i in range(len(wall))) - min(wall[i][2] for i in range(len(wall)))
#     projection.append(center)
#     return projection
#
#
