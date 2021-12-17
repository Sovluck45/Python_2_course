def revers_num(num, rev_num=None):
    if rev_num is None:
        rev_num = str("")
    if num <= 0:
        print(rev_num)
        return
    else:
        rev_num += str(num % 10)
        return revers_num(num // 10, rev_num)


revers_num(int(input("Введите число: ")))
