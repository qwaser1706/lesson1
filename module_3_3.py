# 1.Функция с параметрами по умолчанию:

def print_params(a = 1, b = 'строка', c = True):
    print(a, b, c)
    print(a, c)
    print( )

# 2.Распаковка параметров:

print_params()
print_params(b = 25)
print_params(c = [1,2,3])

values_list = [2, 'строфа', [id]]
values_dict = {'a':555, 'b':'stroka', 'c':False}

print_params(*values_list)
print_params(**values_dict)

# 3.Распаковка + отдельные параметры:

values_list_2 = [1, '1']
print_params(*values_list_2)
