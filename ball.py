from math import sqrt


class Ball:
    def __init__(self, center=None, r=None, alpha=None, ks=None, kd=None, ka=None):
        if center is None:
            center = [0, 0, 0]
        if r is None:
            r = 50
        if alpha is None:
            alpha = 2
        if kd is None:
            kd = [255, 255, 255]
        if ks is None:
            ks = [255, 255, 255]
        if ks is None:
            ka = [255, 255, 255]

        self.center = center # [x, y, z]
        self.r = r
        self.ks = ks
        self.kd = kd
        self.ka = ka
        self.alpha = alpha

    def set_material(self, material):
        if material is None or material == 'metal':
            self.ks = [255, 255, 255]
            self.kd = [200, 200, 200]
            self.ka = [10, 0, 0]
            self.alpha = 10
        elif material == 'polished wood':
            self.ks = [150, 150, 150]
            self.kd = [109, 75, 50]
            self.ka = [50, 0, 0]
            self.alpha = 100
        else:  # rubber
            self.ks = [100, 100, 100]
            self.kd = [80, 80, 80]
            self.ka = [10, 10, 10]
            self.alpha = 500

    def transform_circle_to_3d(self):
        points = []

        for y in range(int(self.center[1] - self.r), int(self.center[1] + self.r + 1), 1):
            current_max_value = abs(self.r ** 2 - y ** 2) ** 0.5
            for x in range(int(self.center[0] - current_max_value), int(self.center[0] + current_max_value) + 1, 1):
                z = abs((self.r ** 2 - (x - self.center[0]) ** 2 - (y - self.center[1]) ** 2)) ** 0.5 + self.center[2]
                points.append([x, y, z])
        return points

