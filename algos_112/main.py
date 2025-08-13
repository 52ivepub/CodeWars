url = 'https://www.codewars.com/kata/5813d19765d81c592200001a/train/python'



def dont_give_me_five(start,end):
    res = [i for i in range(start, end+1) if '5' not in str(i)]
    return len(res)

print(dont_give_me_five(4, 17))