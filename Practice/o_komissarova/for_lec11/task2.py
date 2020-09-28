import os
import sqlite3 as sq


def create_tables(cursor):
    cursor.executescript("""
        PRAGMA foreign_keys=on;
        CREATE TABLE Vendors(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL);

        CREATE TABLE Customers(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        second_name TEXT NOT NULL);

        CREATE TABLE Products(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        vendor_id INTEGER,
        customer_id INTEGER,
        name TEXT NOT NULL,
        price REAL CHECK (price >0),
        quantity INTEGER,
        FOREIGN KEY (Vendor_id) REFERENCES Vendors(id),
        FOREIGN KEY (Customer_id) REFERENCES Customers(id)
        );""")


def insert_data(cursor):
    cursor.execute("INSERT INTO Vendors(name) VALUES('Toy store')")
    cursor.execute("INSERT INTO Vendors(name) VALUES('Book store')")
    cursor.execute("INSERT INTO Vendors(name) VALUES('Fabric store')")
    cursor.execute("INSERT INTO Vendors(name) VALUES('Car store')")
    cursor.execute("INSERT INTO Customers(name, second_name) "
                   "VALUES('John', 'Peterson')")
    cursor.execute("INSERT INTO Customers(name, second_name) "
                   "VALUES('Jack', 'Anderson')")
    cursor.execute("INSERT INTO Customers(name, second_name) "
                   "VALUES('Sandy', 'Clark')")
    cursor.execute("INSERT INTO Products(vendor_id, customer_id, name, price, quantity)"
                   "VALUES(1, 1, 'Puzzle', 5, 1)")
    cursor.execute("INSERT INTO Products(vendor_id, customer_id, name, price, quantity)"
                   "VALUES(1, 3, 'Bear_toy', 8, 1)")
    cursor.execute("INSERT INTO Products(vendor_id, customer_id, name, price, quantity)"
                   "VALUES(1, 3, 'Barbie_toy', 7, 1)")
    cursor.execute("INSERT INTO Products(vendor_id, customer_id, name, price, quantity)"
                   "VALUES(2, 2, 'Lord of the rings', 15, 1)")
    cursor.execute("INSERT INTO Products(vendor_id, customer_id, name, price, quantity)"
                   "VALUES(2, 2, 'The chronics of Narnia', 20, 2)")
    cursor.execute("INSERT INTO Products(vendor_id, customer_id, name, price, quantity)"
                   "VALUES(2, 1, 'Pride and Prejudice', 10, 1)")
    cursor.execute("INSERT INTO Products(vendor_id, customer_id, name, price, quantity)"
                   "VALUES(3, 3, 'Blue cotton', 8, 2)")
    cursor.execute("INSERT INTO Products(vendor_id, customer_id, name, price, quantity)"
                   "VALUES(3, 3, 'Scarlet silk', 25, 3)")
    cursor.execute("INSERT INTO Products(vendor_id, customer_id, name, price, quantity)"
                   "VALUES(3, 3, 'Black velour', 12, 2)")


def get_data(cursor):
    cursor.execute("SELECT DISTINCT Vendors.name FROM Vendors, Products "
                   "WHERE Vendors.id == vendor_id "
                   "AND price <= 10 "
                   "GROUP BY quantity "
                   "HAVING SUM(quantity) >= 2"
                   )
    print(cursor.fetchall())

    cursor.execute("SELECT DISTINCT Customers.name, Vendors.name "
                   "FROM Customers "
                   "INNER JOIN Vendors JOIN Products "
                   "ON Vendors.id == vendor_id "
                   "AND Customers.id == customer_id "
                   "ORDER BY Vendors.name"
                   )
    print(cursor.fetchall())

    cursor.execute("SELECT DISTINCT Vendors.name, Products.name, MAX(quantity) "
                   "FROM Vendors, Products "
                   "WHERE Vendors.id == vendor_id "
                   "GROUP BY Vendors.name "
                   "ORDER BY quantity DESC")
    print(cursor.fetchall())

    cursor.execute("SELECT DISTINCT Vendors.name, Products.name, (price*quantity) as Profit "
                   "FROM Vendors LEFT JOIN Products "
                   "ON Vendors.id == vendor_id "
                   "ORDER BY Profit DESC, Vendors.name ASC")
    print(cursor.fetchall())


if __name__ == '__main__':
    name_bd = "task2.bd"
    bd_created = os.path.exists(name_bd)
    with sq.connect(name_bd) as con:
        cur = con.cursor()
        if bd_created is False:
            create_tables(cur)
            insert_data(cur)
        get_data(cur)

