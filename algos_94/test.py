import pytest

from main import series_sum


def test_series_sum_00():
    assert series_sum(1), "1.00"


def test_series_sum_01():
    assert series_sum(2), "1.25"


def test_series_sum_02():
    assert series_sum(3), "1.39"


def test_error_series_sum_03():
    with pytest.raises(TypeError):
        assert series_sum(None) == None
