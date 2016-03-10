"""
**Configuration Data Module**

This module holds configuration data for the OpenCV camera calibration routines.

Typically the first routine called on an image will be
cv2.findChessboardCorners. This function tries to find the inner corners of a
'chessboard' calibration image.  If an actual chessboard were used for
calibration it would have 7 by 7 inner corners.  It is recommended that
asymmetric patterns be used with one dimension odd and the other dimension
even. That way the calibration target has only one axis of symmetry and
therefore the board orientation can all ways be determined.

The OpenCV installation should come with a set of 14 left and right image pairs
that have calibration targets of the recommended shape, (9, 6), to be exact.

The first parameter for cv2.findChessboardCorners is a gray scale image
converted from the original color image of a 'chessboard' calibration target.

The 'gray_image' variable is initialized with None.
>>> gray_image
None

The second parameter for cv2.findChessboardCorners is, 'pattern_size', which is
tuple containing the width and height count of the calibration patterns inner
points.
>>> pattern_size
(9, 6)

The third parameter is 'corners'.  Which is the total number of inner corners
in the calibration image, or 9 * 6 for the include sample images.
>>> np.prod(pattern_size)
54

This program does not use the optional 'corner_count' parameter.

The final 'flags' argument activate any combination of three different image
filters that are availble to help find the chessboard corners in the image.

These filters do not appear to have python constants in cv2.

* **CV_CALIB_CB_ADAPTIVE_THRESH** Use adaptive thresholding to convert the image to
  black and white, rather than a fixed threshold level (computed from the
  average image brightness).

Termination criteria for cv2.findChessboardCorners

>>> MAXIMUM_ITERATIONS
30
>>> PIXEL_RESOLUTION
0.001
>>> criteria
(3, 30, 0.001)
"""

import cv2
import numpy as np


gray_image = None
pattern_size = (9, 6)


MAXIMUM_ITERATIONS = 30
PIXEL_RESOLUTION = 0.001

criteria = (cv2.TERM_CRITERIA_MAX_ITER + cv2.TERM_CRITERIA_EPS,
            MAXIMUM_ITERATIONS,
            PIXEL_RESOLUTION)

columns = 7
rows = 5


if __name__ == '__main__':
    import doctest
    doctest.testmod()
