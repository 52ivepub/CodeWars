url = 'https://www.codewars.com/kata/51ba717bb08c1cd60f00002f/train/python'

args =  [-61, -58, -56, -53, -52, -51, -50, -47, -44, -43, -40, -37, -35, -33, -31, -30]
# should equal '-61,-58,-56,-53--50,-47,-44,-43,-40,-37,-35,-33,-31,-30'
#               -61,-58,-56,-53--50,-47,-44,-43,-40,-37,-35,-33,-31--30




def solution(args):
    count = 0
    res = ''
    for num in range(len(args)):
        if num == len(args) - 1 and count > 0:
            res += f'{args[num - count]}{"-" if count > 1 else ","}{args[num]},'
            break
        if num == len(args) - 1 and count == 0:
            res += f'{args[num]},'
            break
        if abs(args[num] - args[num+1]) == 1:
            count += 1
        elif count > 1:
            res += f'{args[num-count]}-{args[num]},'
            count = 0
        elif count == 1:
            res += f'{args[num-count]},{args[num]},'
            count = 0
        else:
            res += f'{args[num]},'
            count = 0
    return res[:-1]



print(solution(args))
