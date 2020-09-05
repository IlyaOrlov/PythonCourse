import random, pickle


class Human:
    def __init__(self, name, surname, age, weight, living_place):
        self.name = name
        self.surname = surname
        self.age = age
        self.weight = weight
        self.living_place = living_place

    def __str__(self):
        return "{} {}, age - {}, weight - {}, living place - {}". \
            format(self.name, self.surname, self.age, self.weight, self.living_place)


def create_people(people_number):
    if people_number <= 0:
        return None
    names = ['Ann', 'Andrew', 'Peter', 'Sam', 'Alice']
    surnames = ['Scott', 'Thomson', 'Robertson', 'Richardson', 'Oswald']
    living_places = ['Chicago', 'San Diego', 'Seattle', 'Denver', 'Washington']
    people = []

    for i in range(people_number):
        human = Human(random.choice(names), random.choice(surnames), random.randint(15, 70),
                      random.randint(50, 80), random.choice(living_places))
        people.append(human)
    serialize_people(people)
    return people


def serialize_people(people):
    with open('human.data', 'wb') as f:
        for human in people:
            pickle.dump(human, f, protocol=pickle.HIGHEST_PROTOCOL)


def deserialize_people(file_name, number):
    with open(file_name, 'rb') as f:
        people = []
        for i in range(number):
            people.append(pickle.load(f))
    return people


create_people(5)
people = deserialize_people('human.data', 5)
for human in people:
    print(human)
