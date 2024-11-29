url = 'https://www.codewars.com/kata/56b5afb4ed1f6d5fb0000991/train/python'

strng = "733049910872815764"
sz = 5
       # 733049910872815764
# ) --> "330479108928157"
       # 330479108928157
       # 33047910872815764


def rev_rot(strng, sz):
    if not all(i.isdigit() for i in strng) or sz <= 0 or str == '' or sz > len(strng):
        return ''
    strng = strng[:[i for i in range(len(strng), 0, -1) if i % sz == 0][0]]
    strng_valid = [strng[i:i+sz] for i in range(0, len(strng), sz)]
    res = [i[::-1] if sum([int(x) for x in i]) % 2 == 0 else i[1:] + i[0] for i in strng_valid]
    return "".join(res)



print(rev_rot(strng,sz))


