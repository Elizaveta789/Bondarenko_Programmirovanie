# В двумерном списке найти сумму отрицательных элементов в первой трети матрицы
import random
from functools import reduce


n = int(input('Введите количество строк - '))
m = int(input("Введите количество столбцов - "))

matrix = [[random.randint(-100,100) for i in range(n)] for i in range(m)]

print('Сгенерированный список: ')
for row in matrix:
    print(row)


new_list = [number for row in matrix for number in row]
minus_number = filter(lambda x: x < 0, new_list)
print(reduce(lambda x, y: x + y, minus_number))
