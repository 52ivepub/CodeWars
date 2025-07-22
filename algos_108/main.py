from itertools import permutations

url = 'https://www.codewars.com/kata/5659c6d896bc135c4c00021e'
# https://www.codewars.com/kata/next-bigger-number-with-the-same-digits

n = 414


# ) == 2017

def next_smaller(n):
    set_n = []

    set_n.append(str(n)[::-1])
    for lap in range(len(str(n))):
        x = str(n)[lap]
        for i in range(len(str(n)) - 1):

            if i + 1 >= len(str(n)) - 1:
                i = -1
                x += str(n)[i + 1]
            else:
                x += str(n)[i + 1]
        set_n.append(x)
    return set_n


# print(next_smaller(n))

def next_smaller_simplicity(n):
    x = [i for i in str(n)]
    y = list(permutations(x, len(x)))
    if len(y) < 2: return -1
    res = []
    for i in y:
        i = int(''.join(i))
        if len(str(i)) == len(x) and i not in res:
            res.append(i)
    list_option = sorted(res, reverse=True)
    index_seed = list_option.index(n)
    if index_seed == len(list_option) - 1:
        return -1
    return list_option[index_seed + 1]


print(next_smaller_simplicity(n))
