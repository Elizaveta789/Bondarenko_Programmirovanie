# Дан список размера N. Найти номера тех элементов список, которые больше своего
# левого соседа, и количество таких элементов. Найденные номера выводить в
# порядке их убывания.
import random


N = input('Введите количество элементов в списке - ')
t = 0
count = 0


while N != int:  # проверка на тип переменной
    try:
        N = int(N)
        break
    except ValueError:
        print('Неправильно ввели, ввести нужно число  ')
        N = input('Введите количество элементов в списке - ')


new_List = []
while t < N:
    new_List.append(random.randint(-100, 100))  #добавляем в список рандомные числа
    t += 1


print(f'Получившийся список: {new_List}')

mini_list = []  # здесь будут храниться подходящие под условие элементы
index_list = []  # здесь индексы подходящих элементов
for index in range(1, len(new_List)):
    if new_List[index] > new_List[index - 1]:
        count += 1
        mini_list.append(new_List[index])
        index_list.append(index)
mini_list.sort(reverse=True)  # метод для вывода списка в порядке убывания
index_list.reverse()  # метод, выводящий список в обратном порядке
print(f'Количество элементов в списке, которые больше своего левого соседа = {count}')
print(f'Список данных чисел  порядке убывания: {mini_list}')
print(f'Индексы данных элементов в обратном порядке: {index_list}')

