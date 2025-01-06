from pprint import pprint

url = ''

a = [[1, 2, 3],
    [3, 2, 1],
    [1, 1, 1]]
b = [ [2, 2, 1],
    [3, 2, 3],
    [1, 1, 3]]

# // returns:
#   [ [3, 4, 4],
#     [6, 4, 4],
#     [2, 2, 4] ]

def matrix_addition(a, b):
    res = []
    for i in range(len(a)):
        seed = []
        for x in range(len(b)):
            seed.append(a[i][x] + b[i][x])
        res.append(seed)
    return res


pprint(matrix_addition(a, b), width=30)