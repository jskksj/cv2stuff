"""Basic testing of cv2stuff"""

import pytest
import cv2
import numpy as np

from click.testing import CliRunner
from cv2stuff import cv2stuff


@pytest.fixture
def setup():
    """Return a Configuration object."""
    import cv2stuff.cv2stuff
    return(cv2stuff.cv2stuff.Configuration())


def test_configuration(setup):
    """Check the Configuration defaults.

    Comparing` <http://stackoverflow.com/questions/10580676/
    comparing-two-numpy-arrays-for-equality-element-wise>
    numpy arrays.  The link says that the test I am using can cause certain
    kinds of differing arrays to test True when they should not."""

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

    runner = CliRunner()
    result = runner.invoke(cv2stuff.cli, '-h')
    assert result.exit_code == 0
    assert 'Usage' in result.output

    result = runner.invoke(cv2stuff.cli, '-help')
    assert result.exit_code == 0
    assert 'Usage' in result.output


def test_cli():
    pass
