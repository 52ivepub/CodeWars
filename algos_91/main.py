url = ''

p0, percent, aug, p = 1500, 5, 100, 5000
# ), 15

def nb_year(p0, percent, aug, p):
    percent = percent * 0.01
    count_year = 1
    while (p0 + int(p0 * percent) + aug) < p:
        p0 = p0 + int(p0 * percent) + aug
        count_year += 1
    return count_year


print(nb_year(p0, percent, aug, p))