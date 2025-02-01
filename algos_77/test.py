import pytest

from main import delete_digit


def test_delete_digit_00():
    assert delete_digit(['one', 'two', 'three', 'four']), 'one, two, three and four'


def test_delete_digit_01():
    assert delete_digit(['one']), 'one'


def test_delete_digit_02():
    assert delete_digit(['one', '', 'three']), 'one and three'


def test_error_delete_digit_03():
    with pytest.raises(TypeError):
        assert delete_digit(2) == 2
