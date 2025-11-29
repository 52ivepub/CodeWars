

url = 'https://www.codewars.com/kata/5174a4c0f2769dd8b1000003/train/python'


test, original = "Buckethead", "DeathCubeK"
# ), True

def is_anagram(test, original):
    test = test.lower()
    original = original.lower()
    word_1 = sorted({i: test.count(i) for i in test}.items())
    word_2 = sorted({i: original.count(i) for i in original}.items())
    return word_1 == word_2


print(is_anagram(test, original))
