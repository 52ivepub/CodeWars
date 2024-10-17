import pytest

from main import find_outlier


def test_find_outlier_00():
    assert find_outlier([2, 4, 0, 100, 4, 11, 2602, 36]) == 11


def test_find_outlier_01():
    assert find_outlier([160, 3, 1719, 19, 11, 13, -21]) == 160


# def test_find_outlier_02():
#     assert find_outlier(10) == 2


def test_TypeError():
    with pytest.raises(TypeError):
        assert find_outlier('11') == 1
