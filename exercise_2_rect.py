import math
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
    square_coordinaten = []

    # store the coordinaten of all white dot (which belong to square object) as an array with descending of height
    for h in range(len(img)):
        for w in range(len(img[h])):
            if img[h][w] == True:
                square_coordinaten.append((h, w))
                
    ## Assume we scan the square along y-axis:
    ## ==> square_coordinaten[0] will be the lowest or highes corner of the square. The opposite goes to square_coordinaten[-1]
    ## ==> square_coordinaten[*][0] is y-coordinaten, square_coordinaten[*][1] is x-coordinaten
    
    # Parameter calculating
    x = (square_coordinaten[0][1] + square_coordinaten[-1][1]) / 2
    y = (square_coordinaten[0][0] + square_coordinaten[-1][0]) / 2
    l = math.sqrt((square_coordinaten[0][0] - square_coordinaten[-1][0])**2 + (square_coordinaten[0][1] - square_coordinaten[-1][1])**2) / math.sqrt(2)

    ratio = abs(square_coordinaten[-1][1] - square_coordinaten[0][1]) / (l * math.sqrt(2))
    if (square_coordinaten[-1][1] - square_coordinaten[0][1]) > 0: # die niedrige Ecke steht recht auf die hochste Ecke
        alpha = 180 - math.degrees(math.acos(ratio)) - 45
    else:                                                      # die niedrige Ecke steht link auf die hochste Ecke
        alpha = math.degrees(math.acos(ratio)) - 45

    return x, y, l, alpha
