import pytest

from main import sum_dig_pow


def test_sum_dig_pow_00():
    assert sum_dig_pow(1, 10), [1, 2, 3, 4, 5, 6, 7, 8, 9]


def test_sum_dig_pow_01():
    assert sum_dig_pow(1, 100), [1, 2, 3, 4, 5, 6, 7, 8, 9, 89]


def test_sum_dig_pow_02():
    assert sum_dig_pow(90, 100) == []


def test_error():
    with pytest.raises(TypeError):
        assert sum_dig_pow("234") == "213"
