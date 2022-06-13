"""1. Реализовать класс «Дата», функция-конструктор которого должна принимать дату
в виде строки формата «день-месяц-год»"""


# class Data:
#     def __init__(self, day_month_year):
#         self.day_month_year = str(day_month_year)
#
#     @classmethod
#     def extract(cls, day_month_year):
#         my_date = []
#         for i in day_month_year.split():
#             if i != '-': my_date.append(i)
#         return int(my_date[0]), int(my_date[1]), int(my_date[2])
#
#     @staticmethod
#     def valid(day, month, year):
#         if 1 <= day <= 31:
#             if 1 <= month <= 12:
#                 if 2022 >= year >= 0:
#                     return f'Все правильно'
#                 else:
#                     return f'Неправильный год'
#             else:
#                 return f'Неправильный месяц'
#         else:
#             return f'Неправильный день'
#
#     def __str__(self):
#         return f'Текущая дата {Data.extract(self.day_month_year)}'
#
#
# today = Data('15 - 5 - 2015')
# print(today)
# print(Data.valid(15, 5, 2015))
# print(today.valid(15, 15, 2015))
# print(Data.extract('11 - 11 - 2011'))

"""2. Создайте собственный класс-исключение, обрабатывающий ситуацию деления на ноль"""

# class Null:
#     def __init__(self, divider, denominator):
#         self.divider = divider
#         self.denominator = denominator
#
#     @staticmethod
#     def divide_by_null(divider, denominator):
#         try:
#             return (divider / denominator)
#         except:
#             return (f"Деление на ноль недопустимо")
#
#
# div = Null(1, 10)
# print(Null.divide_by_null(11, 0))
# print(Null.divide_by_null(100, 2))
# print(div.divide_by_null(10, 0))

"""3. Создайте собственный класс-исключение, который должен проверять содержимое списка на наличие только чисел."""


# class OnliInt:
#     def __init__(self, *args):
#         self.my_list = []
#
#     def my_input(self):
#         while True:
#             try:
#                 val = int(input('Введите значения и нажимайте Enter: '))
#                 self.my_list.append(val)
#                 print(f'Текущий список - {self.my_list} \n ')
#             except:
#                 print(f"Недопустимое значение - строка")
#                 y_or_n = input(f'Попробовать еще раз? Y/N ')
#
#                 if y_or_n == 'Y' or y_or_n == 'y':
#                     print(try_except.my_input())
#                 elif y_or_n == 'N' or y_or_n == 'n':
#                     return f'Вы вышли'
#                 else:
#                     return f'Вы вышли'
#
#
# try_except = OnliInt(1)
# print(try_except.my_input())

"""4. Начните работу над проектом «Склад оргтехники».
   5. Продолжить работу над первым заданием.
   6. Продолжить работу над вторым заданием. """


# class OfficeEquipment:
#     def __init__(self, name, quantity, number_of_lists, *args):
#         self.name = name
#         self.quantity = quantity
#         self.numb = number_of_lists
#         self.my_store_full = []
#         self.my_store = []
#         self.my_unit = {'Модель устройства': self.name, 'Количество': self.quantity}
#
#     def __str__(self):
#         return f'{self.name} количество {self.quantity}'
#
#     def reception(self):
#         try:
#                 unit = input(f'Введите наименование ')
#                 unit_q = int(input(f'Введите количество '))
#                 unique = {'Модель устройства': unit, 'Количество': unit_q}
#                 self.my_unit.update(unique)
#                 self.my_store.append(self.my_unit)
#                 print(f'Текущий список -\n {self.my_store}')
#         except:
#             return f'Ошибка ввода данных'
#         print(f'Для выхода - Q, продолжение - Enter')
#         q = input(f'---> ')
#         if q == 'Q' or q == 'q':
#             self.my_store_full.append(self.my_store)
#             print(f'Весь склад -\n {self.my_store_full}')
#             return f'Выход'
#         else:
#             return OfficeEquipment.reception(self)
#
#
# class Printer(OfficeEquipment):
#     def to_print(self):
#         return f'На складе {self.numb} принтеров'
#
#
# class Scanner(OfficeEquipment):
#     def to_scan(self):
#         return f'На складе {self.numb} сканеров'
#
#
# class Copier(OfficeEquipment):
#     def to_copier(self):
#         return f'На складе {self.numb} ксероксов'
#
#
# unit_1 = Printer('hp', 5, 10)
# unit_2 = Scanner('Canon', 5, 10)
# unit_3 = Copier('Xerox', 1, 15)
# print(unit_1.reception())
# print(unit_1.to_print())
# print(unit_3.to_copier())
