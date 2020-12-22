income = float(input('Add company income: '))
costs = float(input('Add company costs: '))

fin_results = income - costs

if fin_results > 0:
    print('The company makes a profit equal to {}'.format(fin_results))

    profitability = float(fin_results / income)
    print("The company's profitability is equal to {}".format(round(profitability, 2)))

    number_of_employees = int(input('Enter the number of employees: '))
    profit_per_person = float(fin_results / number_of_employees)

    print('Profit per person equal to {}'.format(round(profit_per_person, 2)))
else:
    print('The company is operating at a loss equal to {}'.format(fin_results))

