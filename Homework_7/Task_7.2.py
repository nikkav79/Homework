"""
2. Реализовать проект расчета суммарного расхода ткани на производство одежды.
Основная сущность (класс) этого проекта —
одежда, которая может иметь определенное название.
К типам одежды в этом проекте относятся пальто и костюм.
У этих типов одежды существуют параметры: размер (для пальто) и рост (для костюма).
Это могут быть обычные числа: V и H, соответственно.
Для определения расхода ткани по каждому типу одежды использовать формулы:
для пальто (V/6.5 + 0.5), для костюма (2 * H + 0.3).
Проверить работу этих методов на реальных данных.
Реализовать общий подсчет расхода ткани.
Проверить на практике полученные на этом уроке знания:
реализовать абстрактные классы для основных классов проекта,
проверить на практике работу декоратора @property.
"""

from abc import abstractmethod

class Clothes:

    def __init__(self, size = 0, growth = 0):
        self.clothe_size = size
        self.clothe_growth = growth

    @abstractmethod
    def calculate_area(self):
        pass

class SumOfArea:
    def __init__(self, initial_sum):
        self.init_sum = initial_sum

    def __add__(self, other):
        return SumOfArea(self.init_sum + other)

    def __str__(self):
        return f'{self.init_sum}'

class Suit(Clothes):

    def __checkValue(x):
        if isinstance(x, int) or isinstance(x, float):
            return True
        else:
            return False

    @property
    def calculate_area(self):
        return self.clothe_size/6.5 + 0.5


    @calculate_area.setter
    def calculate_area(self, x):
        if Suit.__checkValue(x):
            self.clothe_size = x
        else:
            raise ValueError('Enter a number')

class Coat(Clothes):

    def __checkValue(x):
        if isinstance(x, int) or isinstance(x, float):
            return True
        else:
            return False

    @property
    def calculate_area(self):
        coat_area = self.clothe_growth * 2 + 0.3
        return coat_area


    @calculate_area.setter
    def calculate_area(self, x):
        if Coat.__checkValue(x):
            self.clothe_growth = x
        else:
            raise ValueError('Enter a number')

clothe_1 = Suit()
clothe_1.calculate_area = 10
print(clothe_1.calculate_area)

clothe_2 = Coat()
clothe_2.calculate_area = 1
print(clothe_2.calculate_area)

sum_1 = SumOfArea(0)
print(sum_1)
print(sum_1 + clothe_2.calculate_area + clothe_1.calculate_area)



