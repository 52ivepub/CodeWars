url = 'https://www.codewars.com/kata/59df2f8f08c6cec835000012/train/python'

s = "Fred:Corwill;Wilfred:Corwill;Barney:Tornbull;Betty:Tornbull;Bjon:Tornbull;Raphael:Corwill;Alfred:Corwill"


def meeting(s):
    s, res = s.upper().split(";"), ''
    s_split = [(i.split(":")[1], i.split(":")[0]) for i in s]
    s_split = sorted(s_split, key=lambda x:(x[0], x[1]))
    for i in s_split:
        res += f'({i[0]}, {i[1]})'
    return res



print(meeting(s))


