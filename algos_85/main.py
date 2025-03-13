url = 'https://www.codewars.com/kata/54c9fcad28ec4c6e680011aa/train/python'

s, part1, part2 = 'codewars', 'cod', 'wars'


def is_merge(s, part1, part2):
    dict_sort =  dict(sorted({i: list(s).count(i) for i in list(s)}.items()))
    parts = part1 + part2
    res = dict(sorted({i: list(parts).count(i) for i in list(parts)}.items()))
    return dict_sort == res



print(is_merge(s, part1, part2))


