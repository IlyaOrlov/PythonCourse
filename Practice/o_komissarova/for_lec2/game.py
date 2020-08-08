from random import randint


class Personage:
    x = 0
    speed = 1

    def draw(self):
        pass

    def run(self):
        self.x += self.speed
        print("run forward")

    def shoot(self):
        print("dead shot")

    def peek(self, thing):
        self.speed += thing.speed_change
        print(thing.name + " peeked. Speed is " + str(thing.speed_change))


class Human(Personage):
    def __init__(self):
        print("Human is chosen")

    def draw(self):
        print("I'm Human at {}".format(self.x))


class Vampire(Personage):
    def draw(self):
        print("I'm Vampire at {}".format(self.x))

    def __init__(self):
        print("Vampire is chosen")

    def fly(self):
        self.x += self.speed


class Thing:
    name = "abstract thing"
    speed_change = 0


class FastBoots(Thing):
    name = "fast boots"
    speed_change = 7


class SlowBoots(Thing):
    name = "slow boots"
    speed_change = -3


personages = [Human(), Vampire()]
things = [FastBoots(), SlowBoots()]
for personage in personages:
    personage.draw()
while True:
    n = int(input("Введите номер персонажа (от 0 до 1): "))
    cmd = input("Введите команду (shoot, run, peek или fly (для вампира): ")
    if cmd == "run":
        personages[n].run()
    elif cmd == "shoot":
        personages[n].shoot()
    elif cmd == "peek":
        personages[n].peek(things[randint(0, 1)])
    elif cmd == "fly":
        if isinstance(personages[n], Vampire):
            personages[n].fly()
        else:
            print("Human can't fly")
    else:
        break
    for personage in personages:
        personage.draw()
