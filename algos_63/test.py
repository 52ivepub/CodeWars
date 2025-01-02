import pytest

from main import number_of_pairs


def test_number_of_pairs_00():
    assert number_of_pairs(["red","red"]) == 1


def test_number_of_pairs_01():
    assert number_of_pairs(["red","green","blue"]) == 0


def test_number_of_pairs_02():
    assert number_of_pairs(["gray","black","purple","purple","gray","black"]) == 3


def test_error_number_of_pairs_03():
    with pytest.raises(TypeError):
        assert number_of_pairs(11) == 11
