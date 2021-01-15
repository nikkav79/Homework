'''
Создать (не программно) текстовый файл со следующим содержимым:
One - 1
Two - 2
Three - 3
Four - 4
Необходимо написать программу, открывающую файл на чтение и считывающую
построчно данные. При этом английские числительные должны заменяться на русские.
Новый блок строк должен записываться в новый текстовый файл.
'''
change_data = {'One': 'Один', 'Two': 'Два', 'Three': 'Три', 'Four': 'Четыре'}

with open('some_data_5.4.txt', encoding='utf-8') as object:
    data = object.readlines()
    new_data = []
    for i in data:
        en_num = i.strip().split(' - ')
        keyword = en_num[0]
        new_data.append(f'{change_data[keyword]} - {en_num[1]}')
    print(new_data)

with open('new_some_data_5.4.txt','a', encoding='utf-8') as new_object:
    for i in new_data:
        new_object.write(i+ '\n')




