url = ''

word = 'HJoSjHaqc'
# ), [0, 1, 3, 5]

def capitals(word):
    index_word = []
    count = 0
    for i in word:
        if i.isupper():
            index_word.append(word.index(i, count))
        count += 1
    return index_word


print(capitals(word))