import time
from random import randint


def timer(func):
    start_time = time.perf_counter()

    def current_func(item):
        return func(item)

    end_time = time.perf_counter()
    print(f"Эта операция заняла {end_time - start_time} секунд")
    return current_func


# a)
@timer
def list_fill(user_list):  # Сложность: O(N)
    for i in range(0, 10):
        user_list.append(randint(1, 100))
    return user_list


new_list = []
print(list_fill(new_list), "\n")


@timer
def dict_fill(user_dict):  # Сложность: O(N)
    for i in range(1, 11):
        user_dict[i] = randint(1, 100)
    return user_dict


new_dict = {}
print(dict_fill(new_dict), "\n")


# Операция заполнения списка по времени происходит дольше, чем операция заполнения словаря, примерно в 1.5-2 раза,
# но сложности они имеют одинаковые. Возможно словари заполняются быстрее из-за наличия ключей и значений.

# b)
@timer
def edit_list(user_list):  # Сложность: O(N^2)
    for i in range(0, 5):
        user_list.pop(i)
    user_list.sort()
    user_list.reverse()
    return user_list


print(edit_list(new_list), "\n")


@timer
def edit_dict(user_dict):  # Сложность: O(NlogN)
    for i in range(1, 10, 2):
        user_dict.pop(i)
    lst_user_dict = list(user_dict)
    lst_user_dict.sort()
    lst_user_dict.reverse()
    for i in lst_user_dict:
        print(f"{i} : {user_dict[i]}", end=" ")
    return


edit_dict(new_dict), "\n"
# Операция изменения и удаления из списка дольше из-за сложности
