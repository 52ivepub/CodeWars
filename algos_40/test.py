import pytest

from main import parse


def test_parse_00():
    assert parse("ooo"), [0,0,0]


def test_parse_01():
    assert parse("ioioio"), [1,2,3]


def test_parse_02():
    assert parse("idoiido"), [0,1]


def test_error():
    with pytest.raises(TypeError):
        assert parse(123) == 123
