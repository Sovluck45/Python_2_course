def sum_elem(num, elem=None, result=None):
    if elem is None and result is None:
        result = 0
        elem = 1
    if num <= 0:
        print(result)
        return
    else:
        num -= 1
        result += elem
        elem /= -2
        return sum_elem(num, elem, result)


sum_elem(int(input("Введите количество элементов: ")))
