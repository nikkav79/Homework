'''
2. Реализовать класс Road (дорога),
в котором определить атрибуты: length (длина), width (ширина).
Значения данных атрибутов должны передаваться при создании экземпляра класса.
Атрибуты сделать защищенными.
Определить метод расчета массы асфальта, необходимого для покрытия всего дорожного полотна.
Использовать формулу: длина * ширина * масса асфальта для покрытия одного кв метра дороги асфальтом, толщиной в 1 см * число см толщины полотна.
Проверить работу метода.
Например: 20м * 5000м * 25кг * 5см = 12500 т
'''
class Road:
    """Program calculate mass of asphalt"""
    road_section = 0
    #
    def __init__(self, length, width,thickness):
        self._length = length
        self._width = width
        self.__unit_weight = 25
        self._thickness = thickness
        Road.road_section += 1

    def mass_calculation(self):
        self.mass = (self._width * self._length * self.__unit_weight * self._thickness) / 1000
        print(f'The mass of asphalt of the {Road.road_section} section of the road is {self.mass} tons')

    def display_parameters(self):
        print(f'''The following parametres are used for the calculation: \n length = {self._length} m \n width = {self._width} m \n thickness = {self._thickness} cm \n weight of 1 centimeter of asphalt = {self.__unit_weight} cm''')

section_1 = Road(length=300, width=15, thickness=7)
section_1.display_parameters()
section_1.mass_calculation()

