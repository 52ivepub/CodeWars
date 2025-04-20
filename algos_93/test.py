import pytest

from main import series_sum


def test_series_sum_00():
    assert series_sum(1500, 5, 100, 5000), 15


def test_series_sum_01():
    assert series_sum(1500000, 2.5, 10000, 2000000), 10


def test_series_sum_02():
    assert series_sum(1500000, 0.25, 1000, 2000000), 94


def test_error_series_sum_03():
    with pytest.raises(TypeError):
        assert series_sum(None) == None
