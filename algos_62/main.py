url = 'https://www.codewars.com/kata/581e014b55f2c52bb00000f8/train/python'

s = "65 119esi 111dl 111lw 108dvei 105n 97n 111ka"
# ), "A wise old owl lived in an oak"

def decipher_this(s):
    res = ''
    for word in s.split():
        seed = ''
        number = ''
        for char in word:
            if char.isdigit():
                number += char
            else:
                seed += char
        if len(seed) > 1:
            seed = seed[-1] + seed[1:-1] + seed[0]
        res += chr(int(number)) + seed + ' '
    return res.strip()





print(decipher_this(s))

# print(chr(65))
