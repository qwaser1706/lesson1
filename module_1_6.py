my_dict = {'one': 1, 'two': 2, 'three': 3}
print(my_dict)
print(my_dict.get('one'))
print(my_dict.get('four'))
my_dict.update({'four': 4, 'five': 5})
print(my_dict.pop('five'))
print(my_dict)

my_set = {1, 1, 'e', 'e'}
print(my_set)
my_set.add(5)
my_set.add(6)
my_set.remove(5)
my_set.discard(6)
print(my_set)