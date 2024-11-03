import pytest

from main import product_fib


def test_product_fib_00():
    assert product_fib(4895), ([55, 89, True])


def test_product_fib_01():
    assert product_fib(5895), ([89, 144, False])


# def test_product_fib_02():
#     assert product_fib("breakCamelCase"), ("break Camel Case")


def test_error():
    with pytest.raises(TypeError):
        assert product_fib("1.25") == '1'
