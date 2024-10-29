source_array = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
# =>            [1, 8, 3, 6, 5, 4, 7, 2, 9, 0]


def sort_array(source_array):
    odd = sorted([i for i in source_array if i % 2 != 0], reverse=True)
    return [i if i % 2 == 0 else odd.pop() for i in source_array]


print(sort_array(source_array))







# odd = sorted([i for i in source_array if i % 2 != 0])
# res = []
# for i in source_array:
#     if i % 2 == 0:
#         res.append(i)
#     else:
#         res.append(odd[0])
#         odd.pop(0)
# return res
