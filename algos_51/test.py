import pytest

from main import valid_phone_number


def test_valid_phone_number_00():
    assert valid_phone_number("(123) 456-7890"), True


def test_valid_phone_number_01():
    assert valid_phone_number("(1111)555 2345") == False


def test_valid_phone_number_02():
    assert valid_phone_number("(123)456-7890") == False


def test_error_valid_phone_number_03():
    with pytest.raises(TypeError):
        assert valid_phone_number({132}) == {123}
