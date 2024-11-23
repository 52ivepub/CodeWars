url = 'https://www.codewars.com/kata/55c6126177c9441a570000cc/train/python'

strng = "2000 10003 1234000 44444444 9999 11 11 22 123"
# ), "11 11 2000 10003 22 123 1234000 44444444 9999"


def order_weight(strng):
    strng_sum = []
    for x in strng.split():
        count = sum([int(y) for y in x])
        strng_sum.append([count, x])
    res = sorted(strng_sum, key=lambda x: (int(x[0]), x[1]))
    return " ".join([i[1] for i in res])


print(order_weight(strng))