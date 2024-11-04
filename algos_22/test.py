import pytest

from main import domain_name


def test_domain_name_00():
    assert domain_name("http://google.com"), ("google")


def test_domain_name_01():
    assert domain_name("https://123.net"), ("123")


def test_domain_name_02():
    assert domain_name("http://www.codewars.com/kata/"), ("codewars")


def test_error():
    with pytest.raises(AttributeError):
        assert domain_name([1.25]) == 1
