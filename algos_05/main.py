word = "Success"
# ,")())())"


def duplicate_encode(word):
    res = ["(" if word.lower().count(i) == 1 else ")" for i in word.lower()]
    return "".join(res)


print(duplicate_encode(word))