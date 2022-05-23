def reversed_number(user_number, reverse_num=''):
    if user_number == 0:
        return reverse_num
    else:
        reverse_num += str(user_number % 10)
        user_number = user_number // 10
        return reversed_number(user_number, reverse_num)


if __name__ == "__main__":
    try:
        user_num = int(input("Введите натуральное число: "))
        print(f"Обратное по порядку: {reversed_number(user_num)}")
    except ValueError:
        print("Вы вместо числа ввели строку. Исправьтесь")