'''
Создать вручную и заполнить несколькими строками текстовый файл,
в котором каждая строка будет содержать данные о фирме: название, форма собственности, выручка, издержки.
Пример строки файла: firm_1   ООО   10000   5000.
Необходимо построчно прочитать файл, вычислить прибыль каждой компании, а также среднюю прибыль.
Если фирма получила убытки, в расчёт средней прибыли её не включать.
Далее реализовать список. Он должен содержать словарь с фирмами и их прибылями, а также словарь со средней прибылью.
 Если фирма получила убытки, также добавить её в словарь (со значением убытков).
Пример списка: [{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000}, {“average_profit”: 2000}].
Итоговый список сохранить в виде json-объекта в соответствующий файл.
Пример json-объекта:
[{"firm_1": 5000, "firm_2": 3000, "firm_3": 1000}, {"average_profit": 2000}]
Подсказка: использовать менеджер контекста.
'''
import re
import json

with open('some_data_5.7.txt', 'r', encoding='utf-8') as object:
    data = object.readlines()
    print(data)
    firm_with_profit =[]
    firm_dict = {}
    average_profit_dict = {}

    for i in data:

        data_clean_1 = re.split(' ', i.strip())
        data_clean_2 = (list(filter(str.isdigit, data_clean_1)))
        profit = float(data_clean_2[0]) - float(data_clean_2[1])
        print(f"Profit of the {data_clean_1[0]} is: {profit}")

        firm_dict.setdefault(data_clean_1[0], profit)

        if profit > 0:
            firm_with_profit.append(profit)
    average_profit = sum(firm_with_profit) / len(firm_with_profit)
    print(f'Average profit is: {average_profit}')

    average_profit_dict.setdefault('average_profit', average_profit )

    print(firm_dict, average_profit_dict)

with open('Task_5.7.json', 'w', encoding='utf8') as object_json:
    json.dump([firm_dict, average_profit_dict], object_json)


