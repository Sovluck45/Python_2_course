class TaskBoard:
    def __init__(self):
        self.basic_tasks = ["int", 45, True, 14.1, False, 16, "anecdote", 3.14, 'nuts', 1965]
        self.tasks_for_rev = ["float", 10]
        self.completed_tasks = []

    def is_empty(self):
        return f"Базовые: {self.basic_tasks == []}\n " \
               f"На доработку: {self.tasks_for_rev == []}\n" \
               f"Завершённые: {self.completed_tasks == []}"

    def to_complete_queue(self, num):
        self.completed_tasks.insert(0, self.basic_tasks[num])
        self.basic_tasks.pop(num)

    def to_rev_queue(self, num):
        self.tasks_for_rev.insert(0, self.basic_tasks[num])
        self.basic_tasks.pop(num)

    def to_basic_queue(self, item):
        self.basic_tasks.insert(0, item)

    def from_queue_basic(self):
        return self.basic_tasks.pop()

    def from_queue_rev(self):
        return self.tasks_for_rev.pop()

    def size(self):
        return print(f"Длина списка с базовыми задачами: {len(self.basic_tasks)}\n"
                     f"Длина списка с не доработанными задачами: {len(self.tasks_for_rev)}\n"
                     f"Длина списка с завершёнными задачами: {len(self.completed_tasks)}")

    def check_completed(self):
        return self.completed_tasks

    def check_basic(self):
        return self.basic_tasks

    def check_rev(self):
        return self.tasks_for_rev


if __name__ == '__main__':
    t_b = TaskBoard()

    t_b.size()
    print(t_b.check_rev())
    print(t_b.check_basic(), "\n")

    t_b.to_basic_queue(1887)
    t_b.from_queue_basic()
    print(t_b.check_basic(), "\n")

    t_b.to_complete_queue(2)
    t_b.to_complete_queue(6)
    print(t_b.check_completed(), "\n")

    t_b.to_rev_queue(4)
    print(t_b.check_rev(), "\n")

    print(t_b.check_basic(), "\n")

    t_b.size()
