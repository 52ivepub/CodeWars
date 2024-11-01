s = "breakCamelCase"
# ), "break Camel Case"


def solution(s):
    seed = [' ' + i if i.isupper() else i for i in s]
    return ''.join(seed)



print(solution(s))