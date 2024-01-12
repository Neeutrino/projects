import random


def start_game(counter_num):
    print('Добро пожаловать в числовую угадайку')
    print('До какого числа гадаем?')

    num_right = None
    num_random = None
    flag_right = False
    while not flag_right:
        num_right = input()
        if is_valid_right(num_right):
            num_random = random.randint(1, int(num_right))
            flag_right = True
        else:
            print('Это не число, попробуйте еще раз!')

    print(f'Введите число от 1 до {num_right}')

    flag = False
    while not flag:
        num = input()
        if is_valid(num, num_right):
            num = int(num)
            flag = random_num(num, num_random)
            counter_num += 1
        else:
            print(
                f'А может быть все-таки введем целое число от 1 до {num_right}?')
    return counter_num


def is_valid_right(num):
    if num.isdigit():
        return True
    return False


def is_valid(num, num_right):
    if num.isdigit() and 1 <= int(num) <= int(num_right):
        return True
    return False


def random_num(num, num_random):
    if num < num_random:
        print('Ваше число меньше загаданного, попробуйте еще разок')
        return False
    elif num > num_random:
        print('Ваше число больше загаданного, попробуйте еще разок')
        return False
    else:
        print('Вы угадали, поздравляем!')
        return True


repeat = 'y'
while repeat == 'y':
    counter = 0
    counter = start_game(counter)
    print(f'Ваше число попыток: {counter}')
    print('Хотите повторить игру?', 'y = да, n = нет', sep='\n')
    repeat = input()
    if repeat == 'n':
        print('Спасибо, что играли в числовую угадайку. Еще увидимся...')
