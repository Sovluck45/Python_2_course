# Задание 3, урока 3, курса "Основы языка Python"
from memory_profiler import memory_usage


def decor(func):
    def wrapper(n_1, n_2, n_3):
        m1 = memory_usage()
        func(n_1, n_2, n_3)
        m2 = memory_usage()
        mem_diff = m2[0] - m1[0]
        return mem_diff

    return wrapper


# Исходный код
@decor
def my_func(n_1, n_2, n_3):
    return n_1 + n_2 + n_3 - min(n_1, n_2, n_3)


mem_diff = my_func(
    n_1=int(input("Введите первое число: ")),
    n_2=int(input("Введите второе число: ")),
    n_3=int(input("Введите третье число: ")))
print(f"Выполнение заняло {mem_diff} Mib")


# Оптимизированный код
@decor
def my_func_2(n_1, n_2, n_3):
    n_1, n_2, n_3 = map(int, input("Введите три числа через пробел: ").split())
    return n_1 + n_2 + n_3 - min(n_1, n_2, n_3)


mem_diff = my_func_2(0, 0, 0)
print(f"Выполнение заняло {mem_diff} Mib")
# Для оптимизация использовался map и внесение переменных в функцию, после чего количество занимаемой
# кодом оперативной памяти уменьшилось
