import pickle
from random import randint as rand
from random import choice


class Human:

   def __init__(self, first_name, last_name, age, position, phone):
       self.first_name = first_name
       self.last_name = last_name
       self.age = age
       self.position = position
       self.phone = phone

   def __iter__(self):
       return iter(self)


def create_human(number):
    humans = []
    first_name = ["Noah", "Mason", "Liam", "Alex", "Jack", "Harry", "Oscar", "Jacob"]
    last_name = ["Austin", "Birch", "Carey", "Day", "Dean", "Simon", "Gate", "Taft"]
    position = ["baker", "poet", "butcher", "cook", "doctor", "engineer", "farmer", "pilot"]

    for i in range(number):
        humans.append(Human(choice(first_name), choice(last_name), rand(17, 41), choice(position), made_phone()))

    with open("human.data", "wb") as f:
        pickle.dump(humans, f)


def made_phone():   # for random phone
    phone = [rand(0, 10), rand(0, 10), rand(0, 10), "-", rand(0, 10), rand(0, 10), "-", rand(0, 10), rand(0, 10), rand(0, 10)]
    return "".join([str(x) for x in phone])


if __name__ == "__main__":
    create_human(3)
