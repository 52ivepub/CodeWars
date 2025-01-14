url = 'https://www.codewars.com/kata/5340298112fa30e786000688/train/python'

lst = [4, 3, 1, 5, 6]
# should return [(1, 3), (3, 5), (4, 6)]


def twos_difference(lst):
    res = set()
    for x in lst:
        for y in lst:
            if abs(x - y)==2 and x > y:
                res.add((y, x))
            elif abs(x - y)==2 and x < y:
                res.add((x, y))
    return sorted(res)



print(twos_difference(lst))
