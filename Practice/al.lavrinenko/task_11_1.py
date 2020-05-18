import sqlite3
import json


class SQLiteManager:
    def __init__(self, db_name):
        self.db_name = db_name

    def __enter__(self):
        self.conn = sqlite3.connect(self.db_name)
        self.cur = self.conn.cursor()
        print(f'{self.db_name} is open')
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.conn.close()
        print(f'{self.db_name} is closed')

    def select(self, command):
        try:
            self.cur.execute(command)
            return json.dumps(self.cur.fetchall())
        except Exception as e:
            print(f'Error: {e}')

    def execute(self, command):
        try:
            self.cur.execute(command)
            self.conn.commit()
        except Exception as e:
            print(f'Error: {e}')


if __name__ == '__main__':
    with SQLiteManager('sqlite_db.db') as db:
        while True:
            cmd = input('Enter the SQL command: ')
            if cmd == '.quit':
                break
            elif 'SELECT' in cmd:
                json_data = db.select(cmd)
                if json_data:
                    for row in json.loads(json_data):
                        print(row)
            else:
                db.execute(cmd)
