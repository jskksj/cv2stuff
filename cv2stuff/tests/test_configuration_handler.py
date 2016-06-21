import pytest

import cv2stuff.configuration_handler as config


def test_initialization():
    with pytest.raises(ValueError) as need_names:
        cfg = config.ConfigurationHandler('', '')

    print(need_names.value, cfg)
