import random


class Hero:
    ammunition = 0

    def __init__(self, name, race, speed):
        self.name = name
        self.race = race
        self.speed = int(speed)

    def move(self):
        print('{} moves at a speed {}'.format(self.name, self.speed))

    def shoot(self):
        if self.ammunition != 0:
            self.ammunition -= 1
            print('{} shoot'.format(self.name))
        else:
            print('{} has no ammunition'.format(self.name))

    def collect(self):
        print('{} found an artifact'.format(self.name))
        x = random.randint(10, 50)
        if x < 20:
            self.speed = self.speed // 2
            print('{} slowed down. His speed {}'.format(self.name, self.speed))
        elif 20 <= x < 30:
            self.speed = self.speed * 2
            print('{} accelerated. His speed {}'.format(self.name, self.speed))
        else:
            p = random.randint(1, 10)
            self.ammunition += p
            print('{} found {} ammunition. His ammunition {}'.format(self.name, p, self.ammunition))


class FlyHero(Hero):
    def move(self):
        print('{} flies at a speed {}'.format(self.name, self.speed))


halk = Hero('Halk', 'Human', '5')

halk.move()
halk.collect()
halk.collect()
halk.collect()
print(halk.ammunition)
halk.shoot()
print(halk.ammunition)
halk.shoot()
print(halk.ammunition)

superman = FlyHero('Superman', 'Human', '10')
superman.move()
superman.collect()
superman.shoot()
superman.collect()
superman.shoot()
