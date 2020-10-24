import pickle, random


class Human:
    def __init__(self, name, secondname, age, adress):
        self.name = name
        self.secondname = secondname
        self.age = age
        self.adress = adress

    def __str__(self):
        return "{} {}, age - {}, adress - {}".format(self.name, self.secondname, self.age, self.adress)


def createHuman(numberHuman):
    humans = []
    names = ['Human1', 'Human2', 'Human3', 'Human4', 'Human5']
    secondnames = ['SecNames1', 'SecNames2', 'SecNames3', 'SecNames4', 'SecNames5']
    adress = ['Nizhniy Novgorod', 'Moscow', 'Saint Petersburg', 'Kazan', 'Sarov']
    for i in range(numberHuman):
        human = Human(random.choice(names), random.choice(secondnames),
                      random.randint(5, 30), random.choice(adress))
        humans.append(human)
    with open('human.data', 'wb') as f:
        for human in humans:
            pickle.dump(human, f, protocol=pickle.HIGHEST_PROTOCOL)

def deserializePeople(fileName, number):
    with open(fileName, 'rb') as f:
        humans = []
        for i in range(number):
            humans.append(pickle.load(f))
    return humans

createHuman(5)
humans = deserializePeople('human.data',5)
for human in humans:
    print(human)