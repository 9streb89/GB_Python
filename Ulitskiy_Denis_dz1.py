"""1. Реализовать вывод информации о промежутке времени в зависимости от его
   продолжительности duration в секундах:"""

"""a. до минуты: <s> сек"""

# sec = int(input('duration = '))
# print(sec,'сек')

"""b. до часа: <m> мин <s> сек"""

# sec = int(input('duration = '))
# min_value = sec // 60
# sec = sec % 60
# print(min_value,'мин',sec,'сек')

"""c. до суток: <h> час <m> мин <s> сек"""

# sec = int(input('duration = '))
# hour_value = sec // 3600
# min_value = (sec - hour_value * 3600) // 60
# sec = sec % 60
# print(hour_value,'час',min_value,'мин',sec,'сек')

"""*d. в остальных случаях: <d> дн <h> час <m> мин <s> сек"""

# sec = int(input('duration = '))
# day_value = sec // 86400
# hour_value = (sec - day_value * 86400) // 3600
# min_value = (sec - hour_value * 3600 - day_value * 86400) // 60
# sec = sec % 60
# print(day_value,'дн',hour_value,'час',min_value,'мин',sec,'сек')

"""2.Создать список, состоящий из кубов нечётных чисел от 1 до 1000 (куб X - третья степень числа X:"""

"""a. Вычислить сумму тех чисел из этого списка, сумма цифр которых делится нацело на 7.
    Например, число «19 ^ 3 = 6859» будем включать в сумму, так как 6 + 8 + 5 + 9 = 28 –
    делится нацело на 7. Внимание: использовать только арифметические операции!"""
#
# my_list = [i**3 for i in range(1, 1001, 2)]
# final_sum = 0
# for num in my_list:
#     summ = 0
#     temp_num = num
#     while temp_num != 0:
#         digit = temp_num % 10
#         summ = summ + digit
#         temp_num = temp_num // 10
#     if summ % 7 == 0:
#         final_sum = final_sum + num
# print(final_sum)

""" b. К каждому элементу списка добавить 17 и заново вычислить сумму тех чисел из этого
 списка, сумма цифр которых делится нацело на 7"""

# my_list = [i**3 for i in range(1, 1001, 2)]
# final_sum = 0
# for num in my_list:
#     summ = 0
#     temp_num = num + 17
#     while temp_num != 0:
#         digit = temp_num % 10
#         summ = summ + digit
#         temp_num = temp_num // 10
#     if summ % 7 == 0:
#         final_sum = final_sum + num
# print(final_sum)

""" 3 Реализовать склонение слова «процент» во фразе «N процентов». Вывести эту фразу на
 экран отдельной строкой для каждого из чисел в интервале от 1 до 100:"""

# a = ('Процент')
# b = ('Процента')
# c = ('Процентов')
#
# number = input('Введите число:')
# unique_numb = {11, 12, 13, 14}
# for i in range(100):
#     i = i +1
#     if i in unique_numb:
#         print(i, 'процентов')
#     elif i % 10 == 1:
#         print(i, 'Процент')
#     elif i % 10 > 1 and i % 10 < 5:
#         print(i, 'Процента')
#     else:
#         print(i, 'Процентов')
