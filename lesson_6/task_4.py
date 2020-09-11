"""Реализуйте базовый класс Car. У данного класса должны быть следующие атрибуты: speed, color, name, is_police
(булево).  А также методы: go, stop, turn(direction), которые должны сообщать, что машина поехала, остановилась,
повернула (куда). Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar. Добавьте в базовый
класс метод show_speed, который должен показывать текущую скорость автомобиля. Для классов TownCar и WorkCar
переопределите метод show_speed. При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение
о превышении скорости.
Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к атрибутам, выведите результат.
Выполните вызов методов и также покажите результат.
"""


class Car:
    def __init__(self, speed=60, color='red', name='Car', is_police=False):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        print(f'Машина {self.name} поехала')

    def stop(self):
        print(f'Машина {self.name} остановилась')

    def turn(self, side):
        print(f'Машина {self.name} повернула {side}')

    def show_speed(self):
        print(f'Текущая скорость {self.name} - {self.speed}')


class TownCar(Car):
    def __init__(self, speed=60, color='blue', name='TownCar', is_police=False):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        print(f'Текущая скорость {self.name} - {self.speed}' if self.speed <= 60 else f'Превышение скорости {self.name}'
                                                                                      f' на {self.speed - 60}')


class SportCar(Car):
    def __init__(self, speed=120, color='orange', name='SportCar', is_police=False):
        super().__init__(speed, color, name, is_police)


class WorkCar(Car):
    def __init__(self, speed=40, color='yellow', name='WorkCar', is_police=False):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        print(f'Текущая скорость {self.name} - {self.speed}' if self.speed <= 40 else f'Превышение скорости {self.name}'
                                                                                      f' на {self.speed - 40}')


class PoliceCar(Car):
    def __init__(self, speed=120, color='black', name='PoliceCar', is_police=True):
        super().__init__(speed, color, name, is_police)


town_car = TownCar(90)
sport_car = SportCar()
work_car = WorkCar(50)
police_car = PoliceCar(color='white')


def show_car_info(car):
    print(f'Название машины - {car.name}, скорость машины - {car.speed}, цвет машины - {car.color}, '
          f'машина полицеская? - {car.is_police}')


def car_start_driving(car):
    car.go()
    car.show_speed()
    car.turn('направо')
    car.stop()

show_car_info(town_car)
show_car_info(sport_car)
show_car_info(work_car)
show_car_info(police_car)

car_start_driving(town_car)
car_start_driving(sport_car)
car_start_driving(work_car)
car_start_driving(police_car)
