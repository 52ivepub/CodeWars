url = ''

arr1, arr2 =   ["b", "c", "b", "a"],   ["" , "a", "a", "c"]
# →     0
# →     7



def check_exam(arr1,arr2):
    estimation = 0
    for i in range(len(arr1)):
        if arr2[i] == arr1[i]:
            estimation += 4
        elif arr2[i] == '': pass
        else:
            estimation -= 1
    if estimation < 0: return 0
    return estimation


print(check_exam(arr1, arr2))