url = ''


def delete_digit(n):
    res = []
    for i in str(n):
        num_str = [i for i in str(n)]
        num_str.remove(i)
        res.append(int(''.join(num_str)))
    return max(res)


print(delete_digit(n=362))