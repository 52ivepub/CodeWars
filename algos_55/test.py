import pytest

from main import triple_double


def test_triple_double_00():
    assert triple_double(451999277, 41177722899), 1


def test_triple_double_01():
    assert triple_double( 1222345, 12345) ==  0


def test_triple_double_02():
    assert triple_double(666789, 12345667) ==  1


def test_error_triple_double_03():
    with pytest.raises(TypeError):
        assert triple_double([]) == []
