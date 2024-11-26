url = 'https://www.codewars.com/kata/51e0007c1f9378fa810002a9/train/python'

data = "iiisdoso"
# should return numbers [8, 64].


def parse(data):
    seed = 0
    res = []
    for i in data:
        if i == "i":
            seed += 1
        elif i == "d":
            seed -= 1
        elif i == "s":
            seed = seed**2
        elif i == "o":
            res.append(seed)
    return res



print(parse(data))



