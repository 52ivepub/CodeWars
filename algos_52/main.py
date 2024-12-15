url = 'https://www.codewars.com/kata/55e7280b40e1c4a06d0000aa/train/python'

ts = [91, 74, 73, 85, 73, 81, 87]
t, k = 331, 2
# , 178)





def choose_best_sum(t, k, ls):
    def combs(a):
        if len(a) == 0:
            return [[]]
        cs = []
        for c in combs(a[1:]):
            cs += [c, c + [a[0]]]
        return cs
    all_ls = [i for i in combs(ls) if len(i) == k]
    remains = {t - sum(y): x for x, y in enumerate(all_ls) if t - sum(y) >= 0}
    if remains:
        return t - min(remains.items())[0]
    return None




# print(choose_best_sum(t, k, ls=ts))

