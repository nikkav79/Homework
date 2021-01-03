import math

def fact(n):
    for i in range(1, n+1):
        number = math.factorial(i)
        yield number

for el in fact(10):
    print(el)








