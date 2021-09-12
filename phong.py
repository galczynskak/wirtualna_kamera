from light import Light
from ball import Ball
import numpy as np

def normalize_point(point):
    return point / np.linalg.norm(point)

class Phong:
    def __init__(self, camera, light_source):
        self.camera = camera
        self.light_source = light_source

    def phongify(self, point, ball : Ball):
        cam_vec = normalize_point(point - np.array(self.camera.center))
        normal_vec = normalize_point(np.array(point) - np.array(ball.center))
        light_vec = normalize_point(np.array(self.light_source.center) - np.array(point))
        radius_vec = normalize_point(light_vec - 2 * (light_vec.dot(normal_vec)) * normal_vec)

        print("cam_vec:", cam_vec)
        print("normal_vec:", normal_vec)
        print("light_vec:", light_vec)
        print("radius_vec:", radius_vec)
        
        rgb_color_array = np.array([
            self.__get_light_intensity__(ball, self.light_source, cam_v, norm_v, light_v, rad_v)
            for cam_v, norm_v, light_v, rad_v in zip(cam_vec, normal_vec, light_vec, radius_vec)
        ])

        return rgb_color_array

    def __get_light_intensity__(self, ball : Ball, light_source : Light, cam_v, norm_v, light_v, rad_v):
        intensity = ball.ka * light_source.i_a + ball.kd * light_source.i_d + ball.ks * light_source.i_s
        l_n_v = light_v.dot(norm_v)
        r_c_v = rad_v.dot(cam_v)
        
        if l_n_v > 0:
            intensity += ball.kd * light_source.i_d * l_n_v
        if r_c_v > 0:
            intensity += ball.ks * light_source.i_s * r_c_v ** ball.alpha
        
        return min(int(intensity / 255), 255)
