url = ''

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
