import pytest

from main import is_pangram


def test_is_pangram_00():
    assert is_pangram("The quick brown fox jumps over the lazy dog."), True


def test_is_pangram_01():
    assert is_pangram("Cwmalgos_10 fjord bank glyphs vext quiz"), False


# def test_is_pangram_02():
#     assert is_pangram((1, 2, 2, 3, 3)) == [1, 2, 3]


def test_error():
    with pytest.raises(AttributeError):
        assert is_pangram(000) == '1'
