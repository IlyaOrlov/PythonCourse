import sqlite3
import random
import os
from collections import Counter

db_name = "Shoppingcenter.db"
db_exists = os.path.exists(db_name)
conn = sqlite3.connect(db_name)
conn.row_factory = sqlite3.Row


# Конфигурирование базы данных (если необходимо выполнить в скрипте)
def configure_db(conn):
    cur = conn.cursor()

    # Создаем таблицу Buyers
    cur.execute("CREATE TABLE Buyers"
                "    (Id          INTEGER    PRIMARY KEY  AUTOINCREMENT,"
                "     Name        CHAR(128)  NOT NULL,"
                "     Balance     REAL       DEFAULT 0,"
                "     Login       CHAR(16)   NOT NULL,"
                "     Password    CHAR(16)   NOT NULL)")

    # Создаем таблицу Manufacturers
    cur.execute("CREATE TABLE Manufacturers"
                "    (Id        INTEGER    PRIMARY KEY  AUTOINCREMENT,"
                "     Name      CHAR(128)  NOT NULL,"
                "     Sales     REAL       DEFAULT 0)")

    # Создаем таблицу Goods
    cur.execute("CREATE TABLE Goods"
                "    (Id           INTEGER    PRIMARY KEY  AUTOINCREMENT,"
                "     Name         CHAR(128)  NOT NULL,"
                "     Manufacturer CHAR(128)  NOT NULL,"
                "     Price        REAL       NOT NULL,"
                "     Quantity     INTEGER    DEFAULT 0)")

    # Создаем таблицу BuyersGoods
    cur.execute("CREATE TABLE BuyersGoods"
                "    (BuyerID  INTEGER,"
                "     GoodID   INTEGER,"
                "     Quantity  INTEGER,"
                "     PRIMARY KEY (BuyerID, GoodID))")


# Добавление записей в таблицу Покупатели
def insert_buyers(conn, name, balance, login, pswd):
    cur = conn.cursor()
    cur.execute("INSERT INTO Buyers (Name, Balance, Login, Password)"
                " VALUES (:name, :balance, :login, :pswd)",
                {'name': name, 'balance': balance,
                 'login': login, 'pswd': pswd})
    conn.commit()


# Добавление записей в таблицу Производители
def insert_manufacturers(conn, name, sales):
    cur = conn.cursor()
    cur.execute("INSERT INTO Manufacturers (Name, Sales)"
                " VALUES (:name, :sales)",
                {'name': name, 'sales': sales})
    conn.commit()


# Добавление записей в таблицу Товары
def insert_goods(conn, name, manufacturer, price, quantity):
    cur = conn.cursor()
    cur.execute("INSERT INTO Goods (Name, Manufacturer, Price, Quantity)"
                " VALUES (:name, :manufacturer, :price, :quantity)",
                {'name': name, 'manufacturer': manufacturer, 'price': price, 'quantity': quantity})
    conn.commit()


# Добавление записей в таблицу Покупатели-Товары
def add_goods_to_buyer(conn, buyer_id, good_id, quantity):
    cur = conn.cursor()
    cur.execute("INSERT INTO BuyersGoods (BuyerID, GoodID, Quantity)"
                " VALUES (:buyer_id, :good_id, :quantity)",
                {'buyer_id': buyer_id, 'good_id': good_id, 'quantity': quantity})
    conn.commit()


# Получение списка производителей по заданным условиям
def get_manufacturer(conn, count, price):
    cur = conn.cursor()
    cur.execute("SELECT G.Manufacturer"
                " FROM Goods AS G"
                " WHERE G.Price <= :price",
                {'price': price})
    print("Список Производителей, у которых не менее {} товаров по цене {} долларов и ниже:".format(count, price))
    manufacturer_list = [row['Manufacturer'] for row in cur.fetchall()]
    manufacturer_count = Counter(manufacturer_list)
    return [elem for elem in manufacturer_count if manufacturer_count[elem] >= 2]


# Получение списка покупателей, сделавших заказы
def get_buyers(conn):
    cur = conn.cursor()
    cur.execute("SELECT G.Manufacturer, B.ID, B.Name, B.Balance, B.Login, B.Password"
                " FROM Goods AS G, Buyers AS B, BuyersGoods AS BG"
                " WHERE B.ID = BG.BuyerID AND BG.GoodID = G.Id"
                " GROUP BY G.Manufacturer, B.ID  ORDER BY G.Manufacturer")
    print("Информация о покупателях, которые делали заказы, "
          "сгруппированных по компаниям производителей чьи товары покупались:")
    for row in cur.fetchall():
        print(dict(row))


