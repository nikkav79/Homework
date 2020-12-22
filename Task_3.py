initial_number = input('Enter a number: ')

n = 3

i = 1
numbers = []
while i <= n:
    number = int(initial_number * i)
    numbers.append(number)
    i = i + 1

sum_numbers = sum(numbers)
print(sum_numbers)
