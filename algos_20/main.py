# order = [20, 37, 20, 21]
# max_e = 1
order = [1, 2, 3, 1, 1, 2, 1, 2, 3, 3, 2, 4, 5, 3, 1]
max_e =  3
# [1, 2, 3, 1, 1, 2, 2, 3, 3, 4, 5]



def delete_nth(order ,max_e):
    if len(order) == 0:
        return []
    reverse_order = order[::-1]
    for i in order:
        if order.count(i) > max_e:
            reverse_order.remove(i)
        remain = [i for i in reverse_order if reverse_order.count(i) > max_e]
        if remain == []:
            return reverse_order[::-1]
        # else:
        #     continue


print(delete_nth(order, max_e))







# def delete_nth(order ,max_e):
#     seed = [(x, y) for x, y in enumerate(order)]
#     seed_sort = [i for i in seed if order.count(i[1]) > max_e]
#     subtract = len(seed_sort) - max_e
#     for _ in range(subtract):
#         seed.remove(seed_sort[-1])
#         seed_sort.pop()
#     return [i[1] for i in seed]





