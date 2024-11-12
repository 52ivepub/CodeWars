import pytest

from main import bouncing_ball


def test_bouncing_ball_00():
    assert bouncing_ball(2, 0.5, 1), (1)


def test_bouncing_ball_01():
    assert bouncing_ball(3, 0.66, 1.5), (3)


def test_bouncing_ball_02():
    assert bouncing_ball(30, 0.66, 1.5), (15)


def test_error():
    with pytest.raises(TypeError):
        assert bouncing_ball("a") == "1"
