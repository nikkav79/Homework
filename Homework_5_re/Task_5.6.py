'''
Сформировать (не программно) текстовый файл.
В нём каждая строка должна описывать учебный предмет и наличие лекционных,
практических и лабораторных занятий по предмету.
Сюда должно входить и количество занятий.
Необязательно, чтобы для каждого предмета были все типы занятий.
Сформировать словарь, содержащий название предмета и общее количество занятий по нему.
Вывести его на экран.
Примеры строк файла: Информатика:   100(л)   50(пр)   20(лаб).
                                        Физика:   30(л)   —   10(лаб)
                                        Физкультура:   —   30(пр)   —
Пример словаря: {“Информатика”: 170, “Физика”: 40, “Физкультура”: 30}
'''
import re

with open('some_data_5.6.txt', 'r', encoding='utf-8') as object:
    data = object.readlines()
    dict = {}
    for i in data:
        data_clean_1 = re.split('[-: ().]', i.strip())
        data_clean_2 = (list(filter(str.isdigit, data_clean_1)))
        sumtime = 0
        for v in data_clean_2:
            sumtime = sumtime + float(v)
        dict.setdefault(data_clean_1[0],sumtime)
    print(dict)

    # for i in d:
    #     if i ==None:
    #         d.pop(i)
    #     print(d)
    # training_program = {k: v for k, v in data_staff_dict.items() if v == min_salary}

