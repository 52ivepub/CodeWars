import pytest

from main import dig_pow


def test_dig_pow_00():
    assert dig_pow(89, 1), (1)


def test_dig_pow_01():
    assert dig_pow(92, 1), (-1)


def test_dig_pow_02():
    assert dig_pow(46288, 3), (51)


def test_error():
    with pytest.raises(TypeError):
        assert dig_pow('000') == '1'
