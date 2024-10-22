import pytest

from main import persistence


def test_persistence_00():
    assert persistence(39), (3)


def test_persistence_01():
    assert persistence(4) == (0)


def test_persistence_02():
    assert persistence(999) == (4)


def test_error():
    with pytest.raises(AssertionError):
        assert persistence('0') == '1'
