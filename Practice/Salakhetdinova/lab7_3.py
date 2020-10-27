import random
import pickle

class Human:

    def __init__(self, first_name, last_name, age, location, profession):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.location = location
        self.profession = profession

    def __getstate__(self):
        return self.__dict__

def write_human(number):
    arr = []
    f_name = ['Pietro', 'Chiro', 'Gennaro', 'Maksim', 'Alexander']
    l_name = ['Savastano', 'Di Marzio', 'Navalny', 'Katz', 'Apolonov']
    location = ['Moscow', 'San Juan', 'Neapolis', 'Lhasa', 'Pyatigorsk']
    profession = ['farmer', 'teacher', 'dancer', 'writer', 'scientist']

    for i in range(number):
        name, last, loc, prof, = random.choice(f_name), random.choice(l_name), \
                                  random.choice(location), random.choice(profession)
        arr.append(Human(name, last, random.randint(25, 75), loc, prof))
        f_name.remove(name)
        l_name.remove(last)
        location.remove(loc)
        profession.remove(prof)

    with open("human.data", "wb") as f:
        pickle.dump(arr, f)

def print_human():
    with open("human.data", "rb") as f:
        human = pickle.load(f)
        for data in human:
            print(f'{data.first_name} {data.last_name} from {data.location}. '
                  f'Нe is {data.age} years old and his profession is a {data.profession}.')

write_human(5)
print_human()
