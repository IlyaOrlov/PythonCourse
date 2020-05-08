import collections
from sqlalchemy import create_engine, Column, Integer, String,  ForeignKey
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


class Association(Base):
    __tablename__ = 'association'
    id = Column(Integer, primary_key=True)
    customer_id = Column(Integer, ForeignKey('customer.id'))
    product_id = Column(Integer, ForeignKey('product.id'))

    def __repr__(self):
        return f'Customer_id: {self.customer_id}. Product_id: {self.product_id}'


class Product(Base):
    __tablename__ = 'product'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    price = Column(Integer)
    manufacturer_id = Column(Integer, ForeignKey('manufacturer.id'))
    manufacturer = relationship("Manufacturer", back_populates="products")
    customers = relationship(
        "Customer",
        secondary='association',
        back_populates="products")

    def __repr__(self):
        return f'Product: {self.name}. Price: {self.price}'


class Customer(Base):
    __tablename__ = 'customer'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    products = relationship(
        "Product",
        secondary='association',
        back_populates="customers")

    def __repr__(self):
        return f'Name customer: {self.name}'


Base.metadata.create_all(engine)

print(CreateTable(Manufacturer.__table__).compile(engine))
print(CreateTable(Product.__table__).compile(engine))
print(CreateTable(Customer.__table__).compile(engine))
print(CreateTable(Association.__table__).compile(engine))

Session = sessionmaker(bind=engine)
session = Session()

session.add_all([
    Manufacturer(brand='Sony'),
    Manufacturer(brand='Samsung'),
    Manufacturer(brand='Apple'),
    Manufacturer(brand='LG')])

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
    Product(name='apple laptop', price=50, manufacturer_id=3),
    Product(name='LG TV', price=17, manufacturer_id=3),
    Product(name='LG smartphone', price=30, manufacturer_id=3),
    Product(name='LG laptop', price=50, manufacturer_id=3)])

session.commit()

session.add_all([
    Customer(name='Fred'),
    Customer(name='Alex'),
    Customer(name='Tom'),
    Customer(name='Jack'),
    Customer(name='Ivan')])

session.commit()

session.add_all([
    Association(customer_id=1, product_id=5),
    Association(customer_id=2, product_id=4),
    Association(customer_id=3, product_id=1),
    Association(customer_id=4, product_id=1),
    Association(customer_id=1, product_id=2),
    Association(customer_id=2, product_id=5),
    Association(customer_id=3, product_id=9),
    Association(customer_id=4, product_id=5)])

session.commit()

c = collections.Counter()
for item in session.query(Product).filter(Product.price < 10):
    c[item.manufacturer_id] += 1
for brand_id, values in c.items():
    if values > 2:
        for item in session.query(Manufacturer).filter(Manufacturer.id == brand_id):
            brand = item.brand
            print(f'{brand} has {values} products cheaper than 10')

lst = []
for item in session.query(Association):
    lst.append(item)

d = dict()
for i in lst:
    for item in session.query(Product).filter(Product.id == i.product_id):
        brand = item.manufacturer_id
        if brand not in d:
            d[brand] = list()

for i in lst:
    for item in session.query(Product).filter(Product.id == i.product_id):
        brand = item.manufacturer_id
        if i.customer_id not in d[brand]:
            d[brand].append(i.customer_id)

for brand_id, customers in d.items():
    for item in session.query(Manufacturer).filter(Manufacturer.id == int(brand_id)):
        brand = item.brand
    names_customers = []
    for id in customers:
        for item in session.query(Customer).filter(Customer.id == id):
            name = item.name
            names_customers.append(name)
    print(f'Brand: {brand}. Customers: {" ".join(names_customers)}')

product_counter = collections.Counter()
for item in session.query(Association):
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

brands = []
for product_id in product_counter.keys():
    for product in session.query(Product).filter(Product.id == int(product_id)):
        if product.manufacturer_id not in brands:
            brands.append(product.manufacturer_id)

for i in brands:
    for item in session.query(Manufacturer).filter(Manufacturer.id == i):
        brand = item.brand
        brand_id = item.id
        print(f'{brand}:')
        for product_id, values in product_counter.items():
            for product in session.query(Product).filter(Product.id == int(product_id)):
                if product.manufacturer_id == brand_id:
                    product_name = product.name
                    profit = product.price * values
                    print(f'{product_name}: profit {profit}')

for item in session.query(Manufacturer):
    if item.id not in brands:
        print(f'{item.brand} profit 0')