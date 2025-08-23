import pytest

from main import is_alt


def test_is_alt_00():
    assert is_alt("amazon"), True


def test_is_alt_01():
    assert is_alt("apple") == False


def test_is_alt_02():
    assert is_alt("banana"), True


def test_error_is_alt_03():
    with pytest.raises(TypeError):
        assert is_alt('123', '123') == 132
