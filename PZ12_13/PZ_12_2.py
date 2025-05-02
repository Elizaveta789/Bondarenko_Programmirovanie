# Составить список, в который будут включены только согласные буквы и
# привести их к верхнему регистру. Список: ['Оттава', 'Москва', 'Пекин', 'Полоцк', 'Версаль',
# 'Дели', 'Каир'].


cities = ['Оттава', 'Москва', 'Пекин', 'Полоцк', 'Версаль', 'Дели', 'Каир']

def letters(city):
    yield list(filter(lambda char: char.upper() not in 'АЕЁИОУЫЭЮЯ' and char.isalpha(), city.upper()))


new_listik = [char for city in cities for char in letters(city)]

print('Список букв:', new_listik)