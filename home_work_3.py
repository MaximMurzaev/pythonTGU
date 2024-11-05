from os import listdir
#Создаем текстовый файл и записываем в него строки
def write_strings():
    with open('home_wok_3.txt', 'w', encoding='utf-8') as file:
        file.writelines('строка 1 для домашней работы\n')
        file.writelines('строка 2 для домашней работы\n')
    return  file.name

#Читаем содержимое текстового файла
def read_file(file_name):
    with open(file_name, 'r', encoding='utf-8') as file:
        print(file.read())

#Выводим список файлов текущей дирректории
def list_dir():
    for i in listdir():
        print(i)

#копируем содержимое одного файла в другой
def copy_text(source, dest):
    with open(source, 'r', encoding='utf-8') as source_file:
        source_data = source_file.readlines()
        with open(dest , 'a', encoding='utf-8') as dest_file:
            # for i in source_data:
                dest_file.writelines(source_data)


#file_name = write_strings()
#read_file(file_name)
#list_dir()
copy_text('home_wok_3.txt', 'numbers.txt')
