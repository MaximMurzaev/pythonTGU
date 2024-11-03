# Вывод четных чисел
for i in range(1, 21):
    if i % 2 == 0:
        print(f'Число {i} четное')

# Сумма всех чисел от 1 до 100
result = 0
i = 1
while i <= 100:
    result += i
    i += 1
print(result)

#Вывести делители числа
num = int(input('Enter arbitrary number\n'))
havent_divider = True
for i in range(1, num):
    if num % i == 0 and i > 1:
        print(f'Divider of number {num} is {i}')
        havent_divider = False
if havent_divider:
    print(f'The number {num} have not any dividers')


