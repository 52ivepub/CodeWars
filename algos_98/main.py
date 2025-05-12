url = ''

strng = 'apples, pears # and bananas\ngrapes\nbananas !apples'
markers = ['#', '!']
# , 'apples, pears\ngrapes\nbananas'



def strip_comments(strng, markers):
    res = []
    # for i in range(len(strng)):
        # if strng[i] in markers:
        #     start = i
        # if strng[i] == '\n':
        #     end = i
        #     res.append([start, end])
        #     start = None
    for i in markers:
        start = strng.index(i)-1
        end = strng.index('\n')
        x = strng[start: end]
        strng = strng.replace(strng[start: end], '')
    strng = strng.replace(strng[start:], '')
    return strng


print(strip_comments(strng, markers))