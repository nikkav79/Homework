import random


some_data = [random.randint(1, 1000) for i in range(20)]
print(some_data)
#
# some_data_sorted = [m for i, m in enumerate(some_data) if some_data.count(m) == 1]
# print(some_data_sorted)

some_data_sorted = [i for i in some_data if some_data.count(i) == 1]
print(some_data_sorted)