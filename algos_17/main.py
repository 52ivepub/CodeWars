chars = ['a','b','c','d','f']
# -> 'e'


def find_missing_letter(chars):
    alphavit = [chr(i) for i in range(97, 123)]
    start = alphavit.index(chars[0].lower())
    count = 0
    for _ in range(26):
        if chars[count].lower() != alphavit[start]:
            return alphavit[start].upper() if chars[0].isupper() else alphavit[start]
        count += 1
        start += 1

print(find_missing_letter(chars))