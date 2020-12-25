number_month = int(input('Enter number of month: '))
seasons = {'Winter': (1, 2, 12), 'Spring': (3, 4, 5), 'Summer': (6, 7, 8), 'Autumn': (9, 10, 11)}

for key in seasons.keys():
    if number_month in seasons[key]:
        print(key)

number_month_list = int(input('Enter number of month: '))
seasons_list = [1, 2, 12, 3, 4, 5, 6, 7, 8, 9, 10, 11]
print(seasons_list[6:9])
for key_list in seasons_list:
    if number_month_list in seasons_list[0:3]:
        print('Winter')
        break
    if number_month_list in seasons_list[3:6]:
        print('Spring')
        break
    if number_month_list in seasons_list[6:9]:
        print('Summer')
        break
    else:
        print('Autumn')
        break

