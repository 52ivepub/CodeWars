url = 'https://www.codewars.com/kata/563cf89eb4747c5fb100001b/train/python'


numbers = []
           # , output) = [2,3,4,5]

def remove_smallest(numbers):
    if len(numbers) == 0: return []
    res = [i for i in numbers]
    res.remove(min(res))
    return res


print(remove_smallest(numbers))