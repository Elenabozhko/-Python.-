def my_function(user_number, num=1, result_sum=0):
    if user_number == 0:
        return result_sum
    else:
        user_number -= 1
        result_sum += num
        num /= -2
        return my_function(user_number, num, result_sum)


if __name__ == "__main__":
    try:
        user_num = int(input("Введите натуральное число: "))
        print(f"Сумма n элементов следующего ряда чисел:\n1-0.5 0.25 -0.125 ... n равна:"
              f" {my_function(user_num)}")
    except ValueError:
        print("Вы вместо числа ввели строку. Исправьтесь")