
class House:
    def __init__(self, name, lvl):
        self.name = name
        self.number_of_floors = lvl #максимальный этаж для лифта


    def go_to(self, nf):
        self.new_floor = nf
        if nf > 1 and nf < self.number_of_floors:
            for i in range(1, nf+1):
                print(i)
        else:
            print("Такого этажа не существует")



h1 = House('ЖК Горский', 18)
h2 = House('Домик в деревне', 2)
h3 = House("Палевский жилой массив", 0)
h1.go_to(5)
h2.go_to(10)
h3.go_to(1)