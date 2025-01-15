url = 'https://www.codewars.com/kata/5878520d52628a092f0002d0/train/python'

s = "You Know When  THAT  Hotline Bling"
# ), "bLING hOTLINE  that  wHEN kNOW yOU"



def string_transformer(s):
    res = ''
    s = ' '.join(s.split(' ')[::-1])
    for char in s:
        if char.islower(): res += char.upper()
        elif char.isupper(): res += char.lower()
        else: res += char
    return res


print(string_transformer(s))