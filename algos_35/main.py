url = ''
title = 'a clash of KINGS', 'a an the of'
         # , 'A Clash of Kings')


def title_case(title, minor_words=''):
    if len(title) ==0:
        return ""
    elif type(title) != tuple:
        return title.title()
    rules = title[1].lower().split()
    res = []
    for x, y in enumerate(title[0].title().split()):
        if x == 0:
            res.append(y.capitalize())
        elif y.lower() in rules:
            res.append(y.lower())
            continue
        else:
            res.append(y.capitalize())
    return " ".join(res)



print(title_case(title))

