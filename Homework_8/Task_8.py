import random as rnd


class GenNum:

    """Класс предназначен для генерации неповторяющегося случайного числа (списка или несколько списков с
    неповторяющимися числами"""

    def __init__(self, numbers = None, quantity = None):
        self.in_data = list(range(1, numbers + 1 , 1))
        self.num_quantity = quantity
        self.output_data = []
        self.make_numbers()

    def make_numbers(self):
        for num in range(1):
            self.numbers = rnd.sample(self.in_data, self.num_quantity)
            [(self.output_data.append(i), self.in_data.remove(i)) for i in self.numbers]

        return self.output_data

class Card(GenNum):

    """Дочерний класс от GenNum. Созадет карточку для игрока или компьютера"""

    def __init__(self, numbers, quantity, empty_num, indent, num_string, name):
        super().__init__(numbers, quantity)
        self.name = name
        self.indent = indent
        self.empty_num = empty_num
        self.num_string = num_string
        self.sum_columns = int(quantity/num_string * 2 + empty_num * 2 + (quantity/num_string + empty_num - 1) * 2)
        self.card_maker()

    def __str__(self):

        self.display_card = '\n'.join('  '.join(map(str, line)) for line in self.change)

        return f'{"-" * self.indent}{self.name}{"-" * (self.sum_columns - len(self.name) - self.indent)}\n{self.display_card}\n{"-" * self.sum_columns}'

    def card_maker(self):
        self.change = [sorted(self.output_data[0:5]), sorted(self.output_data[5:10]), sorted(self.output_data[10:15])]

        for num in range(self.empty_num):
            for self.line in self.change:
                self.line.insert(rnd.randint(0, len(self.line)), '**')

class Game:

    def __init__(self, data_for_play, player_card):
        self.data_for_play = data_for_play
        self.card = player_card
        self.balance = len(data_for_play)
        self.play()

    def play(self):
        for self.num in self.data_for_play:
            self.balance -= 1
            print(f'Бочонок: {self.num}. Осталось: {self.balance}')
            print(self.card)
            self.question = input('Будем вычеркивать? y/n' '\n')

            if self.num in self.card.output_data and self.question == 'y':
                print('Отлично!')
                for self.line in self.card.change:
                    if self.num in self.line:
                        self.num_index = self.line.index(self.num)
                        self.line[self.num_index] = '--'
                    else:
                        pass

            elif self.num not in self.card.output_data and self.question == 'n':
                print('ОК, далее')

            elif self.num not in self.card.output_data and self.question == 'y':
                print('Такого числа нет')
                return

            elif self.num in self.card.output_data and self.question == 'n':
                print('Число есть, но Вы не заметили')
                return



player_card = Card(90, 15, 4, 6, 3, 'Efim')

data_for_play = GenNum(90,90)

game = Game(data_for_play.output_data, player_card)




