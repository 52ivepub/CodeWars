people = " gap "
# ["Hello", "hEllo", "heLlo", "helLo", "hellO"]


def wave(people):
    res = []
    for x, y in enumerate(people):
        if y == " ": continue
        people_capital = list(people)
        people_capital[x] = y.upper()
        people_capital = "".join(people_capital)
        res.append(people_capital)
    return res



print(wave(people))