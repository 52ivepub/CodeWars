import pytest

from main import twos_difference


def test_twos_difference_00():
    assert twos_difference([1, 2, 3, 4]), [(1, 3), (2, 4)]


def test_twos_difference_01():
    assert twos_difference([1, 3, 4, 6]), [(1, 3), (4, 6)]


def test_twos_difference_02():
    assert twos_difference([0, 3, 1, 4]), [(1, 3)]


def test_error_twos_difference_03():
    with pytest.raises(TypeError):
        assert twos_difference('{}') == '[]'
