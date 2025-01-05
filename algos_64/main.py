url = 'https://www.codewars.com/kata/5d23d89906f92a00267bb83d/train/python'

order = "milkshakepizzachickenfriescokeburgerpizzasandwichmilkshakepizza"
# ),
x =  "Burger Fries Chicken Pizza Pizza Pizza Sandwich Milkshake Milkshake Coke"


def get_order(order):
    menu = ["Burger", "Fries", "Chicken", 'Pizza', "Sandwich", "Onionrings", "Milkshake", "Coke"]
    new_order = []
    seed = ''
    for i in order:
        if seed.capitalize() in menu:
            new_order.append(seed)
            seed = ''
        seed += i
    new_order.append(seed)
    res_dict = {x:0 for x in menu}
    for i in new_order:
        res_dict[i.capitalize()] += 1
    result = ''
    for x, y in res_dict.items():
        result += (x + ' ') * y
    return result.strip()


print(get_order(order))

# print(sorted(x.split()))