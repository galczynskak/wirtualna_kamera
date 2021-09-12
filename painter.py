from cube import *
import functools as ft


def get_point_distance(point1, point2):
    return ((point1[0] - point2[0]) ** 2 + (point1[1] - point2[1]) ** 2 + (point1[2] - point2[2]) ** 2) ** .5


def compare_triangles(observer, triangle1, triangle2):

    triangle1_max = max([get_point_distance(p, observer) for p in triangle1[:2]])
    triangle1_min = min([get_point_distance(p, observer) for p in triangle1[:2]])
    
    triangle2_max = max([get_point_distance(p, observer) for p in triangle2[:2]])
    triangle2_min = min([get_point_distance(p, observer) for p in triangle2[:2]])

    if ((triangle1_max > triangle2_max and triangle1_min > triangle2_min) or 
            (triangle1_max <= triangle2_max and triangle1_min >= triangle2_min)):
        return -1
    elif ((triangle1_max < triangle2_max and triangle1_min < triangle2_min) or 
            (triangle1_max >= triangle2_max and triangle1_min <= triangle2_min)):
        return 1
    else:
        return 0


def sort_triangles_by_distance(triangles, observer):
    sorted_triangles = triangles
    comparator = ft.cmp_to_key(ft.partial(compare_triangles, observer))
    sorted_triangles.sort(key=comparator)
    return sorted_triangles


def paint(cubes, window, observer, window_height, window_width):
    distance = -observer[2]
    initial_triangles = []
    
    for cube in cubes:
        tmp_triangles = get_triangles(cube)
        for triangle in tmp_triangles:
            initial_triangles.append(triangle)

    sorted_triangles = sort_triangles_by_distance(initial_triangles, observer)

    triangles = []
    for triangle in sorted_triangles:
        new_triangle = []
        for point in triangle[:3]:
            point = project_point(point, distance, window_height, window_width)
            point = np.delete(point, [2, 3])
            new_triangle.append(point)
        new_triangle.append(triangle[3])
        new_triangle.append(triangle[-1])
        triangles.append(new_triangle)

    for triangle in triangles:  #zrzutowane punkty, każdy trójkąt to tylko współrzędne zrzutowane i kolor
        color = triangle[3]
        triangle = np.delete(triangle, 3)
        pygame.draw.polygon(window, color, triangle[:3])