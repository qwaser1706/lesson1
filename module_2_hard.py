import random


def one_():
    a = [3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
    one = random.choice(a)
    return one


one = one_()
one_()


def two_(one):
    two = ''
    for i in range(1, one):
        for j in range(i + 1, one + 1):
            if one % (i + j) == 0:
                two += str(i) + str(j)
    return two


two = two_(one)
print(f'{one}-{two}')
