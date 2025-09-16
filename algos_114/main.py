from fcntl import FASYNC

url = 'https://www.codewars.com/kata/5966847f4025872c7d00015b/train/python'

s = "zero nine five two"
# ), "four"


def average_string(s):
    nums = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    if not all(list(True if i in nums else False for i in s.split())) or len(s) == 0:
        return "n/a"
    nums = dict(enumerate(nums))
    new_nums = {y:x for x, y in nums.items()}
    result = [new_nums[i] for i in s.split()]
    result = (sum(result))//len(result)
    return nums[result]



    for num in s.split():
        pass



print(average_string(s))