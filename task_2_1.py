def input_num(my_string):
    try:
        num = int(input(my_string))
    except ValueError:
        print('Вы ввели не натуральное число')
        num = input_num(my_string)
    return num


def calculate():
    """Вводим знак операции над числами"""
    try:
        sign = input('Введите знак операции: ')
        sign = sign.replace(' ', '')
        if sign == '0':
            print('Работа завершена')
            raise ValueError()
        elif sign not in '+-*/':
            print('Такой операции не существует, или вы указали не знак операции')
            calculate()
    except ValueError:
        pass
    else:

        a = input_num('Введите первое число: ')
        b = input_num('Введите второе число: ')

        if sign == '+':
            print(f'{a}+{b}={a + b}')
            calculate()
        elif sign == '-':
            print(f'{a}-{b}={a - b}')
            calculate()
        elif sign == '*':
            print(f'{a}*{b}={a * b}')
            calculate()
        else:
            try:
                print(f'{a}/{b}={a / b}')
                calculate()
            except ZeroDivisionError:
                print('На ноль делить нельзя')
                calculate()


if __name__ == "__main__":
    calculate()