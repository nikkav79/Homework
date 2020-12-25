rating = [7, 7, 5, 3, 2, 1]
rat_number = None

while rat_number != 'exit':

    print("If you want to exit from program enter 'exit'")
    rat_number = input('Enter the number: ')
    if rat_number == 'exit':
        break
    else:
        rat_number = int(rat_number)
        rating.append(rat_number)
        rating.sort(reverse = True)
        print(rating)
