# -*- coding: utf-8 -*-
"""Command Line Group for OpenCV Functions"""

import cv2
import click
import numpy as np


class Configuration(object):
    """Configuration Defaults"""

    def __init__(self):
        """Set default configuration.

        Termination Criteria:
            Stop on either maximum iterations or subpixel resolution.

        TERM_CRITERIA_MAX_ITER iteration stop
        TERM_CRITERIA_EPS      subpixel resolution stop

        Default is to stop on either 30 iterations or 1/1000 pixel resolution.
        """

        self.MAXIMUM_ITERATIONS = 30
        self.PIXEL_RESOLUTION = 0.001

        self.criteria = (cv2.TERM_CRITERIA_MAX_ITER + cv2.TERM_CRITERIA_EPS,
                         self.MAXIMUM_ITERATIONS,
                         self.PIXEL_RESOLUTION)

        self.COLUMNS = 7
        self.ROWS = 6
        # Size the array to support the number of inner points in the board.
        self.chessboard_points = np.zeros((self.COLUMNS * self.ROWS, 3),
                                          np.float32)
        # Fill the first two columns with an index.
        self.chessboard_points[:, :2] = np.mgrid[0:self.COLUMNS,
                                                 0:self.ROWS].T.reshape(-1, 2)

        self.chessboard3d_points = []
        self.chessboard2d_points = []


pass_configuration = click.make_pass_decorator(Configuration)


@click.group()
@click.pass_context
def cli(ctx):
    """cv2stuff group function

    Instantiate the ctx.obj to be a Configuration object.
    """

    ctx.obj = Configuration()


@cli.command()
def find_show_chessboard_corners():
    pass
