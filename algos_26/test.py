import pytest

from main import increment_string


def test_increment_string_00():
    assert increment_string("foo"), "foo1"


def test_increment_string_01():
    assert increment_string("foobar001"), "foobar002"


def test_increment_string_02():
    assert increment_string("fo99obar99"), "fo99obar100"


def test_error():
    with pytest.raises(AttributeError):
        assert increment_string([1.25]) == 1
