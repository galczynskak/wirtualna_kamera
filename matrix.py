import numpy as np

translation_step = 5
rotation_step = np.radians(0.8)


def translate(cubes, direction):
    translation = np.array([[1, 0, 0, 0], [0, 1, 0, 0], [0, 0, 1, 0], [0, 0, 0, 1]])
    if direction == 'a':
        translation[0, 3] = translation_step
    elif direction == 'd':
        translation[0, 3] = -translation_step
    elif direction == 's':
        translation[1, 3] = -translation_step
    elif direction == 'w':
        translation[1, 3] = translation_step
    elif direction == 'f':
        translation[2, 3] = translation_step
    elif direction == 'r':
        translation[2, 3] = -translation_step

    return [[translation.dot(cube[i]) for i in range(len(cube))] for cube in cubes]


def rotate(cubes, direction):
    if direction == 'j':
        rotation = np.array([[1, 0, 0, 0], [0, np.cos(-rotation_step), -np.sin(-rotation_step), 0],
                             [0, np.sin(-rotation_step), np.cos(-rotation_step), 0], [0, 0, 0, 1]])
    elif direction == 'l':
        rotation = np.array([[1, 0, 0, 0], [0, np.cos(rotation_step), -np.sin(rotation_step), 0],
                             [0, np.sin(rotation_step), np.cos(rotation_step), 0], [0, 0, 0, 1]])
    elif direction == 'k':
        rotation = np.array([[np.cos(-rotation_step), 0, np.sin(-rotation_step), 0], [0, 1, 0, 0],
                             [-np.sin(-rotation_step), 0, np.cos(-rotation_step), 1], [0, 0, 0, 1]])
    elif direction == 'i':
        rotation = np.array([[np.cos(rotation_step), 0, np.sin(rotation_step), 0], [0, 1, 0, 0],
                             [-np.sin(rotation_step), 0, np.cos(rotation_step), 1], [0, 0, 0, 1]])
    elif direction == 'h':
        rotation = np.array([[np.cos(-rotation_step), -np.sin(-rotation_step), 0, 0],
                             [np.sin(-rotation_step), np.cos(-rotation_step), 0, 0], [0, 0, 1, 0], [0, 0, 0, 1]])
    elif direction == 'y':
        rotation = np.array([[np.cos(rotation_step), -np.sin(rotation_step), 0, 0],
                             [np.sin(rotation_step), np.cos(rotation_step), 0, 0], [0, 0, 1, 0], [0, 0, 0, 1]])

    return [[rotation.dot(cube[i]) for i in range(len(cube))] for cube in cubes]