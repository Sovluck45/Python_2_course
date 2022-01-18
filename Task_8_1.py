from collections import Counter, deque


class HaffmanCode:

    def __init__(self, user_string):
        self.string = user_string
        self.dict = {}
        self.code(self.tree())

    def count_letters(self):
        count_letters = Counter(self.string)
        return count_letters

    def tree(self):
        sorted_count = deque(sorted(self.count_letters().items(), key=lambda item: item[1]))
        if len(sorted_count) != 1:
            while len(sorted_count) > 1:
                weight_num = sorted_count[0][1] + sorted_count[1][1]
                combine_elements = {0: sorted_count.popleft()[0], 1: sorted_count.popleft()[0]}
                for i, j in enumerate(sorted_count):
                    if weight_num > j[1]:
                        continue
                    else:
                        sorted_count.insert(i, (combine_elements, weight_num))
                        break
                else:
                    sorted_count.append((combine_elements, weight_num))
        else:
            weight_num = sorted_count[0][1]
            combine_elements = {0: sorted_count.popleft()[0], 1: None}
            sorted_count.append((combine_elements, weight_num))
        return sorted_count[0][0]

    def code(self, tree, path=''):
        if not isinstance(tree, dict):
            self.dict[tree] = path
        else:
            self.code(tree[0], f"{path}0")
            self.code(tree[1], f"{path}1")

    def encode_word(self):
        bin_word = ""
        for i in self.string:
            bin_word += self.dict[i]
        return bin_word


my_string = input("Введите строку для кодирования: ")

haff = HaffmanCode(my_string)
print(f"Исходная строка: {my_string}")
print(f"Дерево: {haff.tree()}")
print(f"Двоичный код каждого символа: {haff.dict}")
print(f"Закодированное слово: {haff.encode_word()}")
