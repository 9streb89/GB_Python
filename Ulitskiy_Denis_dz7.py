"""1. Написать скрипт, создающий стартер (заготовку) для проекта со следующей структурой папок:"""

# import os


# dir_name = 'my_project'
# if not os.path.exists(dir_name):
#     os.mkdir(dir_name)
# folder = ['setting', 'mainapp', 'adminapp', 'authapp']
# for i in folder:
#     folder = os.path.join(dir_name, i)
#     if not os.path.exists(folder):
#         os.mkdir(folder)


# import shutil


# path = os.path.join('my_project')
# shutil.rmtree(path)
import ntpath

"""3. Создать структуру файлов и папок, как написано в задании 2 (при помощи скрипта или «руками» в проводнике). 
Написать скрипт, который собирает все шаблоны в одну папку templates, например:"""

# import os


# dir_name = 'tamplates'
# if not os.path.exists(dir_name):
#     os.mkdir(dir_name)
#
# dir_path = os.path.join(dir_name, 'mainapp')
# if not os.path.exists(dir_path):
#     os.makedirs(dir_path)
# dir_path_1 = os.path.join(dir_name, 'authapp')
# if not os.path.exists(dir_path_1):
#     os.makedirs(dir_path_1)
#
# import shutil


# file = open('base.html', 'w')
# file_1 = open('index.html', 'w')
# file.close()
# file_1.close()
# os.rename('base.html', '/Data Инженер/основы Python/projects/tamplates/authapp/base.html')
# os.rename('index.html', '/Data Инженер/основы Python/projects/tamplates/authapp/index.html')
# shutil.copyfile('/Data Инженер/основы Python/projects/tamplates/authapp/base.html',
#                 '/Data Инженер/основы Python/projects/tamplates/mainapp/base.html')
# shutil.copyfile('/Data Инженер/основы Python/projects/tamplates/authapp/index.html',
#                 '/Data Инженер/основы Python/projects/tamplates/mainapp/index.html')


# path = os.path.join('tamplates')
# shutil.rmtree(path)

"""4. Написать скрипт, который выводит статистику для заданной папки в виде словаря, 
в котором ключи — верхняя граница размера файла (пусть будет кратна 10), а значения — общее количество файлов 
(в том числе и в подпапках), размер которых не превышает этой границы, но больше предыдущей (начинаем с 0), 
например:"""

# import os
# folder = 'some_data'
# size_1 = 100
# size_2 = 1000
# size_3 = 10000
# size_4 = 100000
# list_1 = []
# list_2 = [size_1, size_2, size_3, size_4]
# files_1 = [item
#          for item in os.scandir(folder)
#          if item.stat().st_size < size_1]
# list_1.append(len(files_1))
#
# files_2 = [item
#          for item in os.scandir(folder)
#          if item.stat().st_size < size_2]
# list_1.append(len(files_2))
#
# files_3 = [item
#          for item in os.scandir(folder)
#          if item.stat().st_size < size_3]
# list_1.append(len(files_3))
#
# files_4 = [item
#          for item in os.scandir(folder)
#          if item.stat().st_size < size_4]
# list_1.append(len(files_4))
#
# new_dict = dict(zip(list_2, list_1))
# print(new_dict)
