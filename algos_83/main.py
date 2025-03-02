url = 'https://www.codewars.com/kata/51e04f6b544cf3f6550000c1/train/python'

bonus, price =9, 2
# ), 1
# ); // should === 12


def beeramid(bonus, price):
    if bonus <= 0 or price <= 0:
        return 0
    all_beer = bonus//price
    square = 0
    seed = 0
    while seed <= all_beer:
        square += 1
        seed += square*square
    return square-1



print(beeramid(bonus, price))


