# Составить функцию, которая напечатает сорок любых символов
import random  # добавляем библиотеку для отбора рандомных символов


def simbols_random():
    result = ''  # добавляем перемнную, где будут храниться выбранные символы
    randomizer = 'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯабвгдеёжзийклмнопрстуфхцчшщъыьэюя123456789!№;%:?*()-_=+{}[];:./|><,`~@'
    for i in range(40):
        random_char = random.choice(randomizer)  # метод отбора одного символа
        result += random_char
    return result


print(f'Сорок любых символов: {simbols_random()}')