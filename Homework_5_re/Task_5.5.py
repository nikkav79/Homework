'''
Создать (программно) текстовый файл,
записать в него программно набор чисел, разделённых пробелами.
Программа должна подсчитывать сумму чисел в файле и выводить её на экран.
'''

with open('some_data_5.5.txt', 'w', encoding='utf-8') as object:
    input_data = input('Enter a number: ')
    object.write(input_data)
    print(input_data)

with open('some_data_5.5.txt', 'r', encoding='utf-8') as object:
    data = object.readline().split(' ')
    sum = 0
    for i in data:
       sum = sum + float(i)
    print(sum)
