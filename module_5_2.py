
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



h1 = House('ЖК Эльбрус', 10)
h2 = House('ЖК Акация', 20)

print(len(h1))
print(len(h2))

print(h1)
print(h2)
