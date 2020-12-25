product_data = {}
catalog = []
#Создание наименований в словаре
while True:
    print("Enter 'exit' for end")
    dict_name = input('Enter name of parameters: ')
    if dict_name == 'exit':
        break
    else:
        product_data[dict_name] = None
print(product_data)

#Заполнение словаря
i = 1
number_position = int(input('Enter numbers of product positions: '))
while i <= number_position:
    for key in product_data:
        user_data = input("Enter {} of product: ".format(key))
        if user_data.isdigit():
            product_data[key] = int(user_data)
        else:
            product_data[key] = user_data

    print(' ')
    catalog.append(tuple((i, product_data)))
    i = i + 1

#Вывод каталога
for j in catalog:
    print(j)


# i = 1
# jam = [ ]
# # while i < number_position:
# jam = tuple(i, product_data)
# #    print(jam)
# #    i += 1







