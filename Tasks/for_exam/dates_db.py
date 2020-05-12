import sqlite3


conn = sqlite3.connect('dates.db')
conn.execute('CREATE TABLE USERS'
             '(NAME        CHAR(50)  UNIQUE   NOT NULL,'
             ' BIRTHDATE   DATE               NOT NULL);')

# Добавляем данные
conn.execute("INSERT INTO USERS (NAME, BIRTHDATE)"
             "VALUES ('Paul', '2020-05-11')")
conn.execute("INSERT INTO USERS (NAME, BIRTHDATE)"
             "VALUES ('Peter', '2020-05-10')")
conn.commit()

username = None
while username != 'quit':
    username = input("username: ")
    bd = conn.execute("SELECT BIRTHDATE FROM USERS WHERE NAME = ?", (username, )).fetchone()
    print(bd)

conn.execute('DROP TABLE USERS')
conn.close()
