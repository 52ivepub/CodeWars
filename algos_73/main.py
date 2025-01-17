url = ''

dancing_brigade = "CbcBcbaA"
# ),"AaBbbCcc"


def find_children(dancing_brigade):
    if len(dancing_brigade) == 0: return ''
    seed = ''
    for i in sorted(dancing_brigade.lower()):
        if i.upper() in seed:
            seed += i
        else:
            seed += i.upper()
    return seed






print(find_children(dancing_brigade))