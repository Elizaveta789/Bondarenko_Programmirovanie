# Дано целое число A. Проверить истинность высказывания: «Число A является нечетным».
A = input('Введите число - ')
while type(A) != int:  # проверка на тип переменной
    try:
        A = int(A)
    except ValueError:
        print("Неправильно ввели")
        A = input("Введите число - ")
if A % 2 == 0:
    d = False
else:
    d = True
print(d)
