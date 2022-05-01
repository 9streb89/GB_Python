"""1. Написать функцию num_translate(), переводящую числительные от 0 до 10 c английского на
русский язык."""

#
# user = {'one': 'один', 'two': 'два','three': 'три','four': 'четыре', 'five': 'пять', 'six': 'шесть', 'seven': 'семь',
#         'eight': 'восемь', 'nine': 'девять', 'ten': 'десять'}
#
#
# def translate(i):
#     print(user.get(i))
#
#
# translate('nine')

"""3. Написать функцию thesaurus(), принимающую в качестве аргументов имена сотрудников и
возвращающую словарь, в котором ключи — первые буквы имён, а значения — списки,
содержащие имена, начинающиеся с соответствующей буквы"""

# def thesaurus(*names):
#     res = {}
#     for name in names:
#         key = name[0].capitalize()
#         if key not in res:
#             res[key] = []
#         res[key].append(name)
#     return res
#
# print(thesaurus('Иван', 'Мария', 'Петр', 'Илья'))

"""5. Реализовать функцию get_jokes(), возвращающую n шуток, сформированных из трех
случайных слов, взятых из трёх списков (по одному из каждого):"""

# from random import choice
#
# nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
# adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
# adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]
#
#
# def get_jokes(n):
#     for i in range(n):
#         list = []
#         random_index = choice(nouns)
#         random_index_1 = choice(adverbs)
#         random_index_2 = choice(adjectives)
#         joke = f'{random_index} {random_index_1} {random_index_2}'
#         list.append(joke)
#         print(list)
# get_jokes(1)
