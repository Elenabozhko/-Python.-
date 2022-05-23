def recur_method(num, even=0, odd=0):

    if num == 0:
        return even, odd
    else:
        cur_n = num % 10
        num = num // 10
        if cur_n % 2 == 0:
            even += 1
        else:
            odd += 1
        return recur_method(num, even, odd)


if __name__ == "__main__":
    try:
        NUM = int(input("Введите натуральное число: "))
        print(f"Количество четных и нечетных цифр в числе: {recur_method(NUM)}")
    except ValueError:
        print("Вы вместо числа ввели строку. Исправьтесь")