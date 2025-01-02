url = 'https://www.codewars.com/kata/58235a167a8cb37e1a0000db/train/python'

gloves = ["red", "green", "red", "blue", "blue"]


def number_of_pairs(gloves):
    result_dict = {}
    res = 0
    for i in sorted(gloves):
        if i in result_dict:
            result_dict[i] += 1
        else:
            result_dict[i] = 1
    for x, y in result_dict.items():
        res += y // 2
    return res





print(number_of_pairs(gloves))