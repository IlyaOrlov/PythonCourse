import random
import pickle


class Human:
    item = []

    def __init__(self, fname, lname, age, height, weight):
        self.fname = fname
        self.lname = lname
        self.age = age
        self.height = height
        self.weight = weight
        Human.item.append(self)

    @classmethod
    def from_dict(cls, d):
        fname, lname, age, height, weight = d.get('fname'), d.get('lname'), d.get('age'), d.get('height'), d.get(
            'weight')
        return cls(fname, lname, age, height, weight)


def serialize(N):
    fname_list = ['Petr', 'Bano', 'David', 'John', 'Ashley', 'Eden', 'Frank', 'Michael', 'Arjen', 'Didier', 'Nicolas']
    lname_list = ['Cech', 'Ivanovic', 'Luiz', 'Terry', 'Cole', 'Hazar', 'Lampard', 'Balack', 'Robben', 'Drogba',
                  'Anelca']

    for i in range(N):
        with open(r'C:\Temp\human.data', 'w+b') as f:
            person = {}
            person['fname'] = random.choice(fname_list)
            person['lname'] = random.choice(lname_list)
            person['age'] = random.randint(17, 40)
            person['height'] = random.randint(160, 200)
            person['weight'] = random.randint(60, 100)
            human = Human.from_dict(person)
            pickle.dump(human, f)


def deserialize():
    with open(r'C:\Temp\human.data', 'rb') as f:
        human = pickle.load(f)
        for i in range(len(human.item)):
            print(
                f'{human.item[i].fname} {human.item[i].lname}, возраст - {human.item[i].age}, '
                f'рост - {human.item[i].height}, вес - {human.item[i].weight} ')


serialize(5)
deserialize()
