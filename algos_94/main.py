
url = ''
n = 5

def series_sum(n):
    res = 0.00
    seed = 1.00
    for _ in range(n):
        res += 1/seed
        seed += 3
    res =  str(round(res, 2))
    while len(res) < 4:
        res += '0'
    return res



print(series_sum(n))

