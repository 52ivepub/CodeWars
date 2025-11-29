import pytest

from main import calculate_years


def test_calculate_years_00():
    assert calculate_years(1000, 0.05, 0.18, 1100), 3


def test_calculate_years_01():
    assert calculate_years(1000,0.01625,0.18,1200), 14


def test_calculate_years_02():
    assert calculate_years(1000,0.05,0.18,1000) == 0


def test_error_calculate_years_03():
    with pytest.raises(TypeError):
        assert calculate_years('123', '123') == 132
