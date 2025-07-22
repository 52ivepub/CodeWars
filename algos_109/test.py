import pytest

from main import nb_dig


def test_nb_dig_00():
    assert nb_dig(5750, 0), 4700


def test_nb_dig_01():
    assert nb_dig(11011, 2), 9481


def test_nb_dig_02():
    assert nb_dig(12224, 8), 7733


def test_error_nb_dig_03():
    with pytest.raises(TypeError):
        assert nb_dig(123) == 132
