url = ''

s1 = "my&friend&Paul has heavy hats! &"
s2 = "my friend John has many many friends &"
# mix(s1, s2) --> "2:nnnnn/1:aaaa/1:hhh/2:mmm/2:yyy/2:dd/2:ff/2:ii/2:rr/=:ee/=:ss"

def mix(s1, s2):

    s1 = [i for i in s1 if i.islower()]
    dict_s1 = {x: s1.count(x) for x in s1 if s1.count(x) > 1}
    dict_s1 =  dict(sorted(dict_s1.items(), key=lambda item: item[0]))
    s2 = [i for i in s2 if i.islower()]
    dict_s2 = {x: s2.count(x) for x in s2 if s2.count(x) > 1}
    dict_s2 = dict(sorted(dict_s2.items(), key=lambda item: item[0]))
    all_values = []
    for let, num in dict_s1.items():
        if let in dict_s2 and num > dict_s2[let]:
            all_values.append(f'1:{let*num}/')
        elif let in dict_s2 and num == dict_s2[let]:
            all_values.append(f'=:{let*num}/')
        elif let in dict_s2 and num < dict_s2[let]:
            all_values.append(f'2:{let*dict_s2[let]}/')
        else:
            all_values.append(f'1:{let*num}/')
    for let, num in dict_s2.items():
        if let in ''.join(all_values):
            continue
        if let in dict_s1 and num > dict_s1[let]:
            all_values.append(f'2:{let*num}/')
        elif let in dict_s1 and num == dict_s1[let]:
            all_values.append(f'=:{let*num}/')
        elif let in dict_s1 and num < dict_s1[let]:
            all_values.append(f'1:{let*dict_s1[let]}/')
        else:
            all_values.append(f'2:{let*num}/')

    res_dict = {x: len([i for i in x if i.isalpha()]) for x in all_values}
    res_dict = {val[0]: val[1] for val in sorted(res_dict.items(), key=lambda x: (-x[1], x[0]))}
    return ''.join([x for x, y in res_dict.items()])[:-1]





print(mix(s1, s2))