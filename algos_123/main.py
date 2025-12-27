url = ''

divisor, bound = 2,7
# ),6
def max_multiple(divisor, bound):
    res = 0
    if divisor == bound:
        return divisor
    while res <= bound:
        res += divisor
    if res == bound:
        return res
    return res - divisor



print(max_multiple(divisor, bound))
