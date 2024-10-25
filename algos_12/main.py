n, p = 8, 3
# ), 1)


def dig_pow(n, p):
    digit_n = list(enumerate(str(n), start=p))
    product_num_n = sum([int(i[1]) ** i[0] for i in digit_n])
    result = [i for i in range(100000) if n * i == product_num_n]
    if result:
        return result[0]
    return -1





print(dig_pow(n, p))