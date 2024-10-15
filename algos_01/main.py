a, b = [1,2,2], [1]
# , [2,2]


def array_diff(a, b):
    return [i for i in a if i not in b]


print(array_diff(a, b))