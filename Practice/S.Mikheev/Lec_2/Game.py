import random


class Hero:
    ammunition = 0
    action = None
    artifact = None

    def __init__(self, name, race, speed):
        self.name = name
        self.race = race
        self.speed = int(speed)
        
    def move(self):
        self.action.move(self.name, self.speed)
        
    def collect(self):
        self.artifact.collect(self.name, self.speed, self.ammunition)
        

class SimpleMove():

    def move(self, name, speed):
        print('{} moves at a speed {}'.format(name, speed))


class Fly():

    def move(self, name, speed):
        print('{} flies at a speed {}'.format(name, speed))


class FastSpeed():
    
    def collect(self, name, speed, ammunition):
        speed = speed * 2
        print('{} accelerated. His speed {}'.format(name, speed))
    

class SlowSpeed():
    
    def collect(self, name, speed, ammunition):
        speed = speed // 2
        print('{} slowed down. His speed {}'.format(name, speed))


class Shoot():
    
    def collect(self, name, speed, ammunition):
        p = random.randint(1, 10)
        ammunition += p
        print('{} found {} ammunition. His ammunition {}'.format(name, p, ammunition))    
        for i in range(p):
            print('{} shoot'.format(name))
    

halk = Hero('Halk', 'Human', '5')
superman = Hero('Superman', 'Human', '10')
herous = [halk, superman]
for hero in herous:
    for action in [SimpleMove(), Fly()]:
        hero.action = action
        hero.action.move(hero.name, hero.speed)   
    for artifact in [FastSpeed(), SlowSpeed(), Shoot()]:
        hero.artifact = artifact
        hero.artifact.collect(hero.name, hero.speed, hero.ammunition)
