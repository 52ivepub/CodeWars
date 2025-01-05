url = 'https://www.codewars.com/kata/59f08f89a5e129c543000069/train/python'

arry = ["ccooddddddewwwaaaaarrrrsssss","piccaninny","hubbubbubboo"]
# ),['codewars','picaniny','hubububo']


def dup(arry):
    res = []
    seed = ''
    for word in arry:
        for char in range(len(word)):
            if len(seed) == 0:
                seed += word[char]
            if word[char] == seed[-1]:
                continue
            seed += word[char]
        res.append(seed)
        seed = ''
    return res






print(dup(arry))
