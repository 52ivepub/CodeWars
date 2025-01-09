import pytest

from main import is_solved


def test_is_solved_00():
    assert is_solved([[0, 0, 1],
                      [0, 1, 2],
                      [2, 1, 0]]) == -1


def test_is_solved_01():
    assert is_solved([[1, 1, 1],
                      [0, 2, 2],
                      [0, 0, 0]]) == 1


def test_is_solved_02():
    assert is_solved([[2, 1, 2],
                      [2, 1, 1],
                      [1, 1, 2]]) == 1


def test_error_is_solved_03():
    with pytest.raises(TypeError):
        assert is_solved(11) == 11
