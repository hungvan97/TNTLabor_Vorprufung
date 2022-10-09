import numpy as np
from scipy.ndimage import rotate
from exercise_2_rect import find_rect


def generate_rot_square(w, h, x, y, l, alpha):
    rect = np.ones((l, l))
    rect = rotate(rect, alpha)
    r_h, r_w = rect.shape
    r_h_1 = r_h // 2
    r_h_2 = r_h - r_h_1
    r_w_1 = r_w // 2
    r_w_2 = r_w - r_w_1

    result = np.zeros((h, w), dtype=bool)
    result[y - r_h_1:y + r_h_2, x - r_w_1:x + r_w_2] = rect > .9
    return result


def angle_close(a_true, a_pred, tol=5):
    a_true = a_true % 90

    if a_true < tol:
        a_true += tol
        a_pred += tol
    elif a_true > 90 - tol:
        a_true -= tol
        a_pred -= tol

    a_pred = a_pred % 90

    return abs(a_true - a_pred) < tol


def do_test_rot_square(w, h, x, y, l, alpha):
    img = generate_rot_square(w, h, x, y, l, alpha)
    x_p, y_p, l_p, alpha_p = find_rect(img)

    assert x - 1 <= x_p <= x + 1
    assert y - 1 <= y_p <= y + 1
    assert l * .97 <= l_p <= l * 1.03
    assert angle_close(alpha, alpha_p, tol=5)


def test_ex3_basic():
    do_test_rot_square(1280, 720, 200, 400, 100, 0)


def test_ex3_rotated_30():
    do_test_rot_square(1280, 720, 200, 400, 100, 30)


def test_ex3_rotated_60():
    do_test_rot_square(1280, 720, 200, 400, 100, 60)


def test_ex3_covers_full_height():
    do_test_rot_square(1920, 1080, 1920 // 2, 1080 // 2, 1080, 0)
