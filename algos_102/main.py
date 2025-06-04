url = ''

symbol = { 'M' : 1000, 'CM': 900, 'D': 500, 'CD': 400, 'C': 100,
                   'XC': 90, 'L': 50, 'XL': 40, 'X': 10, 'IX': 9, 'V': 5, 'IV': 4, 'I': 1}

class RomanNumerals:
    @staticmethod
    def to_roman(val : int) -> str:
        res = ''
        for char, num in symbol.items():
            while val >= num:
                val -= num
                res += char

        return res


    @staticmethod
    def from_roman(roman_num : str) -> int:
        res = 0
        while len(roman_num) > 1:
            if roman_num[0] + roman_num[1] in symbol:
                res += symbol[roman_num[0] + roman_num[1]]
                roman_num = roman_num.replace(roman_num[0] + roman_num[1], '')
            else:
                res += symbol[roman_num[0]]
                roman_num = roman_num[1:]
        if len(roman_num) > 0:
            res += symbol[roman_num[0]]
        return res





