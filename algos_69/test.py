import pytest

from main import sum_consecutives


def test_sum_consecutives_00():
    assert sum_consecutives([1, 4, 4, 4, 0, 4, 3, 3, 1]),[1, 12, 0, 4, 6, 1]


def test_sum_consecutives_01():
    assert sum_consecutives([1, 1, 7, 7, 3]),[2, 14, 3]


def test_sum_consecutives_02():
    assert sum_consecutives([-5, -5, 7, 7, 12, 0]),[-10, 14, 12, 0]


def test_error_sum_consecutives_03():
    with pytest.raises(TypeError):
        assert sum_consecutives(11) == 11
