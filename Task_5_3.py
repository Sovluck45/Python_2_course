from collections import deque
from timeit import timeit

my_list = [4, 12, 62, 7, 0, 12]
deque_list = [46, 132, 2, 6, 10, 81]
my_deque = deque(deque_list)
# 1)
print("Изменение справа:")


def append_list():
    for i in range(5):
        my_list.append(i ** 2)
    return my_list


def pop_list():
    for i in range(3):
        my_list.pop()
    return my_list


def extend_list():
    my_list.extend('word')
    return my_list


print(f"Время append списка: {timeit('append_list', globals=globals())} секунд")
print(f"Время pop списка: {timeit('pop_list', globals=globals())} секунд")
print(f"Время extend списка: {timeit('extend_list', globals=globals())} секунд")
print("-----------------------------------------------------------------------")


def append_deque():
    for i in range(5):
        my_deque.append(i ** 2)
    return my_deque


def pop_deque():
    for i in range(3):
        my_deque.pop()
    return my_deque


def extend_deque():
    my_deque.extend('word')
    return my_deque


print(f"Время append дэка: {timeit('append_deque', globals=globals())} секунд")
print(f"Время pop дэка: {timeit('pop_deque', globals=globals())} секунд")
print(f"Время extend дэка: {timeit('extend_deque', globals=globals())} секунд")
print("-----------------------------------------------------------------------")
# Первый замер: Время append списка: 0.016735499999999997 секунд
#               Время pop списка: 0.019403499999999997 секунд
#               Время extend списка: 0.019414599999999997 секунд
# -----------------------------------------------------------------------
#               Время append дэка: 0.018367400000000006 секунд
#               Время pop дэка: 0.017892400000000003 секунд
#               Время extend дэка: 0.01811389999999999 секунд
# -----------------------------------------------------------------------
# Второй замер: Время append списка: 0.0173936 секунд
#               Время pop списка: 0.0168354 секунд
#               Время extend списка: 0.017997899999999997 секунд
# -----------------------------------------------------------------------
#               Время append дэка: 0.015539499999999998 секунд
#               Время pop дэка: 0.016988100000000006 секунд
#               Время extend дэка: 0.015551399999999993 секунд
# -----------------------------------------------------------------------
# Итог: список и дэк, по времени, изменяются примерно одинаково
# 2)
print("Изменение слева:")


def append_left_list():
    for i in range(4):
        my_list.insert(0, i ** 3)
    return my_list


def pop_left_list():
    for i in range(2):
        my_list.pop(0)
    return my_list


def extend_left_list():
    my_list.insert(0, 'word')
    return my_list


print(f"Время append_left списка: {timeit('append_left_list', globals=globals())} секунд")
print(f"Время pop_left списка: {timeit('pop_left_list', globals=globals())} секунд")
print(f"Время extend_left списка: {timeit('extend_left_list', globals=globals())} секунд")
print("-----------------------------------------------------------------------")


def append_left_deque():
    for i in range(4):
        my_deque.appendleft(i ** 3)
    return my_deque


def pop_left_deque():
    for i in range(2):
        my_deque.popleft()
    return my_deque


def extend_left_deque():
    my_deque.extendleft('word')
    return my_deque


print(f"Время append_left дэка: {timeit('append_left_deque', globals=globals())} секунд")
print(f"Время pop_left дэка: {timeit('pop_left_deque', globals=globals())} секунд")
print(f"Время extend_left дэка: {timeit('extend_left_deque', globals=globals())} секунд")
print("-----------------------------------------------------------------------")
# Первый замер: Время append_left списка: 0.016988099999999992 секунд
#               Время pop_left списка: 0.016703999999999997 секунд
#               Время extend_left списка: 0.01582059999999999 секунд
# -----------------------------------------------------------------------
#               Время append_left дэка: 0.0160835 секунд
#               Время pop_left дэка: 0.019328299999999993 секунд
#               Время extend_left дэка: 0.015558199999999994 секунд
# -----------------------------------------------------------------------
# Второй замер: Время append_left списка: 0.015604699999999999 секунд
#               Время pop_left списка: 0.01555780000000001 секунд
#               Время extend_left списка: 0.015757099999999996 секунд
# -----------------------------------------------------------------------
#               Время append_left дэка: 0.015558199999999994 секунд
#               Время pop_left дэка: 0.015572799999999998 секунд
#               Время extend_left дэка: 0.01788780000000001 секунд
# -----------------------------------------------------------------------
# Итог: список и дэк, по времени, изменяются слева примерно одинаково
# 3)
print("Взятие элемента:")


def get_item_list():
    for i in range(3):
        print(my_list[i])
    return


print(f"Время взятия элемента списка: {timeit('get_item_list', globals=globals())} секунд")
print("-----------------------------------------------------------------------")


def get_item_deque():
    for i in range(3):
        print(my_deque[i])
    return


print(f"Время взятия элемента дэка: {timeit('get_item_deque', globals=globals())} секунд")
# # Первый замер: Время взятия элемента списка: 0.016999199999999992 секунд
# -----------------------------------------------------------------------
#                 Время взятия элемента дэка: 0.015657299999999985 секунд
# -----------------------------------------------------------------------
# Второй замер:   Время взятия элемента списка: 0.01622269999999998 секунд
# -----------------------------------------------------------------------
#                 Время взятия элемента дэка: 0.016346099999999975 секунд
# -----------------------------------------------------------------------
# Итог: время взятия элемента из списка и дэка приблизительно одинаковое
