import pytest

import configuration_handler

def test_initialization():
    with pytest.raises(ValueError) as need_names:
        config = configuration_handler.ConfigurationHandler('', '')

    print(need_names.value, config)
