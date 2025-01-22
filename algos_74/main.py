url = ''

x, y = 5, 3
        # , (3,5))


def nbr_of_laps(x, y):
    general = 0
    for i in range(1, 10000):
        if (x*i) % y == 0:
            general = x*i
            return (general/x, general/y)







print(nbr_of_laps(x, y))