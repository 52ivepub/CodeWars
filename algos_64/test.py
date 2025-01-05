import pytest

from main import dup


def test_dup_00():
    assert dup(["ccooddddddewwwaaaaarrrrsssss","piccaninny","hubbubbubboo"]),['codewars','picaniny','hubububo']


def test_dup_01():
    assert dup(["abracadabra","allottee","assessee"]),['abracadabra','alote','asese']


def test_dup_02():
    assert dup(["kelless","keenness"]), ['keles','kenes']


def test_error_dup_03():
    with pytest.raises(TypeError):
        assert dup(11) == 11
