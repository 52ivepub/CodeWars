n_floors = 3
# ['  *  ', ' *** ', '*****'])


def tower_builder(n_floors):
    seed, res = '*', ['*']
    for i in range(1, n_floors):
        seed += "**"
        res.append(seed)
    return [i.center((len(res[-1]))) for i in res]


print(tower_builder(n_floors))

p = ["**"]
p[0] = p[0].center(6)

print(p)

