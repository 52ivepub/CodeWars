import pytest

from main import dashatize


def test_dashatize_00():
    assert dashatize(274),"2-7-4"


def test_dashatize_01():
    assert dashatize( 5311),"5-3-1-1"


def test_dashatize_02():
    assert dashatize(974302),"9-7-4-3-02"


def test_error_dashatize_03():
    with pytest.raises(TypeError):
        assert dashatize([]) == []
