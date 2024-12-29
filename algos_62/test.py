import pytest

from main import decipher_this


def test_decipher_this_00():
    assert decipher_this("65 119esi 111dl 111lw 108dvei 105n 97n 111ka"), "A wise old owl lived in an oak"


def test_decipher_this_01():
    assert decipher_this("84eh 109ero 104e 115wa 116eh 108sse 104e 115eokp"), "The more he saw the less he spoke"


def test_decipher_this_02():
    assert decipher_this("84eh 108sse 104e 115eokp 116eh 109ero 104e 104dare"), "The less he spoke the more he heard"


def test_error_decipher_this_03():
    with pytest.raises(AttributeError):
        assert decipher_this([]) == []
