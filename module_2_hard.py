import random
def one_():
    a = [3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
    one = random.choice(a)
    return one
one = one_()
while 1<2 :
    import random
    def two1():
        b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
        b.remove(one)
        two1 = random.choice(b)
        b.remove(two1)
        two2 = random.choice(b)

        return two1, two2
    two1, two2 = two1()

    if one % (two1 +two2) == int(0):
        break
    else:
        continue
print(f" {one} - {two1} + {two2}")


