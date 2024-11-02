# order = [20, 37, 20, 21]
# max_e = 1
order = [7, 7, 29, 29, 30, 29, 29, 9, 7, 18, 49, 50, 37, 50, 30, 37, 9, 7, 7, 37, 29, 29, 50, 30, 50, 50, 30, 18, 29, 45, 50, 37, 29, 18, 14, 37, 30, 14, 14, 18, 29, 37, 37, 7, 30, 37, 30, 29, 7, 9, 14, 50, 37, 14, 45, 14, 50, 18, 7, 18]
max_e = 8
# [7, 7, 29, 29, 30, 29, 29, 9, 7, 18, 49, 50, 37, 50, 30, 37, 9, 7, 7, 37, 29, 29, 50, 30, 50, 50, 30, 18, 29, 45, 50, 37, 29, 18, 14, 37, 30, 14, 14, 18, 29, 37, 37, 7, 30, 37, 30, 29, 7, 9, 14, 50, 37, 14, 45, 14, 50, 18, 7, 18]
# [7, 7, 29, 29, 30, 29, 29, 9, 7, 18, 49, 50, 37, 50, 30, 37, 9, 7, 7, 37, 29, 29, 50, 30, 50, 50, 30, 18, 29, 45, 50, 37, 29, 18, 14, 37, 30, 14, 14, 18, 37, 37, 7, 30, 37, 30, 7, 9, 14, 50, 14, 45, 14, 50, 18, 7, 18]

# [7, 7, 29, 29, 30, 29, 29, 9, 7, 18, 49, 50, 37, 50, 30, 37, 9, 7, 7, 37, 29, 29, 50, 30, 50, 50, 30, 18, 29, 45, 50, 37, 29, 18, 14, 37, 30, 14, 14, 18, 37, 37, 7, 30, 37, 30, 7, 9, 14, 50, 14, 45, 14, 50, 18, 7, 18]

# max_e =  3
# [1, 2, 3, 1, 1, 2, 2, 3, 3, 4, 5]



def delete_nth(order ,max_e):
    if len(order) == 0:
        return []
    reverse_order = order[::-1]
    for i in order:
        if reverse_order.count(i) > max_e:
            reverse_order.remove(i)
        remain = [i for i in reverse_order if reverse_order.count(i) > max_e]
        if remain == []:
            return reverse_order[::-1]


print(delete_nth(order, max_e))







# def delete_nth(order ,max_e):
#     seed = [(x, y) for x, y in enumerate(order)]
#     seed_sort = [i for i in seed if order.count(i[1]) > max_e]
#     subtract = len(seed_sort) - max_e
#     for _ in range(subtract):
#         seed.remove(seed_sort[-1])
#         seed_sort.pop()
#     return [i[1] for i in seed]





