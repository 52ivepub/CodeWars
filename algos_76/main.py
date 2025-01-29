url = ''

words = ['ninja', 'samurai', 'ronin']
# --> "ninja, samurai and ronin"


def format_words(words):
    if words == None: return ''
    words = [i for i in words if len(i) > 0]
    if len(words) == 1: return words[0]
    res = ''
    for i in range(len(words)):
        if words[i] == '': continue
        elif i == len(words)-1:
            res = res[:-2]
            res += f' and {words[i]}'
        else:
            res += f'{words[i]}, '
    return res


print(format_words(words))