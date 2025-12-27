from itertools import count

url = ''

numbers = [10, 14, 2, 23, 19]
# -->  42 (= 23 + 19)
def largest_pair_sum(numbers):
    max1 = max(numbers)
    numbers.remove(max1)
    max2 = max(numbers)
    return max1 + max2



print(largest_pair_sum(numbers))