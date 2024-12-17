url = 'https://www.codewars.com/kata/57ea70aa5500adfe8a000110/train/python'

array, runs = [2], 1
# [427]


def fold_array(array, runs):
    seed = array
    for j in range(runs):
        res = []
        if len(seed) % 2 == 0:
            for i in range(len(seed)//2):
                res.append(seed[i] + seed[-(i+1)])
        else:
            for i in range(len(seed)//2):
                res.append(seed[i] + seed[-(i+1)])
                if i == len(seed)//2 - 1:
                    res.append(seed[i + 1])
        if len(seed) == 1:
            return seed
        elif len(res) == 1:
            return res
        seed = res
    return res



print(fold_array(array, runs))