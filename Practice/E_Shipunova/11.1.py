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

    def crud_data(self, command: str) -> str:
        '''
        The function return json-format only command is 'SELECT',
        else return information line.
        :param command: str
        :return: str
        '''

        if len(command) != 0:                                     # checking the command
            check_com = command.lower()
        else:
            return 'Command is empty!'

        if ('insert' not in check_com) and ('select' not in check_com) and ('update' not in check_com) and ('delete' not in check_com):
            return 'Incorrect command!'

        conn = sqlite3.connect(self.name_db)

        if 'insert' in check_com:
            conn.execute(command)
            conn.commit()
            conn.close()

            return 'Data added.'

        elif 'select' in check_com:
            arr_json = []
            cursor = conn.execute(command)

            name_row = [description[0] for description in cursor.description]   # for get name of row
            result = cursor.fetchall()                                          # for get result of select

            for row in result:                                                  # made json-format
                buf = dict()
                for i in range(len(name_row)):
                    buf[name_row[i]] = row[i]
                arr_json.append(buf)
            conn.commit()
            conn.close()

            return json.dumps(arr_json, sort_keys=True, indent=4)               # for pretty result

        elif 'update' in check_com:
            conn.execute(command)
            conn.commit()
            conn.close()

            return 'Data updated.'

        conn.execute(command)                                                   # if command is 'delete'
        conn.commit()
        conn.close()

        return 'Data deleted.'


if __name__ == '__main__':
    if create_db_with_persons_tab('persons.db'):
        wrap = WrapperSQLite('persons.db')
        print(wrap.crud_data('INSERT INTO persons (id, name, age) VALUES (8, "David", 44);'))  # position == None
        print(wrap.crud_data('UPDATE persons SET age = 100 WHERE id = 1;'))
        print(wrap.crud_data('DELETE FROM persons WHERE age = 100 AND name = "Noah";'))        # where id = 1
        print(wrap.crud_data('SELECT id, name, age FROM persons WHERE position IS NULL'))      # where id = 8
        print(wrap.crud_data('SELECT * FROM persons WHERE age = 22 OR age = 24 ORDER BY age'))
        print(wrap.crud_data(''))
        print(wrap.crud_data('Incorrect data'))
        if delete_db('persons.db'):
            print('File of db deleted')
