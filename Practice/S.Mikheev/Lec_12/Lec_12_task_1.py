import sqlite3
import json


class Wrapper:
    def __init__(self, dbasename):
        self.dbasename = dbasename

    def __enter__(self):
        self.conn = sqlite3.connect(self.dbasename)
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        self.conn.commit()
        self.conn.close()

    def create(self, table, columns):
        query = "CREATE TABLE {0} ({1})".format(table, columns)
        self.conn.execute(query)

    def select(self, columns, table, condition=None):
        if condition:
            condition = condition.split('=')
            query = "SELECT {0} from {1} WHERE {2} = {3}".format(columns, table, condition[0], condition[1])
        else:
            query = "SELECT {0} from {1}".format(columns, table)
        self.conn.row_factory = sqlite3.Row
        cursor = self.conn.execute(query)
        return json.dumps([dict(row) for row in cursor.fetchall()], sort_keys=True, indent=4)

    def selectall(self):
        cursor = self.conn.execute("SELECT name FROM sqlite_master WHERE type='table'")
        tables = cursor.fetchall()
        d = {}
        for tbl in tables:
            self.conn.row_factory = sqlite3.Row
            cursor = self.conn.execute("SELECT * FROM {}".format(tbl[0]))
            d[tbl[0]] = [dict(row) for row in cursor.fetchall()]
        return json.dumps(d, sort_keys=True, indent=4)

    def insert(self, table, columns, data):
        query = "INSERT INTO {0} ({1}) VALUES ({2})".format(table, columns, data)
        self.conn.execute(query)

    def update(self, table, column, condition):
        condition = condition.split('=')
        query = "UPDATE {0} set {1} WHERE {2} = {3}".format(table, column, condition[0], condition[1])
        self.conn.execute(query)


with Wrapper('company.db') as w:
    w.create('Management', 'id INT PRIMARY KEY NOT NULL, first_name TEXT NOT NULL, second_name TEXT NOT NULL, '
                           'Age INT, Position TEXT NOT NULL, Salary REAL')
    w.insert('Management', 'id, first_name, second_name, Age, Position, Salary', "1, 'Ivan', 'Ivanov', 40, "
                                                                                 "'Director', 100000.00")
    w.insert('Management', 'id, first_name, second_name, Age, Position, Salary', "2, 'Petr', 'Petrov', 35, "
                                                                                 "'Chief_Engineer', 80000.00")
    res = w.select('id, first_name, second_name, Age, Position, Salary', 'Management')
    print(res)
    w.create('Designers',
             'id INT PRIMARY KEY NOT NULL, first_name TEXT NOT NULL, second_name TEXT NOT NULL, Age INT, '
             'Position TEXT NOT NULL, Department TEXT NOT NULL, Salary REAL')
    w.insert('Designers', 'id, first_name, second_name, Age, Position, Department, Salary',
             "1, 'Vasily', 'Grigorev', 35, 'Department_head', 'construction', 60000.00")
    w.insert('Designers', 'id, first_name, second_name, Age, Position, Department, Salary',
             "2, 'Natalia', 'Veselova', 25, 'engineer', 'construction', 35000.00")
    w.insert('Designers', 'id, first_name, second_name, Age, Position, Department, Salary',
             "3, 'Kirill', 'Smirnov', 38, 'Department_head', 'electrical', 60000.00")
    w.insert('Designers', 'id, first_name, second_name, Age, Position, Department, Salary',
             "4, 'Kirill', 'Smirnov', 38, 'Department_head', 'thermomechanical', 60000.00")
    res = w.select('id, first_name, second_name, Age, Position, Department, Salary', 'Designers')
    print(res)
    print(w.selectall())
    res = w.select('id, first_name, second_name, Age, Position, Department, Salary', 'Designers', "Salary=60000.00")
    print(res)
    w.update('Designers', "first_name='Ruslan'", 'id=4')
    w.update('Designers', "second_name='Ludmilov'", 'id=4')
    w.update('Designers', 'Salary=50000.00', 'id=4')
    print(w.selectall())
