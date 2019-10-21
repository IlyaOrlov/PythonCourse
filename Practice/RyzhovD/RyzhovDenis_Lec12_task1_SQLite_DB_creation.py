"""
The database of first american astronauts (Original 7) is created
for tutorial purposes with sqlite3 library.
Python 3.6
sqlite3 3.22.0
"""

import sqlite3
# print(sqlite3.sqlite_version)

conn = sqlite3.connect('original7.db')
conn.execute('CREATE TABLE original7staff'
             '(ID INT PRIMARY KEY NOT NULL,'
             'Name TEXT NOT NULL,'
             'BirthYear INT,'
             'MercuryFlightName TEXT,'
             'MercuryFlightDate TEXT);')
conn.execute("INSERT INTO original7staff (ID, Name, BirthYear, MercuryFlightName, MercuryFlightDate)"
             "VALUES (1, 'Alan Shepard', 1923, 'Freedom 7', '5 May 1961')")
conn.execute("INSERT INTO original7staff (ID, Name, BirthYear, MercuryFlightName, MercuryFlightDate)"
             "VALUES (2, 'Gus Grissom', 1926, 'Liberty Bell 7', '21 Jul 1961')")
conn.execute("INSERT INTO original7staff (ID, Name, BirthYear, MercuryFlightName, MercuryFlightDate)"
             "VALUES (3, 'John Glenn', 1921, 'Friendship 7', '20 Feb 1962')")
conn.execute("INSERT INTO original7staff (ID, Name, BirthYear, MercuryFlightName, MercuryFlightDate)"
             "VALUES (4, 'Scott Carpenter', 1925, 'Aurora 7', '24 May 1962')")
conn.execute("INSERT INTO original7staff (ID, Name, BirthYear, MercuryFlightName, MercuryFlightDate)"
             "VALUES (5, 'Wally Schirra', 1923, 'Sigma 7', '3 Oct 1962')")
conn.execute("INSERT INTO original7staff (ID, Name, BirthYear, MercuryFlightName, MercuryFlightDate)"
             "VALUES (6, 'Gordo Cooper', 1927, 'Faith 7', '15 May 1963')")
conn.execute("INSERT INTO original7staff (ID, Name, BirthYear, MercuryFlightName, MercuryFlightDate)"
             "VALUES (7, 'Deke Slayton', 1924, 'Apollo-Soyuz Test Project', '27 Feb 1982')")
conn.commit()

datum = conn.execute('SELECT Name, MercuryFlightName, MercuryFlightDate FROM original7staff')
for row in datum:
    print(row)
print('---')