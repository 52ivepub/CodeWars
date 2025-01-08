url = 'https://www.codewars.com/kata/525caa5c1bf619d28c000335/train/python'

board = [
         [1, 2, 2],
         [0, 1, 0],
        [1, 0, 1]]

# -1


def is_solved(board):
    diagonal = []
    for x in range(len(board)):
        if len(set(board[x])) == 1 and board[x][0] > 0: return board[x][0]
        vertical = [num[x] for num in board]
        if len(set(vertical)) == 1 and vertical[0] > 0: return vertical[0]
        diagonal.append(board[x][x])
    if len(set(diagonal)) == 1 and diagonal[0] > 0: return diagonal[0]
    for i in range(len(board)):
        if 0 in board[i]: return -1
    return 0


print(is_solved(board))

# x = [1, 2, 3]
# print(x[-3])

