import random as rd

#Функция выбора игрока
def get_user_choice():
    while True:
        user_choice = input('Введите камень, ножницы или бумагу\n').lower()
        if user_choice == 'камень' or user_choice == 'ножницы' or user_choice == 'бумага':
            return  user_choice
        else:
            print('Вы ввели неверное значение!')

#Функция  выбора компьюетера
def get_computer_choice():
    variants = ['камень', 'ножницы', 'бумага']
    return rd.choice(variants)

#функция проверки победителя
def winner_check(user_choice, computer_choice):
    if user_choice == computer_choice:
        print(f'Выбор игрока: {user_choice}')
        print(f'Выбор компьютера: {computer_choice}')
        print('ничья')
        return 'draw'
    elif user_choice == 'камень' and computer_choice == 'ножницы':
        print(f'Выбор игрока: {user_choice}')
        print(f'Выбор компьютера: {computer_choice}')
        print('Вы победили')
        return 'user'
    elif user_choice == 'камень' and computer_choice == 'бумага':
        print(f'Выбор игрока: {user_choice}')
        print(f'Выбор компьютера: {computer_choice}')
        print('Победил компьютер')
        return 'comp'
    elif user_choice == 'ножницы' and computer_choice == 'бумага':
        print(f'Выбор игрока: {user_choice}')
        print(f'Выбор компьютера: {computer_choice}')
        print('Вы победили')
        return 'user'
    elif user_choice == 'ножницы' and computer_choice == 'камень':
        print(f'Выбор игрока: {user_choice}')
        print(f'Выбор компьютера: {computer_choice}')
        print('Победил компьютер')
        return 'comp'
    elif user_choice == 'бумага' and computer_choice == 'камень':
        print(f'Выбор игрока: {user_choice}')
        print(f'Выбор компьютера: {computer_choice}')
        print('Вы победили')
        return 'user'
    elif user_choice == 'бумага' and computer_choice == 'ножницы':
        print(f'Выбор игрока: {user_choice}')
        print(f'Выбор компьютера: {computer_choice}')
        print('Победил компьютер')
        return 'comp'

# начисление баллов
def game_score(winner):
    comp_score = 0
    user_score = 0
    if winner == 'comp':
        comp_score += 1
    elif winner == 'user':
        user_score += 1
    return  comp_score, user_score

#Общий счет игры
def game_winner(user_score, comp_score):
    if user_score > comp_score:
        print(f'Вы победили. Ваш счет: {user_score}. Счет компьютера: {comp_score}')
    elif user_score < comp_score:
        print((f'Вы проиграли. Ваш счет: {user_score}. Счет компьютера: {comp_score}'))
    else:
        print(f'Ничья. Ваш счет: {user_score}. Счет компьютера: {comp_score}')

#главная функция
def main():
    comp_score = 0
    user_score = 0
    print('Добро пожаловать в игру камень, ножницы бумага!')
    rounds = int(input('введите количество раундов '))
    for round in range(rounds):
        print(f'Раунд = {round + 1}')
        user_choice = get_user_choice()
        comp_choice = get_computer_choice()
        result = winner_check(user_choice, comp_choice)
        if result == 'comp':
            comp_score += 1
            print(f'Счет компьютера: {user_score}.')
        elif result == 'user':
            user_score += 1
            print(f'Ваш счет: {user_score}.')
    game_winner(user_score, comp_score)

main()




