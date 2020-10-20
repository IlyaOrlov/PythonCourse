import sqlite3
import os


def make_data_base(name_db):
    conn = sqlite3.connect(name_db)
    conn.execute('CREATE TABLE buyers '                        
                 '(id INT PRIMARY KEY NOT NULL,'
                 'name CHAR(128) NOT NULL);')
    conn.execute('INSERT INTO buyers (id, name)'  
                 'VALUES'
                 '(1, "Peter"),'
                 '(2, "Matt"),'
                 '(3, "Alice"),'
                 '(4, "Marti"),'
                 '(5, "Tom");')
    conn.commit()
    conn.execute('CREATE TABLE products '
                 '(id INT PRIMARY KEY NOT NULL,'
                 'title CHAR(64) NOT NULL,'
                 'price INT NOT NULL,'
                 'idManufacturer INT NOT NULL);')
    conn.execute('INSERT INTO products (id, title, price, idManufacturer)'
                 'VALUES'
                 '(1, "Phone", 100, 1),'
                 '(2, "Laptop", 200, 1),'
                 '(3, "Coffee", 3, 2),'
                 '(4, "Tea", 2, 2),'
                 '(5, "Watch", 70, 1),'
                 '(6, "Game", 60, 3),'
                 '(7, "Crown", 25, 4);')
    conn.commit()
    conn.execute('CREATE TABLE manufacturers '
                 '(id INT PRIMARY KEY NOT NULL,'
                 'company CHAR(128) NOT NULL);')
    conn.execute('INSERT INTO manufacturers (id, company)'
                 'VALUES'
                 '(1, "Apple"),'
                 '(2, "Lipton"),'
                 '(3, "Ubisoft"),'
                 '(4, "British");')
    conn.commit()
    conn.execute('CREATE TABLE buyerProduct '
                 '(idBuyer INT NOT NULL,'
                 'idProduct INT NOT NULL,'
                 'quantityProducts INT NOT NULL,'
                 'PRIMARY KEY (idBuyer, idProduct));')
    conn.execute('INSERT INTO buyerProduct (idBuyer, idProduct, quantityProducts)'
                 'VALUES'
                 '(1, 1, 1),'
                 '(3, 3, 3),'
                 '(2, 5, 1),'
                 '(1, 4, 4),'
                 '(3, 5, 2),'
                 '(4, 6, 3),'
                 '(5, 2, 1);')
    conn.commit()
    conn.close()
    print('Base is done')
    return os.path.isfile(name_db)


def delete_db(name_db):
    os.remove(name_db)


if __name__ == '__main__':
    if make_data_base('online_store.db'):
        conn = sqlite3.connect('online_store.db')
        cursor = conn.execute('SELECT company '
                              'FROM ('
                                     'SELECT m.company, COUNT(*) '        
                                     'FROM manufacturers AS m, products AS p '
                                     'WHERE p.idManufacturer = m.id '
                                     'AND p.price <= 10 '
                                     'GROUP BY m.company HAVING COUNT(*) > 2'
                                     ');')
        print('1. These companies have more than 2 products with a price <= 10$:')
        for row in cursor:
            print(row)
        cursor = conn.execute('SELECT m.company, c.name '     
                              'FROM buyers AS c, buyerProduct AS cp, products AS p, manufacturers AS m '
                              'WHERE c.id = cp.idBuyer '
                              'AND cp.idProduct = p.id '
                              'AND p.idManufacturer = m.id '
                              'ORDER BY m.company;')
        print('2. Companies and their buyers:')
        for row in cursor:
            print(row)
        cursor = conn.execute('SELECT company, title, MAX(sum_prod) '
                              'FROM ('
                                     'SELECT m.company, p.title, '
                                     'SUM(cp.quantityProducts) AS sum_prod '
                                     'FROM buyerProduct AS cp, manufacturers AS m, products AS p '
                                     'WHERE cp.idProduct = p.id '
                                     'AND p.idManufacturer = m.id '
                                     'GROUP BY m.company, p.title'
                                     ')'
                              'GROUP BY company, title')

        print('3. Manufacturers, products and sold count of each product:')
        for row in cursor:
            print(row)
        cursor = conn.execute('Select company, title, max(sum_prod) '
                              'FROM ('
                                     'SELECT m.company, p.title, '
                                     'SUM(cp.quantityProducts*p.price) AS sum_prod '
                                     'FROM buyerProduct AS cp, manufacturers AS m, products AS p '
                                     'WHERE cp.idProduct = p.id '
                                     'AND p.idManufacturer = m.id '
                                     'GROUP BY m.company, p.title'
                                    ') '
                              'GROUP BY company, title;')

        print('4.1 Manufacturer and all sold products and sum_prod:')
        for row in cursor:
            print(row)
        cursor = conn.execute('SELECT m.company, p.title, null '
                              'FROM manufacturers AS m, products AS p '
                              'WHERE p.idManufacturer = m.id '
                              'AND NOT EXISTS ('
                                               'SELECT idProduct '
                                               'FROM buyerProduct AS cp '
                                               'WHERE cp.idProduct=p.id'
                                              ');'
                              )

        print('4.2 Manufacturer and all unsold products:')
        for row in cursor:
            print(row)
        conn.close()
        delete_db('online_store.db')
