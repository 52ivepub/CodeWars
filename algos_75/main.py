url = ''


lst = [
  { 'firstName': 'Gabriel', 'lastName': 'X.', 'country': 'Monaco', 'continent': 'Europe', 'age': 49, 'language': 'PHP' },
  { 'firstName': 'Odval', 'lastName': 'F.', 'country': 'Mongolia', 'continent': 'Asia', 'age': 38, 'language': 'Python' },
  { 'firstName': 'Emilija', 'lastName': 'S.', 'country': 'Lithuania', 'continent': 'Europe', 'age': 19, 'language': 'Python' },
  { 'firstName': 'Sou', 'lastName': 'B.', 'country': 'Japan', 'continent': 'Asia', 'age': 49, 'language': 'PHP' },
]


def find_senior(lst):
    age = {i: lst[i]['age'] for i in range(len(lst))}
    max_age = max(age.items(), key=lambda x: x[1])
    res = [i for i in age.items() if i[1] == max_age[1]]
    return [lst[i[0]] for i in res]




print(find_senior(lst))