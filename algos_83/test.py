import pytest

from main import beeramid


def test_beeramid_00():
    assert beeramid(9, 2), 1


def test_beeramid_01():
    assert beeramid(10, 2), 2


def test_beeramid_02():
    assert beeramid(454, 5), 5


def test_error_beeramid_03():
    with pytest.raises(TypeError):
        assert beeramid(None) == None
