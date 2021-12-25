from timeit import timeit

user_list = [2, 4, 12, 9, 8, 6, 17, 8, 1, 11, 14]


def func_1(nums):
    new_arr = []
    for i in range(len(nums)):
        if nums[i] % 2 == 0:
            new_arr.append(i)
    return new_arr


print(func_1(user_list))
print(timeit("func_1(user_list)", 'from __main__ import func_1, user_list', number=1000))


def my_func(nums):
    new_arr = [i for i in range(len(nums)) if nums[i] % 2 == 0]
    return new_arr


print(my_func(user_list))
print(timeit("my_func(user_list)", 'from __main__ import my_func, user_list', number=1000))
# 0.0010377999999999984
# 0.0010252000000000004
# В своей фунции я применил list comprehension, что позволило уменьшить код и сделать его выполнение немного быстрее
