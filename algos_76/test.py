import pytest

from main import format_words


def test_format_words_00():
    assert format_words(['one', 'two', 'three', 'four']), 'one, two, three and four'


def test_format_words_01():
    assert format_words(['one']), 'one'


def test_format_words_02():
    assert format_words(['one', '', 'three']), 'one and three'


def test_error_format_words_03():
    with pytest.raises(TypeError):
        assert format_words(2) == 2
