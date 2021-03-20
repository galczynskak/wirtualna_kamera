import numpy as np

TRANSLATION_STEP = 5.
ROTATION_STEP = np.pi / 30


def translate(cubes, direction):
    translation = np.eye(4)
    if direction == 'left':
        translation[0, 3] = TRANSLATION_STEP
    elif direction == 'right':
        translation[0, 3] = -TRANSLATION_STEP
    elif direction == 'down':
        translation[1, 3] = -TRANSLATION_STEP
    elif direction == 'up':
        translation[1, 3] = TRANSLATION_STEP
    elif direction == 'back':
        translation[2, 3] = TRANSLATION_STEP
    elif direction == 'forward':
        translation[2, 3] = -TRANSLATION_STEP

    return [[translation.dot(cube[i]) for i in range(len(cube))] for cube in cubes]


def rotate(cubes, direction):
    rotation = np.eye(4)
    if direction == 'rot_left':
        rotation[1] = [0, np.cos(-ROTATION_STEP), -np.sin(-ROTATION_STEP), 0]
        rotation[2] = [0, np.sin(-ROTATION_STEP), np.cos(-ROTATION_STEP), 0]
    elif direction == 'rot_right':
        rotation[1] = [0, np.cos(ROTATION_STEP), -np.sin(ROTATION_STEP), 0]
        rotation[2] = [0, np.sin(ROTATION_STEP), np.cos(ROTATION_STEP), 0]
    elif direction == 'rot_down':
        rotation[0] = [np.cos(-ROTATION_STEP), 0, np.sin(-ROTATION_STEP), 0]
        rotation[2] = [-np.sin(-ROTATION_STEP), 0, np.cos(-ROTATION_STEP), 1]
    elif direction == 'rot_up':
        rotation[0] = [np.cos(ROTATION_STEP), 0, np.sin(ROTATION_STEP), 0]
        rotation[2] = [-np.sin(ROTATION_STEP), 0, np.cos(ROTATION_STEP), 1]
    elif direction == 'rot_forward':
        rotation[0] = [np.cos(-ROTATION_STEP), -np.sin(-ROTATION_STEP), 0, 0]
        rotation[1] = [np.sin(-ROTATION_STEP), np.cos(-ROTATION_STEP), 0, 0]
    elif direction == 'rot_back':
        rotation[0] = [np.cos(ROTATION_STEP), -np.sin(ROTATION_STEP), 0, 0]
        rotation[1] = [np.sin(ROTATION_STEP), np.cos(ROTATION_STEP), 0, 0]

    return [[rotation.dot(cube[i]) for i in range(len(cube))] for cube in cubes]