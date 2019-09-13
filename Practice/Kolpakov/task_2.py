# №1
"""
def large_of_numbers_1(x, y):
    if a > b:
        print(a)
    else:
        print(b)


# №2
def large_of_numbers_2(x, y):
    if a > b:
        return a
    else:
        return b



a = int(input())
b = int(input())
large_of_numbers_1(a, b)
print(large_of_numbers_2(a, b))
"""

# №3
class Hero():

    def __init__(self, name, level, race, move = 'start run...'):
        self.name = name
        self.level = level
        self.race = race
        self.move = move


    def show_hero(self):
        print('Имя: ' + self.name + ' / Уровень: ' + str(self.level) + ' / Расса: ' + self.race)

    def collect(self, collection):
        self.move = collection(self.move)

class Collect:
    def collection(self, move):
        return self.move

class Run(Collect):
    def move(self):
        print('start run...')

class SlowRun(Collect):
    def move(self):
        print('start slow run...')

class FastRun(Collect):
    def move(self):
        print('start fast run...')

class Fly(Collect):
    def move(self):
        print('start fly..')

#class Shoot():



"""если собираем объект 1 - бежит move = Run()
move.move()
если объект 2- медленно идет
если объект 3 - быстро бежит
если объект 4 - летит

#class Animation():"""

a = Hero('Hulk', 1, 'human')
a.show_hero()
a.run()

