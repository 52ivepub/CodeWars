import pytest

from main import presses


def test_presses_00():
    assert presses("LOL"), 9


def test_presses_01():
    assert presses("HOW R U"), 13


# def test_presses_02():
#     assert presses('SOS'), 's-o-s'


def test_error_presses_03():
    with pytest.raises(AttributeError):
        assert presses([]) == []
