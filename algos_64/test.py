import pytest

from main import get_order


def test_get_order_00():
    assert get_order("milkshakepizzachickenfriescokeburgerpizzasandwichmilkshakepizza") == "Burger Fries Chicken Pizza Pizza Pizza Sandwich Milkshake Milkshake Coke"


def test_get_order_01():
    assert get_order("pizzachickenfriesburgercokemilkshakefriessandwich") == "Burger Fries Fries Chicken Pizza Sandwich Milkshake Coke"


# def test_get_order_02():
#     assert get_order(["gray","black","purple","purple","gray","black"]) == 3


def test_error_get_order_03():
    with pytest.raises(TypeError):
        assert get_order(11) == 11
