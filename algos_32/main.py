url = 'https://www.codewars.com/kata/5626b561280a42ecc50000d1'

a = 90
b = 100
# ), [1, 2, 3, 4, 5, 6, 7, 8, 9]


def sum_dig_pow(a, b): # range(a, b + 1) will be studied by the function
    res = []
    for i in range(a, b + 1):
        if i < 10:
            res.append(i)
            continue
        num = dict(enumerate([int(x) for x in str(i)], start=1))
        summary = sum(num[y] ** y for y in range(1, len(str(i)) + 1))
        if summary == i: res.append(i)
    return res



print(sum_dig_pow(a, b))