from collections import defaultdict

user_dict = defaultdict(list)

user_dict['num_1'] = list(input("Введите первое шестнадцатеричное число: ").upper())
num_1_copy = list(user_dict['num_1'])
num_1_hex = int("".join([str(i) for i in user_dict['num_1']]), 16)

user_dict['num_2'] = list(input("Введите второе шестнадцатеричное число: ").upper())
num_2_copy = list(user_dict['num_2'])
num_2_hex = int("".join([str(i) for i in user_dict['num_2']]), 16)

hex_sum = hex(num_1_hex + num_2_hex).upper()[2:]
user_dict['hex_sum'] = list(hex_sum)
hex_multi = hex(num_1_hex * num_2_hex).upper()[2:]
user_dict['hex_multi'] = list(hex_multi)
print(f"Сумма чисел: {user_dict['hex_sum']}\n"
      f"Произведение чисел: {user_dict['hex_multi']}")
