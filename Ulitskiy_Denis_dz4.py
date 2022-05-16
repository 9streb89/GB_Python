"""2. Написать функцию currency_rates(), принимающую в качестве аргумента код валюты (например, USD, EUR, GBP, ...)
и возвращающую курс этой валюты по отношению к рублю. Использовать библиотеку requests.
В качестве API можно использовать http://www.cbr.ru/scripts/XML_daily.asp. Рекомендация:
выполнить предварительно запрос к API в обычном браузере, посмотреть содержимое ответа.
Можно ли, используя только методы класса str, решить поставленную задачу?
Функция должна возвращать результат числового типа, например float.
Подумайте: есть ли смысл для работы с денежными величинами использовать вместо float тип Decimal?
Сильно ли усложняется код функции при этом? Если в качестве аргумента передали код валюты,
которого нет в ответе, вернуть None. Можно ли сделать работу функции не зависящей от того,
в каком регистре был передан аргумент? В качестве примера выведите курсы доллара и евро."""

# import requests
#
#
# def currency_rates(val):
#     url = "http://www.cbr.ru/scripts/XML_daily.asp"
#     result = requests.get(url)
#     res = str(result.text)
#     index_start = res.find('<Value>', res.find(val))
#     index_end = res.find('</Value>', res.find(val))
#     print(res[index_start + 7: index_end])
#
#
# currency_rates('USD')
# currency_rates('EUR')
import sys

"""3. * (вместо 2) Доработать функцию currency_rates(): теперь она должна возвращать кроме курса дату, 
которая передаётся в ответе сервера. Дата должна быть в виде объекта date. 
Подумайте, как извлечь дату из ответа, какой тип данных лучше использовать в ответе функции?"""

# import requests
# import datetime
#
#
# def currency_rates(val):
#     url = "http://www.cbr.ru/scripts/XML_daily.asp"
#     result = requests.get(url)
#     res = str(result.text)
#     index_start = res.find('<Value>', res.find(val))
#     index_end = res.find('</Value>', res.find(val))
#     dt = str(res[60:70])
#     dtd = datetime.datetime.strptime(dt, '%d.%m.%Y').strftime('%Y-%m-%d')
#     print(res[index_start + 7: index_end])
#     print(dtd)
#
#
# currency_rates('USD')
# currency_rates('EUR')

"""4. Написать свой модуль utils и перенести в него функцию currency_rates() из предыдущего задания. 
Создать скрипт, в котором импортировать этот модуль и выполнить несколько вызовов функции currency_rates(). 
Убедиться, что ничего лишнего не происходит."""

# import utils
#
# print(utils.currency_rates('USD'))

"""
5*(вместо 4) Доработать скрипт из предыдущего задания: теперь он должен работать 
и из консоли. Например:
> python task_4_5.py USD
75.18, 2020-09-05
"""

# import utils
# import sys
#
import utils
import sys

print(utils.currency_rates(sys.argv[1]))