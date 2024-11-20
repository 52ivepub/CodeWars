url = 'https://www.codewars.com/kata/52b757663a95b11b3d00062d/train/python'

# words = "String"
words = "Weird string case"
# => "WeIrD StRiNg CaSe"


def to_weird_case(words):
    if len(words.split()) == 1:
        res = [y.upper() if x % 2 == 0 else y.lower() for x, y in enumerate(words)]
        return "".join(res)
    res = []
    for i in words.split():
        seed = "".join([y.upper() if x % 2 == 0 else y.lower() for x, y in enumerate(i)])
        res.extend([seed, " "])
    return "".join(res).strip()








print(to_weird_case(words))

# def to_weird_case(words):
#     res = ""
#     if len(words.split()) == 1:
#         for x, y in enumerate(words):
#             if x % 2 == 0:
#                 res += y.upper()
#             else:
#                 res += y.lower()
#         return res
#     for i in words.split():
#         for x, y in enumerate(i):
#             if x % 2 == 0:
#                 res += y.upper()
#             else:
#                 res += y.lower()
#         res += " "
#     return res.strip()