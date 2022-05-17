# -Python.-
Домашнее задание
"""
Задание 2.

Реализуйте два алгоритма.

Оба должны обеспечивать поиск минимального значения для списка.

Сложность первого алгоритма должна быть O(n^2) - квадратичная.

Сложность второго алгоритма должна быть O(n) - линейная.


"""

"""вариант 1 O(n^2)"""

def min_of_list_1(user_list):

    for i in range(len(user_list)):
        for j in range(len(user_list)):
            if user_list[i] < user_list[j]:
                min_el = user_list[i]
            else:
                min_el = user_list[i]

    return min_el

"""вариант 2 O(n)"""

def min_of_list_2(user_list):

    min_el = user_list[0]
    for i in range(len(user_list)):
        if user_list[i] < min_el:
            min_el = user_list[i]
    return min_el


