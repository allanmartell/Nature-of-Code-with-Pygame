# library written by CodeSurgeon (2017)
# Source: https://stackoverflow.com/questions/46752103/is-there-popmatrix-pushmatrix-translate-in-pygame

import math
import numpy as np

_stack = [np.identity(4)]

def apply_mat(mat):
    _stack[-1] = np.dot(_stack[-1], mat)

def pop_mat():
    _stack.pop()

def push_mat():
    _stack.append(get_mat())

def get_mat():
    return _stack[-1]

def reset_mat():
    _stack[-1] = np.identity(4)

def rotate_mat(radians):
    c = math.cos(radians)
    s = math.sin(radians)
    rotate = np.array([
        [c, s, 0, 0],
        [-s, c, 0, 0],
        [0, 0, 1, 0],
        [0, 0, 0, 1],
    ], dtype=np.float32)
    apply_mat(rotate)

def translate_mat(x_shift, y_shift):
    x, y = x_shift, y_shift
    translate = np.array([
        [1, 0, 0, 0],
        [0, 1, 0, 0],
        [0, 0, 1, 0],
        [x, y, 0, 1],
    ], dtype=np.float32)
    apply_mat(translate)

def scale_mat(x_scale, y_scale):
    x, y = x_scale, y_scale
    scale = np.array([
        [x, 0, 0, 0],
        [0, y, 0, 0],
        [0, 0, 1, 0],
        [0, 0, 0, 1],
    ], dtype=np.float32)
    apply_mat(scale)


# Sample case in main.py:

# import math
# import matstack as ms
#
# if __name__ == "__main__":
#     ms.reset_mat()
#     ms.translate_mat(rect.x, rect.y)
#     ms.rotate_mat(math.radians(45))
#     ms.scale_mat(2, 0.5)
#     print(ms.get_mat())
