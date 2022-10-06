def find_rect(img):
    # Given a binary image with black (=False) background containing a single white (=True) rotated square, return
    # the center of mass (x, y) of said square, its edge length (l) and its rotation angle (alpha). The square will
    # always be fully contained inside the image, i.e. none of its edges intersects with the image border.
    #
    # Return the angle `alpha` in degrees, where 0° is upright and equivalent to ..., -180°, -90°, 90°, 180°, ...
    # and the positive direction of rotation is counter-clockwise
    #
    # Please note the shape of `img` is (height, width) with y-axis first (row-major order).
    # No in-depth knowledge of computer vision, morphological transforms, etc. is required to solve this task,
    # thus it should be sufficient to use standard numpy methods
    #
    # To pass, your solution must give results within the following tolerances:
    #   x, y  :  1 px absolute difference to correct value
    #   l     :  between 97% and 103% of correct value
    #   alpha :  5° absolute difference to correct value
    import numpy as np

    x, y, l, alpha = 0, 0, 0, 0

    # TODO: Add your solution here
    return x, y, l, alpha
