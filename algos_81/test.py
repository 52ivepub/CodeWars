import pytest

from main import loose_change


def test_loose_change_00():
    assert loose_change(29),  {'Nickels': 0, 'Pennies': 4, 'Dimes': 0, 'Quarters': 1}


def test_loose_change_01():
    assert loose_change(91),  {'Nickels': 1, 'Pennies': 1, 'Dimes': 1, 'Quarters': 3}


def test_loose_change_02():
    assert loose_change(0),   {'Nickels': 0, 'Pennies': 0, 'Dimes': 0, 'Quarters': 0}


def test_error_loose_change_03():
    with pytest.raises(TypeError):
        assert loose_change(None) == None
