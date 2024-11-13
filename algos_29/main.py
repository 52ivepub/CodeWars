array1 = ["live", "arp", "strong"]
array2 = ["lively", "alive", "harp", "sharp", "armstrong"]
# r = ['arp', 'live', 'strong']


def in_array(array1, array2):
    res = []
    for x in array1:
        math = [x for y in array2 if x in y]
        if math:
            res.append(x)
    res = list(set(res))
    res.sort()
    return res


print(in_array(array1, array2))