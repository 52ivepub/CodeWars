url = 'https://www.codewars.com/kata/56541980fa08ab47a0000040/train/python'


s="aaaxbbbbyyhwawiwjjjwwm"
# printer_error(s) => "8/22"

def printer_error(s):
    valid = [chr(i) for i in range(97, 110)]
    res = [0 if char in valid else 1 for char in s ]
    return f'{sum(res)}/{len(s)}'



print(printer_error(s))