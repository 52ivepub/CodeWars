from pprint import pprint

url = 'https://www.codewars.com/kata/534e01fbbb17187c7e0000c6/train/python'



def spiralize(size):
    first_row = [1 for i in range(size)]
    # second_row =
    create_zero = [[0 for i in range(size)] for _ in range(size)]
    result = []

    for place, row in list(enumerate(create_zero, start=1)):
        new_row = []
        for num in row:
            if place == 1:
                result.append([1 for _ in range(size)])
                break
            if place == 2:
                result.append([0 for _ in range(size-1)] + [1])
                break
            if place == size-1:
                result.append([1] +[0 for _ in range(size - 2)] + [1])
                break
            if place == size:
                result.append([1 for _ in range(size)])
                break
            if place == size-2:
                result.append([1 for _ in range(size)])
                break
            else:
                result.append([0 for _ in range(size)])
                break
        # result.append(new_row)
    return result




pprint(spiralize(5))


x = [0,1,2,3,4]
print(x[1]^2)



# [[1,1,1,1,1],[0,0,0,0,1],[1,1,1,0,1],[1,0,0,0,1],[1,1,1,1,1]]