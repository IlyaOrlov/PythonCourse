# Подключаемся к базе MongoDB на локальной машине
import mongoengine as me

conn = me.connect('test')
print(conn)


# Объявляем коллекцию
class User(me.Document):
    email = me.StringField(required=True)
    first_name = me.StringField(max_length=50)
    last_name = me.StringField(max_length=50)

    def __repr__(self):
        return ("<User(first_name='{}'), "
                "last_name='{}', "
                "email='{}')>".format(self.first_name,
                                      self.last_name,
                                      self.email))

# Создаем документ
ross = User(email='ross@example.com',
            first_name='Ross',
            last_name='Lawley')
ross.save()
print('Документов в базе: {}'.format(User.objects.count()))

# Делаем запрос
for i in range(5):
    User(email='test@example.com',
         first_name='User'+str(i),
         last_name='Test').save()
print(User.objects.filter(first_name='User3'))
# Двойное нижнее подчеркивание используется для
# задания регулярного выражения
print(User.objects.filter(first_name__startswith='User'))

# Удаляем запись в базе данных
User.objects(first_name__startswith='User').delete()
print('Документов в базе: {}'.format(User.objects.count()))

# Удаляем все записи в базе данных
User.objects.delete()