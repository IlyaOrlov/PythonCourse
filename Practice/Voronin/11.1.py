import sqlite3
import json

class SQLite:
    def __init__(self, name):
        self.name = name
    def __enter__(self):
        self.conn = sqlite3.connect(self.name)
        self.cursor = self.conn.cursor()
        return self
    def execute(self, inquiry):
        self.cursor.execute(inquiry)
        self.conn.commit()
    def select(self, show):
        a = self.cursor.execute(show)
        data = []
        for row in a:
            data.append(row)
        return json.dumps(data)

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.conn.close()

with SQLite('my_db') as d:
    d.execute('CREATE TABLE COMPANY'
                 '    (ID       INT   PRIMARY KEY  NOT NULL,'
                 '     NAME     TEXT               NOT NULL,'
                 '     AGE      INT                NOT NULL,'
                 '     ADDRESS  CHAR(50),'
                 '     SALARY   REAL);')
    d.execute("INSERT INTO COMPANY (ID, NAME, AGE, ADDRESS, SALARY)"
                 "VALUES (1, 'Paul', 32, 'California', 20000.00)")
    print(d.select('SELECT id, name, age, address, salary FROM '
                          'COMPANY WHERE id = 1'))

