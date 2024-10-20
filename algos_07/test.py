import pytest

from main import generate_hashtag


def test_generate_hashtag_00():
    assert generate_hashtag('Codewars'), '#Codewars'


def test_generate_hashtag_01():
    assert generate_hashtag('Codewars      '), '#Codewars'


def test_generate_hashtag_02():
    assert generate_hashtag('CoDeWaRs is niCe'), '#CodewarsIsNice'


def test_error():
    with pytest.raises(AttributeError):
        assert generate_hashtag(0) == 1
