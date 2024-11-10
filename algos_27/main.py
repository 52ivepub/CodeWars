n = 5

def perimeter(n):
    count = 1
    a, b = 1, 1
    res = 0
    while count < n + 1:
        res += a
        a, b = b, a+b
        count += 1
    return (res +a)*4

print(perimeter(n))
