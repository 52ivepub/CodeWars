from pprint import pprint

url = 'https://www.codewars.com/kata/54a2e93b22d236498400134b/train/python'

phrase = "abcdefghijklmnopqrstuvwxyz"
# ), 9


def presses(phrase):
    alphavit = ['1', 'ABC2', 'DEF3', 'GHI4', 'JKL5', 'MNO6', 'PQRS7', 'TUV8', 'WXYZ9', '*', ' 0', '#']
    count = 0
    for i in phrase.upper():
        for char in alphavit:
            if i in char:
                count += char.index(i) + 1
    return count








pprint(presses(phrase))

# x = 'LOG'
# print(x.index('G'))