import pytest

from main import highest_rank


def test_highest_rank_00():
    assert highest_rank([12, 10, 8, 12, 7, 6, 4, 10, 12]), 12


def test_highest_rank_01():
    assert highest_rank([12, 10, 8, 12, 7, 6, 4, 10, 12, 10]), 12


def test_highest_rank_02():
    assert highest_rank([1, 2, 3]), 3


def test_error_highest_rank_03():
    with pytest.raises(ValueError):
        assert highest_rank([]) == []
