url = 'https://www.codewars.com/kata/5544c7a5cb454edb3c000047/train/python'

h, bounce, window =30, 0.66, 1.5
                     # , 1)


def bouncing_ball(h, bounce, window):
    if h <= 0 or bounce <= 0 or bounce >= 1 or window > h:
        return -1
    count_see = -1
    while h > window:
        h = h * bounce
        count_see += 2
    return count_see



print(bouncing_ball(h, bounce, window))