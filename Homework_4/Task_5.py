from functools import reduce

some_data = [i for i in range(100, 1001, 2)]
print(some_data)

multiplication = reduce(lambda num_1, num_2: num_1 * num_2, some_data)
print(multiplication)
