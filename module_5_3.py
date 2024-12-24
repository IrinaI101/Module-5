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
    def __eq__(self, other):
        if isinstance(self.number_of_floors, int) and isinstance(other.number_of_floors, int):
            return self.number_of_floors == other.number_of_floors
        else:
            return 'Ошибка: количество этажей должно быть целым числом'
    def __lt__(self, other):
        if isinstance(self.number_of_floors, int) and isinstance(other.number_of_floors, int):
            return self.number_of_floors < other.number_of_floors
        else:
            return 'Ошибка: количество этажей должно быть целым числом'
    def __le__(self, other):
        if isinstance(self.number_of_floors, int) and isinstance(other.number_of_floors, int):
            return self.number_of_floors < other.number_of_floors \
                or self.number_of_floors == other.number_of_floors
        else:
            return 'Ошибка: количество этажей должно быть целым числом'
    def __gt__(self, other):
        if isinstance(self.number_of_floors, int) and isinstance(other.number_of_floors, int):
            return self.number_of_floors > other.number_of_floors
        else:
            return 'Ошибка: количество этажей должно быть целым числом'
    def __ge__(self, other):
        if isinstance(self.number_of_floors, int) and isinstance(other.number_of_floors, int):
            return self.number_of_floors > other.number_of_floors \
                or self.number_of_floors == other.number_of_floors
        else:
            return 'Ошибка: количество этажей должно быть целым числом'
    def __ne__(self, other):
        if isinstance(self.number_of_floors, int) and isinstance(other.number_of_floors, int):
            return self.number_of_floors != other.number_of_floors
        else:
            return 'Ошибка: количество этажей должно быть целым числом'
    def __add__(self, value):
        if isinstance(self.number_of_floors, int) and isinstance(value, int):
            self.number_of_floors += value
            return self
        else:
            return 'Ошибка: для сложения оба значения должны быть целыми числами'
    def __iadd__(self, value):
        if isinstance(self.number_of_floors, int) and isinstance(value, int):
            return self.__add__(value)
        else:
            return 'Ошибка: для сложения оба значения должны быть целыми числами'
    def __radd__(self, value):
        if isinstance(self.number_of_floors, int) and isinstance(value, int):
            return self.__add__(value)
        else:
            return 'Ошибка: для сложения оба значения должны быть целыми числами'


h1 = House('ЖК Самоцвет', 25)
h2 = House('Хрущевка', 3)

print(h1)
print(h2)
print(f'h1 == h2: {h1 == h2}')
print(f'h1 < h2: {h1 < h2}')
print(f'h1 <= h2: {h1 <= h2}')
print(f'h1 > h2: {h1 > h2}')
print(f'h1 >= h2:{h1 >= h2}')
print(f'h1 != h2: {h1 != h2}')
h1 = h1 + 5
print(h1)
h2 += 3
print(h2)
h2 = 3 + h2
print(h2)
