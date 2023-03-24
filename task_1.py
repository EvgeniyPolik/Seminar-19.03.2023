"""
Задача 22:
Даны два неупорядоченных набора целых чисел (может быть, с повторениями).
Выдать без повторений в порядке возрастания все те числа, которые встречаются
в обоих наборах.
Пользователь вводит 2 числа. n - кол-во элементов первого множества. m - кол-во
элементов второго множества. Затем пользователь вводит сами элементы
множеств.
"""


def get_int_from_user(message, err_message='Введено не число!'):
    try:
        n = int(input(message))
    except ValueError:
        print(err_message)
        return
    else:
        return n


def get_array_from_user(lenght, message, err_message='Введено не число!'):
    result_array = []
    print(message)
    try:
        for i in range(lenght):
            result_array.append(int(input(f'Введите элемент массива №{i + 1}: ')))
    except ValueError:
        print(err_message)
        return
    else:
        return result_array


n = get_int_from_user('Введите размер первого множества: ')
m = None
if n:
    m = get_int_from_user('Введите размер первого множества: ')

arr_a = None
arr_b = None
if n and m:
    arr_a = get_array_from_user(n, 'Введите элементы 1го массива: ')
    if arr_a:
        arr_b = get_array_from_user(m, 'Введите элементы 2го массива: ')

if arr_b and arr_b:
    result = set(arr_a).intersection(set(arr_b))
    for i in sorted(result):
        print(i, end=' ')
else:
    print('Попробуйте еще раз')
