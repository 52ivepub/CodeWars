url = 'https://www.codewars.com/kata/54dc6f5a224c26032800005c/train/python'


stocklist = ["ABART 20", "CDXEF 50", "BKWRK 25", "BTSQZ 89", "DRTYM 60"]
categories = ["A", "B", "C", "W"]


def stock_list(stocklist, categories):
    k = any(i[0] in categories for i in stocklist)
    res = ''
    seed = {x : 0 for x in categories}
    for i in categories:
        for x in stocklist:
            if i == x.split()[0][0]:
                if i in seed:
                    seed[i] += int(x.split()[1])
                else:
                    seed[i] = int(x.split()[1])

    for x, y in seed.items():
        res += f"({x} : {y}) - "
    return res[:-3]





print(stock_list(stocklist, categories))