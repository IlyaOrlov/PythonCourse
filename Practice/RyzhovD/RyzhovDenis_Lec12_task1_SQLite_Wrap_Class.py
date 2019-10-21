"""
We redefine SQLite3 commands as methods of our WrapSQLite class.
List of recognized SQLite commands:'CREATE' (now),
'DELETE', 'INSERT', 'SELECT', 'SET', 'UPDATE' to be included further.

# We will think about lower or upper case later.

Python 3.6
sqlite3 3.22.0
simplejson 3.13.2
"""

import sqlite3
import simplejson


class WrapSQLite:
    def __init__(self, table='original7staff'):
        self.table = table

    def select(self, what='*'):
        # Here we use table which appears to exist.
        with sqlite3.connect('original7.db') as db:
        # db = sqlite3.connect('original7.db')  # connect with database, not a table
            select_string = 'SELECT {} FROM {}'.format(what, self.table)
            selection = db.execute(select_string)  # create a cursor-type object (not a python data
            py_data = selection.fetchall()  # form python-data (list)
        # db.close()
        return simplejson.dumps(py_data)  # serializes Python object to a JSON string


### TEST
w = WrapSQLite()
json_select = w.select('Name, MercuryFlightName, MercuryFlightDate')
