
class House:
    def __init__(self, name, lvl):
        self.name = name
        self.number_of_floors = lvl


    def go_to(self, nf):
        self.new_floor = nf
        if nf > 1 and nf < self.number_of_floors:
            for i in range(1, nf+1):
                print(i)
        else:
            print("Такого этажа не существует")


    def __len__(self):
        return self.number_of_floors


    def __str__(self):
        return f'Название: {self.name}, кол-во этажей: {self.number_of_floors}'


    def __eq__(self, other):
        return  self.number_of_floors == other.number_of_floors


    def __lt__(self, other):
        return  self.number_of_floors < other.number_of_floors


    def __gt__(self, other):
        return  self.number_of_floors > other.number_of_floors


    def __le__(self, other):
        return self.number_of_floors <= other.number_of_floors


    def __ge__(self, other):
        return self.number_of_floors >= other.number_of_floors


    def __ne__(self, other):
        return self.number_of_floors != other.number_of_floors

    def __add__(self, value):
        return House(self.name, self.number_of_floors + value)

    def __iadd__(self, value):
        self.number_of_floors += value
        return self


    def __radd__(self, other):
        return House(self.name, other + self.number_of_floors)



h1 = House('ЖК Эльбрус', 10)
h2 = House('ЖК Акация', 20)

print(h1)
print(h2)

print(h1 == h2) # __eq__

h1 = h1 + 10 # __add__
print(h1)
print(h1 == h2)

h1 += 10 # __iadd__
print(h1)

h2 = 10 + h2 # __radd__
print(h2)

print(h1 > h2) # __gt__
print(h1 >= h2) # __ge__
print(h1 < h2) # __lt__
print(h1 <= h2) # __le__
print(h1 != h2) # __ne__

