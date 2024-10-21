import pytest

from main import alphabet_position


def test_alphabet_position_00():
    assert alphabet_position("The sunset sets at twelve o' clock."), ("20 8 5 19 21 14 19 5 20 19 5 20 19 1 20 20 23 5 12 22 5 15 3 12 15 3 11")


def test_alphabet_position_01():
    assert alphabet_position("The narwhal bacons at midnight."), ("20 8 5 14 1 18 23 8 1 12 2 1 3 15 14 19 1 20 13 9 4 14 9 7 8 20")


# def test_alphabet_position_02():
#     assert alphabet_position('CoDeWaRs is niCe'), '#CodewarsIsNice'


def test_error():
    with pytest.raises(AttributeError):
        assert alphabet_position(0) == 1
