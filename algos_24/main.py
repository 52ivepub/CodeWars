m = 16
# ) --> 45


def find_nb(m):
    count = 0
    for i in range(1, m):
        if m < i ** 3:
            break
        else:
            m -= i ** 3
        count += 1
    if m == 0:
        return count
    else:
        return -1






print(find_nb(m))