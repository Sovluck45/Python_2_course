user_1 = {"User_name": "Ivanov", "Password": "tetriandox", "Conf": "1"}
user_2 = {"User_name": "Petrov", "Password": "parol", "Conf": "0"}
user_3 = {"User_name": "Sidorov", "Password": "qwerty1234", "Conf": "1"}


# Сложность: O(n^2)
def authentication(u_dict=None):
    if u_dict is None:  # O(1)
        u_dict = {}  # O(1)
    u_list = [user_1, user_2, user_3]
    for el in u_list:  # O(n)
        if min(u_dict.values()) == "1":  # O(n)
            print(f"Пользователь {list(u_dict.values())[0]} может получить доступ к веб-ресурсу")  # O(1)
        else:
            print(f"Пользователю {list(u_dict.values())[0]} нужно пройти проверку для доступа к веб-ресурсу")  # O(1)
        break


authentication(user_1)
authentication(user_2)
authentication(user_3)

user_list = ({"User_name": "Ivanov", "Password": "tetriandox", "Conf": "1"},
             {"User_name": "Petrov", "Password": "parol", "Conf": "0"},
             {"User_name": "Sidorov", "Password": "qwerty1234", "Conf": "1"})


# Сложность: O(n)
def user_authentication(u_dict=None):
    if u_dict is None:  # O(1)
        u_dict = list()  # O(1)
    for el in user_list:  # O(n)
        if list(el.values())[2] == "1":
            print(f"Пользователь {list(el.values())[0]} может получить доступ к веб-ресурсу")  # O(1)
        else:
            print(f"Пользователю {list(el.values())[0]} нужно пройти проверку для доступа к веб-ресурсу")  # O(1)


user_authentication(user_list)

# Вывод: второе решение более эфективное, так как в нём используется одна функция n сложности,
# а в первом решение две фунцкции n сложности, одну из них можно спокойно заменить на менее сложную функцию
