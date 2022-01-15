from random import randint
from timeit import timeit

rand_list = [randint(-100, 100) for i in range(10)]
rand_list_copy = rand_list
print(f"Исходный список: {rand_list}")
print(f"Копия исходного списка: {rand_list_copy}\n")


def bubble_sort(lst_obj):
    n = 1
    while n < len(lst_obj):
        for i in range(len(lst_obj)-n):
            if lst_obj[i] < lst_obj[i+1]:
                lst_obj[i], lst_obj[i+1] = lst_obj[i+1], lst_obj[i]
        n += 1
    return lst_obj


print(f"Сортировка заняла: {timeit('bubble_sort(rand_list[:])', globals=globals(), number=1000)} секунд")
print(f"Отсортированный список: {bubble_sort(rand_list[:])}\n")


def modified_bubble_sort(lst_obj):
    n = 1
    stop = 0
    while n < len(lst_obj) and stop == 0:
        stop = 1
        for i in range(len(lst_obj)-n):
            if lst_obj[i] < lst_obj[i+1]:
                lst_obj[i], lst_obj[i+1] = lst_obj[i+1], lst_obj[i]
                stop = 0
        n += 1
    return lst_obj


print(f"Доработанная сортировка заняла: {timeit('modified_bubble_sort(rand_list_copy[:])', globals=globals(), number=1000)}"
      f" секунд")
print(f"Отсортированный список: {modified_bubble_sort(rand_list_copy[:])}")

# Результаты замеров:
# Первый замер:
# Сортировка заняла: 0.0067031999999999994 секунд
# Доработанная сортировка заняла: 0.005801799999999999 секунд
# Второй замер:
# Сортировка заняла: 0.013905100000000004 секунд
# Доработанная сортировка заняла: 0.0119082 секунд
# Итог: доработка сделала сортировку слегка быстрее
