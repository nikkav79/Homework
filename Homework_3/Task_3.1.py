
def division(number_1, number_2):
    """Function performs division of two numbers"""
    try:
        div_number = float(number_1) / float(number_2)
        return div_number

    except ZeroDivisionError:
        print('You cannot devide by zero. Re-enter a number N2')

    except ValueError:
        print('One of the value is not numerical. Re-enter a numbers')

number_1 = input('Enter a number N1: ')
number_2 = input('Enter a number N2: ')

print(division(number_1, number_2))
