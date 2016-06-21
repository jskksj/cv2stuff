import pytest
from hypothesis import given, assume
from hypothesis.strategies import text, integers

import cv2stuff.configuration_handler as config


def test_initialization():
    """If both folder and token are empty raise exception"""
    with pytest.raises(ValueError):
        cfg = config.ConfigurationHandler('', '')
        # get rid of PEP8 error for unused cfg
        assert(cfg)


def test_initialization_folder():
    """If token is empty raise exception"""
    with pytest.raises(ValueError):
        cfg = config.ConfigurationHandler('folder', '')
        # get rid of PEP8 error for unused cfg
        assert(cfg)


def test_initialization_token():
    """If folder is empty raise exception"""
    with pytest.raises(ValueError):
        cfg = config.ConfigurationHandler('', 'token')
        # get rid of PEP8 error for unused cfg
        assert(cfg)


def test_initialization_missing_arguments():
    """folder and token must be present"""
    with pytest.raises(ValueError):
        cfg = config.ConfigurationHandler()
        # get rid of PEP8 error for unused cfg
        assert(cfg)


def test_initialization_token_not_dot():
    """Token must not be dot, '.'

    It will cause both folder and token to be equal.
    """
    with pytest.raises(ValueError):
        cfg = config.ConfigurationHandler('folder', '.')
        # get rid of PEP8 error for unused cfg
        assert(cfg)


@given(folder=text(), token=text())
def test_initialization_text(folder, token):
    assume(folder != '')
    assume(token != '')
    assume(token != '.')
    cfg = config.ConfigurationHandler(folder, token)
    assert(cfg)


@given(folder=integers(), token=integers())
def test_initialization_integers(folder, token):
    with pytest.raises(ValueError):
        cfg = config.ConfigurationHandler('', '')
        # get rid of PEP8 error for unused cfg
        assert(cfg)
