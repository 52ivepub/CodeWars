import pytest

from main import shifted_diff


def test_shifted_diff_00():
    assert shifted_diff("eecoff","coffee"), 4


def test_shifted_diff_01():
    assert shifted_diff("Moose","moose"), -1


def test_shifted_diff_02():
    assert shifted_diff("Esham","Esham") ==  0


def test_error_shifted_diff_03():
    with pytest.raises(TypeError):
        assert shifted_diff(None) == None
