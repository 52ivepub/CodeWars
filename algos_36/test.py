import pytest

from main import multiplication_table


def test_multiplication_table_00():
    assert multiplication_table(3), [[1, 2, 3], [2, 4, 6], [3, 6, 9]]


def test_multiplication_table_01():
    assert multiplication_table(4), [[1, 2, 3, 4], [2, 4, 6, 8], [3, 6, 9, 12], [4, 8, 12, 16]]


def test_multiplication_table_02():
    assert multiplication_table(5), [[1, 2, 3, 4, 5], [2, 4, 6, 8, 10], [3, 6, 9, 12, 15], [4, 8, 12, 16, 20], [5, 10, 15, 20, 25]]


def test_error():
    with pytest.raises(TypeError):
        assert multiplication_table("123") == "123"
