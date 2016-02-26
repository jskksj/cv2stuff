import pytest


def test_zero_division():
        with pytest.raises(ZeroDivisionError):
                    1 / 0


def test_recursion_depth():
    with pytest.raises(RuntimeError) as excinfo:
        def f():
            f()
        f()
    assert 'maximum recursion depth exceeded' in str(excinfo.value)
