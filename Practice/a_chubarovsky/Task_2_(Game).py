import random as rnd


class Common:
    x = 0
    y = 0
    z = 0
    health = 100
    armor = 0

    def move(self):
        self.x = rnd.randint(0, 100)
        self.y = rnd.randint(0, 100)
        self.z = rnd.randint(0, 100)

    def shoot(self):
        print("Ka-Boom!")


class Damage(Common):
    moving_speed = "Fast"

    def draw(self):
        print("I'll kill you at {}, {}, {}.".format(self.x, self.y, self.z))
        print("HP = {}".format(self.health))
        print("Armor = {}".format(self.armor))
        print("Speed = ", self.moving_speed)


class Tank(Common):
    armor = 100
    moving_speed = "Slow"

    def draw(self):
        print("I'll protect you at {}, {}, {}.".format(self.x, self.y, self.z))
        print("HP = {}".format(self.health))
        print("Armor = {}".format(self.armor))
        print("Speed = ", self.moving_speed)


class Support(Common):
    moving_speed = "Normal"

    def draw(self):
        print("I'll help you at {}, {}, {}.".format(self.x, self.y, self.z))
        print("HP = {}".format(self.health))
        print("Armor = {}".format(self.armor))
        print("Speed = ", self.moving_speed)


def medicine(pers):
    pers.health += 50


def shield(pers):
    pers.armor += 50


def speed_boost(pers):
    pers.moving_speed = "Faster Than Light."


characters = [Damage(), Tank(), Support()]
for char in characters:
    char.draw()
while True:
    cmd = input("Введите команду (shoot, move или pick): ")
    n = int(input("Введите номер персонажа (от 0 до 2): "))
    if cmd == "move":
        characters[n].move()
    elif cmd == "shoot":
        characters[n].shoot()
    elif cmd == "pick":
        pick = input("Выберите, что взять (medicine, shield или speed_boost): ")
        if pick == "medicine":
            medicine(characters[n])
        elif pick == "shield":
            shield(characters[n])
        elif pick == "speed_boost":
            speed_boost(characters[n])
        else:
            break
    else:
        break
    for char in characters:
        char.draw()
