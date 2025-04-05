url = 'https://www.codewars.com/kata/521c2db8ddc89b9b7a0000c1/train/python'

# array = [[1,2,3],
#          [4,5,6],
#          [7,8,9]]
# snail(array) #=> [1,2,3,6,9,8,7,4,5]
array = [[1,2,3, 1],
         [4,5,6, 4],
         [7,8,9, 7],
         [7,8,9, 7]]

# x = []
# x.append(array[0].pop(0))
# print(x)
# print(array)


def snail(array):
    if len(array[0]) == 0: return 0
    res = []
    res.extend(array.pop(0))  # добавляем верхний ряд

    while len(array) > 0:
        for i in range(0, len(array)-1):  # добавляем крайний справа
            res.append(array[i].pop(-1))



        for i in array[-1][::-1]:  # добавляем нижний ряд
            res.append(i)
        array.pop(-1)

        for i in range(len(array)-1, -1,    -1):  # добавляем крайний слева
            res.append(array[i].pop(0))

        # if len(array) < 2:
        for i in range(len(array)-2, -1,  -1):  # добавляем центр
            res.append(array[i].pop(0))

    return res

print(snail(array))

