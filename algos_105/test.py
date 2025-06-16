import pytest

from main import printer_error


def test_printer_error_00():
    assert printer_error("aaaaaaaaaaaaaaaabbbbbbbbbbbbbbbbbbmmmmmmmmmmmmmmmmmmmxyz") ==  "3/56"


def test_printer_error_01():
    assert printer_error("kkkwwwaaaaaaaaaaaaaabbbbbbbbbbbbbbbbbbmmmmmmmmmmmmmmmmmmmxyz"), "6/60"


def test_printer_error_02():
    assert printer_error("kkkwwwaaaaaaaaaaaaaabbbbbbbbbbbbbbbbbbmmmmmmmmmmmmmmmmmmmxyzuuuuu"), "11/65"


def test_error_printer_error_03():
    with pytest.raises(TypeError):
        assert printer_error(123) == 132
