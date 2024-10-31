# Вывести на экран привет мир
# print('Привет, мир!')
from calendar import month
from selectors import SelectSelector

# Дано 2 числа найти сумму
# num_1 = 5
# num_2 = 7
# result = num_1 + num_2
# print(result)

#Ввести 2 числа с клавиатуры и вывести их сумму и произведение
# num_1 = int(input('Enter first number\n'))
# num_2 = int(input('Enter second number\n'))
# print(num_1 + num_2)
# print(num_1 * num_2)

#n школьников делят k яблок поровну, неделящийся остаток остается в корзинке.
# Сколько яблок достанется каждому школьнику? Сколько яблок останется в корзинке?
# Программа получает на вход числа n и k и должна вывести искомое количество яблок (два числа).
# n = int(input('Введите количество школьников\n'))
# k = int(input('Введите количество яблок\n'))
# for_each = k // n
# print('Каждому школьнику по', for_each)
# in_basket = k % n
# print('Осталось в корзине', in_basket)
# #Напишите программу, которая считывает длины двух катетов в прямоугольном треугольнике и выводит его площадь.
# Каждое число записано в отдельной строке.
# a = int(input('Введите ллину первого катета\n'))
# b = int(input('Введите длину второго катета\n'))
# s = a * b / 2
# print('Площадь прямоугольноготреугольника '
#       'равна', s)

#Проверка четности числа
# num = int(input('Enter number\n'))
# if num % 2 == 0:
#     print(f'Число {num} является четным')
# else:
#     print(f'Число {num} является нечетным')

#Сравнение трех чисел
# num_1 = int(input('Enter number 1\n'))
# num_2 = int(input('Enter number 2\n'))
# num_3 = int(input('Enter number 3\n'))
#
# if num_1 > num_2 and num_1 > num_3:
#     print('Number 1 is biggest')
# elif num_2 > num_1 and num_2 > num_3:
#     print('Number 2 is biggest')
# else:
#     print('Number 3 is biggest')

# определение времени года
# month = input("Введите номер месяца")
# if month == '1' or month == '2' or month == '12':
#     print('Зима')
# elif month == '3' or month == '4' or month == '5':
#     print('Весна')
# elif month == '6' or month == '7' or month == '8':
#     print('Лето')
# elif month == '9' or month == '10' or month == '11':
#     print('Осень')
# else:
#     print('Нет такого месяца')

#Вывести слово привет 150 раз
# for hello in range(150):
#     print('Привет')
#
# #Вывести все числа от 0 до 5
# for i in range(6):
#     print(i)

#вывести все нечетные от 1 до 15
# for i in range(1, 16, 2):
#     print(i)

#найти сумму всех чисел от 1 до n
n = int(input("Введите n\n")) + 1
result = 0
for i in range(1, n):
    result += i
print(result)


