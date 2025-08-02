url = 'https://www.codewars.com/kata/526d42b6526963598d0004db/train/python'

# returns 'HTIJBFWX'

class CaesarCipher(object):
    def __init__(self, shift):
        self.shift = shift
    def encode(self, st):
        res = []
        for char in list(st.lower()):
            if char.isalpha() == False:
                res.append(char)
                continue
            if ord(char)+self.shift > 122:
                res.append(chr(ord(char)+self.shift-26))
            else:
                res.append(chr(ord(char) + self.shift))
        return ''.join([i.upper() for i in res])

    def decode(self, st):
        res = []
        for char in list(st.lower()):
            if char.isalpha() == False:
                res.append(char)
                continue
            if ord(char)-self.shift < 97:
                res.append(chr(ord(char)-self.shift+26))
            else:
                res.append(chr(ord(char) - self.shift))
        return ''.join([i.upper() for i in res])


cipher = CaesarCipher(26)



