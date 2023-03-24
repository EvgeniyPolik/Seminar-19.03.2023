"""
Задача 24
В фермерском хозяйстве в Карелии выращивают чернику. Она растет на круглой
грядке, причем кусты высажены только по окружности. Таким образом, у каждого
куста есть ровно два соседних. Всего на грядке растет N кустов.
Семинар 4 2
Эти кусты обладают разной урожайностью, поэтому ко времени сбора на них
выросло различное число ягод – на i-ом кусте выросло ai ягод.
В этом фермерском хозяйстве внедрена система автоматического сбора черники.
Эта система состоит из управляющего модуля и нескольких собирающих модулей.
Собирающий модуль за один заход, находясь непосредственно перед некоторым
кустом, собирает ягоды с этого куста и с двух соседних с ним.
Напишите программу для нахождения максимального числа ягод, которое может
собрать за один заход собирающий модуль, находясь перед некоторым кустом
заданной во входном файле грядки.
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
            result_array.append(int(input(f'Введите количество ягод на кусте №{i + 1}: ')))
    except ValueError:
        print(err_message)
        return
    else:
        return result_array


n = get_int_from_user('Введите количество кустов: ')
gaden = None
if n:
    gaden = get_array_from_user(n, 'Введите количество ягод на кустах: ')
if gaden:
    max_count = gaden[-1] + gaden[0] + gaden[1]
    for i in range(1, n - 1):
        if gaden[-1 + i] + gaden[i] + gaden[1 + i] > max_count:
            max_count = gaden[-1 + i] + gaden[i] + gaden[1 + i]
    if gaden[-2] + gaden[-1] + gaden[0] > max_count:
        max_count = gaden[-2] + gaden[-1] + gaden[0]
    print(f'Максимальное количество ягод за заход: {max_count}')
else:
    print('Попробуйте еще раз')