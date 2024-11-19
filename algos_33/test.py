import pytest

from main import diamond


def test_diamond_00():
    assert diamond(1) == "*\n"


def test_diamond_01():
    assert diamond(2) ==  None


def test_diamond_02():
    assert diamond(5) == "  *\n ***\n*****\n ***\n  *\n"


def test_error():
    with pytest.raises(TypeError):
        assert diamond("234") == "213"
