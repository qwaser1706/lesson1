import math


def true_divide(first, second):
    if second == 0:
        q = math.inf
    else:
        q = first / second
    return q

