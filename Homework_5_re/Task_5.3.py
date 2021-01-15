'''
Создать текстовый файл (не программно),
построчно записать фамилии сотрудников и величину их окладов.
Определить, кто из сотрудников имеет оклад менее 20 тыс.,
вывести фамилии этих сотрудников. Выполнить подсчет средней
величины дохода сотрудников.
'''


with open('some_data_5.3.txt', encoding='utf-8') as f_obj:

    data_staff = f_obj.readlines()

    data_staff_dict = {}
    min_salary_group = []

    for staff in data_staff:
        data = staff.strip().split(' - ')
        data_staff_dict.setdefault(data[0], float(data[1]))
        if float(data[1]) < 20000:
            min_salary_group.append(data[0])

    min_salary = min(data_staff_dict.values())
    need_help_men = {k:v for k, v in data_staff_dict.items() if v == min_salary }

    print(f'This mens have salary below 20000: {min_salary_group}')
    print(f'This men need some help: {need_help_men}')
    print(f'Average salary is: {sum(data_staff_dict.values())/len(data_staff_dict)}')





