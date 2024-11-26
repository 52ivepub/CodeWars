url = ''

n = 86240
# n = 539
# should return "(2**5)(5)(7**2)(11)"


def prime_factors(n):
    prime_nums = [2]
    for i in range(3, 7920, 2):
        if not any(i % prime == 0 for prime in prime_nums):
            prime_nums.append(i)
    res = {}
    for i in prime_nums:
        if n ==1: break
        while n % i == 0:
            n = n/i
            if i in res.keys():
                res[i] += 1
            else:
                res[i] = 1
    res_str = ''
    for x, y in res.items():
        if y == 1:
            res_str += f'({x})'
        else:
            res_str += f'({x}**{y})'
    return res_str



print(prime_factors(n))

