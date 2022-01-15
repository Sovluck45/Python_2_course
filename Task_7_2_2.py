from random import randint
from timeit import timeit

m_1 = 5
rand_list_10 = [randint(-100, 100) for i in range(2 * m_1 + 1)]
print(f"Исходный список: {rand_list_10}")
m_2 = 50
rand_list_100 = [randint(-100, 100) for j in range(2 * m_2 + 1)]
print(f"Исходный список: {rand_list_100}")
m_3 = 500
rand_list_1000 = [randint(-100, 100) for k in range(2 * m_3 + 1)]
print(f"Исходный список: {rand_list_1000}\n")


def sort_without_sorting(user_list):
    sort_list = []
    n = 0
    while len(user_list) != 1:
        sort_list.insert(n, min(user_list))
        sort_list.insert(len(sort_list)-n, max(user_list))
        user_list.remove(min(user_list))
        user_list.remove(max(user_list))
        n += 1
    sort_list.insert(5, user_list[0])
    return sort_list


print(f"Отсортированный список: {sort_without_sorting(rand_list_10[:])}")
med = sort_without_sorting(rand_list_10)
print(f"Медиана списка: {med[m_1]}")
print(f"Время сортировки списка с 11 элементами: "
      f"{timeit('sort_without_sorting(rand_list_10[:])', globals=globals(), number=1000)} секунд\n")

print(f"Отсортированный список: {sort_without_sorting(rand_list_100[:])}")
med = sort_without_sorting(rand_list_100)
print(f"Медиана списка: {med[m_2]}")
print(f"Время сортировки списка с 101 элементом: "
      f"{timeit('sort_without_sorting(rand_list_100[:])', globals=globals(), number=1000)} секунд\n")

print(f"Отсортированный список: {sort_without_sorting(rand_list_1000[:])}")
med = sort_without_sorting(rand_list_1000)
print(f"Медиана списка: {med[m_3]}")
print(f"Время сортировки списка с 1001 элементом: "
      f"{timeit('sort_without_sorting(rand_list_1000[:])', globals=globals(), number=1000)} секунд")
# Итоги замера:
# Время сортировки списка с 11 элементами: 0.0002662999999999971 секунд
# Время сортировки списка с 101 элементом: 0.0002575999999999967 секунд
# Время сортировки списка с 1001 элементом: 0.00026149999999999785 секунд
