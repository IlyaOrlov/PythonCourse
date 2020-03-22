import random as rdm


class Common:
    x = 0
    y = 0
    z = 0
    health = 100
    armor = 0

    def move(self):
        self.x = rdm.randint(0, 100)
        self.y = rdm.randint(0, 100)
        self.z = rdm.randint(0, 100)

    def spawn(self):
        print("{} spawn at {}, {}, {}.".format(self.__class__.__name__, self.x, self.y, self.z))
        print("HP = {}".format(self.health))
        print("Armor = {}".format(self.armor))
        print("Speed = {}".format(self.moving_speed))

    def shoot(self):
        print("Ka-Boom!")

    def medicine(self):
        self.health += 50

    def shield(self):
        self.armor += 50

    def speed_boost(self):
        self.moving_speed = "Faster Than Light."


class Fly(Common):

    def spawn(self):
        print("I flying at {}, {}, {}.".format(self.x, self.y, self.z))
        print("HP = {}".format(self.health))
        print("Armor = {}".format(self.armor))
        print("Speed = {}".format(self.moving_speed))


class Damage(Common):
    moving_speed = "Fast"


class Tank(Common):
    armor = 100
    moving_speed = "Slow"


class Support(Common):
    moving_speed = "Normal"


characters = [Damage(), Tank(), Support()]
for char in characters:
    char.spawn()
while True:
    cmd = input("Введите команду (shoot, move или pick): ")
    n = int(input("Введите номер персонажа (от 0 до 2): "))
    if cmd == "move":
        characters[n].move()
    elif cmd == "shoot":
        characters[n].shoot()
    elif cmd == "pick":
        pick = input("Выберите, что взять (medicine, shield, speed_boost или wings): ")
        if pick == "medicine":
            characters[n].medicine()
        elif pick == "shield":
            characters[n].shield()
        elif pick == "speed_boost":
            characters[n].speed_boost()
        elif pick == "wings":
            characters[n] = Fly()
        else:
            break
    else:
        break
    for char in characters:
        char.spawn()
