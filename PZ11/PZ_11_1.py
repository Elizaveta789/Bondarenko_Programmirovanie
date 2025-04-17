# Средствами языка Python сформировать текстовый файл (.txt), содержащий
# последовательность из целых положительных и отрицательных чисел. Сформировать
# новый текстовый файл (.txt) следующего вида, предварительно выполнив требуемую
# обработку элементов:
# Исходные данные:
# Количество элементов:
# Максимальный элемент:
# Произведение элементов меньших 0 в первой половине:

numbers = ['-4 22 7 -62 34 8 10 56 77']
f1 = open('text.txt', 'w', encoding='utf-8')
f1.writelines(numbers)
f1.close()

f2 = open('text_2.txt', 'w', encoding='utf-8')
f2.write('Исходные данные: ')
f2.writelines(numbers)
f2.close()

f1 = open('text.txt')
k = f1.read()
k = k.split()
my_max, t = 0, 1
for i in range(len(k)):
    k[i] = int(k[i])
    my_max = my_max if my_max > k[i] else k[i]
for i in range(len(k) // 2):
    k[i] = int(k[i])
    if k[i] < 0:
        t *= k[i]
f1.close()

f2 = open('text_2.txt', 'a', encoding='utf-8')
print('\n', 'Количество элементов: ', len(k), '\n', 'Максимальный элемент: ', my_max, '\n', 'Произведение элементов меньших 0 в первой половине: ', t, file=f2)
f2.close()





