f = open('some_data.txt', 'w' )
input_data = None
while True:
    if input_data != ' ':
        input_data = input('Enter your data: ')
        f.write(input_data + '\n')
    else:
        break
f.close()

