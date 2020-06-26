def if_case(x):
    if x == True:
        return "yes"
    else:
        return "no"


def elif_case(x):
    if x == 0:
        return "it's a zero"
    elif x == 1:
        return "it's a one"
    else:
        return "something else"


def for_loop(x):
    count = 0
    for n in x:
        count = count + len(n)
    return count


def sum_numbers(x):
    suma = 0
    for n in x:
        if isinstance(n, int):
            suma = suma + n
    return suma
