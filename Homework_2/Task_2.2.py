# replacement = []
#
# while True:
#     print("For exit from program enter 'exit'")
#     something = input("Please, enter something for the list: ")
#     if something == 'exit':
#         break
#     else:
#         replacement.append(something)
#
# print(replacement)

replacement = input("Please, enter something for the list through a space: ").split(' ')
print(replacement)
# print(type(replacement))

auxiliary_variable = None

for number in range(0, len(replacement) - 1, 2):
    auxiliary_variable = replacement[number]
    replacement[number] = replacement[number + 1]
    replacement[number + 1] = auxiliary_variable
print(replacement)

# auxiliary_variable = None
# number = 0
#
# while (number + 1) <= (len(replacement) - 1):
#      auxiliary_variable = replacement[number]
#      replacement[number] = replacement[number + 1]
#      replacement[number + 1] = auxiliary_variable
#      number = number + 2
# print(replacement)










