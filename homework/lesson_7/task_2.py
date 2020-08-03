'''2. Реализовать проект расчета суммарного расхода ткани на производство одежды. Основная сущность
(класс) этого проекта — одежда, которая может иметь определенное название. К типам одежды в этом проекте
относятся пальто и костюм. У этих типов одежды существуют параметры: размер (для пальто) и рост (для костюма).
 Это могут быть обычные числа: V и H, соответственно.'''

from abc import ABC, abstractmethod

class MyAbstractClass(ABC):
    @abstractmethod
    def coat(self, size):
        pass
    @abstractmethod
    def suit(self, height):
        pass

class Clothes(MyAbstractClass):
    def coat(self, size):
        self.size = size
        return (self.size / 6.5 + 0.5)

    def suit(self, height):
        self.height = height
        return (2 * self.height + 0.3)

class SumExp(Clothes):
    def sum_exp(self, h, s):
        return

c = Clothes()
print('Расход ткани на пальто:', c.coat(42))

s = Clothes()
print('Расход ткани на костюм:', s.suit(80))

