
url = 'https://www.codewars.com/kata/563f037412e5ada593000114/train/python'


principal, interest, tax, desired = 1000, 0.05, 0.18, 1100
# ), 3

def calculate_years(principal, interest, tax, desired):
    count = 0
    while principal < desired:
        principal = principal + (principal*interest) - ((principal*interest)*tax)
        count += 1
    return count




print(calculate_years(principal, interest, tax, desired))