url = ''

strg = "01|15|59, 1|47|16, 01|17|20, 1|32|34, 2|17|17"
# ),
#             "Range: 01|01|18 Average: 01|38|05 Median: 01|32|34"


def stat(strg):
    res = []
    all_time_second = []
    strg_split = strg.split(', ')
    if len(strg) == 0:
        return ''
    for i in strg_split:
        run = [int(i) for i in i.split('|')]
        run = run[0] * 3600 + run[1] * 60 + run[2]
        all_time_second.append(run)
    range = max(all_time_second) - min(all_time_second)
    average = sum(all_time_second)//len(all_time_second)
    ats = sorted(all_time_second)
    if len(all_time_second) % 2 == 0:
        median = (ats[(len(ats)//2) - 1] + ats[len(ats)//2])//2
    else:
        median = ats[(len(ats) // 2)]
    for i in [range, average, median]:
        seed = []
        m, s = divmod(i, 60)
        h, m = divmod(m, 60)
        for i in [h, m, s]:
            if len(str(i)) < 2:
                seed.append(f'0{i}')
            else:
                seed.append(f'{i}')
        res.append('|'.join(seed))
    return f'Range: {res[0]} Average: {res[1]} Median: {res[2]}'



print(stat(strg))

