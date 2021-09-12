from phong import Phong
from image import *
from ball import Ball
from light import Light

window_width = 1000
window_height = 1000
window_size = (window_width, window_height)
screenshot_index = 1
clear_directory('screenshots')

window = pygame.display.set_mode(window_size)
pygame.init()
pygame.display.set_caption("Phong model of lighting - ball")

ball : Ball = Ball(
    center=[0, 0, 0],
    r=200,
    alpha=10,
    ks=[255, 255, 255],
    kd=[255, 0, 0],
    ka=[128, 0, 0]
)

light : Light = Light(
    center=[0, 0, 0],
    i_s=[255, 255, 255],
    i_d=[255, 255, 255],
    i_a=[10, 10, 10]
)

run=True
while run:
    for event in pygame.event.get():
        run = False if event.type == pygame.QUIT else True
        keys = pygame.key.get_pressed()

        if event.type == pygame.KEYDOWN:
            # wybór materiału
            if event.key == pygame.K_1:
                ball.set_material('metal')
            if event.key == pygame.K_2:
                ball.set_material('wood')
            if event.key == pygame.K_3:
                ball.set_material('plastic')

            #sterowanie
            if event.key == pygame.K_w:
                light.move_light_source('up')
            if event.key == pygame.K_s:
                light.move_light_source('down')
            if event.key == pygame.K_a:
                light.move_light_source('left')
            if event.key == pygame.K_d:
                light.move_light_source('right')
            if event.key == pygame.K_q:
                light.move_light_source('forwards')
            if event.key == pygame.K_e:
                light.move_light_source('backwards')

            # screenshot
            if event.key == pygame.K_SPACE:
                save_screenshot(screenshot_index, window)
                screenshot_index += 1

        if keys[pygame.K_ESCAPE]:
            pygame.quit()
            raise SystemExit

    window.fill((0, 0, 0))
    pygame.draw.circle(window, ball.ka, (window_width / 2 + ball.center[0], window_height / 2 + ball.center[1]), ball.r)
    points_3d = ball.transform_circle_to_3d()
    # todo
    pygame.display.update()
