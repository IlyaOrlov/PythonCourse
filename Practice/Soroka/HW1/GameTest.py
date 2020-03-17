#загрузить анимацию из библиотеки командой from library import *

class Hero:
    x = 0

    def draw(self):
        print("I'm Hero at {}".format(self.x))

    def run(self):
        self.x += 1

    def shoot(self):
        print("Bang!")

    def pick_thing(self):
        print("Oh, I've found something!")


class PersBig(Hero):
    def draw(self):
        print("I'm PersBig at {} and I can fly!".format(self.x))

    def fly(self):
        print('I have flown to {}'.format(self.x+2))
        #т.е. если выбран fly, то герой передвигается на 2 шага?

class PersMid(Hero):
    def draw(self):
        print("I'm PersMid at {} and I can fly, too!".format(self.x))

    def fly(self):
        print('I have flown to {}'.format(self.x+2))

class PersJr(Hero):
    def draw(self):
        print("I'm PersJr at {}".format(self.x))

class Thing:
    def __init__(self, color, shape):
        self.color=color
        self.shape=shape

class Object1(Thing):
    def speed_change(self):
        self.x += 2


class Object2(Thing):
    def speed_change(self):
        self.x -= 1

heroes = [Hero(), PersBig(), PersMid(), PersJr()]
for hero in heroes:
    hero.draw()
while True:
    cmd = input("What do you want to do? Type shoot, pick object, run or fly: ")
    n = int(input("Which hero from 0 to 3?: "))
    if cmd == "run":
        heroes[n].run()
    elif cmd == "shoot":
        shoot[n].shoot()
    elif cmd == "pick object":
        pick_thing[n].pick_thing()
    elif cmd == "fly":
        heroes[1 or 2].fly()
    else:
        break
    for hero in heroes:
        hero.draw()

things = [Thing(), Object1(), Object2()]
for thing in things:
    print ('Your speed has changed')
