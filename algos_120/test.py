import pytest

from main import capitals


def test_capitals_00():
    assert capitals('CodEWaRs'), [0,3,4,6]


def test_capitals_01():
    assert capitals('tmdXsSjzUsRoCMjDVwtTcRJt'), [3, 5, 8, 10, 12, 13, 15, 16, 19, 21, 22]


def test_capitals_02():
    assert capitals('xqUIxUjaG'), [2, 3, 5, 8]


def test_error_capitals_03():
    with pytest.raises(TypeError):
        assert capitals('123', '123') == 132
