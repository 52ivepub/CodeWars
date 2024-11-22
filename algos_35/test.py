import pytest

from main import to_weird_case


def test_to_weird_case_00():
    assert to_weird_case('This'), 'ThIs'


def test_to_weird_case_01():
    assert to_weird_case('THIs iS a TEST'), 'ThIs Is A TeSt'


def test_to_weird_case_02():
    assert to_weird_case("Weird string case"), "WeIrD StRiNg CaSe"


def test_error():
    with pytest.raises(AttributeError):
        assert to_weird_case(123) == 123
