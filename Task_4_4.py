from timeit import timeit
from collections import Counter
array = [1, 3, 1, 3, 4, 5, 1]


def func_1():
    m = 0
    num = 0
    for i in array:
        count = array.count(i)
        if count > m:
            m = count
            num = i
    return f'Чаще всего встречается число {num}, ' \
           f'оно появилось в массиве {m} раз(а)'


print(f"{timeit('func_1()', 'from __main__ import func_1', number=1000)} секунд")
print(func_1())


def func_2():
    new_array = []
    for el in array:
        count2 = array.count(el)
        new_array.append(count2)

    max_2 = max(new_array)
    elem = array[new_array.index(max_2)]
    return f'Чаще всего встречается число {elem}, ' \
           f'оно появилось в массиве {max_2} раз(а)'


print(f"{timeit('func_2()', 'from __main__ import func_2', number=1000)} секунд")
print(func_2())


def func_3():
    max_count = Counter(array).most_common()[0]
    num_count = max_count[1]
    max_num = max_count[0]
    return f'Чаще всего встречается число {max_num}, ' \
           f'оно появилось в массиве {num_count} раз(а)'


print(f"{timeit('func_3()', 'from __main__ import func_3', number=1000)} секунд")
print(func_3())
# 0.0011853999999999996 секунд - первый способ
# 0.001638599999999997 секунд - второй способ
# 0.0025962999999999993 секунд - третий способ (мой)
# Задачу ускорить не получилось, хоть мой вариант и выглядит меньше, он использует класс, из-за чего делается дольше
