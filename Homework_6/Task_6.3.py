'''
3. Реализовать базовый класс Worker (работник), в котором определить атрибуты: name, surname, position (должность), income (доход).
Последний атрибут должен быть защищенным и ссылаться на словарь, содержащий элементы:
оклад и премия, например, {"wage": wage, "bonus": bonus}.
Создать класс Position (должность) на базе класса Worker.
В классе Position реализовать методы получения полного имени сотрудника (get_full_name) и дохода с учетом премии (get_total_income).
Проверить работу примера на реальных данных (создать экземпляры класса Position, передать данные, проверить значения атрибутов, вызвать методы экземпляров).
'''

class Worker:

    def __init__(self, name, surname, position, wage, bonus):
        self.worker_name = name
        self.worker_surname = surname
        self.worker_position = position
        self._worker_income = {"wage": wage, "bonus": bonus}


class Position(Worker):

    def get_full_name(self):
        self.full_name = f'{self.worker_surname} {self.worker_name}'
        return (f'The next employee works in the company: {self.full_name}')


    def get_total_income(self):
        self.total_income = self._worker_income["wage"] + self._worker_income["bonus"]
        return (f'{self.full_name} has the following total annual income: {self.total_income}')

worker_1 = Position('Victor', 'Stepanov', 'senior engineer', 150000, 25000)
print(worker_1.get_full_name())
print(worker_1.get_total_income())
