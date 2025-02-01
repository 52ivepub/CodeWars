import pytest

from main import delete_digit


def test_delete_digit_00():
    assert delete_digit(152),52


def test_delete_digit_01():
    assert delete_digit(1001),101


def test_delete_digit_02():
    assert delete_digit(10),1


def test_error_delete_digit_03():
    with pytest.raises(ValueError):
        assert delete_digit([]) == []
