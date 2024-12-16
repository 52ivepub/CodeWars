url = 'https://www.codewars.com/kata/5420fc9bb5b2c7fd57000004/train/python'

arr = [12, 10, 8, 12, 7, 6, 4, 10, 12, 10]
# -->  12


def highest_rank(arr):
    res = {i: arr.count(i) for i in arr}
    return max(res.items(), key=lambda x: (x[1], x[0]))[0]

print(highest_rank(arr))