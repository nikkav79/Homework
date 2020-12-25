some_data = [15, 'Alex', 'cdf', ('Alex', 'Mary'), {'CSKA': 1, 'Spartak': 2}, True, 4 + 4j, 0.13, None]

# def type_definition(data):
#     i = 0
#     while i < len(data):
#         print(type(data[i]))
#         i = i + 1

# type_definition(some_data)

def type_definition(data):
    for n in data:
        print(type(n))
type_definition(some_data)




