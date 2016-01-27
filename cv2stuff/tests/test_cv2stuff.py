"""Basic testing of cv2stuff"""

import pytest
import cv2
import numpy as np

from click.testing import CliRunner
from cv2stuff import cv2stuff


@pytest.fixture
def setup():
    """Return a Configuration object."""
    return(cv2stuff.Configuration())


def test_configuration(setup):
    """Check the Configuration defaults.

    `Comparing <http://stackoverflow.com/questions/10580676/
    comparing-two-numpy-arrays-for-equality-element-wise>`_
    numpy arrays.  The link says that the test I am using can cause certain
    kinds of differing arrays to test True when they should not.

    TODO: Check for bad np array.all() comparisons.
    """

    assert setup.MAXIMUM_ITERATIONS == 30
    assert setup.PIXEL_RESOLUTION == 0.001
    assert setup.criteria == (cv2.TERM_CRITERIA_MAX_ITER +
                              cv2.TERM_CRITERIA_EPS,
                              setup.MAXIMUM_ITERATIONS,
                              setup.PIXEL_RESOLUTION)
    assert setup.ROWS == 6
    assert setup.COLUMNS == 7
    assert setup.chessboard_points.shape == (setup.ROWS * setup.COLUMNS, 3)

    index = np.mgrid[0:setup.COLUMNS, 0:setup.ROWS].T.reshape(-1, 2)
    assert (setup.chessboard_points[:, :2] == index).all() == True

    assert setup.chessboard3d_points == []
    assert setup.chessboard2d_points == []

    assert setup.winSize == (11, 11)
    assert setup.minusOne == (-1, -1)


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


def test_path_one_file():
    """
    Echo one existing file.
    """
    runner = CliRunner()

    # echo name of one image file
    result = runner.invoke(cv2stuff.click_paths, ['images/undistort.jpg'])
    assert 'images/undistort.jpg' in result.output
    assert result.exit_code == 0


def test_path_file_missing():
    """
    Show error on non existing path.
    """
    runner = CliRunner()

    # echo error for missing image file
    result = runner.invoke(cv2stuff.click_paths, ['doesNotExist'])
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


def test_path_globbed_files():
    """
    Echo list of files in globbed argument.
    """
    runner = CliRunner()

    # echo names of globbed files
    result = runner.invoke(cv2stuff.click_paths, ['images/my*.jpg'])
    assert 'images/' in result.output
    assert result.exit_code == 2


def test_finding_points(setup):
    """
    Processing images should result in 2d and 3d points in the ctx
    object.
    """
    found, corners_rough = cv2stuff.find_points_rough(setup, "images/undistort")
    assert found is True
    assert len(setup.chessboard2d_points) != 0
    assert len(setup.chessboard3d_points) != 0
