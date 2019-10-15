from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String
from sqlalchemy.schema import CreateTable
from sqlalchemy.orm import sessionmaker


Base = declarative_base()

# Создаем базу данных в памяти (без файла)
engine = create_engine('sqlite://')
print('База данных создана')

# Создаем класс, отображающий таблицу
class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    fullname = Column(String)
    password = Column(String)

    def __repr__(self):
        return "<User(name='{}', fullname='{}', password='{}')>".format(
                self.name, self.fullname, self.password)

# Создаем схему
Base.metadata.create_all(engine)
print(CreateTable(User.__table__).compile(engine))
print('Таблица создана')

# Создаем объект отображаемого класса
ed_user = User(name='ed', fullname='Ed jones', password='edpassword')

# Открываем сессию
Session = sessionmaker(bind=engine)
session = Session()
print('Сессия открыта')

# Добавляем новый объект в базу
session.add(ed_user)
session.commit()
print('Объект добавлен')

# Проверяем, что получилось
print(session.query(User).filter_by(name='ed').first())

# Добавляем несколько объектов в базу
session.add_all([
    User(name='wendy', fullname='Wendy Williams', password='pwd'),
    User(name='mary', fullname='Mary Contrary', password='qwerty'),
    User(name='fred', fullname='Fred Flinstone', password='123')])
session.commit()
print('Объекты добавлены')

# Проверяем, что получилось
print('Объектов User в базе: {}'.format(session.query(User).count()))
print(session.query(User).all())

# Изменяем запись
ed = session.query(User).filter_by(name='ed').first()
ed.password = 'edsnewpassword'
session.add(ed)
session.commit()

# Проверяем, что получилось
#print(session.query(User).filter_by(name='ed').first())
print('Объектов User в базе: {}'.format(session.query(User).count()))
print(session.query(User).all())

# Удаляем запись
session.delete(ed)
session.commit()

# Проверяем, что получилось
print('Объектов User в базе: {}'.format(session.query(User).count()))
print(session.query(User).all())
