from camera import Camera
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
    center=[window_width / 2, window_height / 2, 40],
    r=50
)
ball.set_material('metal')

light : Light = Light(
    center=[0, 0, 1000],
    i_s=[200, 200, 200],
    i_d=[255, 255, 255],
    i_a=[10, 10, 10]
)

camera = Camera(ball, light)
points_3d = ball.transform_circle_to_3d()


def draw(camera, ball):
    for point in points_3d:
        color = camera.phong.phongify(point, ball, camera.light)
        window.set_at((int(point[0]), int(point[1])), color)


window.fill((0, 0, 0))
draw(camera, ball)
pygame.display.update()

run=True

while run:
    for event in pygame.event.get():
        run = False if event.type == pygame.QUIT else True
        keys = pygame.key.get_pressed()
        
        if event.type == pygame.KEYDOWN:
            # wybór materiału
            if keys[pygame.K_1]:
                print('Setting material to metal.')
                ball.set_material('metal')
            if keys[pygame.K_2]:
                print('Setting material to wood')
                ball.set_material('polished wood')
            if keys[pygame.K_3]:
                print('Setting material to rubber.')
                ball.set_material('rubber')

            #sterowanie
            if keys[pygame.K_w]:
                camera.move_light_source('up')
            if keys[pygame.K_s]:
                camera.move_light_source('down')
            if keys[pygame.K_a]:
                camera.move_light_source('left')
            if keys[pygame.K_d]:
                camera.move_light_source('right')
            if keys[pygame.K_q]:
                camera.move_light_source('forwards')
            if keys[pygame.K_e]:
                camera.move_light_source('backwards')

            # screenshot
            if keys[pygame.K_SPACE]:
                save_screenshot(screenshot_index, window)
                screenshot_index += 1

            if keys[pygame.K_ESCAPE]:
                pygame.quit()
                raise SystemExit

            draw(camera, ball)
            pygame.display.update()
