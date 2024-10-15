import pytest

from main import create_phone_number


def test_create_phone_number_00():
    assert create_phone_number([1, 2, 3, 4, 5, 6, 7, 8, 9, 0]) == "(123) 456-7890"


def test_create_phone_number_01():
    assert create_phone_number([1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == "(111) 111-1111"


def test_create_phone_number_02():
    assert create_phone_number([0, 0, 0, 0, 0, 0, 0, 0, 0, 0]) == "(000) 000-0000"


def test_TypeError():
    with pytest.raises(TypeError):
        assert create_phone_number(11) == [1]
