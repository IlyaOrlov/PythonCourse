# Создать класс Human с 5-10 атрибутами (имя, фамилия, возраст, меcто жительства и т.д.).
# Написать функцию, которая создавала бы указанное количество экземпляров, сериализовывала их и сохраняла в файл
# human.data, и другую функцию, которая бы читала файл human.data,десериализовывала его содержимое и выводила результат
# на печать.
# Примечание: чтобы у экземпляров Human были разные значения атрибутов, можно воспользоваться функциями random.randint() и
# random.choice()

import random
from random import randrange
import pickle

class Human():
    def __init__(self, fName, lName, age, residence, phone):
        self.name, self.surname, self.age, self.residence, self.phone = fName, lName, age, residence, phone

def exemplar(num):
    fName = ["Ivan", "Boris", "Arkadiy", "Roman", "Sergey", "Dmitriy", "Petr"]
    lName = ["Petrov", "Ivanov", "Romanov", "Borisov", "Sergeev", "Dmitriev", "Arkadiev"]
    residence = ["Samara", "Kirov", "Rostov", "Moscow", "Saratov"]

    humans = []
    for i in range(num):
        h = Human(random.choice(fName), random.choice(lName), randrange(25, 55), random.choice(residence), randrange(4281010, 4701010) )
        humans.append(h)
    with open('human.data', 'wb') as f:
        pickle.dump(humans, f)

def ret_exemplar(file):
    with open(file, 'rb') as f:
        data_ex = pickle.load(f)
        for ex in data_ex:
            print(f"Name: {ex.name}, Surname: {ex.surname}, Age: {ex.age}, Residence: {ex.residence}, Phone number: {ex.phone}")
        return data_ex

exemplar(4)
ret_exemplar('human.data')
