url = 'https://www.codewars.com/kata/53697be005f803751e0015aa/train/python'

# st = 'How are you today?'
st = 'H4w 1r2 y45 t4d1y?'


# print(list(enumerate(st)))

def encode(st):
    vowels = {"a": "1", "e": '2', "i": '3', "o": '4', "u": '5'}
    list_st = [vowels[i] if i in vowels.keys() else i for i in list(st)]
    return "".join(list_st)


def decode(st):
    vowels = {"1": "a", "2": 'e', "3": 'i', "4": 'o', "5": 'u'}
    list_st = [vowels[i] if i in vowels.keys() else i for i in list(st)]
    return "".join(list_st)
