import sqlite3


if __name__ == "__main__":
    conn = sqlite3.connect('sqlite.db')
    conn.execute('CREATE TABLE USERS'
                 '    (NAME       CHAR(50)   NOT NULL,'
                 '     BIRTHDATE  DATE       NOT NULL);')
    conn.execute("INSERT INTO USERS (NAME, BIRTHDATE)"
                 "VALUES ('Paul', '2020-05-12')")
    conn.execute("INSERT INTO USERS (NAME, BIRTHDATE)"
                 "VALUES ('Peter', '2020-05-11')")
    conn.commit()


    username = None
    while username != 'quit':
        username = input("username: ")
        bd = conn.execute("SELECT BIRTHDATE FROM USERS WHERE NAME = ?", (username, )).fetchone()
        print(bd)


    conn.execute('DROP TABLE USERS')
    conn.close()
