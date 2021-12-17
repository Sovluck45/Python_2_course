def even_odd(num, e=None, o=None):
    if e is None and o is None:
        e = 0
        o = 0
    if num <= 0:
        print(f"Количество чётных цифр: {e}\n"
              f"Количество нечётных цифр: {o}")
        return
    else:
        num_d = num % 10
        if num_d % 2 == 0:
            e += 1
        else:
            o += 1
    return even_odd(num // 10, e, o)


even_odd(int(input("Введите число: ")))
