import random


def game():  # функция игры
    x: list = ['rock', 'paper', 'scissors', 'lizard', 'spock']  # список с элементами игры, которые можно выбрать
    a: str = input('Your choice: rock paper scissors lizard spock?')  # просим пользователя ввести элемент
    if a in x:  # проверяем ести ли этот элемент в списке
        pass  # если есть, идем дальше
    while a not in x:  # пока пользователь не введет правильное значение, будем его задалбывать
        print(f'Invalid input {a}')  # принтим неправильный ввод
        a = input('Your choice: rock paper scissors lizard spock?')  # просим ввести правильное значение
        if a in x:  # и вот наконец-то введено правильное значение
            pass  # идем дальше

    b = random.choice(x)  # рандомом выбираем значение-аппонент
    # здесь блок логики, если пользователь ввел rock
    if a == 'rock':
        if b == 'rock':
            print('dead heat')
        elif b == 'paper':
            print('you lose')
        elif b == 'scissors':
            print('you win!')
        elif b == 'lizard':
            print('you win!')
        else:
            print('you lose')
    # здесь блок логики, если пользователь ввел paper
    elif a == 'paper':
        if b == 'paper':
            print('dead heat')
        elif b == 'rock':
            print('You win!')
        elif b == 'scissors':
            print('You lose')
        elif b == 'lizard':
            print('You lose')
        else:
            print('You win!')
    # здесь блок логики, если пользователь ввел scissors
    elif a == 'scissors':
        if b == 'scissors':
            print('dead heat')
        elif b == 'rock':
            print('You lose')
        elif b == 'paper':
            print('You win!')
        elif b == 'lizard':
            print('You win!')
        else:
            print('You lose')
    # здесь блок логики, если пользователь ввел lizard
    elif a == 'lizard':
        if a == 'lizard':
            print('dead heat')
        elif a == 'rock':
            print('You lose')
        elif a == 'paper':
            print('You win!')
        elif a == 'scissors':
            print('You lose')
        else:
            print('You win!')
    # здесь блок логики, если пользователь ввел spock
    else:
        if b == 'spock':
            print('dead heat')
        elif b == 'paper':
            print('you lose')
        elif b == 'scissors':
            print('you win!')
        elif b == 'lizard':
            print('you lose')
        else:
            print('you lose')
    # когда игра завершена, спрашиваем повторить игру или нет
    print('Repeat? (Y/N)')
    y = input('Your answer')
    # если нет, то игра завершается
    if y == 'N':
        print('Game over')
    # если да, идем вначало функции и играем снова
    elif y == 'Y':
        game()
    # ниже блок проверки на правильный ввод "да" или "нет", будем задалбывать пока пользователь не напишет правильный ответ
    else:
        while y != 'Y' or y != 'N':
            print(f'Invalid input {y}')
            print('Repeat? (Y/N)')
            y = input('Your answer')
            if y == 'Y':
                game()
            elif y == 'N':
                print('Game over')
                break


game()
