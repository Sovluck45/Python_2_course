# Задание 1, урока 2, курса "Алгоритмы и структуры данных на Python. Базовый курс"
from memory_profiler import memory_usage


def decor(func):
    def wrapper(*args, **kwargs):
        m1 = memory_usage()
        res = func()
        m2 = memory_usage()
        mem_diff = m2[0] - m1[0]
        return res, mem_diff
    return wrapper


# Исходный код
@decor
def calculator():
    result = 0
    op = input("Введите операцию +, -, *, / или 0 для выхода: ")
    if op == '0':
        print("Завершение программы")
        return
    elif op == "+" or op == "-" or op == "*" or op == "/":
        try:
            num_1 = int(input("Введите первое число: "))
            num_2 = int(input("Введите второе число: "))
        except ValueError:
            print("Вы вместо числа ввели что-то другое, повторите")
            return calculator()
        if op == "+":
            result = num_1 + num_2
            print(f"Сумма чисел: {result}")
            return calculator()
        elif op == "-":
            result = num_1 - num_2
            print(f"Разность чисел: {result}")
            return calculator()
        elif op == "*":
            result = num_1 * num_2
            print(f"Произведение чисел: {result}")
            return calculator()
        elif op == "/":
            try:
                result = num_1 / num_2
                print(f"Частное чисел: {result}")
            except ZeroDivisionError:
                print("На ноль делить нельзя")
            return calculator()
    else:
        print("Вы вместо знака операции ввели что-то другое, повторите")
        return calculator()


none_1, mem_diff = calculator()
print(f"Выполнение заняло {mem_diff} Mib")


# Оптимизированный код
@decor
def calculator_2():
    op = input("Введите операцию +, -, *, / или 0 для выхода: ")
    if op == '0':
        return print("Завершение программы")
    elif op == "+" or op == "-" or op == "*" or op == "/":
        try:
            num_1, num_2 = map(int, input("Введите два числа: ").split())
        except ValueError:
            return print("Вы вместо чисел ввели что-то другое, повторите"), calculator()
        if op == "+":
            return print(f"Сумма чисел: {num_1 + num_2}"), calculator()
        elif op == "-":
            return print(f"Разность чисел: {num_1 - num_2}"), calculator()
        elif op == "*":
            return print(f"Произведение чисел: {num_1 * num_2}"), calculator()
        elif op == "/":
            try:
                return print(f"Частное чисел: {num_1 / num_2}")
            except ZeroDivisionError:
                return print("На ноль делить нельзя"), calculator()
    else:
        return print("Вы вместо знака операции ввели что-то другое, повторите"), calculator()


none_2, mem_diff_2 = calculator_2()
print(f"Выполнение заняло {mem_diff_2} Mib")
# Для оптимизации кода я укомплектовал код и использовал map, в связи с чем уменьшилось количество
# оперативной памяти занимаемой кодом
