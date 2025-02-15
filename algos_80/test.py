import pytest

from main import minimum_number


def test_minimum_number_00():
    assert minimum_number([3,1,2]), 1


def test_minimum_number_01():
    assert minimum_number([50, 39, 49, 6, 17, 28]), 2


def test_minimum_number_02():
    assert minimum_number([2,12,8,4,6]), 5


def test_error_minimum_number_03():
    with pytest.raises(TypeError):
        assert minimum_number(None) == None
