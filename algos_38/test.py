import pytest

from main import order_weight


def test_order_weight_00():
    assert order_weight("") == ""


def test_order_weight_01():
    assert order_weight("2000 10003 1234000 44444444 9999 11 11 22 123"), "11 11 2000 10003 22 123 1234000 44444444 9999"


def test_order_weight_02():
    assert order_weight("103 123 4444 99 2000"), "2000 103 123 4444 99"


def test_error():
    with pytest.raises(AttributeError):
        assert order_weight(123) == 123
