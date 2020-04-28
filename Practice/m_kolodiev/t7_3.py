import random
import pickle


class Human:

    def __init__(self):
        self.names = ['Jonathan', 'Arthur', "Jeremiah", 'Annie', 'Archibald', 'Elizabeth']
        self.surnames = ['Davies', 'Wright', "Matthews", 'Webb', 'Baker', 'Grant']
        self.locations = ['Nashville', 'San Diego', 'Austin', 'Colorado Springs', 'New Orleans', 'Oakland']
        self.name = random.choice(self.names)
        self.surname = random.choice(self.surnames)
        self.location = random.choice(self.locations)
        self.age = random.randint(18, 70)
        self.phone = random.randint(10000000000, 19999999999)

        print(f"{self.name} {self.surname} is {self.age}, phone number: {self.phone}. Last seen in {self.location}")

    def repr(self):
        print(f"\n{self.name} {self.surname}\nAge: {self.age}\nPhone number: {self.phone}\nLocation: {self.location}")


def serialize(number):
    people = []
    for i in range(number):
        person = Human()
        people.append(person)
    with open("human.data", "wb") as file:
        pickle.dump(people, file)


def deserialize():
    with open("human.data", "rb") as file:
        data = pickle.load(file)
    for man in data:
        print(f"\nName: {man.name} {man.surname}\nAge: {man.age}\nPhone number: {man.phone}\nLocation: {man.location}")


serialize(5)
deserialize()
