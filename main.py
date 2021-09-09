from cube import *
from image import *
from matrix import *

distance = 501.
zoom_step = 50.
window_width, window_height = 1000, 1000
screenshot_index = 1
clear_directory('screenshots')

positions, dimensions = load_cubes_from_file("cubes.txt")
cubes = []
for pos, dim in zip(positions, dimensions):
    cubes.append(create_cube(pos, dim))

window = pygame.display.set_mode((window_width, window_height))
pygame.init()
pygame.display.set_caption("Visual Camera")

run = True
while run:
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
            cubes = rotate(cubes, 'k')
        if keys[pygame.K_l]:
            cubes = rotate(cubes, 'i')
        if keys[pygame.K_k]:
            cubes = rotate(cubes, 'j')
        if keys[pygame.K_i]:
            cubes = rotate(cubes, 'l')
        if keys[pygame.K_h]:
            cubes = rotate(cubes, 'h')
        if keys[pygame.K_y]:
            cubes = rotate(cubes, 'y')

        if keys[pygame.K_UP]:
            distance += zoom_step
        if keys[pygame.K_DOWN]:
            distance -= zoom_step

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                save_screenshot(screenshot_index, window)
                screenshot_index += 1

        if keys[pygame.K_q]:
            pygame.quit()
            raise SystemExit

    window.fill((0, 0, 0))
    projections = project(cubes, distance, window_height, window_width)
    draw(projections, window)
    for cube in cubes:
        triangles = get_triangles(cube)
        draw_triangles(triangles, window, distance, window_height, window_width)
    pygame.display.update()
