url = ''

s = "abcdef"
# ),['AbCdEf', 'aBcDeF']

def capitalize(s):
    odd_chars = ''.join([i[1].upper() if i[0] % 2 == 0 else i[1] for i in list(enumerate(s))])
    # even_chars = ''.join([i[1].upper() if i[0] % 2 != 0 else i[1] for i in list(enumerate(s))])
    return [odd_chars, odd_chars.swapcase()]


print(capitalize(s))