# Получение списка самых популярных товаров у каждого производителя с указанием количества проданных товаров
def get_popular_goods(conn):
    cur = conn.cursor()
    cur.execute("SELECT G.Manufacturer, G.Id, G.Name, G.Price, BG.Quantity"
                " FROM Goods AS G, Buyers AS B, BuyersGoods AS BG"
                " WHERE B.ID = BG.BuyerID AND BG.GoodID = G.Id"
                " GROUP BY G.Manufacturer, G.ID, BG.Quantity")
    popular_goods = {}
    for row in cur.fetchall():
        if row['Manufacturer'] not in popular_goods:
            popular_goods[row['Manufacturer']] = [{row['Name']: row['Quantity']}]
        else:
            if row['Name'] not in popular_goods[row['Manufacturer']][0]:
                popular_goods[row['Manufacturer']][0][row['Name']] = row['Quantity']
            else:
                popular_goods[row['Manufacturer']][0][row['Name']] += row['Quantity']
    for mf in popular_goods:
        max_value = max(popular_goods[mf][0].values())
        final_dict = {k: v for k, v in popular_goods[mf][0].items() if v == max_value}
        popular_goods[mf] = final_dict
    print("Список самых популярных товаров у каждого производителя с указанием количества проданных товаров:")
    print(popular_goods)


# Получение списка производителей товаров, которые продавались, с указанием их выручек по каждому виду товара
def get_manufacturer_sales(conn):
    cur = conn.cursor()
    cur.execute("SELECT G.Manufacturer,G.Name, BG.Quantity * G.Price AS Sales"
                " FROM Goods AS G, BuyersGoods AS BG"
                " WHERE BG.GoodID = G.Id"
                " GROUP BY G.Manufacturer, BG.Quantity * G.Price")
    manufacturer_sales = {}
    print("Список производителей товаров, которые продавались, с указанием их выручек по каждому виду товара:")
    for row in cur.fetchall():
        print(dict(row))
        if row['Manufacturer'] not in manufacturer_sales:
            manufacturer_sales[row['Manufacturer']] = row['Sales']
        else:
            manufacturer_sales[row['Manufacturer']] += row['Sales']
    print("Данные о выручке производителей:")
    print(manufacturer_sales)


if not db_exists:
    configure_db(conn)
    name = ['Alex', 'Sergey', 'Petr', 'Anna',
            'Nikolay', 'Victor', 'Viktoria',
            'Jack', 'Iliya', 'Julia', 'Avgust',
            'Mikhail', 'Jain', 'Bob', 'Erica',
            'Nikanor', 'Socrat', 'Valeria']
    surname = ['Ivanov', 'Petrov', 'Sidorov',
               'Abramov', 'Nikanov', 'Buhalov',
               'Samsonov', 'Baranov', 'Krivonosov',
               'Lomonosov', 'Mendeleev', 'Pushkin',
               'Romanov', 'Vinokurov', 'Putin',
               'Medvedev', 'Navalniy', 'Sechin']
    manufactures = ['manufacturer_' + str(i + 1) for i in range(5)]
    goods = ['good_' + str(i + 1) for i in range(20)]
    d = {}
    for i in range(10):
        name = random.choice(name)
        surname = random.choice(surname)
        bayer = '{} {}'.format(name, surname)
        balance = random.randint(100, 1000)
        login = 'bayer_{}'.format(i + 1)
        pswd = '{}{}'.format(surname, random.randint(12345, 54321))
        insert_buyers(conn, bayer, balance, login, pswd)
    for manufacturer in manufactures:
        insert_manufacturers(conn, manufacturer, 0)
    for good in goods:
        insert_goods(conn, good, random.choice(manufactures), random.randint(1, 30), random.randint(1, 100))
    for i in range(15):
        buyer_id = random.randint(1, 11)
        good_id = random.randint(1, 21)
        if buyer_id not in d:
            d[buyer_id] = [good_id]
            add_goods_to_buyer(conn, buyer_id, good_id, random.randint(1, 20))
        else:
            if good_id in d[buyer_id]:
                while good_id in d[buyer_id]:
                    good_id = random.randint(1, 21)
                    if good_id not in d[buyer_id]:
                        d[buyer_id] += [good_id]
                        add_goods_to_buyer(conn, buyer_id, good_id, random.randint(1, 20))
                        break
            else:
                d[buyer_id] += [good_id]
                add_goods_to_buyer(conn, buyer_id, good_id, random.randint(1, 20))

# print(get_manufacturer(conn, 2, 10.0))
get_buyers(conn)
get_popular_goods(conn)
get_manufacturer_sales(conn)
