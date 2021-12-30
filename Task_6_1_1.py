# Задание 2, урока 6, курса "Основы языка Python"
from pympler import asizeof


# Исходный код
class Road:
    def __init__(self, _length, _width, _weight, _thick):
        self._length = _length = int(input("Введите длину: "))
        self._width = _width = int(input("Введите ширину: "))
        self._weight = _weight = int(input("Введите массу для одного кв. метра: "))
        self._thick = _thick = int(input("Введите толщину полотна в см: "))

    def calc(self):
        return (self._length * self._width * self._weight * self._thick) / 1000


r = Road(1, 1, 1, 1)
print(f"Масса асфальта для покрытия дороги на один кв. метр: {r.calc()} тонн")
print(asizeof.asizeof(r))
print("---------------------------------------------------------------------")


# Оптимизированный код
class Road_2:
    __slots__ = ['_length', '_width', '_weight', '_thick']

    def __init__(self, _length, _width, _weight, _thick):
        self._length = _length = int(input("Введите длину: "))
        self._width = _width = int(input("Введите ширину: "))
        self._weight = _weight = int(input("Введите массу для одного кв. метра: "))
        self._thick = _thick = int(input("Введите толщину полотна в см: "))

    def calc(self):
        return (self._length * self._width * self._weight * self._thick) / 1000


r = Road_2(1, 1, 1, 1)
print(f"Масса асфальта для покрытия дороги на один кв. метр: {r.calc()} тонн")
print(asizeof.asizeof(r))
# Для оптимизация я использовал слоты, что позволило сократить количество занимаемой классом оперативной памяти
