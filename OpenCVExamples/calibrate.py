#!/usr/bin/env python

'''
camera calibration for distorted images with chess board samples
reads distorted images, calculates the calibration and write undistorted images

usage:
    calibrate.py [--debug <output path>] [--square_size] [<image mask>]

default values:
    --debug:    ./output/
    --square_size: 1.0
    <image mask> defaults to images/*.jpg
'''

# Python 2/3 compatibility
from __future__ import print_function

import numpy as np
import cv2

# local modules
from common import splitfn

# built-in modules
import os

if __name__ == '__main__':
    import sys
    import getopt
    from glob import glob

    args, img_mask = getopt.getopt(sys.argv[1:], '', ['debug=', 'square_size='])
    args = dict(args)
    args.setdefault('--debug', './output/')
    args.setdefault('--square_size', 1.0)
    if not img_mask:
        img_mask = 'images/*.jpg'  # default
    else:
        img_mask = img_mask[0]

    img_names = glob(img_mask)
    debug_dir = args.get('--debug')
    if not os.path.isdir(debug_dir):
        os.mkdir(debug_dir)

    square_size = float(args.get('--square_size'))

    # chessboard pattern inner points on x and y axis.
    pattern_size = (7, 5)
    # create an array of zeros in the shape of an image.
    # http://docs.scipy.org/doc/numpy/reference/generated/numpy.zeros.html
    # two dimensions rows = product of chessboard inner points by pixel size.
    pattern_points = np.zeros((np.prod(pattern_size), 3), np.float32)
    # index the first two columns of the pattern.
    pattern_points[:, :2] = np.indices(pattern_size).T.reshape(-1, 2)
    # What does this do, is it a scaling factor?
    pattern_points *= square_size

    obj_points = []
    img_points = []
    h, w = 0, 0
    img_names_undistort = []
    # fn: file name
    for fn in img_names:
        # print('processing %s... ' % fn, end='')
        # img: image numpy array
        img = cv2.imread(fn, 0)
        if img is None:
            print("Failed to load", fn)
            continue

        # height, width: of numpy array for every image read in.
        h, w = img.shape[:2]
        # look for chessboard corners.
        found, corners = cv2.findChessboardCorners(img, pattern_size)
        # if corners are found get the sub pixel coordiantes of each corner.
        if found:
            term = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_COUNT, 30, 0.1)
            # replace pixel with sub pixel corners.
            cv2.cornerSubPix(img, corners, (5, 5), (-1, -1), term)

        if debug_dir:
            vis = cv2.cvtColor(img, cv2.COLOR_GRAY2BGR)
            cv2.drawChessboardCorners(vis, pattern_size, corners, found)
            path, name, ext = splitfn(fn)
            outfile = debug_dir + name + '_chess.png'
            cv2.imwrite(outfile, vis)
            if found:
                img_names_undistort.append(outfile)

        if not found:
            print('chessboard not found')
            continue

        # [a-z]rint("\ncorners: \n", corners)
        # [a-z]rint("\ncorners.reshape(-1, 2): \n", corners.reshape(-1, 2))
        img_points.append(corners.reshape(-1, 2))
        obj_points.append(pattern_points)

        print('ok')

    # calculate camera distortion
    obj_points_tmp = obj_points.copy()
    rms, camera_matrix, dist_coefs, rvecs, tvecs = cv2.calibrateCamera(
        obj_points,
        img_points,
        (w, h),
        None,
        None)
    if obj_points != obj_points_tmp:
        print("obj_points modified\n")

    # [a-z]rint("\nRMS:", rms)
    # [a-z]rint("camera matrix:\n", camera_matrix)
    # [a-z]rint("distortion coefficients: ", dist_coefs.ravel())
    # [a-z]rint("(w, h)", w, h)

    # undistort the image with the calibration
    print('')
    for img_found in img_names_undistort:
        img = cv2.imread(img_found)

        h,  w = img.shape[:2]
        newcameramtx, roi = cv2.getOptimalNewCameraMatrix(camera_matrix,
                                                          dist_coefs,
                                                          (w, h),
                                                          1,
                                                          (w, h))

        dst = cv2.undistort(img, camera_matrix, dist_coefs, None, newcameramtx)

        # crop and save the image
        x, y, w, h = roi
        # [a-z]rint("\ncrop image: roi\n", roi)
        dst = dst[y:y+h, x:x+w]
        outfile = img_found + '_undistorted.png'
        # [a-z]rint('Undistorted image written to: %s' % outfile)
        cv2.imwrite(outfile, dst)

    cv2.destroyAllWindows()
