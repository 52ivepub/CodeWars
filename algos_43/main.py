url = 'https://www.codewars.com/kata/55aa075506463dac6600010d/train/python'

m = 1
n = 250
# ), [[1, 1], [42, 2500], [246, 84100]])



def list_squared(m, n):
    res = []
    for i in range(m, n + 1):
        divicors = []
        for x in range(1, i + 1):
            if i % x == 0:
                divicors.append(x)
        div_square = [y**2 for y in divicors]
        sum_div_square = (sum(div_square) ** (1/2))
        if str(sum_div_square).split('.')[1] == "0":
            res.append([i, int(sum_div_square)**2])
    return res



print(list_squared(m, n))


# def list_squared(m, n):
#     res = []
#     for i in range(m, n + 1):
#         divicors = []
#         for x in range(1, i + 1):
#             if i % x == 0:
#                 divicors.append(x)
#         div_square = list(map(lambda y: y**2, divicors))
#         sum_div_square = (sum(div_square) ** (1/2))
#         if str(sum_div_square).split('.')[1] == "0":
#             res.append([i, int(sum_div_square)**2])
#     return res
