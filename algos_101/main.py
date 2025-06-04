url = 'https://www.codewars.com/kata/5324945e2ece5e1f32000370/train/python'

x, y = "123", "1"
# ), "2"
def sum_strings(x, y):
    dict_num = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}
    res = 0
    for number in [x, y]:
        multiplicity = [10 ** num for num in range(len(number))[::-1]]
        seed = [dict_num[i] for i in number]
        for i in range(len(number)):
            res += seed[i]*multiplicity[i]
    return str(res)





print(sum_strings(x, y))
