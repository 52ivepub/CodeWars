import pytest

from main import find_nb


def test_find_nb_00():
    assert find_nb(4183059834009), (2022)


def test_find_nb_01():
    assert find_nb(135440716410000), (4824)


def test_find_nb_02():
    assert find_nb(26825883955641), (3218)


def test_error():
    with pytest.raises(TypeError):
        assert find_nb([1.25]) == 1
