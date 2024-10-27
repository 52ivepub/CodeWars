import pytest

from main import first_non_repeating_letter


def test_first_non_repeating_letter_00():
    assert first_non_repeating_letter('abba') ==  ''


def test_first_non_repeating_letter_01():
    assert first_non_repeating_letter('~><#~><'), '#'


def test_first_non_repeating_letter_02():
    assert first_non_repeating_letter('sTreSS'), 'T'


def test_error():
    with pytest.raises(TypeError):
        assert first_non_repeating_letter(000) == '1'
