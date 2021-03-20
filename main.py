import pygame
import numpy as np

window_width, window_height = 1000, 1000
window = pygame.display.set_mode((window_width, window_height))
colors = []
translation_step = 5.
rotation_step = np.radians(0.8)
zoom_step = 50.
positions = []
dimensions = []


def create_cube(position, dimensions):
    x, y, z = position
    lx, ly, lz = dimensions
    return np.array([[x, y, z, 1], [x + lx, y, z, 1], [x, y, z + lz, 1], [x + lx, y, z + lz, 1],
                     [x, y + ly, z, 1], [x + lx, y + ly, z, 1], [x, y + ly, z + lz, 1], [x + lx, y + ly, z + lz, 1]])


def project(cubes, distance):
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


def draw(projections):
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


def translate(cubes, direction):
    translation = np.array([[1, 0, 0, 0], [0, 1, 0, 0], [0, 0, 1, 0], [0, 0, 0, 1]])
    if direction == 'a':
        translation[0, 3] = -translation_step
    elif direction == 'd':
        translation[0, 3] = translation_step
    elif direction == 's':
        translation[1, 3] = -translation_step
    elif direction == 'w':
        translation[1, 3] = translation_step
    elif direction == 'f':
        translation[2, 3] = -translation_step
    elif direction == 'r':
        translation[2, 3] = translation_step

    return [[translation.dot(cube[i]) for i in range(len(cube))] for cube in cubes]


def rotate(cubes, direction):
    if direction == 'j':
        rotation = np.array([[1, 0, 0, 0], [0, np.cos(-rotation_step), -np.sin(-rotation_step), 0],
                             [0, np.sin(-rotation_step), np.cos(-rotation_step), 0], [0, 0, 0, 1]])
    elif direction == 'l':
        rotation = np.array([[1, 0, 0, 0], [0, np.cos(rotation_step), -np.sin(rotation_step), 0],
                             [0, np.sin(rotation_step), np.cos(rotation_step), 0], [0, 0, 0, 1]])
    elif direction == 'k':
        rotation = np.array([[np.cos(-rotation_step), 0, np.sin(-rotation_step), 0], [0, 1, 0, 0],
                             [-np.sin(-rotation_step), 0, np.cos(-rotation_step), 1], [0, 0, 0, 1]])
    elif direction == 'i':
        rotation = np.array([[np.cos(rotation_step), 0, np.sin(rotation_step), 0], [0, 1, 0, 0],
                             [-np.sin(rotation_step), 0, np.cos(rotation_step), 1], [0, 0, 0, 1]])
    elif direction == 'h':
        rotation = np.array([[np.cos(-rotation_step), -np.sin(-rotation_step), 0, 0],
                             [np.sin(-rotation_step), np.cos(-rotation_step), 0, 0], [0, 0, 1, 0], [0, 0, 0, 1]])
    elif direction == 'y':
        rotation = np.array([[np.cos(rotation_step), -np.sin(rotation_step), 0, 0],
                             [np.sin(rotation_step), np.cos(rotation_step), 0, 0], [0, 0, 1, 0], [0, 0, 0, 1]])

    return [[rotation.dot(cube[i]) for i in range(len(cube))] for cube in cubes]


def load_cubes_from_file(filename):
    with open(filename, 'r') as f:
        for line in f.readlines():
            cube_data = [float(cell) for cell in line.split(", ")]
            positions.append(cube_data[0:3])
            dimensions.append(cube_data[3:6])
            colors.append((cube_data[6:]))


load_cubes_from_file("cubes.txt")
# positions = [[-300., 0., 100.], [100., 100., 100.], [200., -100., 100.]]
# dimensions = (100., 100., 100.)
cubes = []

for i in range(len(positions)):
    cubes.append(create_cube(positions[i], dimensions[i]))

distance = 501.

pygame.init()
pygame.display.set_caption("popierdalające kropki")

run = True
while run:
    window.fill((0, 0, 0))
    for event in pygame.event.get():
        run = False if event.type == pygame.QUIT else True
        keys = pygame.key.get_pressed()
        if keys[pygame.K_a]:
            cubes = translate(cubes, 'a')
        if keys[pygame.K_d]:
            cubes = translate(cubes, 'd')
        if keys[pygame.K_s]:
            cubes = translate(cubes, 's')
        if keys[pygame.K_w]:
            cubes = translate(cubes, 'w')
        if keys[pygame.K_f]:
            cubes = translate(cubes, 'f')
        if keys[pygame.K_r]:
            cubes = translate(cubes, 'r')

        if keys[pygame.K_j]:
            cubes = rotate(cubes, 'j')
        if keys[pygame.K_l]:
            cubes = rotate(cubes, 'l')
        if keys[pygame.K_k]:
            cubes = rotate(cubes, 'k')
        if keys[pygame.K_i]:
            cubes = rotate(cubes, 'i')
        if keys[pygame.K_h]:
            cubes = rotate(cubes, 'h')
        if keys[pygame.K_y]:
            cubes = rotate(cubes, 'y')

        if keys[pygame.K_UP]:
            distance -= zoom_step
        if keys[pygame.K_DOWN]:
            distance += zoom_step

    projections = project(cubes, distance)
    draw(projections)
    pygame.display.update()
