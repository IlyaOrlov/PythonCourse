import sqlite3
import json
from contextlib import contextmanager

#1st var
class SQLiteManager:
    __exit = 'exit'

    @contextmanager
    def connectManager(self, file):
        conn = sqlite3.connect(file)
        yield conn
        conn.close()

    def start(self):
        print('Welcome to SQLite Python Manager by asintsov. For exit input "{}"'.format(self.__exit))

        self.__file = input('Input DB filename: ')
        if (self.__file != self.__exit):
            while 1:
                command = input('Input SQL command: ')
                if (command == self.__exit):
                    break
                self.__execute(command)

    def execute(self, command):
        with self.connectManager(self.__file) as conn:
            cursor = conn.execute(command)
            if (command.find('SELECT') == 0): #применения методу select не нашел :(
                data = cursor.fetchall()
                self.__createJSON('./out.json', data)
            elif (command.find('INSERT') == 0 or command.find('UPDATE') == 0 or command.find('DELETE') == 0):
                conn.commit()

    def __createJSON(self, file, data):
        with open(file, 'w') as out:
            json.dump(data, out)

#s = SQLiteManager()
#s.start()

#2d var
class SQLiteContextManager():
    __exit = 'exit'

    def __init__(self,file, command):
        self.__file = file
        self.__command = command

    def __enter__(self):
        self.__conn = sqlite3.connect(self.__file)
        if (self.__command.find('SELECT') == 0):
            return self.__select(self.__command)
        elif (self.__command.find('INSERT') == 0
              or self.__command.find('UPDATE') == 0
              or self.__command.find('DELETE') == 0):
            self.__execute(self.__command)
            return ''

    def __exit__(self, type, value, traceback):
        self.__conn.close()

    def __execute(self, command):
        self.__conn.execute(command)
        conn.commit()

    def __select(self, command):
        cursor = self.__conn.execute(command)
        return cursor.fetchall()

class SQLiteWrapper():
    __exit = 'exit'

    def __createJSON(self, file, data):
        with open(file, 'a') as out:
            json.dump(data, out)

    def start(self):
        print('Welcome to SQLite Python Manager by asintsov. For exit input "{}"'.format(self.__exit))
        file = input('Input DB filename: ')
        if (file != self.__exit):
            while 1:
                command = input('Input SQL command: ')
                if (command == self.__exit):
                    break
                with SQLiteContextManager(file, command) as data:
                    self.__createJSON('./out.json', data)


s = SQLiteWrapper()
s.start()
