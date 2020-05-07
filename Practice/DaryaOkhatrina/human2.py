import pickle
import random

class Human:
    name1 = ['Ann', 'Olga', 'Dasha', 'Masha', 'Sasha']
    last_name1 = ['Petrova', 'Ivanova', 'Sidorova', 'Smirnova', 'Avdeeva ']
    age1 = [10, 15, 20, 30, 35]
    salary1 = [25000, 35000, 50000, 10000, 150000]

    def __init__(self, name, last_name, age, salary ):
        self.name = name
        self.last_name =last_name
        self.age = age
        self.salary = salary

    def __repr__(self):
        return f"Human: name = {self.name}, last_name = {self.last_name}, age = {self.age}, salary = {self.salary} "

    @classmethod
    def fabric(cls, num):
        humans = []
        for i in range(num):
            humans.append(Human(random.choice(cls.name1), random.choice(cls.last_name1), random.choice(cls.age1),
                                random.choice(cls.salary1)))
        return humans


    @staticmethod
    def serialize(humans):
        with open("Human.data1", 'wb') as f:
            pickle.dump(humans, f)




    @staticmethod
    def deserialize():
        with open('Human.data1', 'rb') as f:
            humans = pickle.load(f)
            return humans

h = Human.fabric(5)
Human.serialize(h)
print(Human.deserialize())
