from timeit import timeit

num = int(input("Введите число: "))


def revers_1(enter_num, revers_num=0):
    if enter_num == 0:
        return
    else:
        num = enter_num % 10
        revers_num = (revers_num + num / 10) * 10
        enter_num //= 10
        revers_1(enter_num, revers_num)


print(f"{timeit('revers_1(num)', 'from __main__ import revers_1, num', number=1000)} секунд")


def revers_2(enter_num, revers_num=0):
    while enter_num != 0:
        num = enter_num % 10
        revers_num = (revers_num + num / 10) * 10
        enter_num //= 10
    return revers_num


print(f"{timeit('revers_2(num)', 'from __main__ import revers_2, num', number=1000)} секунд")


def revers_3(enter_num):
    enter_num = str(enter_num)
    revers_num = enter_num[::-1]
    return revers_num


print(f"{timeit('revers_3(num)', 'from __main__ import revers_3, num', number=1000)} секунд")


def revers_4(enter_num):
    rev_num = ''
    for i in range(len(str(enter_num))):
        rev_num += str(enter_num % 10)
        enter_num //= 10
    return rev_num


print(f"{timeit('revers_4(num)', 'from __main__ import revers_4, num', number=1000)} секунд")

# Третий способ самый эффективный, так как он не использует цикл, рекурсию или перебор, а просто работает со строкой.
# Также является самым коротким
