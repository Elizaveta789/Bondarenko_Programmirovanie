# Дана строк "Петров Иван ПОКС-29 5 4 3 2 5 4 4 5 4".
# Преобразовать информацию из строки в словарь, найти среднее арифметическое оценок,
# результаты вывести на экран
student = {}
inf = "Петров Иван ПОКС-29 5 4 3 2 5 4 4 5 4"
inf = inf.split()
student['Фамилия'] = inf[0]
student['Имя'] = inf[1]
student['Отчество'] = inf[2]
student['Группа'] = inf[3]
student['Оценки'] = []


summa = 0
count = 0
for i in inf[4:]:
    student['Оценки'].append(int(i))
    summa += int(i)
    count += 1


sr_arif = summa // count


print(f'{student}\n Среднее арифметическое оценок : {sr_arif} ')