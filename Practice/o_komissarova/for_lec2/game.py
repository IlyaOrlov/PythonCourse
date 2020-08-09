from random import randint


class Personage:
    x = 0
    speed = 1
    action = "run"

    def draw(self):
        pass

    def run(self):
        self.x += self.speed
        if self.action == "run":
            print("run forward")
        elif self.action == "fly":
            print("fly forward")
        elif self.action == "swim":
            print("swim forward")

    def shoot(self):
        print("dead shot")

    def peek(self, thing):
        if thing.speed_change != 0:
            print(thing.speed_change, thing.action)
            self.speed += thing.speed_change
            print(self.speed)
        if thing.action is not None:
            print(thing.speed_change, thing.action)
            self.action = thing.action
            print(self.action)
        print(thing.name + " peeked. Speed is " +
              str(self.speed) + ". Action is " + self.action)


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
        print("fly forward")


class Thing:
    name = "abstract thing"
    action = None
    speed_change = 0


class FastBoots(Thing):
    name = "fast boots"
    speed_change = 7


class SlowBoots(Thing):
    name = "slow boots"
    speed_change = -1


class MagicCarpet(Thing):
    name = "magic carpet"
    action = "fly"


class Flippers(Thing):
    name = "flippers"
    action = "swim"


class Boots(Thing):
    name = "boots"
    action = "run"


personages = [Human(), Vampire()]
things = [FastBoots(), SlowBoots(), MagicCarpet(), Flippers(), Boots()]
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
        rand = randint(0, 4)
        personages[n].peek(things[rand])
    elif cmd == "fly":
        if isinstance(personages[n], Vampire):
            personages[n].fly()
        else:
            print("Human can't fly")
    else:
        break
    for personage in personages:
        personage.draw()

