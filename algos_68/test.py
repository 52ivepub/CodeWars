import pytest

from main import get_length_of_missing_array


def test_get_length_of_missing_array_00():
    assert get_length_of_missing_array([[1, 2], [4, 5, 1, 1], [1], [5, 6, 7, 8, 9]]) ==  3


def test_get_length_of_missing_array_01():
    assert get_length_of_missing_array([[5, 2, 9], [4, 5, 1, 1], [1], [5, 6, 7, 8, 9]]), 2


def test_get_length_of_missing_array_02():
    assert get_length_of_missing_array([[None], [None, None, None]]), 2


def test_error_get_length_of_missing_array_03():
    with pytest.raises(TypeError):
        assert get_length_of_missing_array(11) == 11
