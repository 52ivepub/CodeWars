import pytest

from main import josephus


def test_josephus_00():
    assert josephus([1,2,3,4,5,6,7,8,9,10],1),[1,2,3,4,5,6,7,8,9,10]


def test_josephus_01():
    assert josephus([1,2,3,4,5,6,7,8,9,10],2),[2, 4, 6, 8, 10, 3, 7, 1, 9, 5]


def test_josephus_02():
    assert josephus(["C","o","d","e","W","a","r","s"],4),['e', 's', 'W', 'o', 'C', 'd', 'r', 'a']


def test_error_josephus_03():
    with pytest.raises(TypeError):
        assert josephus(None) == None
