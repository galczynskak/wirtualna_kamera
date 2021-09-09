from cube import *


def bsp(cubes, window,  distance, window_height, window_width):

    initial_triangles = []
    for cube in cubes:
        tmp_triangles = get_triangles(cube)
        for triangle in tmp_triangles:
            initial_triangles.append(triangle)

    initial_triangles = center_triangles(initial_triangles)

    triangles = []
    for triangle in initial_triangles:
        new_triangle = []
        for point in triangle[:3]:
            point = project_point(point, distance, window_height, window_width)
            point = np.delete(point, [2, 3])
            new_triangle.append(point)
        new_triangle.append(triangle[3])
        new_triangle.append(triangle[-1])
        triangles.append(new_triangle)


    #sortowanie po z centralnym
    sorted_triangles = sorted(triangles, key=lambda x: x[4], reverse=True)
    print(sorted_triangles)
    print(100*'_')

    #usuwanie współrzędnej centrum
    last_triangles = []
    for triangle in sorted_triangles:
        last_triangle = np.delete(triangle, 4)
        last_triangles.append(last_triangle)

    for triangle in last_triangles:  #zrzutowane punkty, każdy trójkąt to tylko współrzędne zrzutowane i kolor
        color = triangle[3]
        triangle = np.delete(triangle, 3)
        pygame.draw.polygon(window, color, triangle)

