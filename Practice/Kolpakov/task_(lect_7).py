from datetime import date, timedelta
from subprocess import Popen, PIPE



#Num_1
# Написать функцию для подсчета количества рабочих дней между двумя
# датами (даты передаются в качестве параметров).

def work_day(from_date, to_date):
    b = []
    t = 0
    for x in range((to_date - from_date).days + 1):
        d = from_date + timedelta(x)
        b.append(d)

    for day in b:
        if day.weekday() < 5:
            t += 1
    return t


print(work_day(date(2018, 9, 23), date(2019, 9, 29)))
print()
print('---------------------------')


#Num 2
#С помощью библиотеки subprocess прочитать содержимое
#произвольного файла с использованием утилиты cat в Linux или type в
#Windows (имя файла должно передаваться как параметр в вашу
#функцию).

def read(file_name):
    proc = Popen(['cat', file_name], stdout=PIPE, stderr=PIPE)
    proc.wait() # дождаться выполнения
    res = proc.communicate() # получить tuple('stdout', 'stderr')
    if proc.returncode:
        return res[1]
    return 'result:', res[0]

print(read('./file.txt'))
print()
print('---------------------------')

#Num 3
# Создать класс Human с 5-10 атрибутами (имя, фамилия, возраст, меcто
# жительства и т.д.)
import random
import pickle
class Human:
    def __init__(self, name, age, location, profession, hobby):
        self.name = name
        self.age = age
        self.location = location
        self.profession = profession
        self.hobby = hobby

    def __repr__(self):
        return f'{self.name}, {self.age} лет, страна рождения: {self.location}, профессия: {self.profession}, мое хобби: {self.hobby}\n'

name = ['Иннокентий', 'Фадей', 'Лада', 'Арсения', 'Владилен' , 'Аврор', 'Ипатия', 'Октябрина', 'Джозеф', 'Бенедикт']
location = ['Россия', 'Беларусь', 'Греция', 'Словения', 'Мальдивы' , 'Куба', 'Вьетнам', 'Китай', 'Испания', 'Хорватия']
profession = ['Хирург', 'Пилот', 'Исследователь', 'Космонавт', 'Продюсер', 'Биохимик', 'Частный детектив', 'Археолог', 'Дипломат', 'Кондитер', 'Корреспондент']
hobby = ['Охота', 'Охота', 'Ролевые игры', 'Пейнтбол', 'Садоводство', 'Кулинария', 'Коллекционирование', 'Компьютерные игры', 'Чтение', 'фотография']


def new_person(kol):
    humans = list()
    for i in range(kol):
        humans.append(Human(random.choice(name), random.randint(20,65), random.choice(location), random.choice(profession), random.choice(hobby)))
    yield humans
    with open('human.data', 'wb') as f:
        pickle.dump(humans, f)

def read_new_person(file):
    with open(file, 'rb') as f:
        yield pickle.load(f)


for k in new_person(7):
    print(k)
print('*********')
for j in read_new_person('human.data'):
    print(j)