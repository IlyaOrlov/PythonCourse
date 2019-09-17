"""
Superclass and subclasses are created.
Different types of movement are defined as printable strings (for simplicity) \
as a function of speed.

Additional actions are added.
For class Reptile method move now depends on speed and artifact.
"""

class Master:  #
    def __init__(self, name):
        # attribute definition
        self.name = name

    def move(self, speed):  # move on the ground
        print(self.name + ' runs with the speed of ' + str(speed) + '.')

    def act(self, mark):
        if mark == 'p':
            print(self.name + ' picks smth.')
        elif mark == 's':
            print(self.name + ' shoots from smth.')


po = Master('Po')
shifu = Master('Shifu')
tigress = Master('Tigress')
monkey = Master('Monkey')

class Snake(Master):
    def move(self, speed):  # move on the ground
        print(self.name + ' creeps with the speed of ' + str(speed) + '.')
        # creep = to move slowly with the abdomen close to the ground

viper = Snake('Viper')


class Reptile(Master):
    def move(self, speed, artef):  # move on the ground
        if artef == 'magic_pants':
            print(self.name + ' flies with the speed of ' + str(10*speed) + '.')
            # Ability to fly with 10x speed if your reptile wears magic pants
        else:
            print(self.name + ' crawls with the speed of ' + str(speed) + '.')
        # crawl = to move slowly on hands and knees, \
        # or by dragging the body along the ground

oogway = Reptile('Oogway')


class Insect(Master):
    def move(self, speed):  # move on the ground
        print(self.name + ' jumps with the speed of ' + str(speed) + '.')

mantis = Insect('Mantis')


class Bird(Master):
    def move(self, speed):  # move on the ground
        print(self.name + ' flies with the speed of ' + str(speed) + '.')

crane = Bird('Crane')


### TIME TO TEST
po.move(1)
shifu.move(3)
tigress.move(6)
monkey.move(4)
viper.move(2)
oogway.move(0.1, 0)
mantis.move(5)
crane.move(3.3)

### ANOTHER TEST

hero_list = [po, shifu, tigress, monkey, viper, oogway, mantis, crane]
hero_speed = [100, 300, 600, 400, 200, 10, 500, 330]
hero_act = ['p', 's', 'p', 's', 'p', 's', 'p', 's']

some_speed = 5

print('')
for h in hero_list:
    if h == oogway:
        h.move(some_speed,'magic pants')
    else:
        h.move(some_speed)

print('')
for k in range(0, len(hero_list)):
    if h == oogway:
        h.move(some_speed,'magic pants')
    else:
        h.move(some_speed)
    print('   and')
    hero_list[k].act(hero_act[k])