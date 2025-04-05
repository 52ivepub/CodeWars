import pytest

from main import friend


def test_friend_00():
    assert friend(["Ryan", "Kieran", "Mark",]), ["Ryan", "Mark"]


def test_friend_01():
    assert friend(["Ryan", "Jimmy", "abc", "d", "Cool Man"]), ["Ryan"]


def test_friend_02():
    assert friend(["Jimm", "Cari", "aret", "truehdnviegkwgvke", "sixtyiscooooool"]), ["Jimm", "Cari", "aret"]


def test_error_friend_03():
    with pytest.raises(TypeError):
        assert friend(None) == None
