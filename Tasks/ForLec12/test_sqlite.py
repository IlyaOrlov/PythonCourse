import sqlite3


# Подключаемся к базе данных
# Файл базы данных (если он еще не создан будет создан автоматически
conn = sqlite3.connect('sqlite.db')
print('База данных открыта')

# Создаем таблицу
conn.execute('CREATE TABLE COMPANY'
             '    (ID       INT   PRIMARY KEY  NOT NULL,'
             '     NAME     TEXT               NOT NULL,'
             '     AGE      INT                NOT NULL,'
             '     ADDRESS  CHAR(50),'
             '     SALARY   REAL);')
print('Таблица создана')

# Добавляем данные
conn.execute("INSERT INTO COMPANY (ID, NAME, AGE, ADDRESS, SALARY)"
             "VALUES (1, 'Paul', 32, 'California', 20000.00)")
conn.execute("INSERT INTO COMPANY (ID, NAME, AGE, ADDRESS, SALARY)"
             "VALUES (2, 'Allen', 25, 'Texas', 15000.00)")
conn.execute("INSERT INTO COMPANY (ID, NAME, AGE, ADDRESS, SALARY)"
             "VALUES (3, 'Teddy', 23, 'Norway', 20000.00)")
conn.execute("INSERT INTO COMPANY (ID, NAME, AGE, ADDRESS, SALARY)"
             "VALUES (4, 'Mark', 25, 'Richmond', 65000.00)")
conn.commit()
print('Данные добавлены')

# Читаем данные
cursor = conn.execute('SELECT id, name, address, salary from '
                      'COMPANY WHERE id = 1')
for row in cursor:
    print(row)

# Изменяем данные
conn.execute('UPDATE COMPANY set salary = 25000.00 WHERE id = 1')
conn.commit()
print('Данные изменены')
# Проверяем, что получилось
cursor = conn.execute('SELECT id, name, address, salary from '
                      'COMPANY WHERE id = 1')
print(cursor.fetchone())

# Удаляем данные
conn.execute('DELETE from COMPANY where id=2;')
conn.commit()
print('Данные удалены')
# Проверяем, что получилось
cursor = conn.execute('SELECT id, name, address, salary from COMPANY')
for row in cursor:
    print(row)

# Изменяем данные
conn.execute('UPDATE COMPANY set salary = 25000.00 WHERE id = 1')
conn.commit()
print('Данные снова изменены')
# Проверяем, что получилось
cursor = conn.execute('SELECT id, name, address, salary from '
                      'COMPANY WHERE id = 1')
print(cursor.fetchone())

# При необходимости подставить в запрос значения, полученные в коде Python
# НЕ следует использовать строковые операции (например, конкатенацию)
# с текстом запроса!
# Для подстановки параметров в запрос необходимо указать специальный символ
# '?' на местах подстановки в тексте запроса, а параметры передать в кортеже
# в соответствующем порядке в тот же метод execute().
conn.execute("INSERT INTO COMPANY (ID, NAME, AGE, ADDRESS, SALARY)"
             "VALUES (?, ?, ?, ?, ?)",
             (5, 'Allen', 32, 'Texas', 15000.00))
conn.commit()
print('Новые данные добавлены')
# Проверяем, что получилось
cursor = conn.execute('SELECT id, name, address, salary from COMPANY')
for row in cursor:
    print(row)

conn.execute('DROP TABLE COMPANY')
print('Таблица удалена')

conn.close()





