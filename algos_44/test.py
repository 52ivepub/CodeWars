import pytest

from main import PaginationHelper


def test_item_count_00():
    Pag = PaginationHelper(['a', 'b', 'c', 'd', 'e', 'f'], 4)
    assert Pag.item_count() == 6


def test_page_count_01():
    Pag = PaginationHelper(['a', 'b', 'c', 'd', 'e', 'f'], 4)
    assert Pag.page_count() == 2


def test_page_item_count_02():
    Pag = PaginationHelper(['a', 'b', 'c', 'd', 'e', 'f'], 4)
    assert Pag.page_item_count(0) == 4


def test_page_index_03():
    Pag = PaginationHelper(['a', 'b', 'c', 'd', 'e', 'f'], 4)
    assert Pag.page_index(5) == 1


def test_error_page_item_count_04():
    Pag = PaginationHelper(['a', 'b', 'c', 'd', 'e', 'f'], 4)
    with pytest.raises(AssertionError):
        assert Pag.page_item_count('123') == '123'
