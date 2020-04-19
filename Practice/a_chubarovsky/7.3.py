import pickle
import random as rdm


class Human:
    def __init__(self, first_name, last_name, age, height, weight, eye_colour, religion):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.height = height
        self.weight = weight
        self.eye_colour = eye_colour
        self.religion = religion

    def __str__(self):
        return f"Human: first_name={self.first_name}, last_name={self.last_name}, age={self.age}, height={self.height}," \
               f" weight={self.weight}, eye_colour={self.eye_colour}, religion={self.religion}"


def people_maker(peop_numb):
    first_names = ['Max', 'Jillian', 'John', 'Scarlett', 'David', 'Hugo', 'Steve', 'Hanna']
    last_names = ['Fisher', 'Light', 'Jonhson', 'Smith', 'Williams', 'Anderson', 'Brown', 'Davis']
    eye_colours = ['Blue', 'Green', 'Brown', 'Grey', 'Amber']
    religions = ['Christianity', 'Islam', 'Hinduism', 'Buddhism', 'Judaism', 'Spiritualism', 'Zoroastrianism']
    people = []
    if peop_numb > 0:
        for element in range(peop_numb):
            people.append(Human(rdm.choice(first_names), rdm.choice(last_names), rdm.randint(18, 100), rdm.randint(150, 200),
                                rdm.randint(45, 120), rdm.choice(eye_colours), rdm.choice(religions)))
        with open('human.data', 'wb') as f_ser:
            i = 0
            while i < peop_numb:
                pickle.dump(people[i], f_ser, protocol=pickle.HIGHEST_PROTOCOL)
                i += 1
    else:
        print('There are no people here.')
    return people


def unpack(file_name, persons):
    with open(file_name, 'rb') as f_deser:
        for person in persons:
            person = pickle.load(f_deser)
            print(f'{person}')


if __name__ == '__main__':
    pers = people_maker(5)
    unpack('human.data', pers)
