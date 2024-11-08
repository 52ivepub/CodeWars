import pytest

from main import comp


def test_comp_00():
    assert comp([121, 144, 19, 161, 19, 144, 19, 11], [121, 14641, 20736, 361, 25921, 361, 20736, 361]) == True


# def test_comp_01():
#     assert comp(135440716410000), (4824)
#
#
# def test_comp_02():
#     assert comp(26825883955641), (3218)


def test_error():
    with pytest.raises(TypeError):
        assert comp([1.25]) == 1
