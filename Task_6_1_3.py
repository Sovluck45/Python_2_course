# Задание 6, урока 3, курса "Основы языка Python"
from numpy import array
from memory_profiler import profile


# Исходный код
@profile
def int_func_2():
    w = input("Введите предложение: ").split()
    words = ''
    for word in w:
        c = 0
        for l in word:
            if 122 >= ord(l) >= 97:
                c += 1
            else:
                c -= 1
        if c > 0:
            word = word.title()
            words += ' ' + word
    return words


print(int_func_2())


# Оптимизированный код
@profile
def int_func():
    w = array(input("Введите предложение: ").split())
    words = ''
    for word in w:
        c = 0
        for l in word:
            if 122 >= ord(l) >= 97:
                c += 1
            else:
                c -= 1
        if c > 0:
            word = word.title()
            words += ' ' + word
    return words


print(int_func())
# Для оптимизации я использовал функию numpy array, из-за чего код использовал меньше оперативной памяти
