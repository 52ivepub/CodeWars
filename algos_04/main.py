integers = [2, 4, 6, 8, 10, 3]
# ), 3)


def find_outlier(integers):
    if len([i for i in integers if i % 2 == 0]) > 1:
        return [i for i in integers if i % 2 != 0][0]
    else:
        return [i for i in integers if i % 2 == 0][0]


print(find_outlier(integers))
