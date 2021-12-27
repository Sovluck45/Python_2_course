from collections import namedtuple

company_info = namedtuple('Information', 'name first_qr second_qr third_qr fourth_qr')
num = int(input("Введите количество предприятий для расчета прибыли: "))


def company_profit(n, average_profit=None, n_copy=None, max_profit=None, min_profit=None):
    if average_profit is None:
        average_profit = 0
        n_copy = n
        max_profit = ''
        min_profit = ''
    if n == 0:
        return print(f"Средняя годовая прибыль всех предприятий: {average_profit / n_copy}\n"
                     f"Предприятие, с прибылью выше среднего значения: {max_profit}\n"
                     f"Предприятие, с прибылью ниже среднего значения: {min_profit}")
    else:
        company_data = company_info(
            name=input("Введите название предприятия: "),
            first_qr=int(input("Введите данные о прибыли первого квартала: ")),
            second_qr=int(input("Введите данные о прибыли второго квартала: ")),
            third_qr=int(input("Введите данные о прибыли третьего квартала: ")),
            fourth_qr=int(input("Введите данные о прибыли четвёртого квартала: "))
        )
        average_profit += company_data.first_qr + company_data.second_qr + company_data.third_qr + company_data.fourth_qr
        sum_profit = company_data.first_qr + company_data.second_qr + company_data.third_qr + company_data.fourth_qr
        if sum_profit > (average_profit / n_copy):
            max_profit = company_data.name
        else:
            min_profit = company_data.name
        return company_profit(n - 1, average_profit, n_copy, max_profit, min_profit)


company_profit(num)
