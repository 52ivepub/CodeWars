arr = [ 3, 10, 3, 3, 3 ]
# ) == 0.55
# ) == 2


def find_uniq(arr):
    if arr.count(max(arr)) > 1:
        return min(arr)
    return max(arr)



print(find_uniq(arr))
