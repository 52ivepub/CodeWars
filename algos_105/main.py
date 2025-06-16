url = 'https://www.codewars.com/kata/5672682212c8ecf83e000050/train/python'


def dbl_linear(n):
    u = [1]
    for x in range(n):
        y = 2 * u[x] + 1
        z = 3 * u[x] + 1
        if y not in u:
            u.append(y)
        if z not in u:
            u.append(z)
    return sorted(u)[n]


print(dbl_linear(n=50))