import json
from xml.dom.minidom import ProcessingInstruction


def cities():
    city = open("russia.json", 'r', encoding='utf-8')
    cities_data = json.loads(city.read())
    print('Играем в города. Пиши в одном сообщении один город России. Пиши "Стоп" чтобы прекратить игру! Первый Москва, тебе на "А"')
    letter = 'а'
    while True:
        user_input = input('Введите город ').lower()
        if user_input == 'стоп':
            print('Отлично сыграли! Пока')
            break
        elif user_input[0] != letter:
            print('А-а-а-а. Первая буква не соответствует последней букве загаданного города')
        else:
            for i in range(0, len(cities_data)-1):
                if cities_data[i]['city'].lower() == user_input:
                    del cities_data[i]
                    break
            else:
                print('Кажется такого города в Росии нет, либо его уже называли')
                continue
            if user_input[-1] in 'ьъы':
                print('Левая буква')
                letter = user_input[-2]
            else:
                letter = user_input[-1]
            for i in range(0, len(cities_data)-1):
                if cities_data[i]['city'].lower()[0] == letter:
                    print(cities_data[i]['city'])
                    if cities_data[i]['city'].lower()[-1] in 'ьъы':
                        letter = cities_data[i]['city'].lower()[-2]
                    else:
                        letter = cities_data[i]['city'].lower()[-1]
                    del cities_data[i]
                    break
            else:
                print('Ты выиграл')
                return

cities()