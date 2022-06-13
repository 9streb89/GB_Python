"""1. Написать функцию email_parse(<email_address>), которая при помощи регулярного выражения извлекает
имя пользователя и почтовый домен из email адреса и возвращает их в виде словаря. Если адрес не валиден,
выбросить исключение ValueError. Пример:"""

# import re
#
#
# def email_parse(email_address):
#     parsed = re.findall(r'(^\w+)@((\w+).(\w{2,}))$', email_address)
#     if not parsed:
#         raise ValueError(f"wrong email: {email_address}")
#     return dict(zip(["username", "domain"], parsed[0]))
#
#
# print(email_parse("someone@geekbrains.ru"))
# print(email_parse('Vasya@example.ru'))
## print(email_parse('vasyaexaple.ru'))

"""3. Написать декоратор для логирования типов позиционных аргументов функции"""


# def val_checker(func):
#     def wrapper(*args):
#         for arg in args:
#             return f'{func(arg)}: {type(arg)}'
#     return wrapper
#
#
# @val_checker
# def calc_cube(x):
#     return x ** 3
#
#
# a = calc_cube(3)
# print(a)

"""4. Написать декоратор с аргументом-функцией (callback), позволяющий валидировать входные значения функции 
и выбрасывать исключение ValueError"""


# def val_checker(func):
#     def wrapper(*args):
#         if args[0] > 0:
#             return func(*args)
#         else:
#             return f' wrong val {args}'
#
#     return wrapper
#
#
# @val_checker
# def calc_cube(x):
#     return x ** 3
#
#
# print(calc_cube(3))
# print(calc_cube(-3))
