import pytest

from main import find_children


def test_find_children_00():
    assert find_children("abBA"),"AaBb"


def test_find_children_01():
    assert find_children("AaaaaZazzz"),"AaaaaaZzzz"


def test_find_children_02():
    assert find_children("CbcBcbaA"),"AaBbbCcc"


def test_error_find_children_03():
    with pytest.raises(TypeError):
        assert find_children(2) == 2
