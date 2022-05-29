"""1. Не используя библиотеки для парсинга, распарсить (получить определённые данные) файл логов web-сервера
nginx_logs.txt (https://github.com/elastic/examples/raw/master/Common%20Data%20Formats/nginx_logs/nginx_logs) —
получить список кортежей вида: (<remote_addr>, <request_type>, <requested_resource>). Например"""

# file_1 = open('nginx_logs.txt', 'r',  encoding='utf-8')
# line = file_1.readline()
# while line:
#     line = file_1.readline()
#     ind_1 = line.find('- -')
#     ind_2 = line.find('GET')
#     ind_3 = line.find('HTTP')
#     list = line[0:ind_1] + line[ind_2: ind_2 +2] + line[ind_2 + 2:ind_3 - 1]
#     t = tuple(list.split())
#     print(t)
#     list_2 = (list.split())
#     # print(list_2)
#
# file_1.close()

"""2. * (вместо 1) Найти IP адрес спамера и количество отправленных им запросов по данным файла логов из 
предыдущего задания. Примечания: спамер — это клиент, отправивший больше всех запросов; 
код должен работать даже с файлами, размер которых превышает объем ОЗУ компьютера."""

# file_1 = open('nginx_logs.txt', 'r',  encoding='utf-8')
# line = file_1.readline()
# while line:
#     line = file_1.readline()
#     ind_1 = line.find('- -')
#     ind_2 = line.find('GET')
#     ind_3 = line.find('HTTP')
#     list = line[0:ind_1] + line[ind_2: ind_2 +2] + line[ind_2 + 2:ind_3 - 1]
#     t = tuple(list.split())
#     type_ip = (''.join(t[0]))
#     for i in type_ip:
#         data = type_ip.splitlines()
#         print(data)
# file_1.close()
"""не получилось)) я пытался))"""


"""3. Есть два файла: в одном хранятся ФИО пользователей сайта, а в другом — данные об их хобби...."""

# my_file_1 = open('users.csv', 'w+', encoding='utf-8')
# my_file_1.write('Иванов,Иван,Иванович\nПетров,Петр,Петрович')
# my_file_2 = open('hobby.csv', 'w+', encoding='utf-8')
# my_file_2.write('скалолазание, охота\nгорные лыжи')
# my_file_1.close()
# my_file_2.close()

# import json
# with open('users.csv', 'r', encoding='utf-8') as f_1:
#     data_1 = f_1.read()
#     list_1 = []
#     for line in data_1.replace(',', ' ').split('\n'):
#         if not line.strip():
#             continue
#         list_1.append((line.lstrip()))
#
# with open('hobby.csv', 'r', encoding='utf-8') as f_2:
#     data_2 = f_2.read()
#     list_2 = []
#     for line in data_2.replace(',', ' ').split('\n'):
#         if not line.strip():
#             continue
#         list_2.append((line.lstrip()))
#
# new_dict_1 = dict(zip(list_1, list_2))
# print(new_dict_1)
#
# with open('new_dict.txt', 'w', encoding='utf-8') as f:
#     json.dump(new_dict_1, f, ensure_ascii=False)

"""6. Реализовать простую систему хранения данных о суммах продаж булочной. """
"""a)"""
# sale = "5978,5\n8914,3\n7879,1\n1573,7"
# with open('bakery.csv', 'w+', encoding='utf-8') as file:
#     file.write(sale)
#
# with open('bakery.csv', 'r', encoding='utf-8') as file:
#     print(sale)

"""б)"""

# n = int(input())
# with open('bakery.csv', 'r', encoding='utf-8') as file:
#     data = file.read().split()
#     print('\n'.join(data[n - 1:]))

"""в)"""

# n = int(input())
# s = int(input())
# with open('bakery.csv', 'r', encoding='utf-8') as file:
#     data = file.read().split()
#     print('\n'.join(data[n - 1: s]))
