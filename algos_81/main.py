url = 'https://www.codewars.com/kata/5571f712ddf00b54420000ee/train/python'


cents = 3.9
# ),  {'Nickels': 0, 'Pennies': 4, 'Dimes': 0, 'Quarters': 1})

def loose_change(cents):
    change_dict = {'Nickels': 5, 'Pennies': 1, 'Dimes': 10, 'Quarters': 25}
    change_dict = dict(sorted(change_dict.items(), key= lambda x:x[1], reverse=True))
    null_dict = {'Nickels': 0, 'Pennies': 0, 'Dimes': 0, 'Quarters': 0}
    if cents <= 0: return null_dict
    cents = int(cents)
    for key, value in change_dict.items():
        while cents >= value:
            null_dict[key] += 1
            cents = cents - value
    return null_dict

print(loose_change(cents))


