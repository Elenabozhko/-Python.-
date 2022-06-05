"""
Задание 1.
Реализуйте функции:
a) заполнение списка, оцените сложность в O-нотации
   заполнение словаря, оцените сложность в O-нотации
   сделайте аналитику, что заполняется быстрее и почему
   сделайте замеры времени
b) получение элемента списка, оцените сложность в O-нотации
   получение элемента словаря, оцените сложность в O-нотации
   сделайте аналитику, что заполняется быстрее и почему
   сделайте замеры времени
с) удаление элемента списка, оцените сложность в O-нотации
   удаление элемента словаря, оцените сложность в O-нотации
   сделайте аналитику, что заполняется быстрее и почему
   сделайте замеры времени
ВНИМАНИЕ: в задании три пункта
НУЖНО выполнить каждый пункт
обязательно отделяя каждый пункт друг от друга
Подсказка: для замеров воспользуйтесь модулем time (см. примеры урока 1)
вы уже знаете, что такое декоратор и как его реализовать,
обязательно реализуйте ф-цию-декоратор и пусть она считает время
И примените ее к своим функциям!
"""
import time


def time_function(func):
    start_time = time.time()
    func()
    return print(f'Выполнено за время: {time.time() - start_time}')


list1 = []
dict1 = dict()

"""a"""


@time_function
def add_list():
    """Сложность: О(1)"""
    for i in range(100000):
        list1.append(i)
    print(f'Список длиной {len(list1)} элементов заполнен')


@time_function
def add_dict():
    """Сложность: О(1)"""
    for i in range(100000):
        dict1[i] = i
    print(f'Словарь длиной {len(dict1)} элементов заполнен')


print('Словарь заполняется дольше из-за вычисления хеша в словаре')


print()
"""b"""


@time_function
def check_list():

    print('Получение 1000 элементов списка')
    for i in range(1000):
        print(list1[i], end=' ')  # Сложность O(1)
    print()


@time_function
def check_dict():

    print(f'Получение 1000 элементов словаря')
    for i in range(1000):
        print(dict1[i], end=' ')  # Сложность O(1)
    print()


print()
"""c"""


@time_function
def del_list():
    """Сложность O(1)"""
    print('Удаление 100000 элементов списка')
    for i in range(100000):
        list1.pop(0)
    print('Элементы удалены')


@time_function
def del_dict():
    """Сложность O(1)"""
    print('Удаление 100000 элементов словаря')
    for i in range(100000):
        dict1.pop(i)
    print('Элементы удалены')


print()
print('Так как большенство операций по словарю имеют константную сложность\n'
      'они быстрее чем у списков')