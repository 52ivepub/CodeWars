import pytest

from main import tower_builder


def test_tower_builder_00():
    assert tower_builder(1), ['*', ]


def test_tower_builder_01():
    assert tower_builder(2), [' * ', '***']


def test_tower_builder_02():
    assert tower_builder(3), ['  *  ', ' *** ', '*****']


def test_error():
    with pytest.raises(TypeError):
        assert tower_builder(1.25) == '1'
