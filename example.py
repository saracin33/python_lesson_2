#Задачи на циклы и оператор условия------
#----------------------------------------

'''
Задача 1
Вывести на экран циклом пять строк из нулей, причем каждая строка должна быть пронумерована.
'''
# # Вариант 1
#
# i = 0
#
# while i < 5:
#     print(i,0)
#     i = i + 1
#
# # Вариант 2
#
# for i in range(5):
#     print(i,0)

'''
Задача 2
Пользователь в цикле вводит 10 цифр. Найти количество введеных пользователем цифр 5.
'''
# sum = 0
#
# for i in range(10):
#     i = int(input('Введите 10 цифр'))
#     if i == 5:
#         sum+=1
# print(sum)


'''
Задача 3
Найти сумму ряда чисел от 1 до 100. Полученный результат вывести на экран.
'''
# sum = 0
#
# for i in range(1,101):
#     sum+=i
# print(sum)

'''
Задача 4
Найти произведение ряда чисел от 1 до 10. Полученный результат вывести на экран.
'''

# mult = 1
#
# for i in range(1,11):
#     mult*=i
# print(mult)

'''
Задача 5
Вывести цифры числа на каждой строчке.
'''

# integer_number = 4791
#
# #print(integer_number%10,integer_number//10)
#
# while integer_number>0:
#     print(integer_number%10)
#     integer_number = integer_number//10

'''
Задача 6
Найти сумму цифр числа.
'''
# integer_number = 1234562151
#
# sum = 0
#
# while integer_number>0:
#     sum += integer_number%10
#     integer_number = integer_number//10
#
# print(sum)

'''
Задача 7
Найти произведение цифр числа.
'''
# integer_number = 1234567
#
# mult = 1
#
# while integer_number>0:
#     mult *= integer_number%10
#     integer_number = integer_number//10
#
# print(mult)

'''
Задача 8
Дать ответ на вопрос: есть ли среди цифр числа 5?
'''
# integer_number = 263413
# while integer_number>0:
#     if integer_number%10 == 5:
#         print('Yes')
#         break
#     integer_number = integer_number//10
# else: print('No')

'''
Задача 9
Найти максимальную цифру в числе
'''
# number = 2485765567638
# max_=0
# while number>0:
#     digit=number%10
#     if digit>max_:
#         max_ =digit
#     number=number // 10
# print('Максимальное число:',max_)

'''
Задача 10
Найти количество цифр 5 в числе
'''
# integer_number = 5635135595575
# sum = 0
# while integer_number>0:
#     if integer_number%10 == 5:
#         sum+=1
#     integer_number = integer_number//10
# print(sum)