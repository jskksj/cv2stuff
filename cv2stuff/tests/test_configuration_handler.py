import pytest
from hypothesis import given
from hypothesis.strategies import text

import cv2stuff.configuration_handler as config


def test_initialization():
    with pytest.raises(ValueError):
        cfg = config.ConfigurationHandler('', '')
        # get rid of PEP8 error for unused cfg
        assert(cfg)


def test_initialization_folder():
    with pytest.raises(ValueError):
        cfg = config.ConfigurationHandler('folder', '')
        # get rid of PEP8 error for unused cfg
        assert(cfg)


def test_initialization_token():
    with pytest.raises(ValueError):
        cfg = config.ConfigurationHandler('', 'token')
        # get rid of PEP8 error for unused cfg
        assert(cfg)


@given(text())
def test_initialization_text(folder, token):
        cfg = config.ConfigurationHandler('folder', 'token')
        assert(cfg)
