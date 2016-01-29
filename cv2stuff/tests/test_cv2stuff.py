"""Basic testing of cv2stuff"""

import pytest
import cv2
import numpy as np

from click.testing import CliRunner
from cv2stuff import cv2stuff


@pytest.fixture
def ctx():
    """Return a Configuration object."""
    setup = cv2stuff.Configuration()
    # py.test has to be run in cv2stuff for this to work.
    setup.test_image_path = "cv2stuff/tests/images/"
    return(setup)


def test_configuration(ctx):
    """Check the Configuration defaults.

    `Comparing <http://stackoverflow.com/questions/10580676/
    comparing-two-numpy-arrays-for-equality-element-wise>`_
    numpy arrays.  The link says that the test I am using can cause certain
    kinds of differing arrays to test True when they should not.

    TODO: Check for bad np array.all() comparisons.
    """

    assert ctx.MAXIMUM_ITERATIONS == 30
    assert ctx.PIXEL_RESOLUTION == 0.001
    assert ctx.criteria == (cv2.TERM_CRITERIA_MAX_ITER +
                            cv2.TERM_CRITERIA_EPS,
                            ctx.MAXIMUM_ITERATIONS,
                            ctx.PIXEL_RESOLUTION)
    assert ctx.ROWS == 5
    assert ctx.COLUMNS == 7
    assert ctx.chessboard_points.shape == (ctx.ROWS * ctx.COLUMNS, 3)

    index = np.mgrid[0:ctx.COLUMNS, 0:ctx.ROWS].T.reshape(-1, 2)
    assert (ctx.chessboard_points[:, :2] == index).all() == True

    assert ctx.chessboard3d_points == []
    assert ctx.chessboard2d_points == []

    assert ctx.winSize == (11, 11)
    assert ctx.minusOne == (-1, -1)


def test_help_options():
    """
    Both '-h' and '--help' should produce help output.
    """

    runner = CliRunner()
    result = runner.invoke(cv2stuff.cli, '-h')
    assert result.exit_code == 0
    assert 'Usage' in result.output

    result = runner.invoke(cv2stuff.cli, '-help')
    assert result.exit_code == 0
    assert 'Usage' in result.output


def test_path_one_file(ctx):
    """
    Echo one existing file.
    """
    runner = CliRunner()

    # echo name of one image file
    result = runner.invoke(cv2stuff.click_paths, [ctx.test_image_path +
                                                  'undistort.jpg'])
    assert 'undistort.jpg' in result.output
    assert result.exit_code == 0


def test_path_file_missing(ctx):
    """
    Show error on non existing path.
    """
    runner = CliRunner()

    # echo error for missing image file
    result = runner.invoke(cv2stuff.click_paths, [ctx.test_image_path +
                                                  'doesNotExist'])
    assert 'Error:' in result.output
    assert result.exit_code == 2


def test_path_empty_command():
    """
    Echo nothing given nothing.
    """
    runner = CliRunner()

    # echo nothing for nothing on command line
    result = runner.invoke(cv2stuff.click_paths, [''])
    assert '' in result.output
    assert result.exit_code == 2


def test_path_globbed_files(ctx):
    """
    Echo list of files in globbed argument.
    """
    runner = CliRunner()

    # echo names of globbed files
    result = runner.invoke(cv2stuff.click_paths, [ctx.test_image_path +
                                                  'my*.jpg'])
    assert '' in result.output
    assert result.exit_code == 2


def test_find_points_coarse(ctx):
    """
    Processing images should result in an array of pixel points."
    """
    found, corners_coarse = \
        cv2stuff.find_points_coarse(ctx,
                                    ctx.test_image_path +
                                    "undistort.jpg")
    assert found is True


def test_find_all_points(ctx):
    """
    This should result in arrays of points for 3d objects and 2d image
    points.
    """
