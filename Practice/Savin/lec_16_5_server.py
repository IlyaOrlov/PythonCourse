import socket, sqlite3, pickle

conn = sqlite3.connect('data.db')
conn.execute('CREATE TABLE EMPLOYEE'
             '(ID PRIMARY KEY NOT NULL,'
             'NAME TEXT NOT NULL,'
             'AGE INT NOT NULL,'
             'SALARY REAL);')

conn.execute("INSERT INTO EMPLOYEE (ID, NAME, AGE, SALARY)"
             "VALUES (1, 'Frank', 32, 1000.00)")
conn.execute("INSERT INTO EMPLOYEE (ID, NAME, AGE, SALARY)"
             "VALUES (2, 'Jhon', 40, 2500.00)")
conn.execute("INSERT INTO EMPLOYEE (ID, NAME, AGE, SALARY)"
             "VALUES (3, 'Tom', 20, 800.00)")
conn.execute("INSERT INTO EMPLOYEE (ID, NAME, AGE, SALARY)"
             "VALUES (4, 'Alex', 40, 3000.00)")
conn.execute("INSERT INTO EMPLOYEE (ID, NAME, AGE, SALARY)"
             "VALUES (5, 'Frank', 30, 1000.00)")
conn.commit()

cursor = conn.cursor()

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind(('127.0.0.1', 12345))
sock.listen(5)
while True:
    client, addr = sock.accept()
    message = client.recv(1024)
    print(f'Полученное сообщение от клиента: {message.decode()}')
    request = list(cursor.execute(f'SELECT * FROM EMPLOYEE WHERE {message.decode()}'))
    result = pickle.dumps(request)
    client.send(result)
    client.close()

