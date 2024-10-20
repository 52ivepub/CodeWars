s = 'OruJJMrIhWd IVWn xbPXhT mALZnjwRkAh YSMsXAXYKv  fzLVyILfqSP FTtZmvHFSaN'
# print(s)
# print(s.replace('  ', ' '))
# '), '#CodewarsIsNice'
s = 'ABbCccDdddEeeeeFfffffGggggggHhhhhhhhIiiiiiiiiJjjjjjjjjjKkkkkkkkkkkLlllllllllllMmmmmmmmmmmmmNnnnnnnnnnnnnnOooooooooooooooPpppppppppppppppQqq'
# s = 'CoDeWaRs is niCe'
# print(s.rjust(20))


def generate_hashtag(s):
    s_split = s.replace('  ', ' ').split(' ')
    s_split_capital = [i.capitalize() for i in s_split]
    res = f"#{''.join(s_split_capital)}"
    if 140 < len(res) or len(res) == 1:
        return False
    return res


print(generate_hashtag(s))