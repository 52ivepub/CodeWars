import pytest

from main import encode


def test_encode_00():
    assert encode('hello'), 'h2ll4'


def test_encode_01():
    assert encode('How are you today?'), 'H4w 1r2 y45 t4d1y?'


def test_encode_02():
    assert encode('This is an encoding test.'), 'Th3s 3s 1n 2nc4d3ng t2st.'


def test_error_encode_03():
    with pytest.raises(TypeError):
        assert encode({132}) == {123}
