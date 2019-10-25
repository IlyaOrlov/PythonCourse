import pickle
import random

class Human:
    def __init__(self, name, surname, age, height, profess):
        self.name = name
        self.surname = surname
        self.age = age
        self.height = height
        self.profess = profess

    def __repr__(self):
        return f'{self.name}, {self.surname} , {self.age} лет,рост:{self.height}  профессия: {self.profess}'

name = ['Aaron','Abraham','Adam','Adrian','Aidan','Alan','Albert','Alejandro','Alex','Alexander','Alfred',
        'Andrew','Angel','Anthony','Antonio','Ashton','Austin']
surname = ['Chapman','Davidson','Dodson','Duncan','Edwards','Elmers','Finch','Fleming','Ford']
profess = ['Doctor','Lawyer','Animator','Actor','Businessman','BrokerWeb','designer','Guide']

def add_human(count):
    humans = list()
    for i in range(count):
        humans.append(
            Human(random.choice(name), random.choice(surname), random.randint(18,60), random.randint(160,210),
                  random.choice(profess)))

    with open('human.data', 'wb') as f:
        pickle.dump(humans, f)
    return humans


def read_human(file):
    with open(file, 'rb') as f:
        return pickle.load(f)


for a in add_human(5):
    print(a)
print('--------------Transporting and return:--------------------')
for b in read_human('human.data'):
    print(b)
