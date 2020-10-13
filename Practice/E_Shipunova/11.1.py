import sqlite3
import os
import json


def create_db_with_persons_tab(name_db: str) -> bool:             # only for debugging
    conn = sqlite3.connect(name_db)                               # creating db

    conn.execute('CREATE TABLE persons '                          # creating table person into db
                 '(id INT PRIMARY KEY NOT NULL,'
                 'name CHAR(128) NOT NULL,'
                 'age INT NOT NULL,'
                 'position TEXT);')

    conn.execute('INSERT INTO persons (id, name, age, position)'  # filling db
                 'VALUES'
                 '(1, "Noah", 33, "baker"),'
                 '(2, "Mason", 22, "poet"),'
                 '(3, "Liam", 24, "butcher"),'
                 '(4, "Alex", 22, "cook"),'
                 '(5, "Jack", 24, "cook"),'
                 '(6, "Jack", 20, "student"),'
                 '(7, "Oscar", 24, "doctor");')

    conn.commit()                                                 # saving changes
    conn.close()                                                  # disconnecting from db

    return os.path.isfile(name_db)                                # checking the creation db


def delete_db(name_db: str) -> bool:                              # only for debugging
    os.remove(name_db)                                            # delete file of db

    return not os.path.isfile(name_db)                            # checking the deletion db


class WrapperSQLite:

    def __init__(self, name_db):                                  # for any db
        self.name_db = name_db
        self.conn = None

    def __enter__(self):                                          # open the db
        self.conn = sqlite3.connect(self.name_db)                 # initialization of self.conn
        return self                                               # return an instant of the class for later call

    def __exit__(self, exc_type, exc_val, exc_tb):                # close the db
        self.conn.close()

    def execute_ins_upd_del(self, command: str) -> str:
        if self.check_command(command):
            self.conn.execute(command)
            self.conn.commit()
            return 'Changes saved.'

        return 'Incorrect command!'

    def execute_select(self, command: str) -> str:
        if self.check_command(command):
            arr_json = []
            cursor = self.conn.execute(command)
            name_row = [description[0] for description in cursor.description]  # for get name of row
            result = cursor.fetchall()                                         # for get result of select

            for row in result:                                                 # made json-format
                buf = dict()
                for i in range(len(name_row)):
                    buf[name_row[i]] = row[i]
                arr_json.append(buf)

            self.conn.commit()
            return json.dumps(arr_json, sort_keys=True, indent=4)              # for pretty result

        return 'Incorrect command!'

    @staticmethod                                             # class and instance attributes aren't used - log.connect
    def check_command(command: str) -> bool:

        if len(command) != 0:                                 # checking the command
            comm = command.lower()
        else:
            return False

        if ('insert' not in comm) and ('select' not in comm) and ('update' not in comm) and ('delete' not in comm):
            return False

        return True


if __name__ == '__main__':
    if create_db_with_persons_tab('persons.db'):
        with WrapperSQLite('persons.db') as wrap:             # wrap is instant of the class for later call
            print(wrap.execute_ins_upd_del('INSERT INTO persons (id, name, age) VALUES (8, "David", 44);'))  # pos==None
            print(wrap.execute_ins_upd_del('UPDATE persons SET age = 100 WHERE id = 1;'))
            print(wrap.execute_ins_upd_del('DELETE FROM persons WHERE age = 100 AND name = "Noah";'))       # where id=1
            print(wrap.execute_select('SELECT id, name, age FROM persons WHERE position IS NULL'))          # where id=8
            print(wrap.execute_select('SELECT * FROM persons WHERE age = 22 OR age = 24 ORDER BY age'))
            print(wrap.execute_ins_upd_del(''))
            print(wrap.execute_ins_upd_del('Incorrect data'))

        if delete_db('persons.db'):
            print('File of db deleted.')
