import pytest

from main import array_diff


def test_array_diff_00():
    assert array_diff([1, 2], [1]), [2]


def test_array_diff_01():
    assert array_diff([1, 2, 2], [1]), [2, 2]


def test_array_diff_02():
    assert array_diff([1, 2, 2], []), [1, 2, 2]


def test_TypeError():
    with pytest.raises(TypeError):
        assert array_diff(11) == [1]
