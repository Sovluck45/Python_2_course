from random import randint


def game(randnum=None, count_tries=None):
    if randnum is None and count_tries is None:
        randnum = randint(0, 100)
        count_tries = 0
    num = int(input("Введите число: "))
    if num == randnum:
        print(f"Вы ввели правильное число: {num}")
        return
    elif count_tries == 10:
        print(f"Вы не угадали число\n"
              f"Ответ: {randnum}")
        return
    else:
        if num > randnum:
            print("Введённое число больше правильного")
            return game(randnum, count_tries + 1)
        else:
            print("Введённое число меньше правильного")
            return game(randnum, count_tries + 1)


game()
