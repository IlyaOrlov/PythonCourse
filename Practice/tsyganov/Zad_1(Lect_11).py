import json
import sqlite3


class SQLite_class:
    def __init__(self, file):
        self.file = file

    def __enter__(self): # что должен сделать менеджер контекста в начале with
        self.conn = sqlite3.connect(self.file)
        print('База данных открыта')
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.conn.close()

    def creat_table(self):
        self.conn.execute('CREATE TABLE COMPANY'
                     ' (ID INT PRIMARY KEY NOT NULL,'
                     ' NAME TEXT NOT NULL,'
                     ' AGE INT NOT NULL)')
        print('Таблица создана')

    def insert_into_table(self, id, name, age):
        self.cur = self.conn.cursor()
        self.cur.execute("INSERT INTO COMPANY (ID, NAME, AGE)"
                     "VALUES (:ID, :NAME, :AGE)", {'ID':id, 'NAME':name, 'AGE':age})
        self.conn.commit()
        print('Данные внесены')

    def select_name(self, age):
        self.cur = self.conn.cursor()
        self.cur.execute('SELECT NAME FROM COMPANY WHERE AGE > :AGE', {'AGE':age})
        with open("myfile.json", "w") as f:
            res = json.dump(self.cur.fetchall(), f)
            return res

file='sqlite.db'

with SQLite_class(file) as db:
    db.creat_table()
    db.insert_into_table(1, 'Jack', 57)
    db.insert_into_table(2, 'Amy', 57)
    db.insert_into_table(3, 'Bob', 40)
    db.select_name(50)