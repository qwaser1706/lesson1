first = int(input('please 1: '))
second = int(input('please 2: '))
third = int(input('please 3: '))
if first == second == third:
    print(3)
elif first == second or first == third or second == third:
    print(2)
elif first != second and first != third and second != third:
    print(0)
