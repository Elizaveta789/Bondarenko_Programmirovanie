# Дан список размера N. Обнулить элементы списка, расположенные между его
# минимальным и максимальным элементами (не включая минимальный и
# максимальный элементы).
import random


N = input('Введите количество элементов в списке - ')
t = 0


while N != int:  # проверка на тип переменной
    try:
        N = int(N)
        break
    except ValueError:
        print('Неправильно ввели, ввести нужно число  ')
        N = input('Введите количество элементов в списке - ')


my_list = []
while t < N:
    my_list.append(random.randint(-100, 100))  #добавляем в список рандомные числа
    t += 1


print(f'Получившийся список: {my_list}')


max_digit = max(my_list)
max_index = my_list.index(max_digit)

min_digit = min(my_list)
min_index = my_list.index(min_digit)

print(f'Минимальное значение в списке - {min_digit}\nМаксимальное значение в списке - {max_digit}')

if min_index > max_index:  # удаляем из списка определенный срез
    del my_list[max_index + 1 : min_index]
else:
    del my_list[min_index + 1 : max_index]


print(f'Обновленный под условие список: {my_list}')
