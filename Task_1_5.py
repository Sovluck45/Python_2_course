class StackClass:
    def __init__(self):
        self.elems = []
        self.p_list = [self.elems]
        self.copy_list = []

    def is_empty(self):
        return self.elems == []

    def reset_list(self):
        if len(self.elems) >= 5:
            self.copy_list = self.elems
            self.p_list.append(self.copy_list)
            self.elems.clear()

    def push_in(self, el):
        if len(self.elems) >= 5:
            StackClass.reset_list(self)
            self.elems.append(el)
        else:
            self.elems.append(el)

    def pop_out(self):
        return self.elems.pop()

    def get_val(self):
        return self.elems[len(self.elems) - 1]

    def stack_size(self):
        return len(self.elems)

    def stack_number(self):
        return len(self.p_list)

    def check_current_list(self):
        return self.elems

    def check_all_lists(self):
        return self.p_list


if __name__ == '__main__':
    plates = StackClass()

    print(plates.is_empty())
    plates.push_in(5)
    plates.push_in("3")
    plates.push_in(4)
    plates.push_in(False)
    plates.push_in("str")
    print(plates.get_val())
    plates.push_in(4.5)
    plates.push_in(10)
    print(plates.get_val())

    plates.pop_out()

    print(plates.stack_size(), "\n")
    print(plates.stack_number(), "\n")
    print(plates.check_current_list(), "\n")
    print(plates.check_all_lists())
    print(plates.is_empty())
