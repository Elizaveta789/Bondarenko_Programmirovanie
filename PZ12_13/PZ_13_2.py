# В двумерном списке найти сумму отрицательных элементов в первой трети матрицы
import random
from functools import reduce
from traceback import print_tb

n = int(input('Введите количество строк - '))
m = int(input("Введите количество столбцов - "))

matrix = [[random.randint(-100,100) for i in range(n)] for i in range(m)]
print('Сгенерированный список: ')
for row in matrix:
    print(row)


n_row = len(matrix)
first_third_rows = n_row // 3
first_third_matrix = matrix[:first_third_rows]
print('Первая треть матрицы: ')
print(first_third_matrix)

new_list = [number for row in first_third_matrix for number in row]
minus_number = filter(lambda x: x < 0, new_list)
print(f'Сумма отрицательных элементов: {reduce(lambda x, y: x + y, minus_number)}')
