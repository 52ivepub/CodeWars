import pytest

from main import stock_list


def test_stock_list_00():
    assert stock_list( stocklist = ["ABART 20", "CDXEF 50", "BKWRK 25", "BTSQZ 89", "DRTYM 60"],
        categories = ["A", "B", "C", "W"], ), "(A : 20) - (B : 114) - (C : 50) - (W : 0)"


def test_stock_list_01():
    assert stock_list(  stocklist = ["BBAR 150", "CDXE 515", "BKWR 250", "BTSQ 890", "DRTY 600"],
        categories = ["A", "B", "C", "D"]),  "(A : 0) - (B : 1290) - (C : 515) - (D : 600)"


# def test_stock_list_02():
#     assert stock_list("idoiido"), [0,1]


def test_error():
    with pytest.raises(TypeError):
        assert stock_list(123) == 123
