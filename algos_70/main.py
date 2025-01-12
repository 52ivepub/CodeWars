url = ''

n = 2147483647
# ), '2,147,483,647'


def group_by_commas(n):
    n_str_revers = str(n)[::-1]
    res = ''
    for i in range(0, len(n_str_revers), 3):
        res = f'{res}{n_str_revers[i:i+3]},'
    return res.strip(',')[::-1]







print(group_by_commas(n))