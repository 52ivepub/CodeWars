import pytest

from main import count_bits


def test_count_bits_00():
    assert count_bits(0) == 0


def test_count_bits_01():
    assert count_bits(4) == 1


def test_count_bits_02():
    assert count_bits(10) == 2


def test_TypeError():
    with pytest.raises(ValueError):
        assert count_bits('11') == 1
