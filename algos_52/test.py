import pytest

from main import choose_best_sum


def test_choose_best_sum_00():
    assert choose_best_sum(230, 3, [91, 74, 73, 85, 73, 81, 87]) == 228


def test_choose_best_sum_01():
    assert choose_best_sum(230, 4, [100, 76, 56, 44, 89,
                                    73, 68, 56, 64, 123, 2333, 144, 50, 132, 123, 34, 89]) == 230


def test_choose_best_sum_02():
    assert choose_best_sum(230, 4, [100, 64, 123, 2333, 144, 50, 132, 123, 34, 89]) == None


def test_error_choose_best_sum_03():
    with pytest.raises(TypeError):
        assert choose_best_sum({132}) == {123}
