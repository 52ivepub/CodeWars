import pytest

from main import string_transformer


def test_string_transformer_00():
    assert string_transformer("Example string") == "STRING eXAMPLE"


def test_string_transformer_01():
    assert string_transformer("Example Input"), "iNPUT eXAMPLE"


def test_string_transformer_02():
    assert string_transformer("To be OR not to be That is the Question"), "qUESTION THE IS tHAT BE TO NOT or BE tO"


def test_error_string_transformer_03():
    with pytest.raises(AttributeError):
        assert string_transformer(2) == 2
