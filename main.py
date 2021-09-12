from image import *

window_size = (1000, 1000)
screenshot_index = 1
clear_directory('screenshots')

window = pygame.display.set_mode(window_size)
pygame.init()
pygame.display.set_caption("phong model")

run=True
while run:
    for event in pygame.event.get():
        run = False if event.type == pygame.QUIT else True
        keys = pygame.key.get_pressed()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                save_screenshot(screenshot_index, window)
                screenshot_index += 1

        if keys[pygame.K_q]:
            pygame.quit()
            raise SystemExit

    window.fill((0, 0, 0))

    pygame.display.update()
