def calculator():
    result = 0
    op = input("Введите операцию +, -, *, / или 0 для выхода: ")
    if op == '0':
        print("Завершение программы")
        return
    elif op == "+" or op == "-" or op == "*" or op == "/":
        try:
            num_1 = int(input("Введите первое число: "))
            num_2 = int(input("Введите второе число: "))
        except ValueError:
            print("Вы вместо числа ввели что-то другое, повторите")
            return calculator()
        if op == "+":
            result = num_1 + num_2
            print(f"Сумма чисел: {result}")
            return calculator()
        elif op == "-":
            result = num_1 - num_2
            print(f"Разность чисел: {result}")
            return calculator()
        elif op == "*":
            result = num_1 * num_2
            print(f"Произведение чисел: {result}")
            return calculator()
        elif op == "/":
            try:
                result = num_1 / num_2
                print(f"Частное чисел: {result}")
            except ZeroDivisionError:
                print("На ноль делить нельзя")
            return calculator()
    else:
        print("Вы вместо знака операции ввели что-то другое, повторите")
        return calculator()


calculator()
