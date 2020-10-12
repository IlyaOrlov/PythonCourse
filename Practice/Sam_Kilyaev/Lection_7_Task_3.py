import random
import pickle


class Human:
    def __init__(self, first_name, second_name, age, was_born, city, pet, name_pet):
        self.first_name = first_name
        self.second_name = second_name
        self.age = age
        self.was_born = was_born
        self.city = city
        self.pet = pet
        self.name_pet = name_pet

    def __str__(self):
        return f"{self.first_name}, {self.second_name}, {self.age}, {self.was_born}, {self.city}, {self.pet}, {self.name_pet}"


def make_human_and_serialization(quantity):
    first_name = ['Batman', 'Spider-man', 'Daredevil', 'Hulk', 'Superman', 'Starlord', 'Wonder Woman', 'Iron Fist']
    second_name = ['Brus Wayne', 'Peter Parker', 'Matt Murdok', 'Brus Banner', 'Clark Kent', 'Peter Quill', 'Diana',
                   'Danny']
    age = [33, 25, 31, 40, 36, 29, 1126, 22]
    was_born = ['Gotham', 'New York', 'Hell Kitchen', 'USA', 'Krypton', 'Texas', 'Temeskira', 'Chinatown']
    city = ['London', 'Dzerginsk', 'Los Angeles', 'Monreal', 'Stambul', 'Rome', 'Paris']
    pet = ['cat', 'dog', 'spider', 'bird']
    name_pet = ['Bill', 'Ted', 'Robin', 'Ben', 'Marta', 'Doctor Doom']
    human = []
    for i in range(quantity):
        human.append(
            Human(random.choice(first_name), random.choice(second_name), random.choice(age), random.choice(was_born),
                  random.choice(city), random.choice(pet), random.choice(name_pet)))
    with open('human.data', 'wb') as h:
        pickle.dump(human, h)
    return 'Ready'


def unserialization(file):
    with open(file, 'rb') as f:
        new_data = pickle.load(f)
        for i in new_data:
            print(i)
    return new_data


print(make_human_and_serialization(10))
print(unserialization('human.data'))
