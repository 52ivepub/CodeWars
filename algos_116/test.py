import pytest

from main import number


def test_number_00():
    assert number([]) ==  []


def test_number_01():
    assert number(["a", "b", "c"]), ["1: a", "2: b", "3: c"]


# def test_number_02():
#     assert number("one two three four five"), "three"


def test_error_number_03():
    with pytest.raises(TypeError):
        assert number('123', '123') == 132
