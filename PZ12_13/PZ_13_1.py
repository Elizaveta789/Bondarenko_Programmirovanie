# В двумерном списке найти минимальный и максимальный элементы
import random

n = int(input('Введите количество строк - '))
m = int(input("Введите количество столбцов - "))

matrix = [[random.randint(-100,100) for i in range(n)] for i in range(m)]

print('Сгенерированный список: ')
for row in matrix:
    print(row)


new_list = [number for row in matrix for number in row]
print(f"Минимальный элемент: {min(new_list)}\nМаксимально значение: {max(new_list)}")


