url = 'https://www.codewars.com/kata/5898b4b71d298e51b600014b/train/python'

words = "sort the inner content in descending order"
# -->  "srot the inner ctonnet in dsnnieedcg oredr"


def sort_the_inner_content(words):
    res = []
    for i in words.split():
        if len(i) <= 3:
            res.append(i)
            continue
        piece_sort = ''.join(sorted(i[1:-1], reverse=True))
        i = i[0] + piece_sort + i[-1]
        res.append(i)
    return ' '.join(res).strip()



print(sort_the_inner_content(words))

x = 'sort'

