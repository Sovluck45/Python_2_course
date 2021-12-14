# Сложность: O(nlogn)
com_dict = {"Company_1": 32151, "Company_2": 59214,
            "Company_3": 7314, "Company_4": 10052,
            "Company_5": 19230, "Company_6": 72190}  # O(1)
n_dic = {}  # O(1)
c = 0
new_dict = list(com_dict.items())  # O(1)
new_dict.sort(key=lambda i: i[1])  # O(nlogn)
for i in new_dict:  # O(n)
    c += 1
    n_dic.update({"Company_" + str(c): i[1]})  # O(1)
n = 0
while n < 3:
    n_dic.pop(min(n_dic))  # O(1)
    n += 1
print(f"Три компании с наибольшей годовой прибылью:\n{n_dic}")


# Сложность: O(n^3)
com_dict = {"Company_1": 32151, "Company_2": 59214,
            "Company_3": 7314, "Company_4": 10052,
            "Company_5": 19230, "Company_6": 72190,
            "Company_7": 93251, "Company_8": 13007}  # O(1)
n_dic = {}  # O(1)
c = 0
com_values = list(com_dict.values())  # O(1)
com_keys = list(com_dict.keys())  # O(1)
for i in com_values:  # O(n)
    c += 1
    n_dic.update({max(com_keys): max(com_values)})  # O(1)
    com_values.remove(max(com_values))  # O(n)
    com_keys.remove(max(com_keys))  # O(n)
    if c == 3:
        break
print(f"Три компании с наибольшей годовой прибылью:\n{n_dic}")
