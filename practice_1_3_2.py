#определить четность числа
# def user_input():
#     num = int(input('enter number\n'))
#     return num
#
# def is_even(num):
#     if num % 2 == 0:
#         return 'Число четное'
#     else:
#         return 'Число нечетное'
#
# def display_result(num, is_even_result):
#     if is_even_result ==  'Число четное':
#         print(f'Число {num} четное')
#     else:
#         print(f'Число {num} нечетное')
#
# def main():
#     num = user_input()
#     is_even_result = is_even(num)
#     display_result(num, is_even_result)
#
# main()
from pydoc import render_doc
#функция определения корня используя math
# from math import sqrt as st
#
# def sqrt_number(num):
#     return  st(num)
#
# print(sqrt_number(25))

#функция броска кубика
# import random as rd
# def roll_dice(a):
#     return rd.randint(1, a)
#
# print(roll_dice(6))

#функция броска монеты
# from random import randint as rd
#
# def flip_coin(n):
#     heads_count = 0
#     for flip in range(n):
#         flip_result = rd(0, 1)
#         if flip_result == 1:
#             heads_count += 1
#     return heads_count
#
# print(flip_coin(10))

# калькулятор
import my_module_2 as mm
def calculator():
    a = int(input('Введите первое число\n'))
    b = int(input('Введите второе число\n'))

    operation = input('Введите операцию (+ - * /)')

    if operation == '+':
        return f'{a} + {b} = {mm.add(a, b)}'
    elif operation == '-':
        return f'{a} - {b} = {mm.sub(a, b)}'
    elif operation == '*':
        return f'{a} * {b} = {mm.multiply(a, b)}'
    elif operation == '/':
        return f'{a} / {b} = {mm.devide(a, b)}'

print(calculator())
