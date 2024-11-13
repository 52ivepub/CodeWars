import pytest

from main import in_array


def test_in_array_00():
    assert in_array(["live", "arp", "strong"] ,
         ["lively", "alive", "harp", "sharp", "armstrong"]),  ['arp', 'live', 'strong']


def test_in_array_01():
    assert in_array(["arp", "mice", "bull"] , ["lively", "alive", "harp", "sharp", "armstrong"]), ['arp']


# def test_in_array_02():
#     assert in_array(30, 0.66, 1.5), (15)


def test_error():
    with pytest.raises(TypeError):
        assert in_array(444) == 222
