# Туристические агентства предлагают следующие туры. Вояж – Мексика,Канада,Израиль,
# Италия. РейнаТур – Англия, Япония, Канада, ЮАР. Определить:
# 1. какие туры из Вояж, отсутствуют в РейнаТур.
# 2. какие товары из РейнаТур, отсутствуют в Вояж
# 3. перечень одинаковых туров.
# 4. равны ли перечни туров
Voyag = {'Италия', 'Мексика' , 'Канада', 'Израиль'}
ReynaTur = {'Англия', 'Япония', 'Канада', 'ЮАР'}
print(f'Туры, которые есть в Вояже, но отсутствуют в РейнаТур: {Voyag - ReynaTur}\nТуры, которые есть в РейнаТур, но отсутствуют в Вояже: {ReynaTur - Voyag}')
print(f'Перечень одинаковых туров: {Voyag&ReynaTur}')
print('Перечни туров равны' if Voyag == ReynaTur else 'Перечни туров не равны')