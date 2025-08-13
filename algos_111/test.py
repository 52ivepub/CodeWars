import pytest

from main import CaesarCipher


def test_CaesarCipher_00():
    assert CaesarCipher(5).encode('Codewars') == 'HTIJBFWX'


def test_CaesarCipher_01():
    assert CaesarCipher(5).decode('HTIJBFWX') == 'CODEWARS'


# def test_CaesarCipher_02():
#     assert CaesarCipher()


def test_error_CaesarCipher_03():
    with pytest.raises(AttributeError):
        assert CaesarCipher(123).decode(123) == 132
