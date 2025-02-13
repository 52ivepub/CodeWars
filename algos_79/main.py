


url = 'https://www.codewars.com/kata/5596f6e9529e9ab6fb000014/train/python'

first, second = "dog", "god"
# => 2


def shifted_diff(first, second):
    count = 0
    for place in range(len(first)):
        if first == second:
            return count
        else:
            first = first[-1] + first[:-1]
            count += 1
    return -1
    first.find(first)



print(shifted_diff(first, second))