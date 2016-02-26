import click
import cv2
import numpy as np


class Configuration():
    """Setup up data for the rest of the functions
    """
    def __init__(self, criteria):
        self.MAXIMUM_ITERATIONS = 30
        self.SUBPIXEL_RESOLUTION = 0.001

        self.criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER,
                         self.MAXIMUM_ITERATIONS,
                         self.SUBPIXEL_RESOLUTION)

    # prepare object points, like (0,0,0), (1,0,0), (2,0,0) ....,(6,5,0)
    # Set it the the maximum size array needed.
    objp = np.zeros((7 * 6, 3), np.float32)
    objp[:, :2] = np.mgrid[0:7, 0:6].T.reshape(-1, 2)

pass_configuration = click.make_pass_decorator(Configuration)


@click.group()
@click.command()
@click.argument('images', nargs=-1)
@pass_configuration()
def cli(images):

    # Arrays to store object points and image points from all the images.
    # objpoints = []  # 3d point in real world space
    # imgpoints = []  # 2d points in image plane.

    [show_image(image) for image in images]


def show_image(filename):
    click.echo("\n" + filename + "\n")
    image = cv2.imread(filename)
    click.echo(image)
    cv2.imshow('image', image)
    cv2.waitKey(500)
