import pygame
from matrix_handler import translate, rotate
from cuboid import create_cuboid, project_to_2d, draw

WINDOW_DIMENSIONS = (800, 600)
ZOOM_STEP = 50.
focal_length = 501.

colors = []
dots = []
edges = []
cuboids = []


def load_cubes_from_file(filename):
    with open(filename, 'r') as f:
        for line in f.readlines():
            cube_data = [float(cell) for cell in line.split(", ")]
            dots.append(cube_data[0:3])
            edges.append(cube_data[3:6])
            colors.append((cube_data[6:]))


load_cubes_from_file("cubes.txt")

for i in range(len(dots)):
    cuboids.append(create_cuboid(dots[i], edges[i]))

window = pygame.display.set_mode(WINDOW_DIMENSIONS)
pygame.init()
pygame.display.set_caption("Mad dotz")

while True:
    window.fill((0, 0, 0))

    for event in pygame.event.get():
        keys = pygame.key.get_pressed()

        if event.type == pygame.QUIT or keys[pygame.K_ESCAPE]:
            exit()

        if keys[pygame.K_a]:
            cuboids = translate(cuboids, 'left')
        if keys[pygame.K_d]:
            cuboids = translate(cuboids, 'right')
        if keys[pygame.K_s]:
            cuboids = translate(cuboids, 'down')
        if keys[pygame.K_w]:
            cuboids = translate(cuboids, 'up')
        if keys[pygame.K_f]:
            cuboids = translate(cuboids, 'back')
        if keys[pygame.K_r]:
            cuboids = translate(cuboids, 'forward')

        if keys[pygame.K_l]:
            cuboids = rotate(cuboids, 'rot_right')
        if keys[pygame.K_j]:
            cuboids = rotate(cuboids, 'rot_left')
        if keys[pygame.K_k]:
            cuboids = rotate(cuboids, 'rot_down')
        if keys[pygame.K_i]:
            cuboids = rotate(cuboids, 'rot_up')
        if keys[pygame.K_h]:
            cuboids = rotate(cuboids, 'rot_forward')
        if keys[pygame.K_y]:
            cuboids = rotate(cuboids, 'rot_back')

        if keys[pygame.K_EQUALS]:
            focal_length += ZOOM_STEP
        if keys[pygame.K_MINUS]:
            focal_length -= ZOOM_STEP

    projections = project_to_2d(cuboids, focal_length, WINDOW_DIMENSIONS)
    draw(projections, colors, window, pygame)

    pygame.display.update()
