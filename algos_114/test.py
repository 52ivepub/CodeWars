import pytest

from main import average_string


def test_average_string_00():
    assert average_string("zero nine five two"), "four"


def test_average_string_01():
    assert average_string("four six two three"), "three"


def test_average_string_02():
    assert average_string("one two three four five"), "three"


def test_error_average_string_03():
    with pytest.raises(TypeError):
        assert average_string('123', '123') == 132
