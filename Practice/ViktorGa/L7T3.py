import random, pickle


class Human:
    def __init__(self, name, surname, age, iq, place):
        self.name = name
        self.surname = surname
        self.age = age
        self.iq = iq
        self.place = place

    def __str__(self):
        return "This is {} {}, age - {}, iq - {}, place - {}". \
            format(self.name, self.surname, self.age, self.iq, self.place)


def create_people(people_number):
    if people_number <= 0:
        return None
    names = ['Vova', 'Vika', 'Vera', 'Vlad', 'Vita']
    surnames = ['Dundic', 'Semih', 'Ernst', 'Pozner', 'Monday'] #surname Monday is real
    place = ['Pervomaysk', 'Big Murasino', 'Vad', 'Shatki', 'Red Baki']
    people = []

    for i in range(people_number):
        human = Human(random.choice(names), random.choice(surnames), random.randint(18, 100),
                      random.randint(70, 140), random.choice(place))
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