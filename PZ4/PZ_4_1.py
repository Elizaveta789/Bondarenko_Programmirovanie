# Даны два целых числа A и B (A < B). Вывести в порядке убывания все целые числа,
# расположенные между A и B (не включая числа A и B), а также количество N этих чисел
A, B = input('Введите первое число - '), input('Введите второе число(больше чем предыдущее) - ')

while type(A) != int or type(B) != int: # проверка на тип переменной
    try:
        A = int(A)
        B = int(B)
    except ValueError:
        print('Неправильно ввели')
        A = input('Введите число - ')
        B = input('Введите число(больше чем предыдущее) - ')

N = 0 # создаем переменную для счета количества чисел

while A < B - 1: # используем B - 1 чтобы число B не включалось
    B -= 1 #чтобы число выводилось в порядке убывания
    print(B)
    N += 1
print(f'Количество чисел: {N}')

