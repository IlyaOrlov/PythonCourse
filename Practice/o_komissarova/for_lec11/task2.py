import sqlite3 as sq

if __name__ == '__main__':
    with sq.connect('task2.bd') as con:
        cur = con.cursor()
    cur.executescript("""
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

    cur.execute("INSERT INTO Vendors(name) VALUES('Toy store')")
    cur.execute("INSERT INTO Vendors(name) VALUES('Book store')")
    cur.execute("INSERT INTO Vendors(name) VALUES('Fabric store')")
    cur.execute("INSERT INTO Vendors(name) VALUES('Car store')")
    cur.execute("INSERT INTO Customers(name, second_name) "
                "VALUES('John', 'Peterson')")
    cur.execute("INSERT INTO Customers(name, second_name) "
                "VALUES('Jack', 'Anderson')")
    cur.execute("INSERT INTO Customers(name, second_name) "
                "VALUES('Sandy', 'Clark')")
    cur.execute("INSERT INTO Products(vendor_id, customer_id, name, price, quantity)"
                "VALUES(1, 1, 'Puzzle', 5, 1)")
    cur.execute("INSERT INTO Products(vendor_id, customer_id, name, price, quantity)"
                "VALUES(1, 3, 'Bear_toy', 8, 1)")
    cur.execute("INSERT INTO Products(vendor_id, customer_id, name, price, quantity)"
                "VALUES(1, 3, 'Barbie_toy', 7, 1)")
    cur.execute("INSERT INTO Products(vendor_id, customer_id, name, price, quantity)"
                "VALUES(2, 2, 'Lord of the rings', 15, 1)")
    cur.execute("INSERT INTO Products(vendor_id, customer_id, name, price, quantity)"
                "VALUES(2, 2, 'The chronics of Narnia', 20, 2)")
    cur.execute("INSERT INTO Products(vendor_id, customer_id, name, price, quantity)"
                "VALUES(2, 1, 'Pride and Prejudice', 10, 1)")
    cur.execute("INSERT INTO Products(vendor_id, customer_id, name, price, quantity)"
                "VALUES(3, 3, 'Blue cotton', 8, 2)")
    cur.execute("INSERT INTO Products(vendor_id, customer_id, name, price, quantity)"
                "VALUES(3, 3, 'Scarlet silk', 25, 3)")
    cur.execute("INSERT INTO Products(vendor_id, customer_id, name, price, quantity)"
                "VALUES(3, 3, 'Black velour', 12, 2)")

    cur.execute("SELECT DISTINCT Vendors.name FROM Vendors, Products "
                "WHERE Vendors.id == vendor_id "
                "AND price <= 10 "
                "GROUP BY quantity "
                "HAVING SUM(quantity) >= 2"
                )
    print(cur.fetchall())

    cur.execute("SELECT DISTINCT Customers.name, Vendors.name "
                "FROM Customers "
                "INNER JOIN Vendors JOIN Products "
                "ON Vendors.id == vendor_id "
                "AND Customers.id == customer_id "
                "ORDER BY Vendors.name"
                )
    print(cur.fetchall())

    cur.execute("SELECT DISTINCT Vendors.name, Products.name, MAX(quantity) "
                "FROM Vendors, Products "
                "WHERE Vendors.id == vendor_id "
                "GROUP BY Vendors.name "
                "ORDER BY quantity DESC")
    print(cur.fetchall())

    cur.execute("SELECT DISTINCT Vendors.name, Products.name, (price*quantity) as Profit "
                "FROM Vendors LEFT JOIN Products "
                "ON Vendors.id == vendor_id "
                "ORDER BY Profit DESC, Vendors.name ASC")
    print(cur.fetchall())

