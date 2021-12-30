# Задание 1, урока 1, курса "Основы языка Python"
from memory_profiler import memory_usage


def decor(func):
    def wrapper():
        m1 = memory_usage()
        res = func()
        m2 = memory_usage()
        mem_diff = m2[0] - m1[0]
        return res, mem_diff
    return wrapper


@decor
def func_1():
    # Исходный код
    numb_1 = int(input("Введите первое число: "))
    numb_2 = int(input("Введите второе число: "))
    numb_3 = int(input("Введите третье число: "))
    print(f"Вы ввели эти числа:  {numb_1}, {numb_2}, {numb_3}")


none_1, mem_diff = func_1()
print(f"Выполнение заняло {mem_diff} Mib")
print("------------------------------------------------------")


@decor
def func_2():
    # Оптимизированный код
    numb_1, numb_2, numb_3 = map(int, input("Введите три числа через пробел: ").split())
    print(f"Вы ввели эти числа:  {numb_1}, {numb_2}, {numb_3}")


none_2, mem_diff = func_2()
print(f"Выполнение заняло {mem_diff} Mib")
# Для оптимизации кода я использовал map, что помогло уменьшить количество занимаемой кодом оперативной памяти
