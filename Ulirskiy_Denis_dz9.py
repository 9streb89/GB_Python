"""1. Создать класс TrafficLight (светофор)."""

# from time import sleep
# class TrafficLight:
#     __color = ['Красный', 'Желтый', 'Зеленый']
#
#     def running(self):
#         i = 0
#         while i < 3:
#             print(f'{TrafficLight.__color[i]}')
#             if i == 0:
#                 sleep(7)
#             elif i == 1:
#                 sleep(2)
#             elif i == 2:
#                 sleep(5)
#             i += 1
#
#
# a = TrafficLight()
# a.running()

"""2. Реализовать класс Road (дорога)."""

# class Road:
#     def __init__(self, _length, _width):
#         self._length = _length
#         self._width = _width
#
#     def mass(self):
#         return f'{self._length * self._width * 0.125} тонн'
#
#
# b = Road(20, 5000)
# print(b.mass())

"""3. Реализовать базовый класс Worker (работник)."""

# class Worker:
#     def __init__(self, name, surname, position, wage, bonus):
#         self.name = name
#         self.surname = surname
#         self.position = position
#         self._income = {"wage": wage, "bonus": bonus}
#
#
# class Position(Worker):
#
#     def __init__(self, name, surname, position, wage, bonus):
#         super().__init__(name, surname, position, wage, bonus)
#
#     def get_full_name(self):
#         return self.name + ' ' + self.surname
#
#     def get_total_income(self):
#         return self._income.get('wage') + self._income.get('bonus')
#
#
# a = Position('Иван', 'Иванов', 'Прораб', 150000, 50999)
# print(a.get_full_name())
# print(a.position)
# print(a.get_total_income())

"""4. Реализуйте базовый класс Car."""

# class Car:
#     def __init__(self, speed, color, name, is_police):
#         self.speed = speed
#         self.color = color
#         self.name = name
#         self.is_police = is_police
#
#     def go(self):
#         return f'{self.name} поехала'
#
#     def stop(self):
#         return f'{self.name} остановилась'
#
#     def turn_right(self):
#         return f'{self.name} повернула направо'
#
#     def turn_left(self):
#         return f'{self.name} повернула налево'
#
#     def show_speed(self):
#         return f'Текущая скорость {self.name}  {self.speed}'
#
#
# class TownCar(Car):
#     def __init__(self, speed, color, name, is_police):
#         super().__init__(speed, color, name, is_police)
#
#     def show_speed(self):
#         print(f'Текущая скорость {self.name} {self.speed}')
#
#         if self.speed > 60:
#             return f'{self.name} превышает разрешенную скорость'
#         else:
#             return f'Скорость {self.name} нормальная'
#
#
# class SportCar(Car):
#     def __init__(self, speed, color, name, is_police):
#         super().__init__(speed, color, name, is_police)
#
#
# class WorkCar(Car):
#     def __init__(self, speed, color, name, is_police):
#         super().__init__(speed, color, name, is_police)
#
#     def show_speed(self):
#         print(f'Текущая скорость {self.name} {self.speed}')
#
#         if self.speed > 40:
#             return f'{self.name} превышает разрешенную скорость'
#         else:
#             return f'Скорость {self.name} нормальная'
#
#
# class PoliceCar(Car):
#     def __init__(self, speed, color, name, is_police):
#         super().__init__(speed, color, name, is_police)
#
#     def police(self):
#         if self.is_police:
#             return f'{self.name} из отдела полиции'
#
#
# BMW = SportCar(120, 'black', 'BMW', False)
# VAZ_2106 = TownCar(50, 'White', 'VAZ_2106', False)
# Ford_focus = WorkCar(50, 'red', 'Ford_focus', False)
# Lamborghini = PoliceCar(130, 'yellow',  'Lamborghini', True)
#
# print(Ford_focus.turn_left())
# print(BMW.stop())
# print(f'{Ford_focus.name}  {Ford_focus.color}')
# print(BMW.show_speed())
# print(VAZ_2106.show_speed())
# print(Lamborghini.police())
# print(f'{Ford_focus.go()}')
# print(Ford_focus.show_speed())

"""Реализовать класс Stationery (канцелярская принадлежность)"""


# class Stationery:
#     def __init__(self, title):
#         self.title = title
#
#     def draw(self):
#         return f'Запуск отрисовки {self.title}'
#
#
# class Pen(Stationery):
#     def __init__(self, title):
#         super().__init__(title)
#
#     def draw(self):
#         return f'Вы взяли {self.title}, идет отрисовка ручкой'
#
#
# class Pencil(Stationery):
#     def __init__(self, title):
#         super().__init__(title)
#
#     def draw(self):
#         return f'Вы взяли {self.title}, идет отрисовка карандашем'
#
#
# class Handle(Stationery):
#     def __init__(self, title):
#         super().__init__(title)
#
#     def draw(self):
#         return f'Вы взяли {self.title}, идет отрисовка маркером'
#
#
# pen = Pen('Ручка')
# pencil = Pencil('Карандаш')
# handle = Handle('Маркер')
# tassel = Stationery('Кисточка')
#
# print(tassel.draw())
# print(pen.draw())
# print(pencil.draw())
# print(handle.draw())
