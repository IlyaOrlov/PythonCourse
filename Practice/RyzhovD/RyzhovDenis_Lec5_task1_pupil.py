"""
This file create the class Man, which instance is always not ready yet,
and subclass Pupil where think from 3 to 6 second.
Changes: definitions of class instances with brackets
and addition 'name' as an attribute (It looks better, in my opinion).
It allows me to practise with the construction ' {} ..format('') ',
that is really more convenient than the concatenation with '+'.
"""

from random import randint
from time import sleep

class Man:
    def __init__(self, name):
        self.name = name

    def solve_task(self, name):
        print('{} says: I\'m not ready yet.'.format(self.name))

captain = Man('Captain')
captain.solve_task(captain.name)
print('')


class Pupil(Man):

    def solve_task(self, name):
        tau = randint(3, 6)
        print('{} starts to think...'.format(self.name))
        sleep(tau)
        print('And now he says: I\'ve thought for ' + str(tau) + ' seconds.'
                                                ' And I don\'t know.')

rookie = Pupil('Rookie')
rookie.solve_task(rookie.name)