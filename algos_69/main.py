url = 'https://www.codewars.com/kata/55eeddff3f64c954c2000059/train/python'

lst = [0, 1, 1, 2, 2]
# ),[0, 2, 4]
# should return [1,12,0,4,6,1]


def sum_consecutives(lst):
    res = []
    seed = 0
    for i in range(len(lst)-1):
        if lst[i] == lst[i+1]:
            seed += lst[i]
        elif seed:
            seed += lst[i]
            res.append(seed)
            seed = 0
        else:
            res.append(lst[i])
    if seed:
        res.append(lst[-1] + seed)
    else:
        res.append(lst[-1])
    return res




print(sum_consecutives(lst))
