from phong import Phong

LIGHT_STEP=200

class Camera:
    def __init__(self, ball, light):
        self.position = [0, 0, 0]
        self.ball = ball
        self.light = light
        self.focal = 2
        self.phong = Phong(self, self.light)

    def move_light_source(self, direction):
        if direction == 'up':
            new_coord = self.light.center[1] - LIGHT_STEP
            self.light.center = [self.light.center[0], new_coord, self.light.center[2]]
        if direction == 'down':
            new_coord = self.light.center[1] + LIGHT_STEP
            self.light.center = [self.light.center[0], new_coord, self.light.center[2]]
        if direction == 'left':
            new_coord = self.light.center[0] - LIGHT_STEP
            self.light.center = [new_coord, self.light.center[1], self.light.center[2]]
        if direction == 'right':
            new_coord = self.light.center[0] + LIGHT_STEP
            self.light.center = [new_coord, self.light.center[1], self.light.center[2]]
        if direction == 'forwards':
            new_coord = self.light.center[2] + LIGHT_STEP
            self.light.center = [self.light.center[0], self.light.center[1], new_coord]
        if direction == 'backwards':
            new_coord = self.light.center[2] - LIGHT_STEP
            self.light.center = [self.light.center[0], self.light.center[1], new_coord]
        print(self.light.center)