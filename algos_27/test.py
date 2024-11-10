import pytest

from main import perimeter


def test_perimeter_00():
    assert perimeter(5), (80)


def test_perimeter_01():
    assert perimeter(7), (216)


def test_perimeter_02():
    assert perimeter(30), (14098308)


def test_error():
    with pytest.raises(TypeError):
        assert perimeter("a") == "1"
