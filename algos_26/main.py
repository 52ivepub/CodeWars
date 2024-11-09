strng = "kk"
# -> fo99obar100"
        # "foo1"


def increment_string(strng):
    if len(strng) == 0 or strng[-1].isalpha():
        return strng + "1"
    seed_digit = []
    for i in strng[::-1]:
        if i.isdigit():
            seed_digit.append(i)
        else:
            break
    seed_digit = seed_digit[::-1]
    strng = strng[:len(strng) - len(seed_digit)]
    for i in range(len(seed_digit) - 1, -1, -1):
        if seed_digit[i] == "9":
            seed_digit[i] = "0"
        else:
            seed_digit[i] = str(int(seed_digit[i]) + 1)
            if seed_digit[i - 1] == "0":
                break
            break
    if int("".join(seed_digit)) == 0:
        seed_digit.insert(0, "1")
    return strng + "".join(seed_digit)



print(increment_string(strng))
