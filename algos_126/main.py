url = ''

array = [50,60,70,80]
# ), (120,140)

def row_weights(array):
    team_1 = [num for pos, num in list(enumerate(array)) if pos % 2 == 0]
    team_2 = [num for pos, num in list(enumerate(array)) if pos % 2 != 0]
    return sum(team_1), sum(team_2)


print(row_weights(array))