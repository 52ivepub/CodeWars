url = ''

bus_stops = [[10,0],[3,5],[5,8]]
# ),5


def number(bus_stops):
    seed = 0
    for i in bus_stops:
        seed += i[0] - i[1]
    return seed


print(number(bus_stops))