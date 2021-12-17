def check_eq(num, result=None, form=None):
    if result is None and form is None:
        result = 0
        form = (num * (num+1)/2)
    if num == 0 and result == form:
        print(f"Две части равны:\n"
              f"{result} = {form}")
        return
    elif num == 0 and result != form:
        print(f"Две части не равны:\n"
              f"{result} != {form}")
        return
    else:
        result += num
        return check_eq(num - 1, result, form)


check_eq(int(input("Введите число: ")))
