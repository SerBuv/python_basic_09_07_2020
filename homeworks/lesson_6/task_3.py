'''3. Реализовать базовый класс Worker (работник), в котором определить атрибуты: name, surname, position
 (должность), income (доход). Последний атрибут должен быть защищенным и ссылаться на словарь, содержащий
 элементы: оклад и премия, например, {"wage": wage, "bonus": bonus}. Создать класс Position (должность) на
 базе класса Worker. В классе Position реализовать методы получения полного имени сотрудника (get_full_name)
  и дохода с учетом премии (get_total_income). Проверить работу примера на реальных данных (создать экземпляры
  класса Position, передать данные, проверить значения атрибутов, вызвать методы экземпляров).'''

class Worker:

    def __init__(self, name, sername, position, income):
        self.name = name
        self.sername = sername
        self.position = position
        self._income = income

class Position(Worker):

    def get_full_name(self):
        print('Полное имя сотрудника:', self.name + ' ' + self.sername)

    def get_total_income(self):
        print('Общий доход:', self._income['wage'] + self._income['bonus'])

a = Position('Sergey', 'Buvakov', 'Data Engineer', {"wage": 50000, "bonus": 20000})
a.get_full_name()
a.get_total_income()