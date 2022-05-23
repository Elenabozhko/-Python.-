from random import randint


def game(num_x, attempts=10):
    if attempts == 0:
        return print(f'Попытки закончились, загаданное число: {num_x}')
    else:
        try:
            num_user = int(input('Введите натуральное число: '))
        except ValueError:
            return print('Было введено неправильное число, игра окончена!')
        attempts -= 1
        if num_user == num_x:
            return print(f'Действительно, загаданное число: {num_x}')
        elif num_x > num_user:
            return print('Загаданное число больше!'), game(num_x, attempts)
        else:
            return print('Загаданное число меньше!'), game(num_x, attempts)


if __name__ == "__main__":
    game(randint(1, 100))