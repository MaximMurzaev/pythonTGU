#Заметки
#Создать заметку
#Просматривать заметку
#Удалять заметки

def create_note():
    note_text = input("Введите текст заметки: ")
    with open("notes.txt", "a", encoding="utf-8") as file:
        file.write(note_text + "\n" )
    print("Заметка сохранена")

def view_notes():
    try:
        with open("notes.txt", 'r', encoding='utf-8') as file:
            notes = file.readlines()
            if not notes:
                print('Нет заметок')
            else:
                print('Список заметок')
                for idx in range(1, len(notes) + 1):
                    note = notes[idx - 1].strip()
                    print(f'{idx}.{note}')
    except FileNotFoundError:
        print('Файл с заметками не найден. Создайте новую заметку')

def delete_note():
    try:
        with open("notes.txt", 'r', encoding='utf-8') as file:
            notes = file.readlines()
            if not notes:
                print('Нет заметок')
                return
            print('Список заметок для удаления')
            for idx in range(1, len(notes) + 1):
                note = notes[idx - 1].strip()
                print(f'{idx}.{note}')
            note_num = int(input('Введите номер заметки для удаления: '))
            if  len(notes) >= note_num >= 1:
                del notes[note_num - 1]
                with open("notes.txt", 'w', encoding='utf-8') as file:
                    file.writelines(notes)
                print('Заметка удалена')
            else:
                print('Заметки с таким номером нет')
    except:
        print('Ошибка')

def main_menu():
    while True:
        print('\n===Меню===')
        print('1. Создать заметку')
        print('2. Вывести заметки')
        print('3. Удалить заметку')
        print('0. Выход')

        choice = input('Выберите функцию от 0 до 3: ')

        if choice == '1':
            create_note()
        elif choice == '2':
            view_notes()
        elif choice == '3':
            delete_note()
        elif choice == '0':
            break
        else:
            print('Некорректный ввод. Введите опцию от 0 до 2!: ')

main_menu()



