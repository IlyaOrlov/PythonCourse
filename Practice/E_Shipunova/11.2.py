import sqlite3
import os


def create_db(name_db: str) -> bool:
    conn = sqlite3.connect(name_db)                                      # You can look at the db in file 11_2.png

    conn.execute('CREATE TABLE customers '                        
                 '(id INT PRIMARY KEY NOT NULL,'
                 'name CHAR(128) NOT NULL);')

    conn.execute('INSERT INTO customers (id, name)'  
                 'VALUES'
                 '(1, "Noah"),'
                 '(2, "Mason"),'
                 '(3, "Liam"),'
                 '(4, "Alex"),'
                 '(5, "Jack");')
    conn.commit()

    conn.execute('CREATE TABLE customerProduct '
                 '(idCustomer INT NOT NULL,'
                 'idProduct INT NOT NULL,'
                 'countProducts INT NOT NULL,'
                 'PRIMARY KEY (idCustomer, idProduct));')

    conn.execute('INSERT INTO customerProduct (idCustomer, idProduct, countProducts)'
                 'VALUES'
                 '(1, 1, 2),'
                 '(1, 5, 1),'
                 '(1, 7, 1),'
                 '(2, 4, 1),'
                 '(4, 5, 1),'
                 '(5, 5, 2),'
                 '(5, 2, 1);')
    conn.commit()

    conn.execute('CREATE TABLE products '
                 '(id INT PRIMARY KEY NOT NULL,'
                 'title CHAR(64) NOT NULL,'
                 'price INT NOT NULL,'
                 'idManufacturer INT NOT NULL);')

    conn.execute('INSERT INTO products (id, title, price, idManufacturer)'
                 'VALUES'
                 '(1, "productA1", 10, 1),'
                 '(2, "productA2", 7, 1),'
                 '(3, "productA3", 3, 1),'
                 '(4, "productB1", 2, 2),'
                 '(5, "productB2", 14, 2),'
                 '(6, "productB3", 19, 2),'
                 '(7, "productC1", 5, 3);')
    conn.commit()

    conn.execute('CREATE TABLE manufacturers '
                 '(id INT PRIMARY KEY NOT NULL,'
                 'company CHAR(128) NOT NULL);')

    conn.execute('INSERT INTO manufacturers (id, company)'
                 'VALUES'
                 '(1, "CompanyA"),'
                 '(2, "CompanyB"),'
                 '(3, "CompanyC"),'
                 '(4, "CompanyD");')

    conn.commit()
    conn.close()

    return os.path.isfile(name_db)                                # checking the creation db


def delete_db(name_db: str) -> bool:
    os.remove(name_db)                                            # delete file of db

    return not os.path.isfile(name_db)                            # checking the deletion db


if __name__ == '__main__':
    if create_db('store.db'):
        print('Base is done')
        conn = sqlite3.connect('store.db')

        # 1 request
        cursor = conn.execute('SELECT company '
                              'FROM ('
                                     'SELECT m.company, COUNT(*) '        
                                     'FROM manufacturers AS m, products AS p '
                                     'WHERE p.idManufacturer = m.id '
                                     'AND p.price <= 10 '
                                     'GROUP BY m.company HAVING COUNT(*) > 2'
                                     ');')
        print('1. These companies have more than 2 products with a price <= 10 $:')
        for row in cursor:
            print(row)

        # 2 request
        cursor = conn.execute('SELECT m.company, c.name '     
                              'FROM customers AS c, customerProduct AS cp, products AS p, manufacturers AS m '
                              'WHERE c.id = cp.idCustomer '
                              'AND cp.idProduct = p.id '
                              'AND p.idManufacturer = m.id '
                              'ORDER BY m.company;')
        print('2. Companies and their customers:')
        for row in cursor:
            print(row)

        # 3.1 request - manufacturers, products and sold count of each product - ONLY THIS
        cursor = conn.execute('SELECT company, title, MAX(sum_prod) '
                              'FROM ('
                                     'SELECT m.company, p.title, '
                                     'SUM(cp.countProducts) AS sum_prod '
                                     'FROM customerProduct AS cp, manufacturers AS m, products AS p '
                                     'WHERE cp.idProduct = p.id '
                                     'AND p.idManufacturer = m.id '
                                     'GROUP BY m.company, p.title'
                                     ')'
                              'GROUP BY company, title')

        print('3.1 Manufacturers, products and sold count of each product:')
        for row in cursor:
            print(row)

        # OR
        # 3.2 request - manufacturers  and MAX_count of sold products, but without products.title  - ONLY THIS
        cursor = conn.execute('SELECT company, MAX(sum_prod) '
                              'FROM ('
                                     'SELECT m.company, p.title, '
                                     'SUM(cp.countProducts) AS sum_prod '
                                     'FROM customerProduct AS cp, manufacturers AS m, products AS p '
                                     'WHERE cp.idProduct = p.id '
                                     'AND p.idManufacturer = m.id '
                                     'GROUP BY m.company, p.title'
                                    ')'
                              'GROUP BY company;')

        print('3.2 Manufacturers and MAX_count of sold products:')
        for row in cursor:
            print(row)

        # 4.1 request - For each manufacturer all sold products and sum_prod, but without unsold products - ONLY THIS
        cursor = conn.execute('Select company, title, max(sum_prod) '
                              'FROM ('
                                     'SELECT m.company, p.title, '
                                     'SUM(cp.countProducts*p.price) AS sum_prod '
                                     'FROM customerProduct AS cp, manufacturers AS m, products AS p '
                                     'WHERE cp.idProduct = p.id '
                                     'AND p.idManufacturer = m.id '
                                     'GROUP BY m.company, p.title'
                                    ') '
                              'GROUP BY company, title;')

        print('4.1 Manufacturer and all sold products, and sum_prod:')
        for row in cursor:
            print(row)

        # 4.2 request - For each manufacturer all unsold products and sum_prod - ONLY THIS
        cursor = conn.execute('SELECT m.company, p.title, null '
                              'FROM manufacturers AS m, products AS p '
                              'WHERE p.idManufacturer = m.id '
                              'AND NOT EXISTS ('
                                               'SELECT idProduct '
                                               'FROM customerProduct AS cp '
                                               'WHERE cp.idProduct=p.id'
                                              ');'
                              )

        print('4.2 Manufacturer and all unsold products, and sum_prod = None:')
        for row in cursor:
            print(row)

        conn.close()
        delete_db('store.db')
