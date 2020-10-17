class SQLiteManager:
    from contextlib import contextmanager

    exit = 'exit'

    @contextmanager
    def connectManager(self, file):
        import sqlite3

        conn = sqlite3.connect(file)
        yield conn
        conn.close()

    def Start(self):
        print('Welcome to SQLite Python Manager by asintsov. For exit input "{}"'.format(self.exit))

        self.file = input('Input DB filename: ')
        if (self.file != self.exit):
            while 1:
                command = input('Input SQL command: ')
                if (command == self.exit):
                    break
                self.Execute(command)

    def Execute(self, command):
        with self.connectManager(self.file) as conn:
            cursor = conn.execute(command)
            if (command.find('SELECT') == 0): #применения методу select не нашел :(
                data = cursor.fetchall()
                self.CreateJSON('./out.json', data)
            elif (command.find('INSERT') == 0 or command.find('UPDATE') == 0 or command.find('DELETE') == 0):
                conn.commit()

    def CreateJSON(self, file, data):
        import json
        
        with open(file, 'w') as out:
            json.dump(data, out)

s = SQLiteManager()
s.Start()
