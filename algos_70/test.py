import pytest

from main import group_by_commas


def test_group_by_commas_00():
    assert group_by_commas(2147483647), '2,147,483,647'


def test_group_by_commas_01():
    assert group_by_commas(1234567890), '1,234,567,890'


def test_group_by_commas_02():
    assert group_by_commas(123456789), '123,456,789'


def test_error_group_by_commas_03():
    with pytest.raises(AssertionError):
        assert group_by_commas('{}') == '[]'
