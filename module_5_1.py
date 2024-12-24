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

h1 = House('ЖК Das Haus', 18)
h2 = House('Пятиэтажка', 5)

h1.go_to(7)
h2.go_to(8)