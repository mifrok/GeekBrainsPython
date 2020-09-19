"""
Реализовать проект расчета суммарного расхода ткани на производство одежды. Основная сущность (класс) этого
проекта — одежда, которая может иметь определенное название. К типам одежды в этом проекте относятся пальто и
костюм. У этих типов одежды существуют параметры: размер (для пальто) и рост (для костюма). Это могут быть обычные
числа: V и H, соответственно.
Для определения расхода ткани по каждому типу одежды использовать формулы: для пальто (V/6.5 + 0.5), для костюма
(2 * H + 0.3). Проверить работу этих методов на реальных данных.
Реализовать общий подсчет расхода ткани. Проверить на практике полученные на этом уроке знания: реализовать
абстрактные классы для основных классов проекта, проверить на практике работу декоратора @property.
"""
from abc import ABC, abstractmethod


class clothes(ABC):
    def __init__(self, type):
        self.type = type

    @abstractmethod
    def textile_cost(self):
        pass


class Coat(clothes):
    def __init__(self, type, size):
        super().__init__(type)
        self.size = size

    @property
    def textile_cost(self):
        return self.size / 6.5 + 0.5


class Suit(clothes):
    def __init__(self, type, height):
        super().__init__(type)
        self.height = height

    @property
    def textile_cost(self):
        return 2 * self.height + 0.3


new_coat = Coat('Пальто', 52)
new_suit = Suit('Костюм', 52)

print(f'Рсаход ткани на пальто: {new_coat.textile_cost}, расход ткани на костюм: {new_suit.textile_cost}, '
      f'общий расход ткани: {new_coat.textile_cost + new_suit.textile_cost}')