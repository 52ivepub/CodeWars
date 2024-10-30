import pytest

from main import find_missing_letter


def test_find_missing_letter_00():
    assert find_missing_letter(['a','b','c','d','f']), ('e')


def test_find_missing_letter_01():
    assert find_missing_letter(['O','Q','R','S']), ('P')


def test_find_missing_letter_02():
    assert find_missing_letter(['b','d']), ('c')


def test_error():
    with pytest.raises(TypeError):
        assert find_missing_letter(1.25) == '1'
