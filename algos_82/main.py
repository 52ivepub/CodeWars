url = 'https://www.codewars.com/kata/5550d638a99ddb113e0000a2/train/python'

items,k = [1,2,3,4,5,6,7], 3
# ),[3, 6, 2, 7, 5, 1, 4]


def josephus(items,k):
    res = []
    place = 0
    step = 1
    while len(items) > 0:
        if place + k <= len(items):
            res.append(items[place+k-step])
            items.pop(place+k-step)
            place = place+k-step
        else:
            place = place - len(items)
    return res




print(josephus(items, k))