


url = 'https://www.codewars.com/kata/5a946d9fba1bb5135100007c/train/python'

numbers = [50, 39, 49, 6, 17, 28]
           # , 5)


def minimum_number(numbers):
    def check_prime(num):
        if len([i for i in range(1, num) if num % i == 0])==1:
            return True
    for i in range(sum(numbers)):
        if check_prime(num=i + sum(numbers)):
            return i




print(minimum_number(numbers))