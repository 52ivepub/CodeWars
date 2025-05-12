import pytest

from main import remove_smallest


def test_remove_smallest_00():
    assert remove_smallest([1, 2, 3, 4, 5]), [2, 3, 4, 5]


def test_remove_smallest_01():
    assert remove_smallest([5, 3, 2, 1, 4]), [5, 3, 2, 4]


def test_remove_smallest_02():
    assert remove_smallest([1, 2, 3, 1, 1]), [2, 3, 1, 1]


def test_error_remove_smallest_03():
    with pytest.raises(TypeError):
        assert remove_smallest(None) == None
