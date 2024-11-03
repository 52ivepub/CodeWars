_prod = 1


# [55, 89, True]


def product_fib(_prod):
    fib_a, fib_b = 0, 1
    def fibonachi():
        nonlocal fib_a, fib_b
        while fib_a * fib_b < _prod:
            fib_a, fib_b = fib_b, fib_a + fib_b
    fibonachi()
    if fib_a * fib_b == _prod:
        return [fib_a, fib_b, True]
    else:
        return [fib_a, fib_b, False]



print(product_fib(_prod))
