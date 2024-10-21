text = "The sunset sets at twelve o' clock."
# , "20 8 5 19 21 14 19 5 20 19 5 20 19 1 20 20 23 5 12 22 5 15 3 12 15 3 11"


def alphabet_position(text):
    return ' '.join(str(ord(i) - 96) for i in text.lower() if i.isalpha())


print(alphabet_position(text))

print(ord('a') - 96)