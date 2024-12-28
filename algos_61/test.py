import pytest

from main import longest_repetition


def test_longest_repetition_00():
    assert longest_repetition("aaaabb"), ('a', 4)


def test_longest_repetition_01():
    assert longest_repetition("bbbaaabaaaa"), ('a', 4)


def test_longest_repetition_02():
    assert longest_repetition(""), ('', 0)


def test_error_longest_repetition_03():
    with pytest.raises(TypeError):
        assert longest_repetition(11) == 11
