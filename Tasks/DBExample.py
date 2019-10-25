# Practice 6. Task 2.
# Write script usable for SQLite, MySQL, PostgreSQL, working with entities: producers, customers, goods.

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Integer, String
from sqlalchemy import Column
from sqlalchemy import ForeignKey
from sqlalchemy import UniqueConstraint
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.schema import CreateTable
from sqlalchemy import func
from random import randint


Base = declarative_base()


class Producer(Base):
    __tablename__ = 'Producers'

    id = Column(Integer, primary_key=True)
    name = Column(String)

    def __repr__(self):
        return "<Producer(id=%i, name='%s')>" % (self.id, self.name)


class Customer(Base):
    __tablename__ = 'Customers'

    id = Column(Integer, primary_key=True)
    name = Column(String)

    def __repr__(self):
        return "<Customer(id=%i, name='%s')>" % (self.id, self.name)


class Article(Base):
    __tablename__ = 'Articles'

    id = Column(Integer, primary_key=True)
    name = Column(String)

    def __repr__(self):
        return "<Article(id=%i, name='%s')>" % (self.id, self.name)


class Offer(Base):
    __tablename__ = 'Offers'

    id = Column(Integer, primary_key=True)
    article_id = Column(Integer,
                        ForeignKey('Articles.id'))
    producer_id = Column(Integer,
                         ForeignKey('Producers.id'))
    price = Column(Integer, nullable=False)
    __table_args__ = (UniqueConstraint('article_id', 'producer_id', name='uidx_art_prod'),)

    def __repr__(self):
        return  "<Offer(id=%d, article_id=%d, producer_id=%d, price=%d)>" % (
            self.id,
            self.article_id,
            self.producer_id,
            self.price
        )


class Order(Base):
    __tablename__ = 'Orders'

    id = Column(Integer, primary_key=True)
    offer_id = Column(Integer,
                      ForeignKey('Offers.id'),
                      nullable=False)
    customer_id = Column(Integer,
                         ForeignKey('Customers.id'),
                         nullable=False)
    amount = Column(Integer, nullable=False)
    price = Column(Integer, nullable=False)

    def __repr__(self):
        return "<Order(id=%d, offer_id=%d, customer_id=%d, amount=%d, price=%f)>" % (
            self.id,
            self.offer_id,
            self.customer_id,
            self.amount,
            self.price
        )


def get_engine(db_type, db_name):
    engine = None
    try:
        engine = create_engine('{}://{}'.format(db_type, db_name))
        engine.raw_connection().connection.text_factory = str
        Base.metadata.create_all(engine)
    except Exception as e:
        print "Error: cannot start engine. {}".format(e)
    return engine


def open_session(engine):
    session = None
    try:
        session = sessionmaker(bind=engine)()
    except Exception as e:
        print "Error: cannot open session. {}".format(e)
    return session


def close_session(session):
    result = True
    try:
        session.close_all()
    except Exception as e:
        print "Error: cannot close session. {}".format(e)
        result = False
    return result


def create_demo_db(engine, session):
    num_of_producers = 3
    num_of_customers = 3
    num_of_articles = 5
    num_of_offers = 7
    num_of_orders = 5

    CreateTable(Producer.__table__).compile(engine)
    for i in xrange(num_of_producers):
        session.add(Producer(name='Producer_{}'.format(i+1)))
    CreateTable(Customer.__table__).compile(engine)
    for i in xrange(num_of_customers):
        session.add(Customer(name='Customer{}'.format(i+1)))
    CreateTable(Article.__table__).compile(engine)
    for i in xrange(num_of_articles):
        session.add(Article(name='Article_{}'.format(i+1)))
    session.commit()

    CreateTable(Offer.__table__).compile(engine)
    for i in xrange(num_of_offers):
        while True:
            try:
                article_id = randint(1, num_of_articles)
                producer_id = randint(1, num_of_producers)
                session.add(Offer(article_id=article_id,
                                  producer_id=producer_id,
                                  price=randint(1,15)))
                session.commit()
                break
            # Pair of article_id and producer_id should be unique.
            except Exception as e:
                #print "Error: cannot add data to database. {}".format(e)
                session.rollback()

    CreateTable(Order.__table__).compile(engine)
    for index in xrange(num_of_orders):
        while True:
            try:
                offer_id = randint(1, num_of_offers)
                customer_id = randint(1, num_of_customers)
                session.add(Order(offer_id=offer_id,
                                  customer_id=customer_id,
                                  amount=randint(1,10),
                                  price=randint(1,15)))
                session.commit()
                break
            # offer_id and customer_id can be non-unique:
            # customer can order any article multiple times.
            except Exception as e:
                #print "Error: cannot add data to database. {}".format(e)
                session.rollback()


def get_producers(session):
    return session.query(Producer.name).\
        filter(Offer.producer_id == Producer.id).\
        filter(Offer.price <= 10).\
        group_by(Producer.id).\
        having(func.count(Offer.id) > 2).\
        all()


def get_customers(session):
    return session.query(Customer.name, Producer.name).\
        join(Order, Order.customer_id == Customer.id).\
        join(Offer, Order.offer_id == Offer.id).\
        join(Producer, Offer.producer_id == Producer.id).\
        group_by(Producer.id, Customer.id).\
        all()


def get_popular_articles(session):
    subq = session.query(Producer.id.label('producer_id'),
                         Producer.name.label('producer_name'),
                         Article.name.label('article_name'),
                         func.sum(Order.amount).label('amount')).\
        outerjoin(Offer, Offer.producer_id == Producer.id).\
        join(Order, Order.offer_id == Offer.id).\
        join(Article, Article.id == Offer.article_id).\
        group_by(Producer.id, Article.id).\
        subquery()

    return session.query(subq.c.producer_name,
                            subq.c.article_name,
                            func.max(subq.c.amount)).\
        group_by(subq.c.producer_id).\
        all()


def get_sales_info(session):
    return session.query(Producer.name,
                            Article.name,
                            func.sum(Order.amount * Order.price)).\
        outerjoin(Offer, Offer.producer_id == Producer.id).\
        outerjoin(Article, Article.id == Offer.article_id).\
        outerjoin(Order, Order.offer_id == Offer.id).\
        group_by(Producer.id, Article.id).\
        all()


def show_multi_data(headline, data):
    print headline
    for each in data:
        print each


if __name__ == "__main__":
    #new_engine = get_engine("sqlite", "/:memory:")
    new_engine = get_engine("mysql", "/:mysqldb:")
    #new_engine = get_engine("postgresql", "/:user:user@localhost/mypsdb:")
    new_session = open_session(new_engine)
    create_demo_db(new_engine, new_session)
    show_multi_data("Articles table:",
                    new_session.query(Article).all())
    show_multi_data("Producers table:",
                    new_session.query(Producer).all())
    show_multi_data("Customers table:",
                    new_session.query(Customer).all())
    show_multi_data("Offers table:",
                    new_session.query(Offer).all())
    show_multi_data("Orders table:",
                    new_session.query(Order).all())
    show_multi_data("Producers offering > 2 articles with price <= 10:",
                    get_producers(new_session))
    show_multi_data("Customers and producers:",
                    get_customers(new_session))
    show_multi_data("Popular articles:",
                    get_popular_articles(new_session))
    show_multi_data("Sales info:",
                    get_sales_info(new_session))
    close_session(new_session)
