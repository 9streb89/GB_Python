"""1. Написать генератор нечётных чисел от 1 до n (включительно), используя ключевое слово yield, например:"""

# def gen(num):
#     for i in range(num + 1):
#         if i % 2 == 1:
#             yield i
#
#
# old_gen = gen(9)
#
# print(next(old_gen))
# print(next(old_gen))
# print(next(old_gen))
# print(next(old_gen))
# print(next(old_gen))
# print(next(old_gen))

"""2.* (вместо 1) Решить задачу генерации нечётных чисел от 1 до n (включительно), не используя ключевое слово yield"""

# nums_gen = (num + 1 for num in range(0, 9, 2))
# old_gem = nums_gen
# print(next(old_gem))
# print(next(old_gem))
# print(next(old_gem))
# print(next(old_gem))
# print(next(old_gem))
# print(next(old_gem))

"""3. Есть два списка:
Необходимо реализовать генератор, возвращающий кортежи вида (<tutor>, <klass>)"""

# tutors = ['Иван', 'Анастасия', 'Петр', 'Сергей', 'Дмитрий', 'Борис', 'Елена']
# klasses = ['9А', '7В', '9Б', '9В', '8Б', '10А', '10Б', '9А']
#
# gen_1 = (list(x) for x in zip(tutors, klasses))
#
# print(tuple(next(gen_1)))
# print(tuple(next(gen_1)))
# print(tuple(next(gen_1)))
# print(tuple(next(gen_1)))
# print(tuple(next(gen_1)))
# print(tuple(next(gen_1)))
# print(tuple(next(gen_1)))
# print(tuple(next(gen_1)))

"""4. Представлен список чисел. Необходимо вывести те его элементы, значения которых больше предыдущего"""

# src = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
# result = []
# for i in range(1, len(src)):
#     if src[i] > src[i - 1]:
#         result.append(src[i])
# print('result = ', result)

""" 5. Представлен список чисел. Определить элементы списка, не имеющие повторений.
Сформировать из этих элементов список с сохранением порядка их следования в исходном
списке"""

# src = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
# result = []
# for num in src:
#     if num not in result:
#         result.append(num)
#     elif num in result:
#         result.remove(num)
#
# print(result)


