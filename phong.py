from light import Light
from ball import Ball
import numpy as np

def normalize_point(point):
    return point / np.linalg.norm(point)

class Phong:
    def __init__(self, camera, light_source):
        self.camera = camera
        self.light_source = light_source

    def phongify(self, point, ball : Ball, light_source : Light):
        cam_vec = normalize_point(point - np.array(self.camera.position))
        normal_vec = normalize_point(np.array(point) - np.array(ball.center))
        light_vec = normalize_point(np.array(light_source.center) - np.array(point))
        radius_vec = normalize_point(light_vec - 2 * (light_vec.dot(normal_vec)) * normal_vec)

        # print("cam_vec:", cam_vec, point, self.camera.position)
        # print("normal_vec:", normal_vec)
        # print("light_vec:", light_vec)
        # print("radius_vec:", radius_vec)
        # exit(0)
        rgb_color_array = np.array([
            self.__get_light_intensity__(ball, self.light_source, cam_vec, normal_vec, light_vec, radius_vec, idx)
            for idx in range(3)
        ])

        return rgb_color_array

    def __get_light_intensity__(self, ball : Ball, light_source : Light, cam_v, norm_v, light_v, rad_v, idx):
        # print(ball.ks, ball.kd, ball.ka, cam_v, norm_v, light_v, rad_v)
        intensity = ball.ka[idx] * light_source.i_a[idx] #+ ball.kd[idx] * light_source.i_d[idx] + ball.ks[idx] * light_source.i_s[idx]
        # print(light_v, norm_v)
        # print(rad_v, cam_v)
        l_n_v = light_v.dot(norm_v)
        r_c_v = rad_v.dot(cam_v)
        # print(l_n_v, r_c_v)
        if l_n_v > 0:
            intensity += ball.kd[idx] * light_source.i_d[idx] * l_n_v
        if r_c_v > 0:
            intensity += ball.ks[idx] * light_source.i_s[idx] * r_c_v ** ball.alpha
        # print(intensity)
        # exit(0)
        return min(int(intensity / 255), 255)
