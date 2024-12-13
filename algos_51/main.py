url = 'https://www.codewars.com/kata/525f47c79f2f25a4db000025/train/python'

phone_number = "(123) 456-7890"


# ),       True


def valid_phone_number(phone_number):
    if any(False if i in "() -1234567890" else True for i in phone_number): return False
    if len(phone_number.split(" ")) != 2: return False
    if len(phone_number.split("-")) != 2: return False
    if phone_number[0] != "(":return False
    if phone_number[4] != ")": return False
    if phone_number[5] != " ": return False
    if phone_number[9] != "-": return False
    if len(phone_number) != 14: return False
    return True






print(valid_phone_number(phone_number))

# def valid_phone_number(phone_number):
#     if len(phone_number) != 14: return False
#     if any(i.isalpha() for i in phone_number): return False
#     if len(phone_number.split(" ")) != 2: return False
#     if len(phone_number.split("-")) != 2: return False
#     if any(i for i in phone_number if i in "[]{}.:_`,*%#\t"): return False
#     return True
