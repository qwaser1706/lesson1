int()# целое число
float()# дробное число
str()# текст
input("")#ввод чего-то с консоли
имя[0:1:2]# индексация[с:по:шаг]
       :-1]# обратный счёт
sum()# сумма
len()# количество элементов
type()# тип данных
(___ .upper/.lower)# заглавные / маленькие буквы
(___.replace(старое/новое))# замена Элементов
___=[ , , , , ]# список (List)
___=( , , , ,  )# кортеж (tuple) ( неизменяемый)
___={ , , , ,}# множество (уникальные значения)(set)
___.discard/remove("элемент") # удаление элемета из множества дикард не выдыет ошибки
___.add('элемент')# добавляет элемент в множество
___={_:_, _:_} # словарь (пары)(dict)
       (___["ключ"])# обращение к элементам через ключ> значение
       #приравнивание значения несуществующему ключу создаст новый объект
       del ___["ключ"]# удаление пары
       ___.update({_:_,
                   _:_})#обновление нескольких пар
       print(___.get('неизвестный ключ'))# выдаст НОН вместо ошибки
       print(___.get('неизвестный ключ', "такого нет"))# замена нон
       print(___.keys())# выводит все ключи
       print(___.values())# Выводит все значения
       print(___.items())# выводит все пары

___.pop("ключ")# удаляет пару , но можно значение сразу присвоить переменной. работает с длугими колекциями

___.append()# добавление в конец списка или иной колекции
___.exten()#  добавление в конец списка или иной колекции , с разбитем на единичные элементы
___.remove()# УДАЛЕНИЕ этого субъекта
("" in ___)#  проверка на наличие чегото в колекции
("" not in ___)#  проверка на отсутствие чегото в колекции

print('чтото'.__sizeof__())# объём занимаемой памяти объекта

while _словие_:  # цикл пока
       break # прерывание цикла
       continue #  сброс цикла на начало

=  # приравнивание
:= # приравнивание с обновлением
!= # неравенство д/н
== # равенство д/н
** # степень
%  # остаток от деления
True=1
False=0



f stroka
зачем нужны комплексные числа?
в чём разница между := и +=  ?
