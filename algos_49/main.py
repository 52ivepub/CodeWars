url = 'https://www.codewars.com/kata/59c633e7dcc4053512000073/train/python'

s = "cozy"
# -> 26


def solve(s):
    res, count = [], 0
    for i in s:
        if i in "aeiou":
            res.append(count)
            count = 0
        else:
            count += ord(i) - 96
    res.append(count)
    return max(res)



print(solve(s))
