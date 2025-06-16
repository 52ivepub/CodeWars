import pytest

from main import number


def test_number_00():
    assert number([[10,0],[3,5],[5,8]]),5


def test_number_01():
    assert number([[3,0],[9,1],[4,10],[12,2],[6,1],[7,10]]),17


def test_number_02():
    assert number([[3,0],[9,1],[4,8],[12,2],[6,1],[7,8]]),21


def test_error_number_03():
    with pytest.raises(TypeError):
        assert number(123) == 132
