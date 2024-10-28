import pytest

from main import find_uniq


def test_find_uniq_00():
    assert find_uniq([ 1, 1, 1, 2, 1, 1 ]), (2)


def test_find_uniq_01():
    assert find_uniq([ 0, 0, 0.55, 0, 0 ]), (0.55)


def test_find_uniq_02():
    assert find_uniq([ 3, 10, 3, 3, 3 ]), (10)


def test_error():
    with pytest.raises(AttributeError):
        assert find_uniq(1.25) == '1'
