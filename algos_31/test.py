import pytest

from main import wave


def test_wave_00():
    assert wave("hello"), ["Hello", "hEllo", "heLlo", "helLo", "hellO"]


def test_wave_01():
    assert wave("codewars"),["Codewars", "cOdewars", "coDewars", "codEwars", "codeWars", "codewArs", "codewaRs", "codewarS"]


def test_wave_02():
    assert wave("two words"),["Two words", "tWo words", "twO words", "two Words", "two wOrds", "two woRds", "two worDs", "two wordS"]


def test_error():
    with pytest.raises(TypeError):
        assert wave(234) == 213
