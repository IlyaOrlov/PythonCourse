import json
import sqlite3 as sq


class SqLyteConnector:
    def __init__(self, db_name):
        with sq.connect(db_name) as self.con:
            self.cur = self.con.cursor()

    def select(self, sql_request):
        self.cur.execute(sql_request)
        data = self.cur.fetchall()
        print(data)
        response = []
        for i in range(len(data)):
            object_map = {}
            for j in range(len(data[i])):
                key = self.cur.description[j][0]
                value = data[i][j]
                object_map[key] = value
            response.append(object_map)
        return json.dumps(response)

    def execute(self, sql_request):
        self.cur.executescript(sql_request)
        if 'CREATE' in sql_request:
            return json.dumps({'table': 'created'})
        elif 'INSERT' in sql_request:
            return json.dumps({'data': 'inserted'})
        elif 'DROP' in sql_request:
            return json.dumps({'table': 'dropped'})


if __name__ == '__main__':
    my_connector = SqLyteConnector('test.bd')
    print(my_connector.execute("""CREATE TABLE IF NOT EXISTS cars (
            car_id INTEGER PRIMARY KEY AUTOINCREMENT,
            model TEXT,
            price INTEGER
        )"""))
    print(my_connector.execute("INSERT INTO cars VALUES(1,'Audi',52642)"))
    print(my_connector.execute("INSERT INTO cars VALUES(2,'Mercedes',57127)"))
    print(my_connector.select("SELECT * FROM cars"))
    print(my_connector.execute("DROP TABLE cars"))
