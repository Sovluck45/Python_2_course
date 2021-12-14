# Сложность: O(n)
n_list = [9, 3, 7, 6, 1, 0, 2, 8]
el_l = n_list[0]
for el in n_list:
    if el < el_l:
        el_l = el
print(f"Минимальное значение списка: {el_l}")

# Сложность: O(n^2)
n_list = [9, 3, 7, 6, 1, 5, 2, 8]
n_list_copy = n_list
new_list = []
for el in n_list:
    for i in n_list_copy:
        if el < i:
            new_list.append(el)
        else:
            new_list.append(i)
el_n = new_list[0]
for j in new_list:
    if j < el_n:
        el_n = j
print(f"Минимальное значение списка: {el_n}")
