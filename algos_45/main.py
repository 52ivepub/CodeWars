url = 'https://www.codewars.com/kata/514b92a657cdc65150000006/train/python'
number = 10
# ), 23


def solution(number):
    if number < 0: return 0
    return sum(i for i in range(1, number) if i % 3 == 0 or i % 5 == 0)


print(solution(number))




