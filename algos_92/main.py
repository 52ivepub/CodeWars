from poetry.core.version.markers import intersection

url = 'https://www.codewars.com/kata/55983863da40caa2c900004e/train/python'


words = ['cherry', 'peach', 'pineapple', 'melon', 'strawberry', 'raspberry', 'apple', 'coconut', 'banana']
# 'berry'), 'cherry'

class Dictionary:
    def __init__(self, words):
        self.words = words
    def find_most_similar(self, term):
        count_coin = 0
        count_coin_dict = {}
        for word in self.words:
            intersection_word = set(term).intersection(set(word))
            print(intersection_word)
            for num in word:
                if num in term:
                    count_coin +=1
            count_coin_dict[word] = count_coin
            count_coin = 0
        return count_coin_dict


dic = Dictionary(words=words)
print(dic.find_most_similar(term='berry'))