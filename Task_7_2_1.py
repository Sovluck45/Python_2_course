from random import randint
from timeit import timeit

m_1 = 5
rand_list_10 = [randint(0, 100) for i in range(2 * m_1 + 1)]
print(f"Исходный список: {rand_list_10}")
m_2 = 50
rand_list_100 = [randint(0, 100) for j in range(2 * m_2 + 1)]
print(f"Исходный список: {rand_list_100}")
m_3 = 500
rand_list_1000 = [randint(0, 100) for k in range(2 * m_3 + 1)]
print(f"Исходный список: {rand_list_1000}\n")


def shell_sort(user_list):
    inc = len(user_list) // 2
    while inc:
        for i, el in enumerate(user_list):
            while i >= inc and user_list[i - inc] > el:
                user_list[i] = user_list[i - inc]
                i -= inc
            user_list[i] = el
        if inc == 2:
            inc = 1
        else:
            inc = int(inc * 5 / 11)
    return user_list


print(f"Отсортированный список: {shell_sort(rand_list_10[:])}")
med = shell_sort(rand_list_10)
print(f"Медиана списка: {med[m_1]}")
print(f"Время сортировки списка с 11 элементами: "
      f"{timeit('shell_sort(rand_list_10[:])', globals=globals(), number=1000)} секунд\n")

print(f"Отсортированный список: {shell_sort(rand_list_100[:])}")
med = shell_sort(rand_list_100)
print(f"Медиана списка: {med[m_2]}")
print(f"Время сортировки списка с 101 элементом: "
      f"{timeit('shell_sort(rand_list_100[:])', globals=globals(), number=1000)} секунд\n")

print(f"Отсортированный список: {shell_sort(rand_list_1000[:])}")
med = shell_sort(rand_list_1000)
print(f"Медиана списка: {med[m_3]}")
print(f"Время сортировки списка с 1001 элементом: "
      f"{timeit('shell_sort(rand_list_1000[:])', globals=globals(), number=1000)} секунд")
# Итоги замера:
# Время сортировки списка с 11 элементами: 0.0035688000000000004 секунд
# Время сортировки списка с 101 элементом: 0.04201669999999999 секунд
# Время сортировки списка с 1001 элементом: 0.7602002000000001 секунд
