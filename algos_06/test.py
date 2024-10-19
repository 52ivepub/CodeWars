import pytest

from main import rot13


def test_rot13_00():
    assert rot13('test'), 'grfg'


def test_rot13_01():
    assert rot13('Test'), 'Grfg'


def test_rot13_02():
    assert rot13('aA bB zZ 1234 *!?%'), 'nN oO mM 1234 *!?%'


def test_TypeError():
    with pytest.raises(TypeError):
        assert rot13(0) == 1
