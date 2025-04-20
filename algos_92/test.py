import pytest

from main import nb_year


def test_nb_year_00():
    assert nb_year(1500, 5, 100, 5000), 15


def test_nb_year_01():
    assert nb_year(1500000, 2.5, 10000, 2000000), 10


def test_nb_year_02():
    assert nb_year(1500000, 0.25, 1000, 2000000), 94


def test_error_nb_year_03():
    with pytest.raises(TypeError):
        assert nb_year(None) == None
