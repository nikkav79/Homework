initial_distance = int(input('Specify the starting distance: '))
required_distance = int(input('Specify the required distance: '))

progress = 0.1  * initial_distance
days = 0
current_distance = initial_distance

while current_distance != required_distance:
    current_distance = float(initial_distance + progress * days)
    days = days + 1

print('You need {} days'.format(days))




