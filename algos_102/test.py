import pytest

from main import RomanNumerals


def test_RomanNumerals_00():
    assert RomanNumerals.from_roman([1, 2, 3, 4, 5]), [2, 3, 4, 5]


def test_RomanNumerals_01():
    assert RomanNumerals.from_roman([5, 3, 2, 1, 4]), [5, 3, 2, 4]


def test_RomanNumerals_02():
    assert RomanNumerals.from_roman([1, 2, 3, 1, 1]), [2, 3, 1, 1]


def test_error_RomanNumerals_03():
    with pytest.raises(TypeError):
        assert RomanNumerals.from_roman(None) == None
