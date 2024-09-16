immutable_var = 1, 2, 'q', 'w'
#immutable_var[0] = 2 /это кортеж,его елементы нельзя менять
print(immutable_var)
mutable_list = [1, 2, 'q', 'w']
del mutable_list[0:4]
mutable_list.extend(tuple(immutable_var)) # всё равно добавил как список
mutable_list.append((immutable_var))
print(mutable_list)