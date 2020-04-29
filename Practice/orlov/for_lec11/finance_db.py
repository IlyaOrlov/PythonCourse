import sqlite3


# Подключаемся к базе данных
# Файл базы данных (если он еще не создан будет создан автоматически
conn = sqlite3.connect(':memory:')
cur = conn.cursor()
print('База данных открыта')

# Создаем таблицу
cur.execute('CREATE TABLE USERS'
            '    (ID        INTEGER   PRIMARY KEY  AUTOINCREMENT,'
            '     LOGIN     CHAR(50)               NOT NULL,'
            '     PASSWORD  CHAR(50)               NOT NULL,'
            '     SALARY    REAL);')
print('Таблица создана')

# Добавляем данные
cur.execute("INSERT INTO USERS (LOGIN, PASSWORD, SALARY)"
            "VALUES ('Ivan', 'coolpwd', 100000)")
cur.execute("INSERT INTO USERS (LOGIN, PASSWORD, SALARY)"
            "VALUES ('Petr', 'iampetr', 50000)")
cur.execute("INSERT INTO USERS (LOGIN, PASSWORD, SALARY)"
            "VALUES ('Simon', '123', 30000)")
conn.commit()
print('Данные добавлены')

# Читаем данные
cur.execute('SELECT id, login, password from USERS')
for row in cur.fetchall():
    print(row)

login = input('Input login: ')
password = input('Input password: ')

req = "SELECT login, salary from USERS WHERE login='{}' AND password='{}'".format(login, password)
print('This is request: {}'.format(req))
cur.execute(req)
print('Output data:')
rows = cur.fetchall()
if not len(rows):
    print('incorrect login/password')
else:
    for row in rows:
        print(row)

#cursor = conn.execute("SELECT login, salary from USERS WHERE login=? AND password=?", (login, password))
#print('Output data 2:')
#if cursor.rowcount == -1:
#    print('incorrect login/password')
#else:
#for row in cursor:
#    print(row)

#conn.execute('DROP TABLE USERS')
#print('Таблица удалена')

conn.close()





