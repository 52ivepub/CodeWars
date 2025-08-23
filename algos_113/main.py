url = 'https://www.codewars.com/kata/59325dc15dbb44b2440000af/train/python'

s = "amazon"
# ), True


def is_alt(s):
    for i in range(len(s)-1):
        if s[i] in "aeiou" and s[i+1] in "aeiou":
            return False
    first = all(True if s[i] in "aeiou" else False for i in range(0, len(s), 2))
    second = all(True if s[i] in "aeiou" else False for i in range(1, len(s), 2))
    if first or second is True:
        return True
    return False







print(is_alt(s))