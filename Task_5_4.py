from collections import OrderedDict
from timeit import timeit
my_dict = {'one': 1, 'two': 2, 'three': 3, 'four': 4}
my_ordered_dict = OrderedDict([('one', 1), ('two', 2), ('three', 3), ('four', 4)])


def edit_dict(user_dict):
    user_dict.clear()
    for i in range(5):
        user_dict[i] = i ** 3
    user_dict.pop(0)
    user_dict[5] = 5 ** 3
    user_dict.popitem()
    user_dict[7] = 7 ** 3
    user_dict.setdefault(9)
    return user_dict


print(f"Изменение обычного словаря: {timeit('edit_dict(my_dict)', globals=globals())} секунд")


def edit_ordered_dict(user_ordered_dict):
    user_ordered_dict.clear()
    for i in range(5):
        user_ordered_dict[i] = i ** 3
    user_ordered_dict.pop(0)
    user_ordered_dict[5] = 5 ** 3
    user_ordered_dict.popitem()
    user_ordered_dict[7] = 7 ** 3
    user_ordered_dict.setdefault(9)
    return user_ordered_dict


print(f"Изменение 'запоминающего' словаря: {timeit('edit_ordered_dict(my_ordered_dict)', globals=globals())} секунд")
# Первый замер: Изменение обычного словаря: 1.7066217000000001 секунд
#               Изменение 'запоминающего' словаря: 2.1965769999999996 секунд
# --------------------------------------------------------------------------
# Второй замер: Изменение обычного словаря: 1.7254202 секунд
#               Изменение 'запоминающего' словаря: 2.2129659 секунд
# Итог: "запоминающий" словарь выполняет операции медленней обычного.
# Есть смысл в использование OrderedDict в Python 3.6 и более поздних версиях, из-за функций типа move_to_end
# и popitem(last=True), и из-за более точной проверки словарей на эквивалентность
