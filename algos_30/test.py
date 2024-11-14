import pytest

from main import find_even_index


def test_find_even_index_00():
    assert find_even_index([1,2,3,4,3,2,1]), 3


def test_find_even_index_01():
    assert find_even_index([1,100,50,-51,1,1]),1


def test_find_even_index_02():
    assert find_even_index([1,2,3,4,5,6]),-1


def test_error():
    with pytest.raises(TypeError):
        assert find_even_index("444") == "222"
