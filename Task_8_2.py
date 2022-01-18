class BinaryTree:
    def __init__(self, root_obj):
        self.root = root_obj
        self.left_child = None
        self.right_child = None

    def __str__(self):
        return str(self.root)

    def insert_left(self, new_node):
        if self.left_child is None:
            self.left_child = BinaryTree(new_node)
        else:
            tree_obj = BinaryTree(new_node)
            tree_obj.left_child = self.left_child
            self.left_child = tree_obj

    def insert_right(self, new_node):
        if self.right_child is None:
            self.right_child = BinaryTree(new_node)
        else:
            tree_obj = BinaryTree(new_node)
            tree_obj.right_child = self.right_child
            self.right_child = tree_obj

    def insert_func(self, val):
        try:
            if val > self.root:
                return self.insert_right(val)
            elif val < self.root:
                return self.insert_left(val)
            else:
                print(f"{val} - равняется корню")
        except ValueError and TypeError:
            print(f"Неправильно введено значение: {val} - не подходит!")

    def get_right_child(self):
        if self.right_child is None:
            return "Правая ветка пустая"
        return self.right_child

    def get_left_child(self):
        if self.left_child is None:
            return "Левая ветка пустая"
        return self.left_child

    def set_root_val(self, obj):
        if isinstance(obj, int) is True:
            self.root = obj
        else:
            return print(f"Значение '{obj}' не подходит для корня!")

    def get_root_val(self):
        try:
            return self.root
        except Exception as error:
            print(f"Ошибка: {error}")


tree = BinaryTree(8)
print(tree.get_root_val())
print(tree.get_right_child())
print(tree.get_left_child(), "\n")
tree.set_root_val("new_root")
tree.set_root_val(bool)
tree.set_root_val(9)
print(tree.get_root_val(), "\n")

tree.insert_func(4)
print(tree.get_left_child())
tree.insert_func(7)
tree.insert_func("24st4")
tree.insert_func(12)
print(tree.get_right_child())
tree.insert_func(40)
tree.insert_func("str")
tree.insert_func(9)

print(tree.get_left_child())
print(tree.get_left_child().get_root_val())
print(tree.get_right_child())
print(tree.get_right_child().get_root_val())
