import pytest

from main import duplicate_encode


def test_duplicate_encode_00():
    assert duplicate_encode("din") == "((("


def test_duplicate_encode_01():
    assert duplicate_encode("recede") == "()()()"


def test_duplicate_encode_02():
    assert duplicate_encode("Success") == ")())())"


def test_TypeError():
    with pytest.raises(AttributeError):
        assert duplicate_encode(0) == 1
