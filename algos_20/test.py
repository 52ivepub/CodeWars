import pytest

from main import solution


def test_solution_00():
    assert solution("helloWorld"), ("hello World")


def test_solution_01():
    assert solution("camelCase"), ("camel Case")


def test_solution_02():
    assert solution("breakCamelCase"), ("break Camel Case")


def test_error():
    with pytest.raises(TypeError):
        assert solution(1.25) == '1'
