class Man:

    def __init__(self, name):
        self.name = name

    def solve_task(self):
        return "I'm not ready yet"


class Pupil(Man):
    def __init__(self, name):
        super().__init__(name)

    def solve_task(self):
        import time
        import random
        x = random.randint(3, 6)
        print('...thinks {} seconds...'.format(x))
        time.sleep(x)
        return "I'm not ready yet"


b = Pupil('Alex')


print('{} says: {}'.format(b.name, b.solve_task()))