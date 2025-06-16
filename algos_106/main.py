url = 'https://www.codewars.com/kata/56606694ec01347ce800001b/train/python'

a, b, c = 1,2,3

def is_triangle(a, b, c):
    seed = [a, b, c]
    max_seed = max(set(seed))
    seed.remove(max_seed)
    return sum(seed) > max_seed


print(is_triangle(a, b, c))