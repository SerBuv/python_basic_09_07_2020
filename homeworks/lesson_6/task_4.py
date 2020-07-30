'''4. Реализуйте базовый класс Car. У данного класса должны быть следующие атрибуты: speed, color,
 name, is_police (булево). А также методы: go, stop, turn(direction), которые должны сообщать, что
 машина поехала, остановилась, повернула (куда). Опишите несколько дочерних классов: TownCar, SportCar,
  WorkCar, PoliceCar. Добавьте в базовый класс метод show_speed, который должен показывать текущую скорость
  автомобиля. Для классов TownCar и WorkCar переопределите метод show_speed. При значении скорости свыше 60
  (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости.'''
class Car:
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police
    def go(self):
        print('Машина поехала')
    def stop(self):
        print('Машина остановилась')
    def turn(self):
        print('Машина повернула')
    def show_speed(self):
        print(f'Текущая скорость автомобиля {self.name}: {self.speed} км/ч')
class TownCar(Car):
    def show_speed(self):
        if self.speed > 60:
            print(f'Текущая скорость автомобиля {self.name}: {self.speed} км/ч. Превышена скорость!')
class SportCar(Car):
    pass
class WorkCar(Car):
    def show_speed(self):
        if self.speed > 40:
            print(f'Текущая скорость автомобиля {self.name}: {self.speed} км/ч. Превышена скорость!')
class PoliceCar(Car):
    pass


a1 = TownCar(20, 'желтая', 'BMW', False)
a2 = WorkCar(70, 'зеленая', 'Mazda', False)
a3 = SportCar(120, 'красная', 'Ferrari', False)
a4 = PoliceCar(90, 'синяя', 'Ford', False)
a1.show_speed()
a2.show_speed()
a3.show_speed()
a4.show_speed()
a1.go()
a1.stop()
a1.turn()
