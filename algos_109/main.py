url = 'https://www.codewars.com/kata/566fc12495810954b1000030'

n, d = 5750, 0
# ), 4700

def nb_dig(n, d):
    list_square = [str(i**2) for i in range(n+1)]
    remain_list = [i.count(str(d)) for i in list_square if str(d) in i]
    return  sum(remain_list)
    # remain_list = []
    # for i in list_square:
    #     if


print(nb_dig(n, d))