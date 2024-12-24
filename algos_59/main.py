url = ''

st = '42'
# ), 'my-camel-cased-string'


def kebabize(st):
    res = ''
    for i in st:
        if not i.isalpha():
            continue
        elif i.isupper():
            res += '-'
        res += i.lower()
    return res.strip('-')


print(kebabize(st))