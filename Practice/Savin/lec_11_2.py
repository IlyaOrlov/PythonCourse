import collections
from sqlalchemy import create_engine, Column, Integer, String, Table, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy.schema import CreateTable


engine = create_engine("sqlite://")
conn = engine.connect()

Base = declarative_base()


class Manufacturer(Base):
    __tablename__ = 'manufacturer'
    id = Column(Integer, primary_key=True)
    brand = Column(String)
    products = relationship("Product", back_populates="manufacturer")

    def __repr__(self):
        return f'Manufacturer: {self.brand}'


association_table = Table('association', Base.metadata,
    Column('customer_id', Integer, ForeignKey('customer.id')),
    Column('product_id', Integer, ForeignKey('product.id')))


class Product(Base):
    __tablename__ = 'product'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    price = Column(Integer)
    manufacturer_id = Column(Integer, ForeignKey('manufacturer.id'))
    manufacturer = relationship("Manufacturer", back_populates="products")
    customers = relationship(
        "Customer",
        secondary=association_table,
        back_populates="products")

    def __repr__(self):
        return f'Product: {self.name}. Price: {self.price}'


class Customer(Base):
    __tablename__ = 'customer'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    products = relationship(
        "Product",
        secondary=association_table,
        back_populates="customers")

    def __repr__(self):
        return f'Name customer: {self.name}'


Base.metadata.create_all(engine)

print(CreateTable(Manufacturer.__table__).compile(engine))
print(CreateTable(Product.__table__).compile(engine))
print(CreateTable(Customer.__table__).compile(engine))
print(CreateTable(association_table).compile(engine))

Session = sessionmaker(bind=engine)
session = Session()

session.add_all([
    Manufacturer(brand='Sony'),
    Manufacturer(brand='Samsung'),
    Manufacturer(brand='Apple')])

session.commit()

session.add_all([
    Product(name='sony TV', price=9, manufacturer_id=1),
    Product(name='sony smartphone', price=5, manufacturer_id=1),
    Product(name='sony laptop', price=3, manufacturer_id=1),
    Product(name='samsung TV', price=20, manufacturer_id=2),
    Product(name='samsung smartphone', price=25, manufacturer_id=2),
    Product(name='samsung laptop', price=30, manufacturer_id=2),
    Product(name='apple TV', price=17, manufacturer_id=3),
    Product(name='apple smartphone', price=30, manufacturer_id=3),
    Product(name='apple laptop', price=50, manufacturer_id=3)])

session.commit()

session.add_all([
    Customer(name='Fred'),
    Customer(name='Alex'),
    Customer(name='Tom'),
    Customer(name='Jack'),
    Customer(name='Ivan')])

session.commit()

session.execute("INSERT INTO association "
                "VALUES (1, 5), (2, 4), (3, 1), (4, 1), (1, 2), (2, 5), (3, 9), (4, 5)")


c = collections.Counter()
for item in session.query(Product).filter(Product.price < 10):
    c[item.manufacturer_id] += 1
for i, j in c.items():
    if j > 2:
        for item in session.query(Manufacturer).filter(Manufacturer.id == i):
            brand = item.brand
            print(f'{brand} has {j} products cheaper than 10')

lst = []
for item in session.execute("SELECT * FROM association"):
    lst.append(item)

d = dict()
for i in lst:
    for item in session.query(Product).filter(Product.id == i[1]):
        brand = item.manufacturer_id
        if brand not in d:
            d[brand] = list()

for i in lst:
    for item in session.query(Product).filter(Product.id == i[1]):
        brand = item.manufacturer_id
        if i[0] not in d[brand]:
            d[brand].append(i[0])

for i, j in d.items():
    for item in session.query(Manufacturer).filter(Manufacturer.id == int(i)):
        brand = item.brand
    names_customers = []
    for id in j:
        for item in session.query(Customer).filter(Customer.id == id):
            name = item.name
            names_customers.append(name)
    print(f'Brand: {brand}. Customers: {" ".join(names_customers)}')

product_counter = collections.Counter()
for item in session.execute("SELECT * FROM association"):
    product_counter[item.product_id] += 1

top_product = {}
for product_id, c in product_counter.items():
    for item in session.query(Product).filter(Product.id == int(product_id)):
        product = item.name
        brand_id = item.manufacturer_id
    for item in session.query(Manufacturer).filter(Manufacturer.id == int(brand_id)):
        brand = item.brand
        if brand not in top_product:
            top_product[brand] = product

for brand, product in top_product.items():
    print(f'{brand}. Top product: {product}')

