import pytest

from main import solution


def test_solution_00():
    assert solution(10) == 23


def test_solution_01():
    assert solution(-1) == 0


def test_solution_02():
    assert solution(20) == 78


def test_error_solution_03():
    with pytest.raises(TypeError):
        assert solution('123') == '123'
