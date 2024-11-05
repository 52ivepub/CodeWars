import pytest

from main import count_smileys


def test_count_smileys_00():
    assert count_smileys([]) ==  (0)


def test_count_smileys_01():
    assert count_smileys([':D',':~)',';~D',':)']), (4)


def test_count_smileys_02():
    assert count_smileys([':)',':(',':D',':O',':;']), (2)


def test_error():
    with pytest.raises(TypeError):
        assert count_smileys([1.25]) == 1
