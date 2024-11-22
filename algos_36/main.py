url = 'https://www.codewars.com/kata/534d2f5b5371ecf8d2000a08'

size = 5
# [[1, 2, 3], [2, 4, 6], [3, 6, 9]]


def multiplication_table(size):
    res = []
    for x in range(1, size + 1):
        row = []
        for y in range(1, size+1):
            row.append(x * y)
        res.append(row)
    return res



print(multiplication_table(size))