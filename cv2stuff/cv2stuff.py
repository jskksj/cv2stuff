"""Command Line Operations for OpenCV Functions"""

import cv2
import click
import numpy as np


class Configuration(object):
    """Set and maintain configuration defaults for the rest of the
    application.
    """

    def __init__(self):
        """Initilize the defaults.
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
CONTEXT_SETTINGS = dict(help_option_names=['-h', '--help'])


@click.group(context_settings=CONTEXT_SETTINGS)
@click.pass_context
def cli(ctx):
    """
    By default this program should reconize a chessboard image with seven
    columns and six rows.  Since that is the number of 'inner' corners the
    chessboard image actually has 8 columns of square by 7 rows.

    The termination criteria for finding subpixel centers is tostop on either
    maximum iterations or subpixel resolution.

    TERM_CRITERIA_MAX_ITER: iteration stop
    TERM_CRITERIA_EPS:      subpixel resolution stop

    The default behavior is to stop on either 30 iterations or
    1/1000 pixel resolution.
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
    Display an image
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


def find_points(ctx, image_path):
    """
    Get the object and image points.
    """
    image = cv2.imread(image_path, cv2.IMREAD_COLOR)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    found, corners_rough = cv2.findChessboardCorners(gray,
                                                     (ctx.COLUMNS, ctx.ROWS),
                                                     None)

    if found:
        ctx.chessboard_points.append(ctx.chessboard3d_points)
        corners_fine = cv2.cornerSubPix(gray,
                                        corners_rough,
                                        (11, 11),
                                        (-1, -1),
                                        ctx.critera)

    ctx.chessboard2d_points.append(corners_fine)


@cli.command()
@click.argument('images', nargs=-1, type=click.Path(exists=True),)
@click.pass_context
def find_all_points(ctx, images):
    """
    Return the object and image points for all images.
    """
