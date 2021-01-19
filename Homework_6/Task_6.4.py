'''
Реализуйте базовый класс Car.
У данного класса должны быть следующие атрибуты:
speed, color, name, is_police (булево).
А также методы: go, stop, turn(direction), которые должны сообщать, что машина поехала, остановилась, повернула (куда).
Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar.
Добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля.
Для классов TownCar и WorkCar переопределите метод show_speed.
При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости.
Создайте экземпляры классов, передайте значения атрибутов.
Выполните доступ к атрибутам, выведите результат. Выполните вызов методов и также покажите результат.
'''

class Car:

    def __init__(self, speed, color, name, is_police = False):
        self.car_speed = float(speed)
        self.car_color = color
        self.car_name = name
        self.car_police = is_police

        # self.car_is_police = is_police

    def go(self):
        return f'The {self.car_color} car {self.car_name} starting moving'

    def stop(self):
        return f'The {self.car_color} car {self.car_name} stopped'

    def turn(self, direction):
        self.car_direction = direction
        return f'The {self.car_color} car {self.car_name} turned {self.car_direction}'

    def show_speed (self,):
        return f'Current speed of a {self.car_color} {self.car_name} is {self.car_speed}'

class TownCar(Car):
    def show_speed(self):
        if self.car_speed > 60:
            return f'The speed of a {self.car_color} {self.car_name} exceeded'
        else:
            return f'Speed is OK'

class SportCar(Car):
    pass

class WorkCar(Car):
    def show_speed(self):
        if self.car_speed > 40:
            return f'The speed of a {self.car_color} {self.car_name} exceeded'
        else:
            return f'Speed is OK'

class PoliceCar(Car):
    pass

car_1 = TownCar(50, 'green', 'Volvo XC90', False)
print(car_1.go())
print(car_1.stop())
print(car_1.turn('left'))
print(car_1.show_speed())

car_2 = WorkCar(30, 'yellow', 'Honda Civic', False)
print(car_2.go())
print(car_2.stop())
print(car_2.turn('left'))
print(car_2.show_speed())