import random

# class InitialData:
#     def  __init__(self, numbers, num_lines, player_name):
#         self.num_for_card = list(range(1, numbers + 1 , 1))
#         self.num_lines = num_lines
#         self.player_name = player_name
#

class Card:

    def __init__(self, data_for_card, num_lines = 3, num_elem = 5):
        self.data_for_card = data_for_card
        self.temporary_data = []
        self.num_lines = num_lines
        self.num_elem = num_elem
        self.example_card = []
        self.make_card()

    def __str__(self):
        return f'{self.example_card}'

    def make_card(self):

        for line in range(self.num_lines):
            self.line = random.sample(self.data_for_card, self.num_elem)
            self.example_card.append(sorted(self.line))

            self.temporary_data = [self.temporary_data.append(i) for i in self.example_card]
            self.data_for_card = [i for i in self.data_for_card if i not in self.temporary_data]

        return self.example_card


# init_data = InitialData(91, 3, 'Nik')

data = range(1, 91, 1)
temp_data = []

player_card = Card(data, 3, 5)
print(player_card)

