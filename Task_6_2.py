from memory_profiler import memory_usage, profile


def decor(func):
    def wrapper(*args, **kwargs):
        m1 = memory_usage()
        res = func(args[0])
        m2 = memory_usage()
        mem_diff = m2[0] - m1[0]
        return res, mem_diff

    return wrapper


# Исходный код
@profile
@decor
def revers_num(num, rev_num=None):
    if rev_num is None:
        rev_num = str("")
    if num <= 0:
        return print(rev_num)
    else:
        rev_num += str(num % 10)
        return revers_num(num // 10, rev_num)


none_1, mem_diff = revers_num(int(input("Введите число: ")))
print(f"Выполнение заняло {mem_diff} Mib")
print("---------------------------------------------------")


# Оптимизированный код
@profile
@decor
def rec_func(num):
    def revers_num(num, rev_num=None):
        if rev_num is None:
            rev_num = str("")
        if num <= 0:
            return print(rev_num)
        else:
            rev_num += str(num % 10)
            return revers_num(num // 10, rev_num)

    return revers_num(num)


none_2, mem_diff = rec_func(int(input("Введите число: ")))
print(f"Выполнение заняло {mem_diff} Mib")
# Суть проблемы заключается в том, что при каждом вызове функции вызывается таблица @profile,
# а по-скольку рекурсия вызывает себя несколько раз, то вызывается несколько таблиц.
# Моё решение проблемы: я создал новую функию, в которую входит уже существующая, и замеряю её,
# в связи с чем появляется только одна таблица.
# Также это уменьшило количество занимаемой кодом оперативной памяти
