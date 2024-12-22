import pytest

from main import nb_months


def test_nb_months_00():
    assert nb_months(2000, 8000, 1000, 1.5), [6, 766]


def test_nb_months_01():
    assert nb_months(12000, 8000, 1000, 1.5) ,[0, 4000]


def test_nb_months_02():
    assert nb_months(7500, 32000, 300, 1.55), [25, 122]


def test_error_nb_months_03():
    with pytest.raises(TypeError):
        assert nb_months([]) == []
