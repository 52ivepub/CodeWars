url = ''

n = 12

def round_to_next5(n):
    while n % 5 != 0:
        n += 1
    return n


print(round_to_next5(n))
