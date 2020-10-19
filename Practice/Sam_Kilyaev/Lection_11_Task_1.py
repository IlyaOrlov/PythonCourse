import sqlite3
import os
import json


def make_data_base(name_data_base):
    conn = sqlite3.connect(name_data_base)
    print('Data base created')
    conn.execute('CREATE TABLE PLAYERS'
                 ' (ID INT PRIMARY KEY NOT NULL,'
                 '  NAME TEXT NOT NULL,'
                 '  AGE INT NOT NULL,'
                 '  COUNTRY TEXT NOT NULL,'
                 '  PLATFORM TEXT NOT NULL);')
    print('Table created')
    conn.execute('INSERT INTO PLAYERS (ID, NAME, AGE, COUNTRY, PLATFORM)'
                 'VALUES (1, "Jon", 25, "Great Britain", "PS4");')
    conn.execute('INSERT INTO PLAYERS (ID, NAME, AGE, COUNTRY, PLATFORM)'
                 'VALUES (2, "Brus", 36, "Norway", "XBOX ONE");')
    conn.execute('INSERT INTO PLAYERS (ID, NAME, AGE, COUNTRY, PLATFORM)'
                 'VALUES (3, "Mary", 28, "USA", "PC");')
    conn.execute('INSERT INTO PLAYERS (ID, NAME, AGE, COUNTRY, PLATFORM)'
                 'VALUES (4, "Helen", 23, "France", "PS4");')
    conn.execute('INSERT INTO PLAYERS (ID, NAME, AGE, COUNTRY, PLATFORM)'
                 'VALUES (5, "Sergey", 31, "Russia", "PC");')
    conn.execute('INSERT INTO PLAYERS (ID, NAME, AGE, COUNTRY, PLATFORM)'
                 'VALUES (6, "Shan Chao", 19, "China", "PS4");')
    conn.commit()
    conn.close()
    return os.path.isfile(name_data_base)


def delete_db(name_data_base):
    os.remove(name_data_base)


class SQLiteClass:
    def __init__(self, name_data_base):
        self.name_db = name_data_base
        self.conn = None

    def __enter__(self):
        self.conn = sqlite3.connect(self.name_db)
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.conn.close()

    def execute_ins_upd_del(self, order):
        self.conn.execute(order)
        self.conn.commit()

    def execute_select(self, order):
        arr_json = []
        cursor = self.conn.execute(order)
        name_row = [description[0] for description in cursor.description]
        result = cursor.fetchall()
        for row in result:
            buf = dict()
            for i in range(len(name_row)):
                buf[name_row[i]] = row[i]
            arr_json.append(buf)
        self.conn.commit()
        return json.dumps(arr_json, sort_keys=True, indent=4)


if __name__ == '__main__':
    if make_data_base('players.db'):
        with SQLiteClass('players.db') as wrap:
            print(wrap.execute_ins_upd_del('INSERT INTO PLAYERS (ID, NAME, AGE, COUNTRY, PLATFORM)'
                                           ' VALUES (7, "Bill", 40, "Iceland", "XBOX ONE");'))
            print(wrap.execute_ins_upd_del('UPDATE PLAYERS SET AGE = 26 WHERE id = 1;'))
            print(wrap.execute_ins_upd_del('DELETE FROM PLAYERS WHERE PLATFORM = "XBOX ONE" AND NAME = "Brus";'))
            print(wrap.execute_select('SELECT * FROM PLAYERS WHERE AGE > 30'))
            print(wrap.execute_select('SELECT * FROM PLAYERS WHERE PLATFORM = "PS4" AND AGE > 20 ORDER BY PLATFORM'))
    delete_db('players.db')
