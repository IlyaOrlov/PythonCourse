"""
Superclass and subclasses are created.
Different types of movement are defined as printable strings (for simplicity) \
as a function of speed.
Definitions of different types of shooting etc. are supposed further.
Encapsulation ( with extra '_' ?) is not done, since is not understood yet.
"""

class Master:  #
    def __init__(self, name, shoot, pick):
        # attribute definition
        self.name = name
        self.shoot = shoot
        self.pick = pick

    def move(self, speed):  # move on the ground
        print(self.name + ' runs with the speed of ' + str(speed))

po = Master('Po', 'shoot', 'pick')
shifu = Master('Shifu', 'shoot', 'pick')
tigress = Master('Tigress', 'shoot', 'pick')
monkey = Master('Monkey', 'shoot', 'pick')

class Snake(Master):
    def move(self, speed):  # move on the ground
        print(self.name + ' creeps with the speed of ' + str(speed))

viper = Snake('Viper', 'shoot', 'pick')


class Reptile(Master):
    def move(self, speed):  # move on the ground
        print(self.name + ' crawls with the speed of ' + str(speed))

oogway = Master('Oogway', 'shoot', 'pick')


class Insect(Master):
    def move(self, speed):  # move on the ground
        print(self.name + ' jumps with the speed of ' + str(speed))

mantis = Master('Mantis', 'shoot', 'pick')


class Bird(Master):
    def move(self, speed):  # move on the ground
        print(self.name + ' flies with the speed of ' + str(speed))

crane = Master('Mantis', 'shoot', 'pick')


### TIME TO TEST
po.move(1)
shifu.move(3)
tigress.move(6)
monkey.move(4)
viper.move(2)
oogway.move(0.1)
mantis.move(5)