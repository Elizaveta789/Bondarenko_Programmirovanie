#Дана строка, содержащая латинские буквы и круглые скобки. Если скобки
#расставлены правильно (то есть каждой открывающей соответствует одна
#закрывающая), то вывести число 0. В противном случае вывести или номер позиции,
#в которой расположена первая ошибочная закрывающая скобка, или, если
#закрывающих скобок не хватает, число —1.


def open_close(s):
    open_count = 0  # считаем открывающиеся скобки

    for i, j in enumerate(s):
        if j == '(':
            open_count += 1  # увеличиваем, если встречается '('
        elif j == ')':
            if open_count == 0:  # если встретилась закрывающая без открывающей
                return f'Индекс ошибочной закрывающей скобки - {i}'  # возвращаем индекс этой скобки
            else:
                open_count -= 1  # уменьшаем, если скобки расставлены правильно

    if open_count > 0:  # Если открывающихся скобок больше
        return 'Лишняя открывающая скобка: -1'
    else:
        return 'Все верно: 0' # всё верно


text = input('Введите какой-либо текст - ')
print(open_close(text))