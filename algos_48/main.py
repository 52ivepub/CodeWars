url = 'https://www.codewars.com/kata/5848565e273af816fb000449/train/python'

text = "An wise old owl lived in an oak"
# ) == "72olle"


def encrypt_this(text):
    res = ''
    for i in text.split():
        if len(i) == 1:
            res += str(ord(i[0])) + ' '
        elif len(i) == 2:
            res += str(ord(i[0])) + i[1] + ' '
        else:
            res += str(ord(i[0])) + i[-1] + i[2:-1] + i[1] + ' '
    return res.strip()


print(encrypt_this(text))