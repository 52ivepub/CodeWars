import pytest

from main import sort_the_inner_content


def test_sort_the_inner_content_00():
    assert sort_the_inner_content("sort the inner content in descending order"), "srot the inner ctonnet in dsnnieedcg oredr"


def test_sort_the_inner_content_01():
    assert sort_the_inner_content("wait for me"), "wiat for me"


def test_sort_the_inner_content_02():
    assert sort_the_inner_content("this kata is easy"), "tihs ktaa is esay"


def test_error_sort_the_inner_content_03():
    with pytest.raises(AttributeError):
        assert sort_the_inner_content(None) == None
