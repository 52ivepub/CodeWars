url = 'https://www.codewars.com/kata/5679aa472b8f57fb8c000047/train/python'

arr = [1,2,3,4,3,2,1]
# ),3



def find_even_index(arr):
    for i in range(len(arr)):
        if sum(arr[:i]) == sum(arr[i +1:]):
            return i
    return -1





print(find_even_index(arr))