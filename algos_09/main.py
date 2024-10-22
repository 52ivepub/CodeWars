n = 4
# ), 3


def persistence(n):
    count = 0
    while len(str(n)) > 1:
        split_str = [int(i) for i in str(n)]
        n = 1
        for i in split_str:
            n = n * i
        count += 1
    return count


print(persistence(n))