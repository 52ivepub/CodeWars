import pytest

from main import cakes


def test_cakes_00():
    assert cakes(recipe={"flour": 500, "sugar": 200, "eggs": 1},
                 available={"flour": 1200, "sugar": 1200, "eggs": 5, "milk": 200}) == 2


def test_cakes_01():
    assert cakes(recipe={"apples": 3, "flour": 300, "sugar": 150, "milk": 100, "oil": 100},
                 available={"sugar": 500, "flour": 2000, "milk": 2000}) == 0


# def test_cakes_02():
#     assert cakes(46288, 3), (51)


def test_error():
    with pytest.raises(TypeError):
        assert cakes('000') == '1'
