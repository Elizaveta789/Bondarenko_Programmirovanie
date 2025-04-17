# Из предложенного текстового файла (text18-2.txt) вывести на экран его содержимое,
# количество знаков препинания. Сформировать новый файл, в который поместить текст в
# стихотворной форме выведя строки в обратном порядке.


import string
from os import write

f1 = open('text18-2.txt','r', encoding='utf-16')
print(f1.read())
f1.close()

f1 = open('text18-2.txt', 'r', encoding='utf-16')
lines = f1.readlines()
count = 0
for line in lines:
    for letters in line:
        if letters in string.punctuation:
            count += 1
print(f'Количество знаков препинания: {count}')
f1.close()

f2 = open('reversed_f1.txt', 'w', encoding='utf-16')
for line in reversed(lines):
    f2.write(line)
f2.close()





