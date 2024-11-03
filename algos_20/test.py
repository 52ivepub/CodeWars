import pytest

from main import delete_nth


def test_delete_nth_00():
    assert delete_nth(([20, 37, 20, 21]), 1),  [20, 37, 21]


def test_delete_nth_01():
    assert delete_nth(([1, 1, 3, 3, 7, 2, 2, 2, 2]), 3), [1, 1, 3, 3, 7, 2, 2, 2]


def test_delete_nth_02():
    assert delete_nth(([1, 1, 1, 1, 1]), 5), [1, 1, 1, 1, 1]


def test_error():
    with pytest.raises(TypeError):
        assert delete_nth(1.25) == '1'
