url = 'https://www.codewars.com/kata/58223370aef9fc03fd000071/train/python'

n = -1
# ),
# "2-7-4


def dashatize(n):
    res = ''
    n = abs(n)
    for i in range(len(str(n))):
        if int(str(n)[i]) % 2 == 0:
            res += str(n)[i]
        else:
            res += f'-{str(n)[i]}-'
    return res.strip('-').replace("--", "-")



print(dashatize(n))