import pytest

from main import check_exam


def test_check_exam_00():
    assert check_exam(["a", "a", "b", "b"], ["a", "c", "b", "d"]), 6


def test_check_exam_01():
    assert check_exam(["a", "a", "c", "b"], ["a", "a", "b",  ""]), 7


def test_check_exam_02():
    assert check_exam(["a", "a", "b", "c"], ["a", "a", "b", "c"]), 16


def test_error_check_exam_03():
    with pytest.raises(TypeError):
        assert check_exam(123, 123) == 'aaa'
