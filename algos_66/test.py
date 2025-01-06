import pytest

from main import matrix_addition


def test_matrix_addition_00():
    assert matrix_addition(  [ [1, 2],[1, 2] ],[ [2, 3], [2, 3] ]) == [ [3, 5], [3, 5] ]


def test_matrix_addition_01():
    assert matrix_addition( [ [1] ],[ [2] ] ) == [ [3] ]


# def test_matrix_addition_02():
#     assert matrix_addition(["gray","black","purple","purple","gray","black"]) == 3


def test_error_matrix_addition_03():
    with pytest.raises(TypeError):
        assert matrix_addition(11) == 11
