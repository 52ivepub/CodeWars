url = 'https://www.codewars.com/kata/57b6f5aadb5b3d0ae3000611/train/python'

array_of_arrays = [1, 2, [4, 5, 1, 1], [1], [5, 6, 7, 8, 9]]


# --> 3


def get_length_of_missing_array(array_of_arrays):
    if len(array_of_arrays) == 0: return 0
    for i in array_of_arrays:
        if not isinstance(i, list):
            return 0
        elif len(i) == 0:
            return 0
    arr_sort = sorted(array_of_arrays, key=len)
    len_arr = [len(i) for i in arr_sort]
    for i in range(len(len_arr)-1):
        if len_arr[i+1] - 1 != len_arr[i]:
            return len_arr[i] + 1


print(get_length_of_missing_array(array_of_arrays))

