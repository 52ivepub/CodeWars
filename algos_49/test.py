import pytest

from main import solve


def test_solve_00():
    assert solve("cozy"), 51


def test_solve_01():
    assert solve("xyzzy"), 126


def test_solve_02():
    assert solve("chruschtschov"), 80


def test_error_solve_03():
    with pytest.raises(TypeError):
        assert solve({132}) == {123}
