message = "CC8NhuSO"
# ' PP8AuhFB'
# ), 'nN oO mM 1234 *!?%'
print(ord('L'))

def rot13(message):
    res = ''
    list_chr_lower = range(97, 123)
    list_chr_upper = range(65, 91)
    for i in message:
        if i.islower():
            if ord(i) + 13 >= 122:
                res += chr(list_chr_lower[ord(i) + 13 - 123])
            else:
                x = chr(ord(i) + 13)
                res += x
        elif i.isupper():
            if ord(i) + 13 >= 91:
                res += chr(list_chr_upper[ord(i) + 13 - 91])
            else:
                x = chr(ord(i) + 13)
                res += x
        else:
            res += i
    return res




print(rot13(message))