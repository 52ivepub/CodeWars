url = 'https://www.codewars.com/kata/586d6cefbcc21eed7a001155/train/python'

chars = "bbbaaabaaaa"
         # , ('a', 4))


def longest_repetition(chars):
    if len(chars) == 0: return ('', 0)
    count_chars = []
    count = 1
    for i in range(len(chars)-1):
        if chars[i] == chars[i+1]:
            count += 1
        else:
            count_chars.append((chars[i], count))
            count = 1
    count_chars.append((chars[-1], count))
    return max(count_chars, key=lambda x:x[1])




print(longest_repetition(chars))

