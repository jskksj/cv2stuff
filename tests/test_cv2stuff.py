# -*- coding: utf-8 -*-
import pytest
import cv2


@pytest.fixture
def setup():
    import cv2stuff.cv2stuff
    return(cv2stuff.cv2stuff.Configuration())


def test_configuration(setup):

    assert setup.MAXIMUM_ITERATIONS == 30
    assert setup.PIXEL_RESOLUTION == 0.001
    assert setup.criteria == (cv2.TERM_CRITERIA_MAX_ITER +
                              cv2.TERM_CRITERIA_EPS,
                              setup.MAXIMUM_ITERATIONS,
                              setup.PIXEL_RESOLUTION)
    assert setup.ROWS == 6
    assert setup.COLUMNS == 7
    assert setup.chessboard_points.shape == (setup.ROWS * setup.COLUMNS, 3)
