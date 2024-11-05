arr = [':D', ';-(', ':o(', ':(', ':(', ':oD', ':oD', ';-D', ':D', ';o(', ';oD', ';~D']
# );       // should return 2;


def count_smileys(arr):
    eyes_valid = [i for i in arr if i[0] in ":;"]
    mouth_valid = [i for i in eyes_valid if i[-1] in ")D" and len(i) == 2]
    nose_valid = [i for i in eyes_valid if len(i) > 2 and i[1] in "-~" and i[-1] in ")D"]
    return len(nose_valid + mouth_valid)



print(count_smileys(arr))

