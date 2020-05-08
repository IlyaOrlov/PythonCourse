import sqlite3
import json


class MySqlite:

    def __init__(self, db_name):
        self.db_name = db_name

    def __enter__(self):
        self.conn = sqlite3.connect(self.db_name)
        print(f'DataBase {self.db_name} is open.')
        self.cursor = self.conn.cursor()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        print('DataBase is closed.')
        self.conn.close()

    def execute(self, some_cmd):
        self.cursor.executescript(some_cmd)
        if 'CREATE' in some_cmd:
            print('Table created.')
        elif 'INSERT' in some_cmd:
            print('Data added into Table.')
        elif 'UPDATE' in some_cmd:
            print('Table changed successfully.')
        elif 'DROP' in some_cmd:
            print('Table was deleted.')
        self.conn.commit()

    def select(self, some_cmd):
        c = self.cursor.execute(some_cmd)
        data = []
        for row in c:
            data.append(row)
        return json.dumps(data)


if __name__ == '__main__':
    try:
        with MySqlite('my_sqlite_database.db') as table:
            while True:
                cmd = input('Type SQL command: ')
                if cmd == 'quit':
                    break
                elif 'SELECT' in cmd:
                    json_data = json.loads(table.select(cmd))
                    for element in json_data:
                        print(element)
                else:
                    table.execute(cmd)
    except Exception as Error:
        print(f'Error: {Error}')
