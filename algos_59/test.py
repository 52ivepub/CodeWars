import pytest

from main import kebabize


def test_kebabize_00():
    assert kebabize('myCamelCasedString'), 'my-camel-cased-string'


def test_kebabize_01():
    assert kebabize('myCamelHas3Humps'), 'my-camel-has-humps'


def test_kebabize_02():
    assert kebabize('SOS'), 's-o-s'


def test_error_kebabize_03():
    with pytest.raises(TypeError):
        assert kebabize(12) == 12
