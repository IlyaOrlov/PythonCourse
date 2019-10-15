from random import randint, choice
import pickle


class Human:
    def __init__(self, name, surname, age, height, weight, zip_code, nationality, phone_number):
        self.name = name
        self.surname = surname
        self.age = age
        self.height = height
        self.weight = weight
        self.zip_code = zip_code
        self.nationality = nationality
        self.phone_number = phone_number

    def __repr__(self):
        return '{} {}\nage: {}\nheight: {}\nweight: {}\nzip_code: {}\nnationality: ' \
               '{}\nphone number: {}\n'.format(self.name, self.surname, self.age,
                                               self.height, self.weight, self.zip_code,
                                               self.nationality, self.phone_number)


def creat_human(count):
    name = ['Alex', 'Sergey', 'Petr', 'Anna',
            'Nikolay', 'Victor', 'Viktoria',
            'Jack', 'Iliya', 'Julia', 'Avgust',
            'Mikhail', 'Jain', 'Bob', 'Erica',
            'Nikanor', 'Socrat', 'Valeria']
    surname = ['Ivanov', 'Petrov', 'Sidorov',
               'Abramov', 'Nikanov', 'Buhalov',
               'Samsonov', 'Baranov', 'Krivonosov',
               'Lomonosov', 'Mendeleev', 'Pushkin',
               'Romanov', 'Vinokurov', 'Putin',
               'Medvedev', 'Navalniy', 'Sechin']
    nationality = ['British', 'Scottish', 'Danish',
                   'Finnish', 'Swedish', 'Estonian',
                   'Latvian', 'Lithuanian', 'Russian',
                   'Belarusian', 'Ukrainian', 'Indian']

    for _ in range(count):
        human = Human(choice(name), choice(surname), randint(18, 90),
                      randint(145, 225), randint(50, 150), randint(100000, 999999),
                      choice(nationality), randint(79010000000, 79999999999))
        yield human
        p = pickle.dumps(human, protocol=pickle.HIGHEST_PROTOCOL)
        with open('human.data', 'ab') as f:
            f.write(p)


def read_human(file_name):
    with open(file_name, 'rb') as f:
        try:
            while True:
                yield pickle.load(f)
        except EOFError:
            pass


for i in creat_human(10):
    print(i)
for i in read_human('human.data'):
    print(i)
