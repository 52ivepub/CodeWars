import pytest

from main import format_duration


def test_format_duration_00():
    assert format_duration(132030240), "4 years, 68 days, 3 hours and 4 minutes"


def test_format_duration_01():
    assert format_duration(1), "1 second"


def test_format_duration_02():
    assert format_duration(0), "now"


def test_error_format_duration_03():
    with pytest.raises(TypeError):
        assert format_duration(None) == None
