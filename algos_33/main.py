url = 'https://www.codewars.com/kata/5503013e34137eeeaa001648/train/python'

n = 5


def diamond(n):
    # Make some diamonds!
    res = ''
    if n % 2 == 0 or n < 0:
        return None
    diamonds_start = list(range(1, n, 2))
    diamonds_end = diamonds_start[::-1]
    diamonds_start.append(n)
    diamonds_start.extend(diamonds_end)
    list_space = [" " * i for i in range(n//2, -1, -1)]
    list_space.extend(list_space[(n//2 - 1)::-1])
    for i in range(len(diamonds_start)):
        res += list_space[i] + ("*" * diamonds_start[i]) + "\n"
    return res






print(diamond(n))

x = ['a', "b", "c"]
x.extend(x[-2: :-1])
print(x)

