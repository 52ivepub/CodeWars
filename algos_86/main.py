url = 'https://www.codewars.com/kata/555624b601231dc7a400017a/train/python'

n=11
k=19
# [10]

def josephus_survivor(n,k):
    seed = [i for i in range(1, n+1)]
    count = 0
    place = -1
    while len(seed) > 1:
        place += 1
        count += 1
        if count == k and place <= len(seed)-1:
            count = 1
            seed.remove(seed[place])
        elif count == k and place > len(seed) - 1:
            place = abs(len(seed) - place)
            while place > len(seed) - 1:
                place = abs(len(seed) - place)
            seed.remove(seed[place])
            count = 1

    return seed[0]







print(josephus_survivor(n,k))

