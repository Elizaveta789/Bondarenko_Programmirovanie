# Приложение АБИТУРИЕНТ для автоматизации работы приемной комиссии,
# которая обеспечивает обработку анкетных данных абитуриентов. Таблица Анкета
# содержит следующие данные об абитуриентах: Регистрационный номер, Фамилия, Имя,
# Отчество, Дата Рождения, Награды (наличие кр. Диплома или медали (да/нет)), Адрес,
# выбранная Специальность.

import sqlite3 as sq
from os.path import curdir

data = [(1, 'Иванов', 'Иван', 'Иванович', '2007-07-07', 'да', 'Пушкинская 67', 'Программирование'),
        (2, 'Петров', 'Алексей', 'Сергеевич', '2006-05-12', 'да', 'Ленина 15', 'Математика'),
        (3, 'Сидорова', 'Мария', 'Игоревна', '2005-11-23', 'нет', 'Гагарина 21', 'Программирование'),
        (4, 'Кузнецов', 'Дмитрий', 'Алексеевич', '2007-03-08', 'да', 'Тверская 9', 'Банковское дело'),
        (5, 'Смирнова', 'Елена', 'Владимировна', '2008-01-14', 'нет', 'Советская 33', 'Физика'),
        (6, 'Воробьев', 'Олег', 'Павлович', '2006-09-30', 'да', 'Пушкина 45', 'Химия'),
        (7, 'Федорова', 'Анна', 'Николаевна', '2007-07-07', 'да', 'Чехова 12', 'Программирование'),
        (8, 'Морозов', 'Илья', 'Евгеньевич', '2005-04-18', 'нет', 'Карла Маркса 5', 'Банковское дело'),
        (9, 'Зайцева', 'Оксана', 'Юрьевна', '2006-12-01', 'да', 'Кирова 66', 'Информатика'),
        (10, 'Семенов', 'Артем', 'Борисович', '2008-06-25', 'нет', 'Невский 101', 'Экономика'),
        (11, 'Мельникова', 'Татьяна', 'Романовна', '2007-10-19', 'да', 'Жукова 87', 'Банковское дело')]


with sq.connect('abiturient.db') as abt:
    cur = abt.cursor()
    cur.execute('drop table if exists anketa')
    cur.execute('create table if not exists anketa ('
                'id_reg integer primary key, '
                'surname text not null, '
                'name text not null, '
                'dad_name text, '
                'date data, '
                'diplom text check (diplom in ("да", "нет")) not null, '
                'adress text not null, '
                'spec text not null)')

    cur.executemany("INSERT INTO anketa VALUES(?, ?, ?, ?, ?, ?, ?, ?)", data)
    print('Изначальные данные')
    for row in cur.fetchall():
        print(row)

    print('\nСтуденты идущие на Программирование')
    cur.execute('select * from anketa where spec = "Программирование"')
    for row in cur.fetchall():
        print(row)


    print('\nСтуденты с красным аттестатом: ')
    cur.execute('select * from anketa where diplom = "да"')
    for row in cur.fetchall():
        print(row)

    print('\nСтуденты с красным аттестатом: ')
    cur.execute('select * from anketa where spec = "Банковское дело"')
    for row in cur.fetchall():
        print(row)


    cur.execute('update anketa set spec = "Строители" where spec = "Физика"')
    print('\nИзменение Физика на Строители: ')


    cur.execute('update anketa set spec = "Бух. учет" where spec = "Экономика"')
    print('\nИзменение Экономики на Бух. учет: ')


    cur.execute('update anketa set spec = "Программирование" where spec = "Информатика"')
    print('\nИзменение Информатики на Программирование: ')


    cur.execute('delete from anketa where surname = "Петров"')
    print('\nУдаление студента с фамилией Петров')

    cur.execute('delete from anketa where name = "Олег"')
    print('\nУдаление студента с именем Олег')

    cur.execute('delete from anketa where adress = "Жукова 87"')
    print('\nУдаление студента, который живет по адресу Жукова 87')

    print('\nТаблица после всех действий')
    for row in cur.execute('select * from anketa '):
        print(row)







    




    cur.close()

