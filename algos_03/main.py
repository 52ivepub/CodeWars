n = 1234
# ), 1)


def count_bits(n):
    return format(n, 'b').count('1')


print(count_bits(n))