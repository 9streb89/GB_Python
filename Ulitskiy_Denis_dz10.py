"""1. Реализовать класс Matrix (матрица). Обеспечить перегрузку конструктора класса (метод __init__()),
который должен принимать данные (список списков) для формирования матрицы."""

# import copy
#
#
# class Matrix:
#     def __init__(self, matrix):
#         self.matrix = matrix
#
#     def __str__(self):
#         s = ''
#         for i in range(len(self.matrix)):
#             s = s + '\t'.join(map(str,self.matrix[i])) + '\n'
#         return s
#
#     def __add__(self, other):
#         if len(self.matrix) != len(other.matrix):
#             return None
#         res = copy.deepcopy(self.matrix)
#         for i in range(len(self.matrix)):
#             for k in range(len(self.matrix[i])):
#                 res[i][k] = self.matrix[i][k] + other.matrix[i][k]
#         return Matrix(res)
#
#
# l1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# l2 = [[10, 10, 10], [10, 10, 10], [10, 10, 10]]
# m = Matrix(l1)
# s = Matrix(l2)
# print(m)
# print(s)
# z = m + s
# print(z)

"""2. Реализовать проект расчёта суммарного расхода ткани на производство одежды."""


# class Textil:
#     def __init__(self, width, height):
#         self.width = width
#         self.height = height
#
#     def get_square_c(self):
#         return self.width / 6.5 + 0.5
#
#     def get_square_j(self):
#         return self.height * 2 + 0.3
#
#     @property
#     def get_sj_full(self):
#         return str(f'Площадь общая ткани \n'
#                    f' {(self.width / 6.5 + 0.5) + (self.height * 2 + 0.3)}')
#
#
# class Coat(Textil):
#     def __init__(self, width, height):
#         super().__init__(width, height)
#         self.square_c = self.width / 6.5 + 0.5
#
#     def __str__(self):
#         return f'Площадь на пальто {self.square_c}'
#
#
# class Jacket(Textil):
#     def __init__(self, width, height):
#         super().__init__(width, height)
#         self.square_j = self.height * 2 + 0.3
#
#     def __str__(self):
#         return f'Площадь на костюм {self.square_j}'
#
#
# coat = Coat(2, 4)
# jacket = Jacket(1, 2)
# print(coat)
# print(jacket)
# print('\n')
# print(coat.get_square_c())
# print(coat.get_square_j())
# print(coat.get_sj_full)
# print('\n')
# print(jacket.get_square_c())
# print(jacket.get_square_j())
# print(jacket.get_sj_full)

"""3. Осуществить программу работы с органическими клетками, состоящими из ячеек"""


# class Cell:
#     def __init__(self, quantity):
#         self.quantity = int(quantity)
#
#     def __str__(self):
#         return f'Результат операции {self.quantity * "*"}'
#
#     def __add__(self, other):
#         return Cell(self.quantity + other.quantity)
#
#     def __sub__(self, other):
#         return self.quantity - other.quantity if (self.quantity - other.quantity) > 0 else print('Отрицательное число!')
#
#     def __mul__(self, other):
#         return Cell(int(self.quantity * other.quantity))
#
#     def __truediv__(self, other):
#         return Cell(round(self.quantity // other.quantity))
#
#     def make_order(self, cells_in_row):
#         row = ''
#         for i in range(int(self.quantity / cells_in_row)):
#             row += f'{"*" * cells_in_row} \\n'
#         row += f'{"*" * (self.quantity % cells_in_row)}'
#         return row
#
#
# cells1 = Cell(15)
# cells2 = Cell(5)
# print(cells1)
# print(cells2)
# print(cells1 + cells2)
# print(cells2 - cells1)
# print(cells2.make_order(3))
# print(cells1.make_order(3))
# print(cells1 / cells2)
