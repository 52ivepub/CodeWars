import pytest

from main import is_triangle


def test_is_triangle_00():
    assert is_triangle(1, 2, 2), True


def test_is_triangle_01():
    assert is_triangle(7, 2, 2) == False


def test_is_triangle_02():
    assert is_triangle(1, 2, 3) ==  False


def test_error_is_triangle_03():
    with pytest.raises(TypeError):
        assert is_triangle(123) == 132
