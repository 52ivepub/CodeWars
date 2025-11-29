url = ''

ages = [1, 5, 87, 45, 8, 8]
# ), [45, 87]
# ), "www.codewars.com/katas/?page=1"

def two_oldest_ages(ages):
    return sorted(ages)[-2:]


print(two_oldest_ages(ages))


