"""Wrap default values around OpenCV functions"""
import numpy as np


def findCorners(gray_image=[], pattern_size=(9, 6), corners=[]):
    """Typically the first routine called on an image will be
    cv2.findChessboardCorners. This function tries to find the inner corners of
    a 'chessboard' calibration image.  If an actual chessboard were used for
    calibration it would have 7 by 7 inner corners.  It is recommended that
    asymmetric patterns be used with one dimension odd and the other dimension
    even. That way the calibration target has only one axis of symmetry and
    therefore the board orientation can all ways be determined.

    The OpenCV installation should come with a set of 14 left and right image
    pairs that have calibration targets of the recommended shape, (9, 6), to be
    exact.

    The first parameter for cv2.findChessboardCorners is a gray scale image
    converted from the original color image of a 'chessboard' calibration
    target.

    The 'gray_image' variable needs to be an OpenCV gray scale image.

    The second parameter for cv2.findChessboardCorners is, 'pattern_size',
    which is tuple containing the width and height count of the calibration
    patterns inner points.

    The third parameter is 'corners'.  Which is the total number of inner
    corners in the calibration image, or 9 * 6 for the include sample images.

    These utilites do not use the optional 'corner_count' parameter as of now.

    The final 'flags' argument activate any combination of three different image
    filters that are availble to help find the chessboard corners in the image.

    >>> findCorners()
    162
    [] (9, 6) 54 []
    """
    pattern_points = np.zeros((np.prod(pattern_size), 3), np.float32)
    print(pattern_points.size)

    print(gray_image, pattern_size, np.prod(pattern_size), corners)

#   if gray_image or corners == []:
#       raise RuntimeError('Neither gray_image or corners may be an empty list')

if __name__ == '__main__':
    import doctest
    doctest.testmod()
