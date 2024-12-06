import pytest

from main import encrypt_this


def test_encrypt_this_00():
    assert encrypt_this("A wise old owl lived in an oak"), "65 119esi 111dl 111lw 108dvei 105n 97n 111ka"


def test_encrypt_this_01():
    assert encrypt_this("The more he saw the less he spoke"), "84eh 109ero 104e 115wa 116eh 108sse 104e 115eokp"


def test_encrypt_this_02():
    assert encrypt_this("The less he spoke the more he heard"), "84eh 108sse 104e 115eokp 116eh 109ero 104e 104dare"


def test_error_encrypt_this_03():
    with pytest.raises(AttributeError):
        assert encrypt_this({132}) == {123}
