import pytest

from main import is_merge


def test_is_merge_00():
    assert is_merge('codewars', 'code', 'wars'), True


def test_is_merge_01():
    assert is_merge('codewars', 'cdw', 'oears'),True


def test_is_merge_02():
    assert is_merge('codewars', 'cod', 'wars') == False


def test_error_is_merge_03():
    with pytest.raises(TypeError):
        assert is_merge(None) == None
