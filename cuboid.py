import numpy as np


def create_cuboid(position, dimensions):
    x, y, z = position
    lx, ly, lz = dimensions
    return np.array([[x, y, z, 1],
                     [x + lx, y, z, 1],
                     [x, y, z + lz, 1],
                     [x + lx, y, z + lz, 1],
                     [x, y + ly, z, 1],
                     [x + lx, y + ly, z, 1],
                     [x, y + ly, z + lz, 1],
                     [x + lx, y + ly, z + lz, 1]]
                    )


def project_to_2d(cubes, focal_dist, dimensions):
    window_width, window_height = dimensions
    projections = []
    for cube in cubes:
        projection = []
        projection_matrix = np.eye(4)
        projection_matrix[2][2] = 0
        projection_matrix[3][2] = 1 / focal_dist

        for i in range(len(cube)):
            projection.append(projection_matrix.dot(cube[i]))
            projection[i] *= (focal_dist / (cube[i][2] + focal_dist))
            projection[i][1] += window_height / 2
            projection[i][0] += window_width / 2
        projections.append(projection)
    return projections


def draw(projections, colors, window, pygame):
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