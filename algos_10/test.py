import pytest

from main import unique_in_order


def test_unique_in_order_00():
    assert unique_in_order('AAAABBBCCDAABBB') == ['A', 'B', 'C', 'D', 'A', 'B']


def test_unique_in_order_01():
    assert unique_in_order('ABBCcAD') == ['A', 'B', 'C', 'c', 'A', 'D']


def test_unique_in_order_02():
    assert unique_in_order((1, 2, 2, 3, 3)) == [1, 2, 3]


def test_error():
    with pytest.raises(TypeError):
        assert unique_in_order(000) == '1'
