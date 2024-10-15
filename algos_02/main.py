n = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
# ), "(123) 456-7890"



def create_phone_number(n):
    return "({0}{1}{2}) {3}{4}{5}-{6}{7}{8}{9}".format(*n)



print(create_phone_number(n))