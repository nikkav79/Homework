def my_func_1(x, y):
    degree = x ** y
    return degree

print(my_func_1(-34, -2))

def my_func_2(x, y):

    degree = 1
    for i in range(abs(y)):
        degree = degree * x

    dev = 1 / degree
    return dev

print(my_func_2(2, -4))
