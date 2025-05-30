# Приложение АБИТУРИЕНТ для автоматизации работы приемной комиссии,
# которая обеспечивает обработку анкетных данных абитуриентов. Таблица Анкета
# содержит следующие данные об абитуриентах: Регистрационный номер, Фамилия, Имя,
# Отчество, Дата Рождения, Награды (наличие кр. Диплома или медали (да/нет)), Адрес,
# выбранная Специальность.

import sqlite3 as sq


with sq.connect('abiturient.db') as abt:
    cur = abt.cursor()
    cur.execute('create table if not exists anketa ('
                'id_reg integer primary key, '
                'surname text not null, '
                'name text not null, '
                'dad_name text, '
                'date data, '
                'avords text check (avords in ("да", "нет")) not null, '
                'adress text not null, '
                'spec text not null)')


    abt.commit()


    cur.execute('SELECT * FROM anketa')
    rows = cur.fetchall()

    for row in rows:
        print(row)
    cur.close()

