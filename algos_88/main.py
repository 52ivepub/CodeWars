url = 'https://www.codewars.com/kata/52742f58faf5485cae000b9a/train/python'

seconds = 3600
# "1 hour, 1 minute and 2 seconds"

def format_duration(seconds):
    res = ''
    if seconds == 0: return 'now'
    seed = {"year": 31536000, "day": 86400,  "hour": 3600, 'minute': 60, "second": 1}
    for name, num in seed.items():
        division = seconds // num
        if division > 0:
            res += f'{division} {name}{"s" if division>1 else ""}, '
            seconds = seconds - (num*division)
    res = res.strip(' ,')
    search_and = [i for i in res.split() if i.isdigit()]
    if len(search_and) > 1:
        res = res[::-1].replace(",", "dna ", 1)
        return res[::-1]
    else:
        return res









print(format_duration(seconds))