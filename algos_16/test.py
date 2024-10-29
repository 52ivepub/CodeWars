import pytest

from main import sort_array


def test_sort_array_00():
    assert sort_array([5, 3, 2, 8, 1, 4]), ([1, 3, 2, 8, 5, 4])


def test_sort_array_01():
    assert sort_array([5, 3, 1, 8, 0]), ([1, 3, 5, 8, 0])


def test_sort_array_02():
    assert sort_array([])== ([])


def test_error():
    with pytest.raises(TypeError):
        assert sort_array(1.25) == '1'
