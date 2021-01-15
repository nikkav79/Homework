def my_func(number_1, number_2, number_3):

    set = [number_1, number_2, number_3]
    a = min(set)
    set.remove(a)
    sum_num = sum(set)

    return sum_num

print(my_func(0.3, 21, 35))

