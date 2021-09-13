LIGHT_STEP=100

class Light:
    def __init__(self, center=None, i_a=None, i_d=None, i_s=None):
        if center is None:
            center = [0, 0, 0] # [x, y, z]
        if i_a is None:
            i_a = [255, 255, 255]
        if i_d is None:
            i_d = [255, 255, 255]
        if i_s is None:
            i_s = [255, 255, 255]

        self.center = center
        self.i_a = i_a  # ambient intensity
        self.i_d = i_d  # diffuse intensity
        self.i_s = i_s  # specular intensity
