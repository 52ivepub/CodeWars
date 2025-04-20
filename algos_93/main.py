
url = 'https://www.codewars.com/kata/5259b20d6021e9e14c0010d4/train/python'

text = 'have to  Kata   always is hardocoded  This a case   avoid rule! should   random  tests'
# ), '  elbuod  decaps  sdrow  '
# ), 'a b c d'

def series_sum(text):
    return " ".join([i[::-1] for i in text.split(' ')])



print(series_sum(text))