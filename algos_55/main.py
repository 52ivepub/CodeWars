url = 'https://www.codewars.com/kata/55d5434f269c0c3f1b000058/train/python'

num1, num2 = 12345, 12345
# ) == 1


def triple_double(num1, num2):
    intersection = ''
    for i in range(len(str(num1))):
        if i + 2 < len(str(num1)) and str(num1)[i] == str(num1)[i+1] == str(num1)[i+2]:
            intersection += str(num1)[i]*2
    if intersection and intersection in str(num2):
        return 1
    return 0




print(triple_double(num1, num2))