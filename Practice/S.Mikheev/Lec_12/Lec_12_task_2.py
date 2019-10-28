from sqlalchemy import create_engine, PrimaryKeyConstraint, func, or_
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String
from sqlalchemy.schema import CreateTable
from sqlalchemy.orm import sessionmaker
import random
import os

db_name = 'Shoppingcenter.db'
engine = create_engine('sqlite:///' + db_name)
db_exists = os.path.exists(db_name)

Base = declarative_base()


class Buyer(Base):
    __tablename__ = 'Buyers'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String)
    balance = Column(Integer)
    login = Column(String)
    password = Column(String)

    def __repr__(self):
        return "<Buyer(name='{}', balance='{}', login='{}', password='{}')>".format(
            self.name, self.balance, self.login, self.password)


class Good(Base):
    __tablename__ = 'Goods'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String)
    manufacturer = Column(String)
    price = Column(Integer)
    quantity = Column(Integer)

    def __repr__(self):
        return "<Good(name='{}', manufacturer='{}', price='{}', quantity='{}')>".format(
            self.name, self.manufacturer, self.price, self.quantity)


class BuyersGoods(Base):
    __tablename__ = 'BuyersGoods'
    __table_args__ = (
        PrimaryKeyConstraint('BuyerID', 'GoodID'),)
    BuyerID = Column(Integer)
    GoodID = Column(Integer)
    quantity = Column(Integer)

    def __repr__(self):
        return "<BuyersGoods(BuyerID='{}', GoodID='{}', quantity='{}')>".format(
            self.BuyerID, self.GoodID, self.quantity)


if not db_exists:
    Base.metadata.create_all(engine)
    print(CreateTable(Buyer.__table__).compile(engine))
    print('Таблица Buyer создана')
    print(CreateTable(Good.__table__).compile(engine))
    print('Таблица Good создана')
    print(CreateTable(BuyersGoods.__table__).compile(engine))
    print('Таблица BuyersGoods создана')

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
    Session = sessionmaker(bind=engine)
    session = Session()
    for i in range(10):
        name_user = random.choice(name)
        surname_user = random.choice(surname)
        user = '{} {}'.format(name_user, surname_user)
        balance = random.randint(100, 1000)
        login = '{}.{}'.format(name_user[0], surname_user)
        pswd = '{}{}'.format(surname_user, random.randint(12345, 54321))
        # Добавляем новый объект в базу
        session.add(Buyer(name=user, balance=balance, login=login, password=pswd))
        session.commit()
        print('Покупатель {} добавлен в базу данных'.format(user))
    for good in goods:
        session.add(Good(name=good,
                         manufacturer=random.choice(manufactures),
                         price=random.randint(1, 100),
                         quantity=random.randint(1, 30)))
        session.commit()
    d = {}
    for i in range(15):
        buyer_id = random.randint(1, 10)
        good_id = random.randint(1, 20)
        if buyer_id not in d:
            d[buyer_id] = [good_id]
            session.add(BuyersGoods(BuyerID=buyer_id,
                                    GoodID=good_id,
                                    quantity=random.randint(1, 20)))
            print('Добавлена новая запись в таблицу BuyersGoods')
            session.commit()
        else:
            if good_id in d[buyer_id]:
                while good_id in d[buyer_id]:
                    good_id = random.randint(1, 20)
                    if good_id not in d[buyer_id]:
                        d[buyer_id] += [good_id]
                        session.add(BuyersGoods(BuyerID=buyer_id,
                                                GoodID=good_id,
                                                quantity=random.randint(1, 20)))
                        print('Добавлена новая запись в таблицу BuyersGoods')
                        session.commit()
                        break
            else:
                d[buyer_id] += [good_id]
                session.add(BuyersGoods(BuyerID=buyer_id,
                                        GoodID=good_id,
                                        quantity=random.randint(1, 20)))
                print('Добавлена новая запись в таблицу BuyersGoods')
                session.commit()

# Получение списка производителей товаров по определенным параметрам
def get_manufacturer(engine, count, price):
    Session = sessionmaker(bind=engine)
    session = Session()
    print('Список производителей, у которых не менее {} товаров по цене {} долларов и ниже:'.format(count, price))
    for manufacturer, count_goods in session.query(Good.manufacturer, func.count(Good.manufacturer)).filter(
            Good.price <= price).group_by(Good.manufacturer):
        if count_goods >= count:
            print('Производитель {} имеет {} товара(ов) по цене 10 долларов и ниже'.format(manufacturer, count_goods))


# Получение списка покупателей, сделавших заказы
def get_buyers(engine):
    Session = sessionmaker(bind=engine)
    session = Session()
    print("Информация о покупателях, которые делали заказы, "
          "сгруппированных по компаниям производителей чьи товары покупались:")
    for manufacturer, id, name, login in session.query(Good.manufacturer, Buyer.id, Buyer.name, Buyer.login).filter(
            Buyer.id == BuyersGoods.BuyerID).filter(BuyersGoods.GoodID == Good.id).group_by(Good.manufacturer,
                                                                                            Buyer.id):
        print('Производитель: {} => Покупатель: ID: {}, Имя: {}, login: {}'.format(manufacturer, id, name, login))


# Получение списка популярных товаров
def get_popular_goods(engine):
    Session = sessionmaker(bind=engine)
    session = Session()
    print("Список самых популярных товаров у каждого производителя с указанием количества проданных товаров:")
    for manufacturer, id in session.query(Good.manufacturer, Good.id).group_by(Good.manufacturer):
        result = session.query(Good.manufacturer, Good.id, Good.name, Good.price, BuyersGoods.quantity).filter(
            Buyer.id == BuyersGoods.BuyerID).filter(BuyersGoods.GoodID == Good.id).filter(
            Good.manufacturer == manufacturer).order_by(BuyersGoods.quantity.desc()).all()[0]
        print('Производитель: {} => Товар: ID: {}, Наименование: {}, цена: {}, количество проданных: {}'.
              format(result[0], result[1], result[2], result[3], result[4]))


# Получение списка производителей товаров, которые продавались, с указанием их выручек по каждому виду товара
def get_manufacturer_sales(engine):
    Session = sessionmaker(bind=engine)
    session = Session()
    print("Список производителей товаров, которые продавались, с указанием их выручек по каждому виду товара:")
    for manufacturer, id, name, sales in session.query(Good.manufacturer, Good.id, Good.name,
                                                       BuyersGoods.quantity * Good.price).filter(
        Good.id == BuyersGoods.GoodID).group_by(Good.manufacturer, Good.id).order_by(Good.id):
        print('Производитель: {} => Товар: ID: {}, Наименование: {}, выручка: {}'.format(manufacturer, id, name, sales))
    print("Список производителей товаров, которые еще не продавались:")
    for manufacturer, id, name in session.query(Good.manufacturer, Good.id, Good.name).filter(
            ~Good.id.in_(session.query(BuyersGoods.GoodID))).group_by(Good.manufacturer, Good.id):
        print('Производитель: {} => Товар: ID: {}, Наименование: {}, выручка: 0'.format(manufacturer, id, name))


get_manufacturer(engine, 2, 10)
print()
get_buyers(engine)
print()
get_popular_goods(engine)
print()
get_manufacturer_sales(engine)
