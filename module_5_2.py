class House:
    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors

    def go_to(self, new_floor):
        if 1 > new_floor or new_floor > self.number_of_floors:
            print(f'Такого этажа не существует. В этом доме {self.number_of_floors} этажей.')
        else:
            for floor in range(1, new_floor + 1):
                print(floor)
            print ('Приехали!')
    def __len__(self):
        return self.number_of_floors
    def __str__(self):
        return f"Название: {self.name}, кол-во этажей: {self.number_of_floors}"


h1 = House('ЖК Самоцвет', 25)
h2 = House('Хрущевка', 3)

print(len(h1))
print(len(h2))
print(h1)
print(h2)
