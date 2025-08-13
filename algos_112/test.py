import pytest

from main import dont_give_me_five


def test_dont_give_me_five_00():
    assert dont_give_me_five(1, 9) == 8


def test_dont_give_me_five_01():
    assert dont_give_me_five(4, 17) == 12


# def test_dont_give_me_five_02():
#     assert dont_give_me_five()


def test_error_dont_give_me_five_03():
    with pytest.raises(TypeError):
        assert dont_give_me_five('123', '123') == 132
