import pytest

from main import fold_array


def test_fold_array_00():
    assert fold_array([1, 2, 3, 4, 5],  1),    [6, 6, 3]


def test_fold_array_01():
    assert fold_array( [1, 2, 3, 4, 5],  2),    [9, 6]


def test_fold_array_02():
    assert fold_array([1, 2, 3, 4, 5],  3),    [15]


def test_error_fold_array_03():
    with pytest.raises(TypeError):
        assert fold_array([]) == []
