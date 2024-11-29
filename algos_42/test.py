import pytest

from main import rev_rot


def test_rev_rot_00():
    assert rev_rot( "1234", 0) == ""


def test_rev_rot_01():
    assert rev_rot( "1234", 5) ==  ""


# def test_rev_rot_02():
#     assert rev_rot("idoiido"), [0,1]


def test_error():
    with pytest.raises(TypeError):
        assert rev_rot(123) == 123
