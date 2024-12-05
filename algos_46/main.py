url = 'https://www.codewars.com/kata/52de553ebb55d1fca3000371/train/python'

sequence = [1, -2, -5, -8, -11, -14, -20, -23, -26]
# ) == -17
# print(sequence[:-1])

def find_missing(sequence):
    step_all = [sequence[i] - sequence[i-1] for i in range(len(sequence) - 1, 0, -1)]
    step = [i for i in step_all if step_all.count(i) > 1][0]
    for i in range(len(sequence) - 1, 0, -1):
        if sequence[i] - sequence[i-1] != step:
            return sequence[i-1] + step




print(find_missing(sequence))


# def find_missing(sequence):
#     step_all = [sequence[i] - sequence[i-1] for i in range(len(sequence) - 1, 0, -1)]
#     step = [i for i in step_all if step_all.count(i) > 1][0]
#     for i in range(len(sequence) - 1, 0, -1):
#         if sequence[i] - sequence[i-1] != step:
#             return sequence[i-1] + step