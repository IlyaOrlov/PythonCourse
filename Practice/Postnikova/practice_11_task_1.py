import sqlite3
import json


def create_new_bd():
    conn = sqlite3.connect('new.db')

    conn.execute('CREATE TABLE IF NOT EXISTS USERS'
                 '(USERID INT PRIMARY KEY NOT NULL,'
                 'USERNAME TEXT NOT NULL,'
                 'EMAIL TEXT NOT NULL);')
    print('The table is created')

    conn.execute("INSERT INTO USERS (USERID, USERNAME, EMAIL)"
                 "VALUES (1, 'Nickodim', 'nickodim@n.ru')")
    conn.execute("INSERT INTO USERS (USERID, USERNAME, EMAIL)"
                 "VALUES (2, 'Marpha', 'marpha@m.ru')")
    conn.execute("INSERT INTO USERS (USERID, USERNAME, EMAIL)"
                 "VALUES (3, 'Svyatoslav', 'svyatoslav@s.ru')")
    conn.execute("INSERT INTO USERS (USERID, USERNAME, EMAIL)"
                 "VALUES (4, 'Fekla', 'fekla@f.ru')")
    conn.commit()
    conn.close()


class SQLLiteDBWrapper:
    def __init__(self, db_name):
        self.db_name = db_name
        self.conn = None

    def execute(self, command):
        self.conn.execute(command)
        self.conn.commit()
        print("Data are changed")

    def select(self, command):
        cursor = self.conn.execute(command)
        row_tadle_columns = command.lower().split('select ')[1].split(' from ')[0].split(',')
        table_columns = []
        for column in row_tadle_columns:
            table_columns.append(column.strip())
        result_list = []
        for row in cursor.fetchall():
            map_for_json = {}
            for i in range(len(table_columns)):
                map_for_json[table_columns[i]] = row[i]
            result_list.append(map_for_json)
        print(result_list)
        return json.dumps(result_list)

    def __enter__(self):
        self.conn = sqlite3.connect(self.db_name)
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.conn.close()


#create_new_bd()

with SQLLiteDBWrapper('new.db') as sq:
    sq.execute("INSERT INTO USERS (USERID, USERNAME, EMAIL)"
               "VALUES (16, 'Evdokiya', 'evdokiyam@ev.ru');")
    sq.execute("UPDATE USERS set EMAIL = 'vasya@v.com' WHERE USERID = 11")
    sq.select("SELECT USERID, USERNAME, EMAIL from USERS")
