url = 'https://www.codewars.com/kata/55b42574ff091733d900002f/train/python'

x = ["Ryan", "Kieran", "Jason", "Yous"]
# Output = ["Ryan", "Yous"]

def friend(x):
    return [i for i in x if len(i) ==4]



print(friend(x))