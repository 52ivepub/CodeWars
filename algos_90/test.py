import pytest

from main import validate_pin


def test_validate_pin_00():
    assert validate_pin("1") ==  False


def test_validate_pin_01():
    assert validate_pin("1234"), True


def test_validate_pin_02():
    assert validate_pin("090909"), True


def test_error_validate_pin_03():
    with pytest.raises(TypeError):
        assert validate_pin(None) == None
