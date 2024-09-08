class House:
    houses_history = []

    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors

    def __new__(cls, *args, **kwargs):
        cls.houses_history.append(args[0])
        return object.__new__(cls)


    def go_to(self, new_floor):
        for i in range(self.number_of_floors):
            print()
            return
        int(new_floor)
        if new_floor < 1:
            print("Такого этажа не существует")
        elif new_floor > self.number_of_floors:
            print("Такого этажа не существует")
        else:
            print(new_floor)

    def len(self):
        return self.number_of_floors

    def str(self):
        return f"Название: {self.name}, кол-во этажей: {self.number_of_floors}"

    def eq(self, value):
        return self.number_of_floors == value

    def lt(self, value):
        return self.number_of_floors < value

    def le(self, value):
        return self.number_of_floors <= value

    def gt(self, value):
        return self.number_of_floors > value

    def ge(self, value):
        return self.number_of_floors >= value

    def ne(self, value):
        return self.number_of_floors != value

    def add(self, value):
        if isinstance(self.number_of_floors, int):
            self.number_of_floors += int(value)
        return self

    def radd(self, value):
        if isinstance(value, int):
            return House(self.name, self.number_of_floors + value)

    def iadd(self, value):
        if isinstance(value, int):
            return House(self.name, self.number_of_floors + value)

    def __del__(self):
        print(f" {self.name} снесён, но он останется в истории")



h1 = House('ЖК Эльбрус', 10)
print(House.houses_history)
h2 = House('ЖК Акация', 20)
print(House.houses_history)
h3 = House('ЖК Матрёшки', 20)
print(House.houses_history)

# Удаление объектов
del h2
del h3

print(House.houses_history)
