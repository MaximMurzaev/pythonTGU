# Создайте файл с именем "example.txt" и запишите в него строку "Привет, мир!
# with open("example.txt", 'w', encoding="utf-8") as file:
#     file.write("Hello, world!")

# Прочитайте содержимое файла "example.txt" и выведите его на экран.
# with open("example.txt", 'r', encoding="utf-8") as file:
#     content = file.read()
#     print(content)

# Создайте файл "numbers.txt" и запишите в него числа от 1 до 10, каждое число на новой строке.
with open("numbers.txt", 'w') as file:
    for i in range(1, 11):
        file.write(str(i) + '\n')

# Подсчет количества строк в файле
# def count_lines(filename):
#     with open(filename, 'r') as file:
#         return len(file.readlines())
# lines_count = count_lines("numbers.txt")
# print(lines_count)

# Подсчитать количество символов в файле
with open("numbers.txt", 'r') as file:
    content = file.read()
    count_symbols = 0
    for i in range(len(content)):
        if content[i] != '\n':
            count_symbols += 1
    print(len(content))
    print(count_symbols)