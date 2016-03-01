"""
Command Line Operations for OpenCV Functions

"""


import cv2
import click
import numpy as np


class Configuration(object):
    """Set and maintain configuration values for the rest of the
    application.
    """

    def __init__(self):
        """
        Initilize the defaults.
        """

        self.MAXIMUM_ITERATIONS = 30
        self.PIXEL_RESOLUTION = 0.001

        self.criteria = (cv2.TERM_CRITERIA_MAX_ITER + cv2.TERM_CRITERIA_EPS,
                         self.MAXIMUM_ITERATIONS,
                         self.PIXEL_RESOLUTION)

        # Default calibration chessboard dimensions for inner points.  For
        # an actual chessboard both would be seven.
        self.COLUMNS = 7
        self.ROWS = 5

        # Size the array to support the number of inner points in the
        # chessboard.
        self.chessboard_points = np.zeros((self.COLUMNS * self.ROWS, 3),
                                          np.float32)
        # Fill the first two columns with an index.
        self.chessboard_points[:, :2] = np.mgrid[0:self.COLUMNS,
                                                 0:self.ROWS].T.reshape(-1, 2)

        # 3D points are an estimate of the 'pose' of each chessboard in
        # cartesian space.
        self.chessboard3d_points = []

        # 2D points are the subpixel coordiates of each chessboard images
        # corners.
        self.chessboard2d_points = []

        self.corners = []
        self.winSize = (11, 11)
        self.minusOne = (-1, -1)

        # If set, this fl ag causes the image to be normalized via
        # cvEqualizeHist() before the thresholding is applied.
        self.flags = cv2.CV_CALIB_CB_ADAPTIVE_THRESH


# Make click accept -h for help.
pass_configuration = click.make_pass_decorator(Configuration)
CONTEXT_SETTINGS = dict(help_option_names=['-h', '--help'])


@click.group(context_settings=CONTEXT_SETTINGS)
@click.pass_context
def cli(ctx):
    """
    By default this program should reconize a chessboard image with seven
    columns and six rows.  Since that is the number of 'inner' corners the
    chessboard image actually has given it's 8 columns by 7 rows of squares.

    TERM_CRITERIA_MAX_ITER: iteration stop
    TERM_CRITERIA_EPS:      subpixel resolution stop

    The default behavior is to stop on either 30 iterations or
    1/1000 pixel resolution.

    winSize = (11, 11):
    Half of the side length of the search window.

    For example, if winSize=Size(11, 11), then a  11*2+1 by 11*2+1 ==
    23 by 23 search window is used.

    minusOne = (-1, -1):
    Half of the size of the dead region in the middle of the search zone
    over which the summation in the formula below is not done.

    It is sometimes used to avoid possible singularities of the
    autocorrelation matrix.

    The value of (-1,-1) indicates that there is no such a size of a
    window and zeroOne indicate there is.
    """
    ctx.obj = Configuration()


@cli.command()
@click.argument('images', nargs=-1, type=click.Path(exists=True),)
def click_paths(images):
    """
    This is just for demonstrating how to test click path functioning.
    """
    [click.echo(click.format_filename(image)) for image in images]


def show_image(image_path):
    """
    Utility function.

    Display one single image.
    """
    image = cv2.imread(image_path, cv2.IMREAD_COLOR)
    cv2.imshow('color', image)
    cv2.waitKey(0)


@cli.command()
@click.argument('images', nargs=-1, type=click.Path(exists=True),)
def show_images(images):
    """
    Display one or more images.
    """
    [show_image(image) for image in images]
    cv2.destroyAllWindows()


# TODO: The color and gray images could even be kept in the ctx object.
def find_points_pixel(ctx, image, gray, flags):
    """
    Utility function.

    Get the object and image points at the pixel level.
    """
    found, corners_pixel = cv2.findChessboardCorners(gray,
                                                     (ctx.COLUMNS,
                                                      ctx.ROWS),
                                                     flags)
    if not found:
        raise RuntimeError('Chessboard corners not found')
    return(found, corners_pixel)


# TODO: not tested yet.
def find_points_subpixel(ctx, image_path, gray, corners_pixel):
    """
    Utility function.

    Get the object and image points at the **sub** pixel level for a
    single image.
    """
    # TODO: Why am I doing this?  Where do the 3d points come from?
    ctx.chessboard_points.append(ctx.chessboard3d_points)
    corners_subpixel = cv2.cornerSubPix(gray,
                                        corners_pixel,
                                        ctx.winSize,
                                        ctx.minusOne,
                                        ctx.critera)

    ctx.chessboard2d_points.append(corners_subpixel)


@cli.command()
@click.argument('images', nargs=-1, type=click.Path(exists=True))
@click.pass_context
def find_all_points(ctx, images):
    """
    Return the object and image points for all images.

    The ctx object will contain the 2d and 3d points generated by
    findChessboardCorners and cornerSubPix.
    """
