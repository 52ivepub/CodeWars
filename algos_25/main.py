array1 = [121, 144, 19, 161, 19, 144, 19, 11]
array2 = [121, 14641, 20736, 361, 25921, 361, 20736, 361]


def comp(array1, array2):
    if type(array1) != list or type(array2) != list:
        return False
    elif len(array2) == len(array1):
        res = list(map(lambda x: x ** 2, array1))
        return all(res.count(i) == array2.count(i) for i in res)
    return False


print(comp(array1, array2))


