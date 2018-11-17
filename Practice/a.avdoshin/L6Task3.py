import pickle
from random import randint
import os


class Human:
    def __init__(self, pr0, pr1, pr2, pr3, pr4, pr5, pr6, pr7, pr8, pr9):
        self.pr0, self.pr1, self.pr2, self.pr3, \
        self.pr4, self.pr5, self.pr6, self.pr7, \
        self.pr8, self.pr9 = pr0, pr1, pr2, pr3, \
                             pr4, pr5, pr6, pr7, pr8, pr9

    def __str__(self):
        return str(self.pr0) + ' ' + str(self.pr1) + ' ' + str(self.pr2) + ' ' + str(self.pr3) + ' ' + \
               str(self.pr4) + ' ' + str(self.pr5) + ' ' + str(self.pr6) + ' ' + str(self.pr7) + ' ' + \
               str(self.pr8) + ' ' + str(self.pr9)


temp_file = 'temp.tmp'


def maternity_hospital(numh):
    people = []
    for i in range(numh):
        props = []
        for i in range(10):
            props.append(randint(0, 100))
        people.append(Human(*props))
    print('Saved people:')
    for persan in people:
        print(persan)
    with open(temp_file, 'wb') as f:
        pickle.dump(people, f)


def load_people():
    with open(temp_file, 'rb') as f:
        g = pickle.load(f)
    print('\nLoaded people:')
    for i in g:
        print(i)


maternity_hospital(3)
load_people()
os.remove(temp_file)
