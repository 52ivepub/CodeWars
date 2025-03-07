import pytest

from main import hex_string_to_RGB


def test_hex_string_to_RGB_00():
    assert hex_string_to_RGB("#FF9933"), {'r':255, 'g':153, 'b':51}


def test_hex_string_to_RGB_01():
    assert hex_string_to_RGB("#beaded"), {'r':190, 'g':173, 'b':237}


def test_hex_string_to_RGB_02():
    assert hex_string_to_RGB("#000000"), {'r':0, 'g':0, 'b':0}


def test_error_hex_string_to_RGB_03():
    with pytest.raises(TypeError):
        assert hex_string_to_RGB(None) == None
